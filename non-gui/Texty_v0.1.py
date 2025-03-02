import pyperclip
import time
import ctypes
from threading import Thread
from plyer import notification

def get_clipboard_data():
    try:
        return pyperclip.paste()
    except Exception:
        return None

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=3
    )

def monitor_clipboard():
    last_text = get_clipboard_data()
    while True:
        current_text = get_clipboard_data()
        if current_text != last_text:
            last_text = current_text
            if current_text:
                Thread(target=show_notification, args=("Copied to Clipboard", current_text)).start()
            else:
                try:
                    ctypes.windll.user32.OpenClipboard(0)
                    count = ctypes.windll.user32.CountClipboardFormats()
                    ctypes.windll.user32.CloseClipboard()
                    Thread(target=show_notification, args=("Files Copied", f"{count} item(s) copied" )).start()
                except Exception:
                    pass
        time.sleep(0.5)

if __name__ == "__main__":
    monitor_clipboard()
