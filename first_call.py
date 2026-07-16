import os
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=200,
    messages=[
        {
            "role":"user",
            "content":"In one sentence, what is an AI engineer?"
         }
    ]
)

for block in response.content:
    if block.type == "text":
        print(block.text)

usage = response.usage
print("input tokens: ",usage.input_tokens)
print("output tokens: ",usage.output_tokens)