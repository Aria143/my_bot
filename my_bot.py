import logging
from telegram.ext import Updater, MessageHandler, Filters
from transformers import pipeline

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = "6121818840:AAE1yRFg9wkjKbaniYwnTtWjI5iyOPNdIuM"
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

model = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

def generate_text(update, context):
    input_text = update.message.text
    output_text = model(input_text, max_length=100)[0]['generated_text']
    update.message.reply_text(output_text)

dispatcher.add_handler(MessageHandler(Filters.text, generate_text))

updater.start_polling()
updater.idle()
