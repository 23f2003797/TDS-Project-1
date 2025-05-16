# TDS Virtual TA

An automated Teaching Assistant for the IITM TDS course.

## Features
- Answer questions based on course content & Discourse discussions
- Supports screenshot-based questions (OCR)
- Simple API endpoint using FastAPI

## Usage
```bash
curl "https://app.example.com/api/" \
  -H "Content-Type: application/json" \
  -d '{"question": "Should I use gpt-4o-mini which AI proxy supports, or gpt3.5 turbo?", "image": "$(base64 -w0 example.webp)"}'
```

## Run locally
```bash
uvicorn app.main:app --reload
```
