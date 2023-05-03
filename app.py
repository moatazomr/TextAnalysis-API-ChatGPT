import json
import requests
from flask import Flask, request

app = Flask(__name__)

# Load the JSON list of prompts
with open('prompts.json') as file:
    prompts = json.load(file)

# Define a function to generate the prompts
def generate_prompt(prompt, input_text, params):
    # Replace any placeholders in the prompt with input_text and params
    for key, value in params.items():
        prompt = prompt.replace(key, str(value))
    prompt = prompt.replace('input_text', input_text)
    # Add triple backticks around the input_text
    prompt = f'```{prompt}```'
    return prompt

# Define the API routes dynamically based on the operations in the prompts
for prompt in prompts:
    operation = prompt['operation']
    route = f'/{operation.lower()}'
    @app.route(route, methods=['POST'])
    def chatgpt():
        # Get the input text and parameters from the request
        input_text = request.form['input_text']
        params = request.form.to_dict()
        del params['input_text']
        # Generate the prompt
        generated_prompt = generate_prompt(prompt['prompt'], input_text, params)
        # Call the ChatGPT API with the generated prompt
        response = requests.post('https://api.openai.com/v1/engine/...',
                                 headers={'Content-Type': 'application/json'},
                                 json={'prompt': generated_prompt})
        # Return the output from ChatGPT as the API response
        return response.json()['choices'][0]['text']
