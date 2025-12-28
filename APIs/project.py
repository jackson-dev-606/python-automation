"""
Project: Bruno would like to ask Science and Computer related trivia questions during standup call.
Website: https://opentdb.com/
Goal: Get the number of questions to ask, and the difficulty (easy, medium or hard).
IMP: HTML UNESCAPE should be used to remove all the HTML formats from the text.
"""
import requests
import html
from datetime import datetime
import csv

def load_data_to_csv(question_answers):
    today = datetime.today().date()
    file_name = f"Trivia - {today}.csv"
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Question", "Answer"])
        writer.writerows(question_answers)

number_of_questions = int(input("Please enter the number of trivia questions you'd like to see: "))
difficulty = input("Please specify how difficult you'd like the questions to be (easy/medium/hard): ").lower()

if number_of_questions and difficulty:
    url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy"
    parameters_search = {
        "amount": number_of_questions,
        "category": 18,
        "difficulty": difficulty
    }
    response = requests.get(url, params=parameters_search, headers={"Accept": "application/json"})
    data = response.json()

    trivia_questions = []
    # print(data['results'])
    for item in data["results"]:
        if item['type'] == 'boolean':
            question = f"True or False? {html.unescape(item['question'])}"
        else:
            question = item['question']
        answer = html.unescape(item['correct_answer'])
        # print(question, answer)
        trivia_questions.append([question, answer])

    load_data_to_csv(trivia_questions)