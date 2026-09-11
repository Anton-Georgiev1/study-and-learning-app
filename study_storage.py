"""
Study Data Storage Engine.
Manages persistent decks, flashcards, revision notes, and study statistics.
"""

import json
import time
from pathlib import Path

DATA_FILE = Path(__file__).parent / "study_data.json"

DEFAULT_DATA = {
    "decks": [
        {
            "id": "deck-python",
            "title": "Python Architecture & Internals",
            "category": "Computer Science",
            "description": "Essential Python language mechanisms, object models, and memory management.",
            "color": "#6366F1",
            "cards": [
                {
                    "id": "c1",
                    "front": "What is the difference between a List and a Tuple in Python?",
                    "back": "Lists are mutable (modifiable in-place using .append(), .pop()), whereas Tuples are immutable and hashable (can be dictionary keys). Tuples also have slight memory and optimization advantages."
                },
                {
                    "id": "c2",
                    "front": "How does Python garbage collection work?",
                    "back": "Python primarily uses reference counting for immediate reclamation, supplemented by a generational cyclic garbage collector to detect and break isolated circular references."
                },
                {
                    "id": "c3",
                    "front": "What is the Python GIL (Global Interpreter Lock)?",
                    "back": "A mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecode simultaneously within one CPython process."
                },
                {
                    "id": "c4",
                    "front": "What is the difference between '__str__' and '__repr__'?",
                    "back": "'__str__' aims for readability for end users. '__repr__' aims to be unambiguous, detailed, and ideally valid Python code to recreate the object for developers."
                }
            ]
        },
        {
            "id": "deck-cognition",
            "title": "Learning Science & Memory",
            "category": "Cognitive Psychology",
            "description": "Evidence-based learning techniques: active recall, spaced repetition, and interleaving.",
            "color": "#10B981",
            "cards": [
                {
                    "id": "m1",
                    "front": "What is Active Recall and why is it superior to passive rereading?",
                    "back": "Active recall requires your brain to retrieve knowledge from memory without looking at answers. Retrieval strengthens neural synapses and dramatically reduces the Ebbinghaus forgetting curve."
                },
                {
                    "id": "m2",
                    "front": "How does the Leitner Spaced Repetition system work?",
                    "back": "Cards are sorted into compartments based on difficulty. Correctly recalled cards move to boxes reviewed less frequently, while missed cards return to Box 1 for immediate review."
                },
                {
                    "id": "m3",
                    "front": "What is 'Interleaving' in study methodology?",
                    "back": "Mixing different topics or problem types during one study session rather than blocked practice. It trains the brain to categorize and select the appropriate strategy dynamically."
                }
            ]
        }
    ],
    "notes": [
        {
            "id": "n1",
            "title": "Feynman Technique Master Guide",
            "topic": "Study Strategies",
            "content": "1. Pick a concept.\n2. Explain it as if teaching a 12-year-old using simple words and vivid analogies.\n3. Spot your explanation gaps whenever you rely on technical jargon.\n4. Re-read source material and refine until crystal clear.",
            "updated_at": "Today, 10:15 AM"
        },
        {
            "id": "n2",
            "title": "Optimal Pomodoro Interval Structuring",
            "topic": "Productivity",
            "content": "Standard interval: 25 min deep work, 5 min physical break.\nUltradian rhythm variation: 50 min high focus followed by 10 min rest.\nKey rule: Never check social media during short breaks; allow default mode network recovery.",
            "updated_at": "Today, 11:40 AM"
        }
    ],
    "stats": {
        "pomodoros_completed": 3,
        "study_minutes": 75,
        "cards_reviewed": 18,
        "streak_days": 4
    }
}

def get_data() -> dict:
    """Retrieve data from study_data.json or initialize with defaults."""
    if not DATA_FILE.exists():
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading {DATA_FILE}: {e}")
        return DEFAULT_DATA

def save_data(data: dict):
    """Write data to study_data.json."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error writing {DATA_FILE}: {e}")

def add_deck(title: str, description: str, category: str = "General", color: str = "#6366F1", cards: list = None) -> dict:
    data = get_data()
    deck_id = f"deck-{int(time.time()*1000)}"
    new_deck = {
        "id": deck_id,
        "title": title,
        "description": description,
        "category": category,
        "color": color,
        "cards": cards or []
    }
    data.setdefault("decks", []).append(new_deck)
    save_data(data)
    return new_deck

def delete_deck(deck_id: str):
    data = get_data()
    data["decks"] = [d for d in data.get("decks", []) if d["id"] != deck_id]
    save_data(data)

def add_card_to_deck(deck_id: str, front: str, back: str) -> dict:
    data = get_data()
    for deck in data.get("decks", []):
        if deck["id"] == deck_id:
            new_card = {
                "id": f"card-{int(time.time()*1000)}",
                "front": front,
                "back": back
            }
            deck.setdefault("cards", []).append(new_card)
            save_data(data)
            return new_card
    return {}

def delete_card_from_deck(deck_id: str, card_id: str):
    data = get_data()
    for deck in data.get("decks", []):
        if deck["id"] == deck_id:
            deck["cards"] = [c for c in deck.get("cards", []) if c["id"] != card_id]
            break
    save_data(data)

def save_note(title: str, topic: str, content: str, note_id: str = None) -> dict:
    data = get_data()
    now_str = time.strftime("%b %d, %I:%M %p")
    if note_id:
        for n in data.get("notes", []):
            if n["id"] == note_id:
                n["title"] = title
                n["topic"] = topic or "General"
                n["content"] = content
                n["updated_at"] = now_str
                save_data(data)
                return n
    new_note = {
        "id": f"note-{int(time.time()*1000)}",
        "title": title,
        "topic": topic or "General",
        "content": content,
        "updated_at": now_str
    }
    data.setdefault("notes", []).append(new_note)
    save_data(data)
    return new_note

def delete_note(note_id: str):
    data = get_data()
    data["notes"] = [n for n in data.get("notes", []) if n["id"] != note_id]
    save_data(data)

def increment_stat(name: str, value: int = 1) -> dict:
    data = get_data()
    stats = data.setdefault("stats", {})
    if name in ["pomodoros_completed", "study_minutes", "cards_reviewed", "streak_days"]:
        stats[name] = stats.get(name, 0) + value
        save_data(data)
    return stats
