from ollama import chat

def ask(query):
    # Call the chat function with the model and query
    response = chat(
        model='llama3.2:latest',
        messages=[
            {'role': 'user', 'content': query}
        ],
        options={'temperature': 0.0,
                 'seed': 420}
    )

    # Return the content of the message
    return response['message']['content']

