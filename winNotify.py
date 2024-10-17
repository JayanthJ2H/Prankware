from winotify import Notification, audio
import os
import sys
from Notepad import notepad

def sendNotification(userInput):
    message = userInput.lower()
    yes_or_no = False

    if "site:" in message:
        text = message.replace("site:", "").strip()
        site = text
        yes_or_no = True
    elif "type:" in message:
        text = message.replace("type:", "").strip()
        word = text
        notepad(word)
        text = ''
    else:
        text = message

    def show(text):
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)

        icon_path = os.path.join(base_path, "hacker.png")

        toast = Notification(
            app_id="http://g4bn1n3sis9ck2koasjkbv9kja4tlkj5asi20c90kqkzlac9..onion",
            title="Anonymous",
            msg=text,
            icon=icon_path,
        )
        toast.set_audio(audio.Mail, loop=False)

        if yes_or_no:
            toast.add_actions(label="Open", launch=site)
        toast.show()

    show(text)
