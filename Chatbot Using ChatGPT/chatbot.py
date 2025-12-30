from openai import OpenAI
from dotenv import dotenv_values

env_variables = dotenv_values(".env")
client = OpenAI(api_key=env_variables["OPEN_AI_KEY"])

famous_person = input("What celebrity would you like to talk to?\n")
initial_prompt = input(f"Ok! Now ask {famous_person} a question!\n")
initial_prompt += initial_prompt + " Please limit the response to a single response."
creativity = input("How creative do you want the response to be (on a scale from 0-10)?\n")

creativity_num = float(creativity)/5
messages = [
    {
      "role": "system",
      "content": [
        {
          "type": "input_text",
          "text": f"You are {famous_person}. Please respond from that person's perspective, as though you are, in fact, {famous_person}."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
            "type": "input_text",
            "text": initial_prompt
        }
      ]
    }
]

while True:
    response = client.responses.create(
      model="gpt-4.1-mini",
      input= messages,
      text={"format": {"type": "text"}},
      reasoning={},
      tools=[],
      temperature=creativity_num,
      max_output_tokens=2048,
      top_p=1,
      store=False,
      include=["web_search_call.action.sources"]
    )
    print(response.output[0].content[0].text)

    messages.append({"role":"assistant", "content": [
        {"type": "output_text", "text":  response.output[0].content[0].text}
    ]})

    prompt = input(f"Respond to {famous_person} (or type 'bye' to exit):\n")
    if prompt.lower() == "bye":
        break

    messages.append({"role":"user", "content": [
        {"type": "input_text", "text": prompt}
    ]})