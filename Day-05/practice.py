#Simple Multiple Choice Test
 
from Question import Question


question_prompts = [
    'Apple color?\n(a) Red\n(b) Yelloe\n(c) Purple\n(d) Blue\n\n',
    'Banana color?\n(a) Red\n(b) Yellow\n(c) Purple\n(d) Yellow\n\n',
    'Mango color?\n(a) Red\n(b) Yelloe\n(c) Purple\n(d) Black\n\n'
]

questions = [Question(question_prompts[0], "a"),
             Question(question_prompts[1], "b"),
             Question(question_prompts[2], "b")
]
        
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.query)
        if answer == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} correct")

run_test(questions)



