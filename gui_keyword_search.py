from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import asyncio

# Replace with your credentials
api_id = 27029779
api_hash = 'ae52e445711e8865e6520109dabbbd96'
session_name = 'keyword_search_gu_session'

# Set up event loop and client globally
loop = asyncio.new_event_loop()
client = TelegramClient(session_name, api_id, api_hash, loop=loop)

# Function to keep the event loop running in background
def start_event_loop():
    asyncio.set_event_loop(loop)

    async def runner():
        await client.connect()
        if not await client.is_user_authorized():
            await client.start()  # This will prompt login or use saved session
        else:
            print("Client is already authorized and connected.")

    loop.run_until_complete(runner())
    loop.run_forever()



# Start loop in background thread
threading.Thread(target=start_event_loop, daemon=True).start()

# GUI logic
def search_messages():
    keyword = keyword_entry.get()
    chat = chat_entry.get()

    if not keyword or not chat:
        messagebox.showwarning("Input Error", "Please enter both a keyword and chat username.")
        return

    def run_search():
        async def do_search():
            try:
                entity = await client.get_entity(chat)
                history = await client(GetHistoryRequest(
                    peer=entity,
                    limit=200,
                    offset_date=None,
                    offset_id=0,
                    max_id=0,
                    min_id=0,
                    add_offset=0,
                    hash=0
                ))

                messages = [
                    f"{msg.date.strftime('%Y-%m-%d %H:%M')} - {msg.message}"
                    for msg in history.messages
                    if msg.message and keyword.lower() in msg.message.lower()
                ]

                def update_results():
                    results_text.delete(1.0, tk.END)
                    if messages:
                        for msg in messages:
                            results_text.insert(tk.END, msg + "\n\n")
                    else:
                        results_text.insert(tk.END, "No matching messages found.")

                window.after(0, update_results)

            except Exception as e:
                window.after(0, lambda: messagebox.showerror("Error", str(e)))

        # Schedule the coroutine in the background loop
        asyncio.run_coroutine_threadsafe(do_search(), loop)

    threading.Thread(target=run_search).start()

# GUI Setup
window = tk.Tk()
window.title("Telegram Keyword Finder")
window.geometry("600x400")

tk.Label(window, text="Keyword:").pack()
keyword_entry = tk.Entry(window, width=50)
keyword_entry.pack(pady=5)

tk.Label(window, text="Group/Channel Username (e.g. @somegroup):").pack()
chat_entry = tk.Entry(window, width=50)
chat_entry.pack(pady=5)

tk.Button(window, text="Search", command=search_messages).pack(pady=10)

results_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=15)
results_text.pack(padx=10, pady=10)

window.mainloop()
