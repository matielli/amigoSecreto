import random

def amigo_secreto():
    # Passo 1: Solicitar os nomes dos participantes
    participantes = []
    print("Rafa, Angela, Nice, Alemão, Moisés, Laura (fim):")
    while True:
        nome = input("Nome: ").strip()
        if nome.lower() == 'fim':
            break
        if nome:  # Evitar nomes vazios
            participantes.append(nome)
    
    if len(participantes) < 2:
        print("Número insuficiente de participantes. Adicione pelo menos 2.")
        return
    
    # Passo 2: Embaralhar e distribuir os amigos secretos
    sorteio = participantes[:]
    random.shuffle(sorteio)
    
    # Garantir que ninguém se tire a si mesmo
    for i in range(len(participantes)):
        if participantes[i] == sorteio[i]:
            random.shuffle(sorteio)  # Embaralha novamente
            i = 0  # Reinicia o loop
    
    # Passo 3: Mostrar resultados
    print("\nResultado do Amigo Secreto:")
    for i in range(len(participantes)):
        print(f"{participantes[i]} tirou {sorteio[i]}.")

# Executar o programa
amigo_secreto()
