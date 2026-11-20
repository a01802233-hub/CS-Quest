"""CS Quest – a Duolingo-style quiz for Computer Science Topic 1 (Data Representation).

Run:  python3 app.py            then open http://localhost:8000
Only the Python standard library is used (no installs needed).
"""
import json
import os
import random
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import questions as Q

HERE = os.path.dirname(os.path.abspath(__file__))
LESSONS = Q.lessons()


def public_question(q):
    """Question data that is safe to send to the browser (no answers)."""
    base = {"id": q["id"], "type": q["type"]}
    if q["type"] == "choice":
        opts = q["options"][:]
        random.shuffle(opts)
        base.update(instruction="Select the correct answer", prompt=q["prompt"], options=opts)
    elif q["type"] == "blank":
        base.update(instruction="Fill in the blank" + ("s" if len(q["answers"]) > 1 else ""),
                    parts=q["prompt"].split("___"))
    else:
        base.update(instruction="Type your answer", prompt=q["prompt"],
                    placeholder="Type here…")
    return base


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json"):
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path in ("/", "/index.html"):
            with open(os.path.join(HERE, "index.html"), "rb") as f:
                return self._send(200, f.read(), "text/html")
        if path == "/api/lessons":
            return self._send(200, [
                {"id": l["id"], "section": l["section"], "unit": l["unit"],
                 "title": l["title"], "count": len(l["ids"])} for l in LESSONS])
        if path.startswith("/api/lessons/"):
            try:
                lesson = LESSONS[int(path.rsplit("/", 1)[1])]
            except (ValueError, IndexError):
                return self._send(404, {"error": "no such lesson"})
            qs = [public_question(Q.QUESTIONS[i]) for i in lesson["ids"]]
            random.shuffle(qs)
            return self._send(200, {"id": lesson["id"], "title": lesson["title"], "questions": qs})
        self._send(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/api/check":
            return self._send(404, {"error": "not found"})
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length))
            q = Q.QUESTIONS[int(body["id"])]
        except (ValueError, KeyError, IndexError, json.JSONDecodeError):
            return self._send(400, {"error": "bad request"})
        ok = Q.grade(q, body.get("answer"))
        self._send(200, {"correct": ok,
                         "explanation": q["explanation"],
                         "answer": Q.correct_display(q)})

    def log_message(self, fmt, *args):  # quieter console
        pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"CS Quest running → http://localhost:{port}   (Ctrl+C to stop)")
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
