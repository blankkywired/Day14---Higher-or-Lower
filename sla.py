import random
import dictbase


choice_A = {}
choice_B = {}
def choice_celebrity():
    global choice_A
    global choice_B
    choice_A = dict(random.choice(dictbase.data))
    choice_B = dict(random.choice(dictbase.data))


print(choice_B)


print(5 * '\n' , 'VS', 5 * '\n')


#Comparação de dados
#print(escolha1['follower_count']) # Output: Valor de seguidores da primeira escolha
#if escolha1['follower_count'] > 0:
#    print(escolha1['name'], 'Tem mais seguidores')

