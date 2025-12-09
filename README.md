🧠 Agentic AI Weight-Loss Coach
Built with Google ADK • Gemini 2.5 Flash • Tool-Calling

This project is an Agentic AI system built using Google’s Agent Development Kit (ADK).
It implements a weight-loss coaching agent that intelligently interacts with users, collects basic fitness information, and autonomously calls a tool to generate personalized weight-loss guidance.

The agent runs in the ADK Web UI, which allows easy chat interaction from desktop or mobile.

🚀 Features

Root Agent powered by Gemini 2.5 Flash

Tool Calling (Python function) to generate weight-loss plans

Neat, readable output with bullet-points

Runs in ADK CLI and ADK Web UI

Mobile-friendly via local network access

Simple two-file agent setup (agent.py + __init__.py)

📁 Project Structure
project-root/
│
└── my_agent/
    ├── agent.py
    ├── __init__.py
    └── .env       # contains GOOGLE_API_KEY
│
└── README.md

🛠️ Installation & Setup

Follow these steps exactly to run the agent locally and access the ADK UI.

1️⃣ Install Python Environment
Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

2️⃣ Install Google ADK
pip install google-adk

3️⃣ Add Your API Key

Inside the my_agent folder, create a file named .env:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"

📦 Agent Code
my_agent/agent.py
from google.adk.agents.llm_agent import Agent

def weight_loss_plan(user_info: str) -> dict:
    plan = {
        "diet": [
            "- Reduce daily calories by 300–400",
            "- Eat high-protein meals",
            "- Avoid sugary drinks",
            "- Include vegetables in every meal"
        ],
        "workout": [
            "- 30 minutes brisk walking daily",
            "- 2x/week light strength training",
            "- 10 minutes stretching after workouts"
        ],
        "habits": [
            "- Drink 2–3 liters water daily",
            "- Sleep 7–8 hours",
            "- Avoid late-night snacking"
        ]
    }

    return {
        "status": "success",
        "input_received": user_info,
        "plan": plan
    }

root_agent = Agent(
    model="gemini-2.5-flash",
    name="weight_loss_agent",
    description="A simple agent that guides the user for weight loss.",
    instruction=(
        "You are a professional weight-loss coach. "
        "Ask for details like age, weight, height, and goal. "
        "Whenever the user mentions weight loss, call the 'weight_loss_plan' tool. "
        "Format answers with hyphen bullets and clear spacing. Do NOT use '*' characters."
    ),
    tools=[weight_loss_plan],
)

my_agent/__init__.py
from .agent import root_agent, weight_loss_plan

__all__ = ["root_agent", "weight_loss_plan"]

▶️ Running the Agent
4️⃣ Test in Terminal

From the project root, run:

adk run my_agent


Now chat with your agent in the terminal.

5️⃣ Start ADK Web UI
adk web --host 0.0.0.0 --port 8000


You should see:

Uvicorn running on http://0.0.0.0:8000

📱 Open the Web UI From Phone

Find your PC’s local IP
Windows:

ipconfig


Look for IPv4 Address, e.g. 192.168.1.12

On your phone (same Wi-Fi):

http://192.168.1.12:8000


UI will load → select my_agent → chat with your Agentic AI Weight-Loss Coach.

🔧 Troubleshooting
❌ Site doesn't load on phone

Use PC IP, NOT 0.0.0.0

Ensure both devices are on same Wi-Fi

Allow port 8000 in Windows Firewall:

Run PowerShell as Administrator:
New-NetFirewallRule -DisplayName "Allow ADK 8000" -Direction Inbound -LocalPort 8000 -Protocol TCP -Action Allow

❌ Works on PC but not phone

Phone may be on guest Wi-Fi

PC firewall blocking

Router AP isolation enabled

❌ Still not working?

Use ngrok:

ngrok http 8000


Open the ngrok URL on phone.

📘 What This Project Demonstrates

✔ Agentic AI
✔ LLM reasoning & tool-calling
✔ AI-driven decision-making
✔ Clean, structured outputs
✔ Multi-device UI access
✔ Real AI engineering workflow using Google ADK


