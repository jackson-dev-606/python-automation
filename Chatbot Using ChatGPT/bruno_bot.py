"""
Create a chatbot called BrunoBotNatch, which will answer his employees questions even when the real Bruno is busy doing something else.
"""
from openai import OpenAI
from dotenv import dotenv_values

env_variables = dotenv_values(".env")
client = OpenAI(api_key=env_variables["OPEN_AI_KEY"])

user_question = input("Ask Bruno a question!\n")
message = [{
    "role": "system",
    "content": [{
        "type": "input_text",
        "text": "You are BrunoBotNatch, a chatbot that would answer Bruno's employees questions even when the real Bruno is busy doing something else. Bruno is a demanding, but fair leader with a blunt communication style, but also has a dry sense of humor. When replying to the user, make sure to provide Bruno's personality and communication style so that users conversing with the chatbot gets the real Bruno experience as possible."
    }]
},
{
    "role": "user",
    "content": [{
        "type": "input_text",
        "text": user_question
    }]
}]

while True:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=message,
        text={"format":{"type":"text"}},
        temperature=0.5,
        max_output_tokens=1000,
        top_p=1
    )
    print(response.output[0].content[0].text)
    message.append({
        "role":"assistant",
        "content": [{
            "type": "output_text",
            "text": response.output[0].content[0].text
        }]
    })

    next_question = input("Respond to Bruno with another question (or type 'thanks' to exit):\n")
    if next_question.lower() == "thanks":
        break

    message.append({
        "role":"user",
        "content": [{
            "type": "input_text",
            "text": next_question
        }]
    })

