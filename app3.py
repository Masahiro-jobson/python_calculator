from Question import Question
questions_prompts = [
    "What colors are Apples ?\n(a) Red/Green\n(b) Purple\n(c) Orange \n\n",
    "What colors are Bananas ?\n(a) Teal\n(b) Magenda\n(c) Yellow \n\n",
    "What colors are Strawberries ?\n(a) Yellow\n(b) Red\n(c) Blue \n\n",

]

questions = [
    # Quetstion() refers to Question class
    Question(questions_prompts[0], "a"),
    Question(questions_prompts[1], "c"),
    Question(questions_prompts[2], "b"),

]

# We need questions as an argument of run_test to clarify questions in for loop
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)