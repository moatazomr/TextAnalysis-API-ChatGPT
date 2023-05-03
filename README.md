 

## Text Analysis Toolbox API Using ChatGPT

The project aims to create a RESTful API for a text analysis toolbox that uses ChatGPT to perform various text analysis tasks, including the following:

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

The API will provide a simple and easy-to-use interface for developers and businesses to integrate text analysis capabilities into their applications. The output can then be used for a variety of applications such as content curation, customer support, language translation, and more. The project demonstrates the power and versatility of modern language models and the potential of AI to revolutionize the field of natural language processing.


t the beginning of the project, ChatGPT is used to generate a full list of prompts for each of the supported text transformation operations. The prompts include the input text, desired operation, and relevant tuning parameters. This list is formatted in JSON format for easy use in the next step of creating the API layer on top of ChatGPT. The API will allow users to send text data along with the specified operation and tuning parameters, and receive the corresponding transformed text as the response from ChatGPT.

> Create a JSON list of 20 items with the following format:
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
    "full_prompt_input": "Summarize a news article about climate change",
    "input_text": "A new study shows that global warming is causing more extreme weather events, such as heat waves, droughts, and hurricanes. The study, published in the journal Nature, found that these events are becoming more frequent and more intense as temperatures continue to rise.",
    "operation": "Summarization",
    "parameters": {
      "max_length": 50,
      "temperature": 0.8
    }
  },
  {
    "full_prompt_input": "Infer the author's opinion on a book review",
    "input_text": "I found this book to be incredibly engaging and thought-provoking. The author's writing style is vivid and captivating, and the characters are well-developed and relatable. However, the plot could be a bit slow at times, and the ending felt somewhat rushed.",
    "operation": "Inference",
    "parameters": {
      "model": "roberta-large",
      "temperature": 0.5
    }
  },
  {
    "full_prompt_input": "Translate a paragraph from English to Spanish",
    "input_text": "The quick brown fox jumps over the lazy dog.",
    "operation": "Language Translation",
    "parameters": {
      "source_language": "en",
      "target_language": "es"
    }
  },
  {
    "full_prompt_input": "Answer a trivia question about history",
    "input_text": "Who was the first president of the United States?",
    "operation": "Question Answering",
    "parameters": {
      "model": "bert-large-uncased-whole-word-masking-finetuned-squad",
      "max_length": 50
    }
  }
] 
```


Here is sample python snippet to test calling actual ChatGPT based on generated prompt

```Python
prompts= [
  {
    "prompt": "Summarize the following sentence below, delimited by triple backticks, in at most `max_length`.",
    "operation": "Summarization",
    "parameters": {
      "max_length": 50,
      "temperature": 0.8
    }
  },
  {
    "prompt": "Infer the sentiment of the following sentence below, delimited by triple backticks: `input_text`.",
    "operation": "Sentiment Analysis",
    "parameters": {
      "model": "bert-base",
      "score_type": "polarity"
    }
  },
  {
    "prompt": "Translate the following sentence below, delimited by triple backticks, from `source_language` to `target_language`: `input_text`.",
    "operation": "Language Translation",
    "parameters": {
      "source_language": "en",
      "target_language": "es"
    }
  },
  {
    "prompt": "Answer the following question below, delimited by triple backticks, in at most `max_length`.",
    "operation": "Question Answering",
    "parameters": {
      "model": "bert-large-uncased-whole-word-masking-finetuned-squad",
      "max_length": 50
    }
  }
]

def generate_prompt(prompt, input_text, params):
    # Replace any placeholders in the prompt with input_text and params
    for key, value in params.items():
        prompt = prompt.replace(key, str(value))
    prompt = prompt.replace('input_text', input_text)
    # Add triple backticks around the input_text
    prompt = f'```{prompt}```'
    return prompt

param = {
      "max_length": 50 ,
    "source_language": "en",
      "target_language": "ar"
    }
print(param)
 

prompt = generate_prompt(prompts[2]['prompt'] ,prod_review , param )

print(prompt)



response = get_completion(prompt)
print(response)
```
