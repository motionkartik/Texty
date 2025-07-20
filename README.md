# 📋 Clipboard Flash Notifier

A lightweight, cross-platform Python tool that flashes a popup notification near your cursor whenever **text** or **files** are copied to your clipboard.

Perfect for editors, developers, or power users who want quick visual feedback on clipboard activity.

---

## ✨ Features

- ✅ Cross-platform support: **Windows** and **macOS**
- 📎 Detects both **copied text** and **copied files**
- ⚡ Fast & responsive popup near the mouse cursor
- 🌙 Auto-fades after a second with smooth animation
- 🧠 Smart truncation to avoid long text blocking your screen
- 🔒 Zero intrusive windows or system tray clutter

---

## 🖥️ Preview

![Demo(not ready yet)](link)  

---

## 🛠 Requirements

Install Python dependencies using `pip`:

### Windows
```bash
pip install pyperclip pyautogui pywin32

pip install pyperclip pyautogui pyobjc


The script will run in the background and display a small flash popup near your mouse cursor whenever you copy:

📝 Text (e.g., Ctrl+C or ⌘+C)

📁 Files (copied from Explorer or Finder)

⚙️ Platform-Specific Notes
macOS:
Uses pyobjc and AppKit to read filenames from the clipboard

Transparency may vary depending on macOS window manager

Windows:
Uses pywin32 for clipboard file detection via CF_HDROP

Works well with Explorer and text from most apps

📦 Optional Enhancements
You can customize or extend the notifier with:

Native system notifications (via osascript or win10toast)

System tray toggle

Clipboard history log

Styling with icons or themes

❌ Limitations
Linux is currently not supported (due to clipboard model differences)

Cannot detect images or rich text (yet)

📄 License
MIT License — use it freely, modify it, improve it.
