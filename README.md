# 🛡️ AI Scam Detector

An automated cybersecurity tool designed to detect phishing, social engineering, and scam indicators in text messages or emails using Large Language Models (LLMs).

## 🚀 Features
- **Automated Risk Scoring:** Evaluates text data and returns a definitive risk metric (0-100).
- **Threat Indicator Flags:** Highlights specific manipulation tactics (e.g., Urgency, Financial Requests, Suspicious Links).
- **Technical Analysis Breakdown:** Provides an LLM-powered expert explanation detailing why the input is flagged or deemed safe.
- **Structured JSON Integration:** Leverages Gemini's structured output capability for consistent, reliable telemetry processing.

## 🛠️ Tech Stack
- **Frontend/UI:** Streamlit (Python)
- **Engine:** Google Gemini API (`gemini-2.5-flash`)
- **Data Format:** Structured JSON

## 📦 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ai-scam-detector.git](https://github.com/YOUR_USERNAME/ai-scam-detector.git)
   cd ai-scam-detector