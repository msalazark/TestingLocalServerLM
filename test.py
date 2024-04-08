from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

completion = client.chat.completions.create(
  model="local-model", # this field is currently unused
  messages=[
    {"role": "system", "content": "Eres un asistente en español y ayudas con respuestas breves."},
    {"role": "user", "content": "Buenos días, ¿cuantos días llueve en Paris al año?"}
  ],
  temperature=0.7,
)

msg = completion.choices[0].message

print(msg.content)