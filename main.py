import random
import dictbase

def choice():
    first_Choice = dict(random.choice(dictbase.data))
    return first_Choice

print(choice())

#print(data[0]["name"])


#Output --> Instagram  346 A social media plataform Unite States Of America
#
# for i in data[0]:
#    print(data[0][i])


