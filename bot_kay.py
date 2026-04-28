
import anthropic
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
 
TELEGRAM_TOKEN = "сюда_токен_от_botfather"
ANTHROPIC_KEY = "сюда_ключ_от_anthropic"
 
client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
 
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
 
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": user_text}]
    )
 
    await update.message.reply_text(response.content[0].text)
 
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
