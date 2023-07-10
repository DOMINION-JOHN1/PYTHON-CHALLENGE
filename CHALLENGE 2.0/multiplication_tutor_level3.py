import random


def get_response(is_correct):
    if is_correct:
        responses = ["Very good!", "Excellent!", "Nice work!", "Keep up the good work!"]
    else:
        responses = ["No. Please try again.", "Wrong. Try once more.", "Don't give up!", "No. Keep trying."]
    return random.choice(responses)


def generate_question():
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    question = f"How much is {num1} times {num2}? "
    answer = num1 * num2
    correct_answer = answer.__str__()
    return question, correct_answer


def main_game():
    num_correct = 0
    num_incorrect = 0
    print("Welcome to the multiplication game!")
    question, correct_answer = generate_question()
    while True:
        user_input = str(input(question))
        if user_input == correct_answer:
            print(get_response(True))
            num_correct += 1
            question, correct_answer = generate_question()
        else:
            print(get_response(False))
            num_incorrect += 1
            question, correct_answer = generate_question()
        if num_correct + num_incorrect == 10:
            percentage_correct = num_correct / (num_correct + num_incorrect) * 100
            if percentage_correct < 75:
                print("Please ask your teacher for extra help.")
            else:
                print("Congratulations, you are ready to go to the next level!")
                break
            break


main_game()
