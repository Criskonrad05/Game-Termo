import sys

class colors:
    WHITE = '\033[97m'
    BLACK = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    PURPLE = '\033[0;38;5;129m'

    @staticmethod
    def colour(texto, cor):
        return cor + texto + colors.WHITE

def clean(): # apaga a ultima linha que foi utilizada
    
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def validate_word(message, string):
    laps = 0
    while True:
            word = input (message)

            if not check_number(word):
                laps += 1
                print("Digite apenas palavras válidas")
                continue
            elif len(word) != string:
                laps += 1
                print("A palavra deve ter 5 apenas letras.")
                continue
            break
    return word

def check_number(string):
    for i in range (len(string)):
        try:
            num = int (string[i])           
            return False
        except ValueError:           
            continue
          
    return True   

def input_valided(message):# verifica se o valor é valido
    while True:        
             value = input(message) 
             try: 
                value = int(value) 
             except ValueError: 
                print("Opção inválida.") 
                continue 
             break
    return int(value)
