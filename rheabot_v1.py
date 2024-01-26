from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_response(question):
    try:
        response = chat.send_message(question)
        return response.text  # Return the response directly without filtering

    except Exception as e:
        error_messages = [
            "I'm sorry, but this topic is a bit too sensitive for me to handle. I'm committed to staying away from potentially harmful or inappropriate content.",
            # ... (other error messages)
        ]
        return random.choice(error_messages)

TOKEN: Final = 'YOUR_TELEGRAM_TOKEN'
BOT_USERNAME: Final = '@your_bot_username'

# Commands
async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I am Rhea")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am Rhea, I am trained by Priyanshu, and I can be your friend")

async def exit_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Goodbye!")

# Responses
async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    
    conversational_prompt = "In a messaging conversation, in one or two lines one naturally replies in, tell me what Rhea the Therapist, companion and a caring girl, but is not overdramatic or overspoken and never says no to a question, would reply in chat if her patient who seems to be looking for lighthearted conversation said" + user_input + "."
    
    response = get_response(conversational_prompt)

    # Print the conversation in the console
    print(f"User: {user_input}")
    print(f"Rhea: {response}")

    # Remove inverted commas before sending the message
    response_text = response.replace('"', '')

    await update.message.reply_text(response_text)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} throws an error: {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_cmd))
    app.add_handler(CommandHandler('help', help_cmd))
    app.add_handler(CommandHandler('exit', exit_cmd))

    # Message handler for AI chatbot responses
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))

    # Error handler
    app.add_error_handler(error)

    # Polling
    print('Polling...')
    app.run_polling(poll_interval=2)
