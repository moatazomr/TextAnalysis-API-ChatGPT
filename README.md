
 

## Text Analysis Toolbox API Using ChatGPT

**Introduction** 

This project aims to create a comprehensive API to cover common text analysis tasks by using ChatGPT  without having to worry about prompt engineering or other technical details. Simply input the text you want to analyze and let our API handle the rest. 

To achieve this, I followed recursive approach by utilizing ChatGPT itself  to help in identifing its top text analsysis use cases can be done by ChatGPT  then what are sample prompts for it? then ask it to converted it into a user-friendly API to facilitate text analysis taks.

  
**Project Details**

The project's outcome is creating a RESTful API for a text analysis toolbox that perform a variety of  text transformation tasks  including the following:

- **Text completion:** Given a prompt or incomplete sentence, generate the most likely continuation or next word(s).
- **Language modeling:** Train a language model on a text corpus to generate new text.
- **Text generation:** Generate new text based on a given prompt or context.
- **Text summarization:** Generate a shorter version of a longer text while preserving its main ideas and important details.
- **Text correction:** Correct spelling, grammar, and punctuation errors in a given text.
- **Text normalization:** Convert text in different formats or representations to a standard format, such as converting abbreviations to their full forms or normalizing numbers and dates.
- **Text formatting:** Format text in a specific way, such as capitalizing the first letter of each sentence or adding line breaks at regular intervals.
- **Text clustering:** Group similar texts together based on their content or features.
- **Text classification:** Categorize text into predefined classes or categories based on their content or features.
- **Named entity recognition:** Identify and extract named entities such as people, organizations, and locations from a given text.
- **Text similarity:** Measure the similarity between two or more texts based on their content or features.
- **Sentiment analysis:** Analyze the sentiment or emotion expressed in a given text and categorize it as positive, negative, or neutral.
- **Text tagging:** Assign tags or labels to different parts of a given text, such as parts of speech or semantic categories.
- **Text embedding:** Represent a given text as a numerical vector in a high-dimensional space, which can be used for various downstream tasks such as text classification and clustering.

First step, I used ChatGPT  to generate a full list of prompts for each of the supported text transformation operations. The prompts include the input text, desired operation, and relevant tuning parameters. This list is formatted in JSON format for easy use in the next step of creating the API layer on top of ChatGPT. The API will allow users to send text data along with the specified operation and tuning parameters, and receive the corresponding transformed text as the response from ChatGPT.

> Create a JSON list with the following format:
> {full_prompt_input, input_text, operation, parameters}. The input_text
> represents the text to be processed by ChatGPT, and the operation
> specifies the required  text transformation  such as summarization,
> inference,  sentiment analysis,  language translation,  question
> answering, or text classification. The  parameters field  includes all
> applicable  tuning parameters  used by the operation, such as
> max_length, temperature, language, or category_count.
 

The response is like :
```javascript
 [
  {
    "prompt": "Summarize the following sentence below, delimited by triple backticks, in at most `max_length`:\n\n```\n`input_text`\n```",
    "operation": "Summarization",
    "parameters": {
      "max_length": 50,
      "temperature": 0.8
    }
  },
  {
    "prompt": "Infer the sentiment of the following sentence below, delimited by triple backticks:\n\n```\n`input_text`\n```",
    "operation": "Sentiment Analysis",
    "parameters": {
      "model": "bert-base",
      "score_type": "polarity"
    }
  },
  {
    "prompt": "Translate the following sentence below, delimited by triple backticks, from `source_language` to `target_language`:\n\n```\n`input_text`\n```",
    "operation": "Language Translation",
    "parameters": {
      "source_language": "en",
      "target_language": "es"
    }
  },
  {
    "prompt": "Answer the following question below, delimited by triple backticks, in at most `max_length`.\n\n```\n`input_text`\n```",
    "operation": "Question Answering",
    "parameters": {
      "model": "bert-large-uncased-whole-word-masking-finetuned-squad",
      "max_length": 50
    }
  }
]
```
This list includes different operations: Summarization, Sentiment Analysis, Language Translation, and Question Answering. For each operation, there is a prompt that specifies the required input format and any relevant tuning parameters. The `input_text` field represents the text that needs to be processed by ChatGPT, while the `parameters` field includes any required tuning parameters for the specified operation.


Then , I built following prompt to ask ChatGPT to create a Python Restful API  that utilizes the  ChatGPT API  for various text processing tasks based on above JSON list.
 
> Create a Python API based on the JSON list provided. The API should
> have a route equal to the operation specified in the JSON. The API
> should take in input_text, along with any required parameters
> specified in the JSON.
> 
> The API should generate the required prompt by inserting the
> input_text between triple backticks and replacing any required
> parameters with their corresponding values. The generated prompt
> should be used as an input to the ChatGPT API, and the output returned
> by ChatGPT should be returned as the response from the Python API.
> 
> For example, if the operation in the JSON is "Summarization", the
> Python API should have a route /summarization and take in input_text
> and max_length as parameters. The API should generate a prompt like
> "Summarize the following sentence below, delimited by triple
> backticks, in at most max_length.", insert input_text between the
> triple backticks, call the ChatGPT API with the generated prompt, and
> return the output as the API response.




```Python
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

```

In this implementation, we first load the JSON list of prompts from a file. We then define a function  `generate_prompt`  that takes in a prompt, input_text, and parameters and generates the final prompt by replacing any placeholders in the prompt with the actual input_text and parameters, and adding  triple backticks  around the input_text then define the  API routes  dynamically based on the operations in the prompts. For each prompt,  When this route is hit, we extract the input_text and parameters from the request, generate the prompt using the  `generate_prompt`  function, call the  ChatGPT API  with the generated prompt, and return the output from ChatGPT as the API response.

Please note that this is just an example implementation and may need to be adapted or extended depending on your specific use case and requirements.

Now I need to build documentation for this API so I used following prompt to generate Swaager file to describe this API based on supported operations 

> regarding above code for text analysis api , create complete swagger
> yaml file for this api have different routes per operation with
> description for each field and example for input output

You may need Iterative prompts to tune your output 

> Regenerate swagger file to include full set of operations in this json
> as spererated endpoint with structured paramters with example and
> description
> 
>  Generate for all operations and make all routes and parameters in
> camel case.

The output is valid swagger file with well documendating APIs as below:

![image](https://user-images.githubusercontent.com/9541045/235903406-6d41cea0-35f4-465f-af0d-f0ce2353c0bf.png)


You can find full generated files and source code in repo.

**Conclusion** 


ChatGPT is  a powerful tool that can greatly assist in rapid development and documentation for various processing tasks. However, despite its impressive capabilities, it still requires human intervention for fine-tuning and validating the output. This is because the quality of the generated output depends on various factors, such as the quality of the  input text  and the prompt used to generate the response.

To get the most out of ChatGPT, developers must adopt an iterative approach to generate more powerful results. This means learning how to prompt the model in the most effective way and experimenting with different inputs and parameters to achieve the desired output.

Using ChatGPT for  rapid development  also requires a mindset shift from doing everything manually to leveraging the power of  AI  to speed up the development process. This may involve learning new skills and techniques, as well as being open to new ideas and approaches.

As compelling proof of this conclusion, the entire project - including the  source code,  Swagger documentation, and even this readme - was almost constructed using prompts on ChatGPT. This demonstrates the power and effectiveness of using ChatGPT in the development process. 



Note: project is intended for demonstration purposes only, mentioned prompts may be not final as it requires iterative tuning to get good results. 
