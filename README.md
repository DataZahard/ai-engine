# Rayeva – AI Systems (Sustainable Commerce)

### Developer: DataZahard
**Role:** Full Stack / AI Intern Assignment  
**Focus:** Applied AI for Sustainable Commerce  

---

## 🏗️ Architecture Overview
This project implements a **Decoupled AI Service Architecture**. By separating the AI orchestration (`ai_engine.py`) from the business logic and database layer, the system remains scalable and model-agnostic.

* **Backend:** FastAPI (Asynchronous Python)
* **Database:** SQLite (SQLAlchemy ORM) for local persistence in Termux.
* **AI Layer:** ~~OpenAI GPT-4o-mini~~ → Mocked AI Logic (Architected for GPT-4o-mini/Gemini integration).
* **State Management:** Automated status logging and human-intervention flagging.

---

## 🛠️ Implemented Modules

### Module 1: AI Auto-Category & Tag Generator
- **Logic:** Extracts product intent from raw descriptions.
- **Features:** Auto-assigns primary categories (Home, Personal Care, etc.), generates SEO tags, and maps sustainability filters (e.g., plastic-free).
- **Output:** Validated JSON stored directly in the `products` table.

### Module 4: AI WhatsApp Support Bot
- **Logic:** A "Database-Grounded" chat agent.
- **Features:** It does not hallucinate; it queries order status from the DB. 

---

## 🚀 Setup & Installation (Termux)

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/DataZahard/ai-engine.git](https://github.com/DataZahard/ai-engine.git)
   cd ai_engine
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration:**
   This version uses a Mock AI Engine for demonstration. No API key or .env file is required to run the current build.


4. **Run the Server:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## 🧠 AI Prompt Design Strategy

* **Role-Based Prompting:**The AI is initialized as a "Sustainable Supply Chain Auditor" to ensure technical accuracy in tagging.
* **Structured Outputs:**We use response_format={ "type": "json_object" } to ensure the AI never returns prose, only parseable data.
* **Logic Grounding:**The WhatsApp bot is provided with "Order Context" in the prompt to prevent hallucinations regarding delivery dates.

## ​📐 Planned Modules (Architecture Only)

* **Module 2 (B2B Proposal):**Logic involves a weighted scoring algorithm to match client budget with high-margin sustainable stock.
* **Module 3 (Impact Reporting):**Uses mathematical constants (e.g., CO2 saved per kg of bamboo) to generate human-readable impact statements.

## 📹 Demo Video

* **Google drive link:**https://drive.google.com/file/d/1TJIbU7wykt5p92fk5h9Prg1ws9xNg_Mh/view?usp=drivesdk
