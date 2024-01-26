# Rheabot_v1
This is a simple therapy bot powered by google's gemini pro
# Rhea Telegram Chatbot

Rhea is a Telegram chatbot powered by Google's Generative AI. It is designed to provide lighthearted and positive responses to user inputs.

## Features

- Start a conversation with Rhea by sending messages to the bot on Telegram.
- Use commands like `/start`, `/help`, and `/exit` for specific interactions.
- Rhea engages in lighthearted conversations, responding to user prompts.

## Prerequisites

Before running the bot, make sure you have the following:

- Python 3.x installed
- Create a virtual environment (optional but recommended)
- Install dependencies: `pip install -r requirements.txt`
- Obtain a Telegram bot token from the [BotFather](https://core.telegram.org/bots#botfather)
- Obtain a Google API key for Generative AI from the [Google Cloud Console](https://cloud.google.com/docs/authentication/getting-started)

## Configuration

Create a `.env` file in the project root and add your API keys:

```plaintext
GOOGLE_API_KEY=your_google_api_key
TELEGRAM_TOKEN=your_telegram_bot_token
