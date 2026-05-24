import os

from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_diagnostic_report(
    analysis_data
):

    prompt = f"""
You are a senior network security support engineer.

Analyze the following packet capture summary.

Generate:

1. Root cause summary
2. Security observations
3. Troubleshooting recommendations
4. Severity assessment

Packet Analysis Data:
{analysis_data}
"""

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert "
                    "network troubleshooting engineer."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content