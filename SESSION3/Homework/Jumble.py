import random
WORDS = ["random","pick","end","print","character","user","check"]


play = input("Do you want to start?(yes/no)")
while play == "yes":
    word = random.choice(WORDS)
    correct = word
    jumble = ""
    for i in word:
        i = random.randrange(len(word))
        
        jumble += word[i] +", "
        
        word = word[:i] + word[i + 1:]
        
    print(jumble)
    answer = input("\nYour answer: ")
    while answer != correct:
        print(":(")
        answer = input("Your answer: ")
    print("Hura")
    play = input("Do you continus? (yes or no)")


print("Thanks for playing.")
