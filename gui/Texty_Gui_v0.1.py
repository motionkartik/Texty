import pyperclip
import time
import ctypes
import threading
import logging
import logging.handlers
import tkinter as tk
from tkinter import scrolledtext
from plyer import notification
from ctypes import wintypes

# Configure logging with rotation
log_handler = logging.handlers.RotatingFileHandler(
    "clipboard_log.txt", maxBytes=100000, backupCount=5
)
logging.basicConfig(
    handlers=[log_handler],
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

class ClipboardMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Texty by MotionKartik")
        self.root.geometry("400x250")
        
        self.is_running = False

        # Label
        self.label = tk.Label(root, text="Texty by MotionKartik", font=("Arial", 14, "bold"))
        self.label.pack(pady=5)

        # Display area for copied text
        self.text_display = scrolledtext.ScrolledText(root, height=6, width=45, wrap=tk.WORD)
        self.text_display.pack(pady=5)
        self.text_display.insert(tk.END, "Monitoring clipboard...\n")

        # Start/Stop Button
        self.toggle_button = tk.Button(root, text="Start Monitoring", command=self.toggle_monitor, bg="green", fg="white")
        self.toggle_button.pack(pady=5)

    def log_clipboard(self, content):
        """Logs clipboard content to a file."""
        logging.info(content)

    def show_notification(self, title, message):
        """Displays a system notification."""
        if len(message) > 25:
            message = message[:25] + " ..."
        
        notification.notify(
            title=title,
            message=message,
            timeout=3
        )

    def get_clipboard_data(self):
        """Fetches clipboard text safely."""
        try:
            return pyperclip.paste()
        except Exception:
            return None

    def get_clipboard_file_count(self):
        """Checks if files are copied and returns the count."""
        CF_HDROP = 15  # Clipboard format for file drops
        try:
            ctypes.windll.user32.OpenClipboard(0)
            if ctypes.windll.user32.IsClipboardFormatAvailable(CF_HDROP):
                hGlobal = ctypes.windll.user32.GetClipboardData(CF_HDROP)
                ctypes.windll.user32.CloseClipboard()

                if hGlobal:
                    count = ctypes.windll.shell32.DragQueryFileW(hGlobal, -1, None, 0)
                    return count

            ctypes.windll.user32.CloseClipboard()
        except Exception:
            pass
        return None

    def monitor_clipboard(self):
        """Monitors the clipboard for changes and triggers notifications."""
        last_text = self.get_clipboard_data()

        while self.is_running:
            current_text = self.get_clipboard_data()
            
            if current_text != last_text:
                last_text = current_text
                
                if current_text:
                    self.log_clipboard(current_text)
                    self.show_notification("Copied to Clipboard", current_text)

                    # Update GUI
                    if len(current_text) > 25:
                        current_text = current_text[:25] + " ..."
                    self.text_display.insert(tk.END, f"\n{current_text}\n")
                    self.text_display.yview(tk.END)
                else:
                    file_count = self.get_clipboard_file_count()
                    if file_count:
                        self.show_notification("Files Copied", f"{file_count} file(s) copied")

            time.sleep(0.5)

    def toggle_monitor(self):
        """Starts or stops clipboard monitoring."""
        if self.is_running:
            self.is_running = False
            self.toggle_button.config(text="Start Monitoring", bg="green")
        else:
            self.is_running = True
            self.toggle_button.config(text="Stop Monitoring", bg="red")
            threading.Thread(target=self.monitor_clipboard, daemon=True).start()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ClipboardMonitorApp(root)
    root.mainloop()
  
