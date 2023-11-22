from  components import container_one
from  components import container_two
from  components import menus

def start(word):
    menus.start_menu()
    option  = container_two.input_valided(container_two.colors.colour("\t Digite a opção desejada: ", container_two.colors.GREEN))
    if option == 1:
        while True:  
                while True:
                    word_discover = container_one.random_word(word) # verifica se a palavra está no arquivo de palavras usadas
                    if container_one.word_already_used(word_discover) == False:
                        break

                result =  start_game(word_discover) 

                if result:
                    container_one.add_word(word_discover) # adiciona a palavra escolhida no arquivo de palavras usadas
                if start(word) == False:
                    break
    elif option == 2:
        menus.rule()
        input()
        start(word)
    elif option == 3:
        container_one.exit()
    elif option == 4:
        container_one.delete_words_used()
        start(word)
    
    

    return False

def start_game(word_term):
    list_word = []

    for x in range(5):
        while True:
            word = container_one.attempt_word("Digite o palpite: ")
            if word in list_word:
                print("Você já digitou essa palavra.")
                continue
            list_word.append(word)
            break

        result, letter = container_one.analyze_word(word, word_term)

        if result is True:
            print(f"{letter[0]}|{letter[1]}|{letter[2]}|{letter[3]}|{letter[4]}")
            print (container_two.colors.colour("Parabéns você acertou!!", container_two.colors.PURPLE))
            print(f"Palavra: {word_term}")
            list_word.clear()
            return True
        else:
            print(f"{letter[0]}|{letter[1]}|{letter[2]}|{letter[3]}|{letter[4]}")

       
    list_word.clear()
    print("Você errou!!") 
    return False