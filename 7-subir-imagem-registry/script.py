import random

def jogo_par_ou_impar():
    print("Bem-vindo ao Jogo do Par ou Ímpar!")
    
    while True:
        # Jogador escolhe par ou ímpar
        jogador_escolha = input("Escolha par (p) ou ímpar (i): ").lower()
        if jogador_escolha not in ['p', 'i']:
            print("Escolha inválida. Tente novamente.")
            continue
        
        # Jogador escolhe um número
        jogador_numero = int(input("Escolha um número (entre 1 e 10): "))

        # Oponente escolhe par ou ímpar aleatoriamente
        oponente_escolha = random.choice(['p', 'i'])
        print(f"O oponente escolheu {oponente_escolha}.")

        # Oponente escolhe um número aleatório
        oponente_numero = random.randint(1, 10)
        print(f"O oponente escolheu o número {oponente_numero}.")

        # Verifica se ambos escolheram par ou ímpar
        if jogador_escolha == oponente_escolha:
            print("Empate! Ambos escolheram par ou ímpar. Repetindo o jogo.")
            continue

        # Calcula a soma dos números
        total = jogador_numero + oponente_numero

        # Determina o vencedor com base na paridade
        resultado = 'p' if total % 2 == 0 else 'i'
        vencedor = "Jogador" if jogador_escolha == resultado else "Oponente"
        
        print(f"Você escolheu {jogador_escolha} e {jogador_numero}.")
        print(f"O oponente escolheu {oponente_escolha} e {oponente_numero}.")
        print(f"A soma dos números é {total}.")

        print(f"{vencedor} venceu!")
        
        jogar_novamente = input("Quer jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até mais.")
            break

# Inicia o jogo
jogo_par_ou_impar()
