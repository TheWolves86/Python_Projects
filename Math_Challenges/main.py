import random
import time
Operators = ["+", "-", "*"]
min_value = 3
max_value = 12
wrong = 0
def generate_problem():
    left = random.randint(min_value, max_value)
    right = random.randint(min_value, max_value)
    operator = random.choice(Operators)
    expre = f"{left} {operator} {right}"
    answer = eval(expre)
    return expre, answer


input("Welcome!Pls press enter to start the game.")
print("--------------------------------------")
Total_problems = int(input("How many problems do you want to solve? "))
start_time = time.time()
for i in range(Total_problems):
    problem, answer = generate_problem()
    while True:
        user_guess = int(input(f"{problem} = "))
        if user_guess == answer:
            break
        wrong += 1
end_time = time.time()
solved_time = end_time - start_time
print("Congratts!")
print(f"You solved {Total_problems} problems in {solved_time:.2f} seconds with {wrong} wrong attempts.")