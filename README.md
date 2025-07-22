# 🤖 Jarvis AI Desktop Assistant

**Jarvis AI** is a powerful offline voice assistant for your desktop — built with local LLaMA3 (via Ollama), Whisper for speech recognition, and Python. It can listen, think, speak, and even control your PC — just like in the movies.

---

## ✨ Features

- 🎙️ Voice Activation (Wake word: **"Hey Nova"**)
- 🧠 Local LLM (LLaMA 3 via Ollama — No internet needed)
- 🗣️ Offline Speech-to-Text using Whisper
- 💬 Instant replies via Text-to-Speech (TTS)
- 🖥️ Animated Desktop UI using Tkinter
- 📂 Run custom PC commands (open apps, check time, etc.)
- 🧵 Typing animation + waveform visuals
- 💾 Optional Chat History with SQLite
- 🌍 Multilingual: English, Hindi, Chinese, Japanese, etc.

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/javidh357/jarvis_ai.git
cd jarvis_ai
2. Create and activate a virtual environment
bash
Copy
Edit
python -m venv .jack
.\.jack\Scripts\activate
3. Install the dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Start Ollama and load the LLaMA model
bash
Copy
Edit
ollama run llama3
💡 You can use llama3:medium or llama3:large if installed.

5. Run the assistant
bash
Copy
Edit
python main.py
📁 Project Structure
bash
Copy
Edit
jarvis_ai/
├── main.py              # Starts the assistant
├── nova_ai.py           # Core logic (transcribe, reply, speak)
├── ui.py                # UI: animations, buttons, waveform
├── database.py          # Save & retrieve chat history
├── requirements.txt     # Dependencies
└── README.md            # You're reading this
🧠 How It Works
Listens through microphone using sounddevice

Transcribes voice locally using Whisper

Sends prompt to LLaMA 3 via Ollama

Speaks the reply with pyttsx3

Shows animated response on desktop UI

🛠️ Coming Soon
🌐 Search the web

🖱️ Control mouse and keyboard

🧠 Memory for past chats

🔌 Plugin support

🙌 Credits
Built by Kovvuru Javidh

Using:

Ollama

Whisper by OpenAI

Tkinter

pyttsx3

sounddevice

📸 Demo
Coming soon: YouTube video demo of Jarvis AI in action.

📜 License
Licensed under the MIT License. Feel free to fork, improve, and build your own AI Jarvis.

yaml
Copy
Edit

---

Let me know if you also want:

- A cool banner image at the top  
- A `.gif` demo
- Screenshots or badges (like Python version, stars, forks)  
- OR markdown buttons (to launch, download, or watch demo)

I can add all that too!








Ask ChatGPT
