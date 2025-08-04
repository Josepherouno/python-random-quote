# Shinexa Telegram Voice Chatbot

Shinexa is a Telegram mini game that chats with users and replies using an AI-generated female voice from OpenAI's text-to-speech model. It transcribes incoming voice notes to keep the conversation fluid without storing personal data.

## Features
- Send text or voice messages and get spoken responses
- Interactive conversations powered by ChatGPT
- Replies delivered using OpenAI's built-in TTS voice
- Webhook or polling operation

## Setup
1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure environment**
   Copy the example file and fill in your keys:
   ```bash
   cp .env.example .env
   # edit .env and set TELEGRAM_TOKEN, OPENAI_API_KEY
   ```
   - Optionally change `OPENAI_VOICE` to another built-in name such as `coral` or `nova`.
   - Set `WEBHOOK_URL` to your public HTTPS URL if you want webhook mode; leave blank to use polling.
3. **Run the bot**
   ```bash
   python telegram_bot.py
   ```

4. **Optional web demo**
   Open `index.html` in a modern browser to try a simple client-side demo that speaks back what you type.

## Webhook
When `WEBHOOK_URL` is defined, the bot starts an HTTPS webhook and automatically registers it with Telegram. The webhook listens on `PORT` (default `8443`).

## Replit Deployment
1. Import this repository into a Replit project.
2. Add the environment variables from `.env.example` in the **Secrets** tab.
3. Set `WEBHOOK_URL` to the URL shown by Replit when the bot runs.
4. Start the bot with `python telegram_bot.py` in the Replit shell.

## Component Tool Suggestions

| Component               | Tool Suggestions                              |
| ----------------------- | --------------------------------------------- |
| Content Autogenerierung | GPT-4o, ElevenLabs, D-ID, RunwayML             |
| Scripting / Scheduling  | Python + Playwright + cron                     |
| Analytics              | Google Analytics / Matomo / Fathom             |
| Monitoring             | UptimeRobot + custom HTML parsers              |
| Link-Tracking          | Bitly, T2M, self-hosted redirect servers       |
| Payment-Logic          | Stripe webhooks (for external services)        |

## Notes
- The spoken voice is AI-generated; OpenAI does not support custom voice cloning.
- The bot does not store user messages or audio on disk.

## Running Tests
```bash
pytest
```
