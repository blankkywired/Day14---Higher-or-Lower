import random
import dictbase
import draws

#Escolha inicial


#Evita que ocorra escolhas semelhantes entre as duas opções


#print(first_Choice)
#print(second_Choice)


print(f"{draws.image_Logo}\n\n")

gameStart = True
score = 0
def main():
    global user_question
    print(f"\nCompare A: {first_Choice['name']} a {first_Choice['description']}\n{draws.vs_Logo}\n\nAgainst B: {second_Choice['name']}, a {second_Choice['description']}")

    user_question = input("Who has more followers? Type 'A' or 'B': ")
    check_answer(user_question)
    
#Preciso criar uma função aqui para checar as respostas do usuario
def check_answer(answer):
    global score
    if user_question == "A":
        if first_Choice['follower_count'] > second_Choice['follower_count']:
            score += 1
            print(f"\nYou're right!, Current score: {score}")
        else:
            print(f"\nSorry, you're wrong, Final Score: {score}")
            #Parar o loop
            score = -1

    elif user_question == "B":
        if second_Choice['follower_count'] > first_Choice['follower_count']:
            score += 1
            print(f"\nYou're right!, Current score: {score}")
            first_Choice['follower_count'] = second_Choice['follower_count']
        else:
            print(f"\nSorry, you're wrong, Final Score: {score}")
            score = -1 

    else:
        print("Invalid option!, Please insert a valid number(A or B)")


first_Choice = dict(random.choice(dictbase.data))

#Guardar o resultado do maior palpite
#highestFollowerCount = dict()
while gameStart != False:
    if score >= 0:
        second_Choice = dict(random.choice(dictbase.data))
        #Impedir que sejam feita duas escolhas semelhantes
        while first_Choice == second_Choice:
            second_Choice = dict(random.choice(dictbase.data))
        main()
    


    


