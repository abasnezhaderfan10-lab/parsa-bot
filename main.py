from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

TOKEN = "8619545446:AAGDIEq4z4kNYPTg2Y87X3Kkmqk4Hx0FbQg"

WELCOME_TEXT = """سلام !
به کارگروه پارسا خوش آمدید 
لیزینگ اقساطی خودرو و ملک"""

async def auto_approve_and_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    await update.chat_join_request.approve()
    print(f"کاربر {user.first_name} تایید شد.")
    
    try:
        await context.bot.send_message(
            chat_id=user.id,
            text=WELCOME_TEXT
        )
        print(f"ارسال شد پیام خوش‌آمدگویی به {user.first_name}")
    except Exception as e:
        print(f"خطا در ارسال پیام: {e}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(auto_approve_and_welcome))
    print("ربات روشن شد و منتظر اعضای جدید است...")
    app.run_polling()

if name == 'main':
    main()
