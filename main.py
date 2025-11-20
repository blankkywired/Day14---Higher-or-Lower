import random
import dictbase
import draws

#Escolha inicial
first_Choice = dict(random.choice(dictbase.data))
second_Choice = dict(random.choice(dictbase.data))

#Evita que ocorra escolhas semelhantes entre as duas opções
while first_Choice == second_Choice:
    first_Choice = dict(random.choice(dictbase.data))

print(first_Choice)
print(second_Choice)


print(f"{draws.image_Logo}\nCompare A: {first_Choice['name']} a {first_Choice['description']}\n{draws.vs_Logo}\nAgainst B: {second_Choice['name']}, a {second_Choice['description']}")

score = 0
user_question = input("Who has more followers? Type 'A' or 'B': ")
#Preciso criar uma função aqui para checar as respostas do usuario
if user_question == "A":
    if first_Choice['follower_count'] > second_Choice['follower_count']:
        score += 1
        print(f"You're right!, Current score: {score}")
    else:
        print(f"Sorry, you're wrong, Final Score: {score}")

elif user_question == "B":
    if second_Choice['follower_count'] > first_Choice['follower_count']:
        score += 1
        print(f"You're right!, Current score: {score}")
    else:
        print(f"Sorry, you're wrong, Final Score: {score}")
else:
    print("Invalid option!, Please insert a valid number(A or B)")




    
















#print(data[0]["name"])


#Output --> Instagram  346 A social media plataform Unite States Of America
#
# for i in data[0]:
#    print(data[0][i])


