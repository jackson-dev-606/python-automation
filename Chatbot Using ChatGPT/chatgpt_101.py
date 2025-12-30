from openai import OpenAI
from dotenv import dotenv_values

env_vars = dotenv_values(".env")

client = OpenAI(api_key=env_vars["OPEN_AI_KEY"])

response = client.responses.create(
  model="gpt-4.1-mini",
  input=[
    {
      "role": "system",
      "content": [
        {
          "type": "input_text",
          "text": "You are an executive at a company. You dislike your job, and feel very dissatisfied with your career. This has taken a toll on your demeanor at work, which has become increasingly grumpy. It is also reflected in your writing style, which is best described as sarcastic and passive aggressive."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "Please write a note to your employees, thanking them for all their hard work throughout the year. The message should be at least four paragraphs in length."
        }
      ]
    }
  ],
  text={
    "format": {
      "type": "text"
    }
  },
  reasoning={},
  tools=[],
  temperature=1,
  max_output_tokens=2048,
  top_p=1,
  store=False,
  include=["web_search_call.action.sources"]
)

## Get the output from OpenAI
content = response.output[0].content
text = content[0].text
print(text)