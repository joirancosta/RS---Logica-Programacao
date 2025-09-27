print("Olá, eu sou a sua assistente, Pythrina. O que você quer faze hoje?")

comando = input("Digite um comando: ")

match comando:
    case "oi" | "ola":
        print("Oi, como vai você?")
    case "tchau" | "sair":
        print("Tchau, foi bom conversar com você.")
    case "piada":
        print("Sabes qual é o padroeiro das pessoas que trabalham com TI?")
        print("É o São Login.")
    case "clima":
        print("Tá muuuuuuuito quente! Deve ter passado de 40°C.")
    case _:
        print("Perdão, não entendi o comando.")