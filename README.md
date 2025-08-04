# Shinexa Telegram Voice Chatbot

[![Run on Replit](https://replit.com/badge/github/openai/python-random-quote)](https://replit.com/github/openai/python-random-quote)

Shinexa is a Telegram mini game that chats with users and replies using an AI-generated female voice from OpenAI's text-to-speech model. It transcribes incoming voice notes to keep the conversation fluid without storing personal data.

## Try it
Play the demo bot on Telegram: [t.me/ShineQuest25Bot?game=ShineQuest](https://t.me/ShineQuest25Bot?game=ShineQuest).
Or launch the browser demo instantly via Replit: [https://replit.com/github/openai/python-random-quote](https://replit.com/github/openai/python-random-quote).

## Features
- Send text or voice messages and get spoken responses
- Interactive conversations powered by ChatGPT
- Replies delivered using OpenAI's built-in TTS voice
- Webhook or polling operation

## Setup
1. **Install dependencies (for local use)**
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

4. **Voice web demo**
   ```bash
   python web_server.py
   ```
   Then open [http://localhost:5000](http://localhost:5000) and click the microphone button to chat with Shinexa in your browser.

## Webhook
When `WEBHOOK_URL` is defined, the bot starts an HTTPS webhook and automatically registers it with Telegram. The webhook listens on `PORT` (default `8443`).

## Replit Deployment
1. Import this repository into a Replit project or click the badge above.
2. Add the environment variables from `.env.example` in the **Secrets** tab.
3. Press **Run**. Replit installs dependencies automatically and starts the web demo on the public URL shown in the console.
4. To run the Telegram bot instead, stop the web demo and execute `python telegram_bot.py` in the Replit shell.

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
pip install -r dev-requirements.txt
pytest
```
