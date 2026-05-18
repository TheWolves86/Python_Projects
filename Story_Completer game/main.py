with open("story.txt", "r", encoding="utf-8") as f:
    story = f.read()

words = set()
start_of_word = -1

starting_index = "<"
ending_index = ">"

for i, chars in enumerate(story):
    if chars == starting_index:
        start_of_word = i
    if chars == ending_index and start_of_word != -1:
        word = story[start_of_word: i+1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input(f"What is the answer for {word}? ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)