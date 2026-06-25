import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word.encode('utf-8', 'backslashreplace').decode('utf-8'))
guess = input("Guess a letter : ").lower()
print(guess)
for letter in chosen_word :
    if letter == guess :
        print("Correct")
    else :
        print("Wrong")
        
