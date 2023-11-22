import sys
from  components import container_two
import random

def attempt_word(message): 
    
    attempt = container_two.validate_word(message, 5)
    container_two.clean()
    return attempt

def random_word(list_word): # gera uma palavra aleatória
    
    list_word = [word.strip() for word in list_word]
    word_discover = random.choice(list_word).strip()

    return word_discover

def analyze_word(attempt, word_term): 
    letter_used = [] 
    result = [1, 2, 3, 4, 5]

    for x in range (len(attempt)):
        if attempt[x] not in word_term: 
            result[x] = container_two.colors.colour(attempt[x], container_two.colors.WHITE) # verifica se a letra não está na palavra secreta
    for x in range (len(attempt)):
        if attempt[x] in word_term and attempt[x] not in letter_used:
            result[x] = container_two.colors.colour(attempt[x], container_two.colors.RED) # verifica se tem a letra na palavra e nao esta na posição certa
            letter_used.append(attempt[x])
    for x in range (len(attempt)): 
        if attempt [x] == word_term[x]: 
            result[x] = container_two.colors.colour(attempt[x], container_two.colors.GREEN) # verifica se a letra da palavra digitada está na mesma posição da palavra secreta
            letter_used.append(attempt[x])

    if word_term == attempt:
            return True, result
 
    return False, result

def add_word(word_discover): # adicionar a palavra sorteada no arquivo

    file = open('word_used.txt', 'a')
    file.write(str(f'{word_discover}\n'))
    file.close()

    return True

def word_already_used(word_discover): # verifica se a palavra existe no arquivo de palavras usadas
    
    file = open('word_used.txt', 'r') 
    if word_discover in file:
        file.close()
        return True
    file.close()
    return False

def delete_words_used (): # função pra deletar as palavras usadas
  
    word = open('word_used.txt', 'w')
    word.close ()
    print("Palavars Deletadas")

def exit(): # Função para sair 
    print("Você saiu. Volte Sempre")
    sys.exit()
