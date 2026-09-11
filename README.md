<div align="center">
  <h1>✨ StudyHub -Smart Learning Web Application</h1>
  <p><strong>A Dribbble-inspired, minimalist, distraction-free study station powered by Google Gemini AI. Built entirely with pure Python and zero third-party dependencies.</strong></p>

  <p>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" /></a>
    <img src="https://img.shields.io/badge/Gemini%20API-3.5%20%7C%203.6%20Flash-orange.svg?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini Models" />
    <img src="https://img.shields.io/badge/Dependencies-Zero%20Python%20Pkgs-success.svg?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDQgNnYxMmwxOCA0bDgtNHYtMTJMMTIgMnpNMTAuNSAxNy41bC0zLjUtMy41IDEuNDEtMS40MSA9Mi4wOSA9Mi4wOSA9NS4wOS01LjA5IDEuNDEgMS40MS02LjUgNi41eiIvPjwvc3ZnPg==" alt="Zero Python Dependencies" />
    <img src="https://img.shields.io/badge/UI--UX-Dribbble%20Minimalist-indigo.svg?style=for-the-badge&logo=dribbble&logoColor=white" alt="Dribbble Minimalist Design" />
  </p>
</div>

---

## 📖 The Vision Behind StudyHub

Traditional learning tools are often cluttered with distracting social loops, heavy databases, and slow loading screens. **StudyHub** was crafted with a different philosophy: **absolute cognitive simplicity**.

By merging evidence-based learning principles (such as active recall, spaced repetition, and Pomodoro-driven deep focus intervals) with the conversational intelligence of **Google Gemini**, StudyHub acts as a private, high-fidelity digital study study room.

Designed with a strict, minimalist aesthetic, StudyHub runs **instantly** and stores your data **locally**. It is built on a custom, zero-dependency Python core that consumes virtually no memory, initializes in under 5 milliseconds, and can be deployed anywhere with a single command.

---

## 🎨 Exquisite UI/UX & Aesthetic Guidelines

StudyHub features a premium, hyper-clean dashboard crafted under meticulous design guidelines:

*   **The Strict 3-Color Palette:**
    *   **Canvas:** Beautiful, calming canvas hues (`#f8fafc` in light mode; deep obsidian `#090d16` in dark mode) that reduce eye fatigue during long sessions.
    *   **Ink:** Crisp, structural slate neutrals ensuring high contrast ratios and comfortable typography reading.
    *   **Accent:** A singular, focused indigo highlight (`#4f46e5` / `#6366f1`) to direct attention, manage interface hierarchies, and signal action states.
*   **Aesthetic Continuity:** No distracting icon backgrounds, heavy borders, or chaotic card shadows. Every action, card, and layout element responds to seamless hover animations.
*   **Dual-Theme Mode:** Fluid transitions between a premium workspace **Light Theme** and a deep-space **Dark Theme**.
*   **Physical 3D-Flip Interactions:** Flashcards flip smoothly using beautiful CSS transform properties, offering a physical feel to digital memory retention.
*   **Modern Typography:** Clean, premium sans-serif headings using `Plus Jakarta Sans` balanced with beautiful code-focused monospace blocks in `JetBrains Mono`.

---

## 🚀 Core Features

StudyHub integrates everything you need for productive learning into a single tab:

### 🧠 Spaced Repetition Decks & Flashcards
*   **Structured Categories:** Create, rename, and manage separate learning decks (pre-configured with high-fidelity decks such as *Python Architecture & Internals* and *Learning Science & Memory*).
*   **Interactive 3D Cards:** Test your active recall with sleek, flippable flashcards.
*   **Frictionless CRUD:** Add and delete custom cards on-the-fly directly from the sidebar.

### ⏱️ Pomodoro Focus Station
*   **Built-in Focus Timer:** Toggle between a standard 25-minute deep focus interval or keep track of custom study periods.
*   **Persistent Statistics:** Progress is logged to track completed Pomodoros, accumulated study minutes, and active daily streak counts.
*   **Default Mode Network Recovery:** Reminders built to encourage physical, screen-free rest intervals.

### 📝 Dynamic Revision Notes
*   **Quick Study Sheets:** Store key takeaways, syntax sheets, or concept outlines.
*   **Preloaded Guides:** Includes masterclasses on cognitive learning (*Feynman Technique Guide* and *Optimal Pomodoro Structuring*).
*   **Instant Updates:** Create, edit, and delete notes dynamically with automatic persistence.

### 🤖 Google Gemini AI Study Assistant
Fully integrated with Google's advanced `gemini-3.5-flash-lite` and `gemini-3.6-flash` models:
*   **The Feynman Explainer:** Break down complex jargon into three different mental frameworks:
    *   *Simplify:* Explains concepts like you are teaching a 12-year-old, using rich everyday analogies.
    *   *Summarize:* Perfect for exam cramming—extracts high-yield takeaways, definitions, and memory hooks.
    *   *Deconstruct:* Formats explanations like a supportive professor, offering clear structures and real-world examples.
