from components import container_two

def start_menu(): 
    print(container_two.colors.colour(" Jogo Termo!", container_two.colors.GREEN))
    print (container_two.colors.colour(" 1- Jogar", container_two.colors.WHITE))
    print (container_two.colors.colour(" 2- Regras", container_two.colors.WHITE))
    print (container_two.colors.colour(" 3- Sair", container_two.colors.WHITE))
    print (container_two.colors.colour(" 4- deletar as Palavras que já foram Sorteadas", container_two.colors.WHITE))

def rule():
    print(container_two.colors.colour("Regras:", container_two.colors.RED))
    print("A palavra tem 5 letras, você tem 6 chances para adivinhar a palavra certa. Se a letra estiver no lugar certo ela aparecera de verde, caso ela tenha na palavra mas esta na posição errada ela ficara em vermelho, e caso ela não esteja na palavara ficara branca.")
