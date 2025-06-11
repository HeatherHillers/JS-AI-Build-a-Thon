"""Run this model in Python

> pip install mistralai
"""
import os
from mistralai import Mistral, UserMessage, AssistantMessage, SystemMessage, ToolMessage

# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings.
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
client = Mistral(
    server_url = "https://models.inference.ai.azure.com",
    api_key = os.environ["GITHUB_TOKEN"],
)

response = client.chat.complete(
    model = "mistral-medium-2505",
    messages = [
        UserMessage(content = [
            {
                "type": "text",
                "text": "INSERT_INPUT_HERE",
            },
        ]),
    ],
    temperature = 0.8,
    top_p = 0.1,
)

print(response.choices[0].message.content)