*   **AI Flashcard Generator:** Input a topic or raw study notes, and Gemini will instantly parse the context and output exactly 4 structured, high-yield Q&A cards to insert into your deck.
*   **Interactive Quiz Master:** Instantly generate a 3-question multiple-choice interactive quiz about any topic, complete with four distinct options, automated grading, and a deep educational explanation for each answer.

### 🔒 Privacy & Local-First Key Management
*   **Secure Credential Handling:** Store your `GEMINI_API_KEY` on your local server. It is saved securely in local JSON configurations and is never logged, printed, or exposed.
*   **Key Preview & Deletion:** View active key status safely (e.g., `••••1234`) and wipe credentials with a single click.

---

## 🛠️ Behind the Code: Architecture Philosophy

```
                    ┌────────────────────────┐
                    │       Web Browser      │
                    │   (Plus Jakarta Sans)   │
                    └───────────┬────────────┘
                                │ HTTP Requests (JSON / HTML)
                                ▼
                    ┌────────────────────────┐
                    │   ThreadingHTTPServer  │  ◄── [Standard python http.server]
                    │      (server.py)       │
                    └─────┬────────────┬─────┘
                          │            │
         Reads templates  │            │  Performs API Tasks
                          ▼            ▼
               ┌─────────────┐      ┌─────────────────────────┐
               │templates.py │      │   gemini_service.py     │
               └─────────────┘      │ (urllib.request/Gemini) │
                                    └─────────────────────────┘
                                                 │
                                                 ▼
               ┌─────────────┐      ┌─────────────────────────┐
               │  Local Disk │ ◄──  │    study_storage.py     │
               │ (JSON Data) │      │  (study_data.json)      │
               └─────────────┘      └─────────────────────────┘
```

StudyHub represents a masterclass in **Defensive, Low-Dependency Python Engineering**:

1.  **Zero Python Dependencies:** Communicates with the external world and Google Gemini REST APIs strictly using Python standard libraries (`urllib.request`, `http.server`, `json`, `pathlib`). No heavyweight frameworks or library overhead.
2.  **Multithreaded Server:** Built on `ThreadingHTTPServer`, ensuring that heavy LLM requests or storage writes do not block user interface updates.
3.  **Local-First Persistence:** All flashcards, custom notes, focus statistics, and configuration details are stored locally inside `study_data.json` on your device.
4.  **Atomic File Integrity:** Reads and writes to disk are safely isolated to prevent file corruption in case of immediate shutdowns.

---

## 🚀 Getting Started

Running StudyHub is incredibly straightforward, requiring only **Python 3.12+**.

### Run with Python (Direct & Lightweight)
The most direct way to launch StudyHub:
```bash
# Clone and enter the directory
cd study-and-learning-app

# Run the server immediately
python3 server.py
```
By default, the server will launch at: **`http://localhost:3000`**

### Run with Node/NPM (Optional Wrapper)
If you prefer running using npm script runners:
```bash
# Install wrapper structure
npm install

# Run the app in development mode
npm run dev
```

### Configurable Flags
You can customize the host and port directly through command-line parameters:
```bash
# Launch on a custom port and open it up to your local network
python3 server.py --port 8080 --host 0.0.0.0
```

---

## ⚙️ Configuration & API Key Setup

To unlock the AI-powered Feynman Explainer, Card Generator, and Quiz Master, you need a Google Gemini API Key. You can get one for free at [Google AI Studio](https://aistudio.google.com/).

You have **two seamless ways** to configure your key:

### Option A: The Key Guide Dashboard (Recommended)
1. Launch StudyHub and navigate to the **Key Guide** tab in the sidebar.
2. Paste your key into the secure input box and click **Save API Key**.
3. The server will persist it locally and activate all AI features instantly.

### Option B: Local Environment File
1. Create a file named `.env` in the root directory.
2. Add your key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
3. Restart the server.

---

## 📂 Project Blueprint

An overview of the codebase architecture:

*   📂 **`server.py`**: The central application hub. Handles multithreaded routing, processes JSON API endpoints, and delivers template-rendered frontends.
*   📂 **`gemini_service.py`**: Houses Gemini REST API integrations. Gracefully attempts queries on multiple flash-model tiers (`gemini-3.5-flash-lite`, `gemini-3.6-flash`) with automatic fallback and prompt orchestration.
*   📂 **`study_storage.py`**: Handles localized reading/writing for focus stats, notes CRUD, deck operations, and key obfuscation.
*   📂 **`templates.py`**: Contains the beautiful, Dribbble-inspired SPA layout with interactive CSS transitions, Lucide icons, and dual theme toggles.
*   📂 **`study_data.json`**: The persistent local database file where all your study data, notes, and custom flashcards live.
*   📂 **`metadata.json`**: Package capability specifications.

---

## 📄 License & Collaboration

This project is licensed under the **MIT License**.

StudyHub is built to prove that you don't need heavy, tracking-laden modern web frameworks to create a fast, beautiful, and intelligent product. If you have suggestions for new cognitive templates, study features, or performance refactoring, feel free to submit a pull request!

---

