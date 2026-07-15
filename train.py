import res.values as values
import res.functions as functions
import random

i = 0
while i <= 100:
    functions.train(values.numbers[random.randint(0, 9)])
    i = i + 1
    print(f"""
You completed {i} questions,
you must finish another {100 - i} questions.
if you sabotage, I WILL KNOW.
""")