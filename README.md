````markdown
# 🕵️ Telegram Keyword Finder

This is a simple desktop GUI app I built to search for specific keywords inside any Telegram group or channel I'm part of. It uses the [Telethon](https://github.com/LonamiWebs/Telethon) Python library to connect to Telegram and pull message history, and `Tkinter` for the user interface.

---

## 🚀 Features

- Search Telegram messages by keyword
- Works with groups, channels, and private chats (as long as I'm a member)
- Simple GUI interface using Python's built-in Tkinter
- Auto-scroll message box to view search results

---

## 🧱 Technologies Used

### 🔌 Telethon

```python
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
```
````

- `TelegramClient`: Handles the connection to Telegram’s API.
- `GetHistoryRequest`: Fetches message history from a chat.

### 🖥️ Tkinter

```python
import tkinter as tk
from tkinter import scrolledtext, messagebox
```

- `tk`: Base GUI framework.
- `scrolledtext`: A text box with scrollbar support (so results are easy to scroll through).
- `messagebox`: Used to show popups when something goes wrong.

### 🔁 Other Python Modules

```python
import threading
import asyncio
```

- `threading`: Makes sure the Telegram search runs in a background thread so the GUI doesn’t freeze.
- `asyncio`: Handles the async nature of Telethon since it requires an event loop.

---

## ⚙️ How It Works

1. I start the GUI and enter:

   - A keyword to search for
   - The username of the Telegram chat (group, channel, or user)

2. When I click "Search":

   - It connects to Telegram (or reuses a session if one already exists).
   - It fetches the most recent messages (up to 100 by default).
   - Filters the messages that contain the keyword.
   - Displays the results in the scrollable text box.

---

## 📌 Notes

- The Telegram session file (e.g., `session_name.session`) is saved locally and reused for future logins.
- For now, it supports one keyword at a time. I plan to add support for multiple keywords using comma separation in a future update.
- If you get a popup asking to authorize your account, it means the session hasn’t been created yet and you need to log in.

---

## 🧪 Setup Instructions

1. **Install dependencies:**

```bash
pip install telethon
```

2. **Clone the repo:**

```bash
git clone https://github.com/your-username/keyword-finder.git
cd keyword-finder
```

3. **Update your API credentials in the code:**

```python
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
```

You can get these from [https://my.telegram.org](https://my.telegram.org).

4. **Run the script:**

```bash
python gui_keyword_search.py
```

---

## ✅ Todo

- [ ] Support searching multiple keywords (comma-separated)
- [ ] Let users choose how many messages to scan
- [ ] Export results to `.txt` or `.csv`
- [ ] Improve layout and add dark mode

---

## 📬 Contact

If you want to collaborate or have questions, feel free to reach out.
