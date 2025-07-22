
# 🤖 Jarvis AI Assistant

A local, voice-based desktop AI assistant — works **offline** using [Ollama](https://ollama.com), [Whisper](https://github.com/openai/whisper), and a Jarvis-style desktop UI.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/javidh357/jarvis_ai.git
cd jarvis_ai
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .jack
.\.jack\Scriptsctivate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Ollama and Load the LLaMA Model

```bash
ollama run llama3
```

💡 You can also run `llama3:medium` or `llama3:large` if installed.

### 5. Run the Assistant

```bash
python main.py
```

---

## 📁 Project Structure

```bash
jarvis_ai/
├── main.py              # Starts the assistant
├── nova_ai.py           # Core logic (transcribe, reply, speak)
├── ui.py                # UI: animations, buttons, waveform
├── database.py          # Save & retrieve chat history
├── requirements.txt     # Dependencies
└── README.md            # You're reading this
```

---

## 🧠 How It Works

- 🎙️ Listens via your microphone (`sounddevice`)
- 📝 Transcribes audio locally with Whisper (`openai-whisper`)
- 💬 Sends the prompt to LLaMA 3 (`Ollama`)
- 🗣️ Speaks the reply using `pyttsx3`
- 🖥️ Displays response in a custom animated UI (`tkinter`)

---

## 🛠️ Coming Soon

- 🌐 Web search integration
- 🖱️ Mouse & keyboard control
- 🧠 Memory for past chats
- 🔌 Plugin support

---

## 🙌 Credits

Built by **Kovvuru Javidh**

Powered by:

- [Ollama](https://ollama.com)
- [Whisper by OpenAI](https://github.com/openai/whisper)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- `pyttsx3`, `sounddevice`

---

## 📸 Demo

🎥 Coming soon: YouTube video demo of Jarvis AI in action.

---

## 📜 License

Licensed under the [MIT License](LICENSE). Feel free to fork, improve, and build your own AI Jarvis.

