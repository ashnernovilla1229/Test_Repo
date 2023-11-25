

quiz = {
    "question1": {
        "question": "What is the capital of Philippines?",
        "answer": "Manila"
    },
    "question2": {
        "question": "What is the capital of Korea?",
        "answer": "Seoul"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of United Arab Emirates?",
        "answer": "Abu Dhabi"
    }, "question5": {
        "question": "What is the capital of Malaysia?",
        "answer": "Kuala Lumpur"
    }, "question6": {
        "question": "What is the capital of China?",
        "answer": "Beijing"
    }, "question7": {
        "question": "What is the capital of Vietnam?",
        "answer": "Hanoi"
    },
}

# import pandas as pd
# df = pd.DataFrame.from_dict(quiz, orient='index')

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))
        print("")
        print("")
    else:
        print("Wrong!")
        print("The answer is : " + value['answer'])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score / 7 * 100)) + "%")