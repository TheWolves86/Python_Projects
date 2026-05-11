print("Welcome to Quizzzz!")

play = input("Do you want to play? (y/n): ")
if play.lower() == "y":
    score = 0
    no_of_question = 0
    print("Starting the quiz.........")
    print('---------------------------------------------')
    print("Question 1: What is the full form of AI?")
    answer1 = input("Answer: ")
    no_of_question += 1
    if answer1.lower() == "artificial intelligence":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print('---------------------------------------------')
    print("Question 2: Which is the best university for engineering in the world? ")
    answer2 = input("Answer: ")
    no_of_question += 1
    if answer2.lower() == "mit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print('---------------------------------------------')
    print("Question 3: Who is the most richest person in the world? ")
    answer3 = input("Answer: ")
    no_of_question += 1
    if answer3.lower() == "elon musk":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print('---------------------------------------------')
    print("Question 4: Which is the most populated country? ")
    answer4 = input("Answer: ")
    no_of_question += 1
    if answer4.lower() == "india":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print('---------------------------------------------')
    print("Question 5: Which is the largest country(in size)?")
    answer5 = input("Answer: ")
    no_of_question += 1
    if answer5.lower() == "russia":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("Scores incoming.........")
    print(f"You scored {score} marks out of {no_of_question} question. ")
elif play.lower() == "n":
    print("Byeee!")
    exit()