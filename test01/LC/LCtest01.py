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
