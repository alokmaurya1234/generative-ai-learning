from pathlib import Path
import os
from dotenv import load_dotenv
from typesafe_sdk import TypeSafeClient, Choice, Score, Noul

# Explicitly load the .env file from the jevpilot root directory
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

gateway_url = os.getenv("VERCEL_GATEWAY_URL")
gateway_key = os.getenv("AI_GATEWAY_API_KEY")

client = TypeSafeClient(
    api_key=gateway_key,
    base_url=f"{gateway_url}/typesafe"
)

print(f"Loaded Gateway URL: {gateway_url}")  # Quick check to ensure it is not None

# Initialize the client pointing to Vercel Gateway
client = TypeSafeClient(
    api_key=gateway_key,
    base_url=f"{gateway_url}/typesafe"
)

# 1. Define the State
state = {
    "ticket": "I was charged twice for my subscription this month and I want a refund right now! I am locked out of my dashboard."
}

# 2. Evaluate the state using Jev's typed questions
try:
    response = client.system_one(
        state=state,
        questions={
            "department": Choice(
                instructions="Which department should handle this request?",
                criteria={
                    "billing": "Questions about payments, refunds, and charges",
                    "technical": "App crashes, bugs, and login issues",
                    "general": "Other inquiries"
                }
            ),
            "severity": Score(
                instructions="Rate the customer's frustration level.",
                criteria=[
                    "Neutral or polite",
                    "Slightly annoyed",
                    "Very angry or urgent"
                ]
            ),
            "wants_refund": Noul(
                instructions="Is the customer explicitly asking for a refund?"
            )
        }
    )

    # 3. Extract and print the answers
    dept = response.answers["department"]
    wants_refund = response.answers["wants_refund"]
    severity = response.answers["severity"]

    print(f"Selected Department: {dept.choice} (Confidence: {dept.confidence:.2f})")
    print(f"Refund Request Probability: {wants_refund.probability:.2f}")
    print(f"Severity Score: {severity.score:.2f}")

except Exception as e:
    print(f"Gateway Routing Error: {e}")