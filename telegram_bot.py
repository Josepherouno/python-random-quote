import os
import tempfile
from io import BytesIO

from dotenv import load_dotenv
from openai import OpenAI
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

load_dotenv()

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_VOICE = os.environ.get("OPENAI_VOICE", "alloy")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
PORT = int(os.environ.get("PORT", "8443"))

if not TELEGRAM_TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN environment variable not set")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY environment variable not set")

openai_client = OpenAI(api_key=OPENAI_API_KEY)


def chatgpt_reply(prompt: str) -> str:
    resp = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.choices[0].message["content"].strip()


def tts(text: str) -> bytes:
    """Generate speech audio for the given text."""
    with tempfile.NamedTemporaryFile(suffix=".mp3") as tmp:
        with openai_client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice=OPENAI_VOICE,
            input=text,
        ) as response:
            response.stream_to_file(tmp.name)
        tmp.seek(0)
        return tmp.read()


def transcribe(file_path: str) -> str:
    """Transcribe an audio file to text."""
    with open(file_path, "rb") as f:
        result = openai_client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
        )
    return result.text.strip()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to Shinexa! Send text or a short voice message to chat with me. Replies are in an AI-generated voice."
    )


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    prompt = update.message.text
    reply_text = chatgpt_reply(prompt)
    audio_bytes = tts(reply_text)
    bio = BytesIO(audio_bytes)
    bio.name = "reply.mp3"
    await update.message.reply_audio(audio=bio)


async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = await context.bot.get_file(update.message.voice.file_id)
    with tempfile.NamedTemporaryFile(suffix=".ogg") as tmp:
        await file.download_to_drive(tmp.name)
        prompt = transcribe(tmp.name)
    reply_text = chatgpt_reply(prompt)
    audio_bytes = tts(reply_text)
    bio = BytesIO(audio_bytes)
    bio.name = "reply.mp3"
    await update.message.reply_audio(audio=bio)


def main() -> None:
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    if WEBHOOK_URL:
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TELEGRAM_TOKEN,
            webhook_url=f"{WEBHOOK_URL}/{TELEGRAM_TOKEN}",
        )
    else:
        app.run_polling()


if __name__ == "__main__":
    main()
