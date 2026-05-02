---
name: voice-assistant
version: 1.0.0
description: Voice input/output capabilities - speech-to-text, text-to-speech, and voice mode for hands-free interaction
category: productivity
tags: [voice, tts, stt, whisper, elevenlabs, audio]
tools: [terminal, file]
---

# Voice Assistant

Full voice interaction capabilities for Yusuf Mussa - speech recognition, text-to-speech, and voice mode.

## Capabilities

- **Speech-to-Text**: Transcribe audio files and real-time speech
- **Text-to-Speech**: Generate natural-sounding audio from text
- **Voice Mode**: Continuous voice conversation mode
- **Multi-Language**: Support for 50+ languages
- **Audio Processing**: Format conversion, noise reduction

## Speech-to-Text Options

| Engine | Quality | Speed | Cost |
|--------|---------|-------|------|
| Whisper (OpenAI) | Excellent | Medium | Free (local) |
| Deepgram | Excellent | Fast | Pay-per-use |
| Google STT | Good | Fast | Pay-per-use |

## Text-to-Speech Options

| Engine | Quality | Voices | Cost |
|--------|---------|--------|------|
| Edge TTS | Good | 100+ | Free |
| ElevenLabs | Excellent | 1000+ | Pay-per-use |
| OpenAI TTS | Excellent | 6 | Pay-per-use |
| NeuTTS | Good | 10+ | Free |

## Usage Examples

User: "Transcribe this audio file"
→ Use Whisper to convert speech to text

User: "Read this text aloud"
→ Generate TTS audio and play it

User: "Let's have a voice conversation"
→ Enter voice mode with continuous STT/TTS loop
