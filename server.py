#!/usr/bin/env python3
"""
StudyHub — Smart Learning Web Application
Modular Python HTTP server powering the Dribbble-inspired study platform.
Provides endpoints for decks, flashcards, revision notes, Pomodoro focus stats,
and Google Gemini study assistants with zero third-party dependencies.
"""

import argparse
import json
import os
import sys
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path

# Load local environment if available
ENV_FILE = Path(__file__).parent / ".env"
if ENV_FILE.exists():
    try:
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    if k and not os.environ.get(k):
                        os.environ[k] = v
    except Exception as e:
        print(f"Notice loading .env: {e}")

import gemini_service
import study_storage
import templates


class StudyAppHandler(BaseHTTPRequestHandler):
    """HTTP Request Handler for StudyHub Web App."""

    def log_message(self, format, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

    def send_json(self, status_code: int, data: dict):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        path = self.path.split("?")[0]

        if path in ["/", "/index.html"]:
            html_content = templates.render_app().encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html_content)))
            self.end_headers()
            self.wfile.write(html_content)

        elif path == "/api/status":
            api_key = gemini_service.get_api_key()
            has_key = bool(api_key)
            data = study_storage.get_data()
            key_preview = f"••••{api_key[-4:]}" if (has_key and len(api_key) >= 4) else ("Active" if has_key else "Not configured")
            self.send_json(200, {
                "status": "ok",
                "gemini_configured": has_key,
                "gemini_preview": key_preview,
                "has_stored_key": bool(study_storage.get_stored_api_key()),
                "stats": data.get("stats", {}),
                "decks_count": len(data.get("decks", [])),
                "notes_count": len(data.get("notes", []))
            })

        elif path == "/api/decks":
            data = study_storage.get_data()
            self.send_json(200, {"decks": data.get("decks", [])})

        elif path == "/api/notes":
            data = study_storage.get_data()
            self.send_json(200, {"notes": data.get("notes", [])})

        elif path == "/api/stats":
            data = study_storage.get_data()
            self.send_json(200, data.get("stats", {}))

        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        path = self.path.split("?")[0]
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length) if content_length > 0 else b"{}"

        try:
            body = json.loads(post_data.decode("utf-8")) if post_data else {}
        except Exception:
            body = {}

        if path == "/api/decks":
            title = body.get("title", "").strip()
            desc = body.get("description", "").strip()
            category = body.get("category", "General").strip() or "General"
            if not title:
                self.send_json(400, {"error": "Deck title is required"})
                return
            deck = study_storage.add_deck(title=title, description=desc, category=category)
            self.send_json(201, {"deck": deck})

        elif path == "/api/decks/delete":
            deck_id = body.get("deck_id")
            if deck_id:
                study_storage.delete_deck(deck_id)
            self.send_json(200, {"status": "deleted"})

        elif path == "/api/decks/card":
            deck_id = body.get("deck_id")
            front = body.get("front", "").strip()
            back = body.get("back", "").strip()
            if not deck_id or not front or not back:
                self.send_json(400, {"error": "deck_id, front, and back are required"})
                return
            card = study_storage.add_card_to_deck(deck_id, front, back)
            self.send_json(201, {"card": card})

        elif path == "/api/decks/card/delete":
            deck_id = body.get("deck_id")
            card_id = body.get("card_id")
            if deck_id and card_id:
                study_storage.delete_card_from_deck(deck_id, card_id)
            self.send_json(200, {"status": "deleted"})

        elif path == "/api/notes":
            title = body.get("title", "").strip()
            content = body.get("content", "").strip()
            topic = body.get("topic", "General").strip() or "General"
            note_id = body.get("id")
            if not title or not content:
                self.send_json(400, {"error": "Title and content are required"})
                return
            study_storage.save_note(title, topic, content, note_id)
            data = study_storage.get_data()
            self.send_json(200, {"status": "success", "notes": data.get("notes", [])})

        elif path == "/api/notes/delete":
            note_id = body.get("note_id")
            if note_id:
                study_storage.delete_note(note_id)
            data = study_storage.get_data()
            self.send_json(200, {"status": "deleted", "notes": data.get("notes", [])})

        elif path == "/api/stats/increment":
            stat_name = body.get("name")
            value = int(body.get("value", 1))
            stats = study_storage.increment_stat(stat_name, value)
            self.send_json(200, stats)

        elif path == "/api/gemini/explain":
            prompt = body.get("prompt", "").strip()
            mode = body.get("mode", "simplify")
            if not prompt:
                self.send_json(400, {"error": "Prompt is required"})
                return
            res = gemini_service.explain_concept(prompt, mode)
            status_code = 200 if "text" in res else 400
            self.send_json(status_code, res)

        elif path == "/api/gemini/generate-cards":
            text = body.get("text", "").strip()
            if not text:
                self.send_json(400, {"error": "Topic or study text is required"})
                return
            res = gemini_service.generate_flashcards(text)
            self.send_json(200 if "cards" in res else 400, res)

        elif path == "/api/gemini/quiz":
            topic = body.get("topic", "").strip()
            if not topic:
                self.send_json(400, {"error": "Topic is required"})
                return
            res = gemini_service.generate_quiz(topic)
            self.send_json(200 if "quiz" in res else 400, res)

        elif path == "/api/gemini/key":
            api_key = body.get("api_key", "").strip()
            if not api_key:
                self.send_json(400, {"error": "API key cannot be empty"})
                return
            study_storage.set_stored_api_key(api_key)
            preview = f"••••{api_key[-4:]}" if len(api_key) >= 4 else "Active"
            self.send_json(200, {
                "status": "saved",
                "gemini_configured": True,
                "gemini_preview": preview
            })

        elif path in ["/api/gemini/key/delete", "/api/gemini/delete-key"]:
            study_storage.delete_stored_api_key()
            self.send_json(200, {
                "status": "deleted",
                "gemini_configured": False,
                "gemini_preview": "Not configured"
            })

        else:
            self.send_error(404, "Not Found")


def main():
    parser = argparse.ArgumentParser(description="StudyHub — Python Study & Learning App")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", 3000)), help="Port to listen on (default 3000)")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host address (default 0.0.0.0)")
    args, _ = parser.parse_known_args()

    port = args.port
    host = args.host

    server_address = (host, port)
    httpd = ThreadingHTTPServer(server_address, StudyAppHandler)
    print(f"StudyHub running at http://{host}:{port}/")
    print(f"   Using Python {sys.version.split()[0]} | Pure Standard Library")
    print(f"   Dribbble Aesthetic: White & Dark Themes | Gemini Key: {'Active' if gemini_service.get_api_key() else 'Setup Required'}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()


if __name__ == "__main__":
    main()
