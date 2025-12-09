from google.adk.agents.llm_agent import Agent

def weight_loss_plan(user_info: str) -> dict:
    plan = {
        "diet": [
            "- Reduce daily calories by 300-400",
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
            "- Drink 2-3 liters water daily",
            "- Sleep 7-8 hours",
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
