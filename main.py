from components import start_game
from components import container_one

def main ():
    file = open ("word.txt", "r")

    line = file.readline()

    word = line.split(', ') 
     
    file.close()

    start_game.start(word)

    container_one.exit()
    print("Você saiu. Volte Sempre")
    
main()