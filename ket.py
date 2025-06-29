
from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
