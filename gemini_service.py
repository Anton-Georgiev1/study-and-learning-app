"""
Google Gemini API integration service.
Handles requests using Python's standard library (urllib.request).
"""

import json
import os
import urllib.request
import urllib.error

MODELS_TO_TRY = ["gemini-3.5-flash-lite", "gemini-3.6-flash"]

def get_api_key() -> str:
    """Retrieve GEMINI_API_KEY from environment."""
    return os.environ.get("GEMINI_API_KEY", "").strip()

def call_gemini(prompt: str, system_instruction: str = None) -> dict:
    """
    Calls Google Gemini REST API using urllib.
    Returns dict with 'text' and 'model' on success, or 'error' on failure.
    """
    api_key = get_api_key()
    if not api_key:
        return {
            "error": "GEMINI_API_KEY is not configured on the server. Please visit the Key Guide tab to set it up."
        }

    last_error = "Unknown error connecting to Gemini API"

    for model in MODELS_TO_TRY:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        if system_instruction:
            payload["systemInstruction"] = {
                "parts": [{"text": system_instruction}]
            }

        data_bytes = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=data_bytes,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "study-learning-app-python"
            },
            method="POST"
        )

        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                resp_body = resp.read().decode("utf-8")
                result = json.loads(resp_body)
                candidates = result.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    text_parts = [p.get("text", "") for p in parts if "text" in p]
                    full_text = "".join(text_parts).strip()
                    if full_text:
                        return {"text": full_text, "model": model}
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode("utf-8", errors="ignore")
            try:
                err_json = json.loads(err_msg)
                message = err_json.get("error", {}).get("message", err_msg)
            except Exception:
                message = err_msg
            last_error = f"Gemini API error ({e.code}): {message}"
            continue
        except Exception as e:
            last_error = f"Connection error: {str(e)}"
            continue

    return {"error": last_error}

def explain_concept(prompt: str, mode: str = "simplify") -> dict:
    """Generate study explanation based on mode."""
    if mode == "simplify":
        sys_prompt = (
            "You are an inspiring educator using the Feynman Technique. "
            "Explain this concept to a curious 12-year-old student using simple language, "
            "vivid everyday analogies, and clear breakdown. Avoid unnecessary jargon."
        )
    elif mode == "summarize":
        sys_prompt = (
            "You are an academic exam prep tutor. Summarize this content into key takeaways, "
            "high-yield exam bullet points, core definitions, and memory hooks."
        )
    else:
        sys_prompt = (
            "You are a supportive university professor and study tutor. Provide a comprehensive, "
            "structured explanation with clear sections, real-world examples, and study tips."
        )

    return call_gemini(prompt, sys_prompt)

def generate_flashcards(text_or_topic: str) -> dict:
    """Generate structured flashcards from text."""
    sys_prompt = (
        "You are an AI study assistant. Generate exactly 4 high-yield flashcards from the provided topic or text. "
        "Output ONLY a valid JSON array of objects with keys 'front' (the question or prompt) and 'back' (the clear, concise answer). "
        "Do NOT include markdown, backticks, or comments. Only the raw JSON array."
    )
    res = call_gemini(f"Create 4 flashcards for:\n{text_or_topic}", sys_prompt)
    if "text" in res:
        raw = res["text"].strip()
        if raw.startswith("```"):
            lines = raw.splitlines()
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]
            raw = "\n".join(lines).strip()
        try:
            cards = json.loads(raw)
            return {"cards": cards}
        except Exception:
            return {"cards": [], "raw_text": res["text"]}
    return res

def generate_quiz(topic: str) -> dict:
    """Generate a 3-question multiple choice quiz."""
    sys_prompt = (
        "You are an academic test maker. Generate 3 multiple choice study questions about the given topic. "
        "Output ONLY a valid JSON array of objects, where each object has: "
        "'question' (string), 'options' (array of 4 distinct strings), 'correct_index' (integer 0-3), and 'explanation' (string). "
        "Do NOT include markdown or backticks. Only the raw JSON array."
    )
    res = call_gemini(f"Create 3 multiple choice questions for topic: {topic}", sys_prompt)
    if "text" in res:
        raw = res["text"].strip()
        if raw.startswith("```"):
            lines = raw.splitlines()
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].startswith("```"):
                lines = lines[:-1]
            raw = "\n".join(lines).strip()
        try:
            quiz = json.loads(raw)
            return {"quiz": quiz}
        except Exception:
            return {"quiz": [], "raw_text": res["text"]}
    return res
