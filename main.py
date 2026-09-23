from ollama import chat

response = chat(
    model='gemma3:1b',
    messages=[{'role': 'user', 'content': 'What is NLP explain in 1 sentence?'}]
)

print(response.message.content)