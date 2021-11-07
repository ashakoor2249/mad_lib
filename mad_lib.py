#This is a program that simulates a mad libs game.
#Program takes input of seven adjectives, three nouns, and four verbs. Aterwards the story is printed to the screen with
#the inputed words.

def input_adjectives():
    total_adjectives=7
    temp_list=[]
    for count in range(1, (total_adjectives+1)):
        print("Number "+str(count)+":",end='' )
        temp_list.append(input())
    return temp_list

def input_nouns():
    total_nouns=3
    temp_list=[]
    for count in range(1, (total_nouns+1)):
        print("Number "+str(count)+":",end='' )
        temp_list.append(input())
    return temp_list

def input_verbs():
    total_verbs=4
    temp_list=[]
    for count in range(1, (total_verbs+1)):
        print("Number "+str(count)+":",end='' )
        temp_list.append(input())
    return temp_list

def mad_lib_worksheet(a_list, n_list, v_list):
    a_count=0;
    n_count=0
    v_count=0
    print("I walk through the color jungle. I take out my "+a_list[a_count]+" canteen.")
    a_count+=1
    print("There's a "+a_list[a_count]+" parrot with a "+n_list[n_count], end='')
    a_count+=1
    n_count+=1
    print(" in his mouth right in front of me in the "+a_list[a_count]+" trees! ", end='')
    a_count+=1
    print("I gaze at his "+a_list[a_count]+" "+n_list[n_count]+".")
    a_count+=1
    n_count+=1
    print("A sudden sound awakes me from my daydream! A panther's "+v_list[v_count]+" in front of my head!")
    v_count+=1
    print("I "+v_list[v_count]+ " his "+a_list[a_count]+" breath. ", end='')
    v_count+=1
    print("I remember I have a packet of "+n_list[n_count]+ " that makes go into a deep slumber! I "+v_list[v_count])
    v_count+=1
    a_count+=1
    print("it away in front of the "+n_list[n_count]+". Yes he's eating it! I "+v_list[v_count]+" away through the "+a_list[a_count]+" jungle.")
    print("I meet my parents at the tent. Phew. It's been an exciting day in the jungle.")
    return
    
print("Please input seven adjectives")
adjective_list=input_adjectives()

print("Please input three nouns.")
noun_list=input_nouns()

print("Please input four verbs.")
verb_list=input_verbs()

mad_lib_worksheet(adjective_list, noun_list, verb_list)


