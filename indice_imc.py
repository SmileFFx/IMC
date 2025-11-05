while True:
    # Ler dados do usuário (input retorna string)
    nome = input("Nome: ")
    idade = input("Idade: ")

    # Ler altura e peso e converter para float para poder calcular
    # Repetir o prompt enquanto a entrada for inválida, sem fechar o programa
    while True:
        try:
            altura_metros = float(input("Altura em metros: ").replace(',', '.').strip())
            if altura_metros <= 0:
                print("Altura deve ser maior que zero. Tente novamente.")
                continue
            break
        except ValueError:
            print("Altura inválida. Digite um número como 1.75 ou 1,75.")
        except (KeyboardInterrupt, EOFError):
            print("\nEntrada cancelada pelo usuário.")      
            raise SystemExit(1)

    while True:
        try:
            peso = float(input("Peso em kg: ").replace(',', '.').strip())
            if peso <= 0:
                print("Peso deve ser maior que zero. Tente novamente.")
                continue
            break
        except ValueError:
            print("Peso inválido. Digite um número como 70.5 ou 70,5.")
        except (KeyboardInterrupt, EOFError):
            print("\nEntrada cancelada pelo usuário.")
            raise SystemExit(1)

    # Calcular IMC: peso dividido pela altura ao quadrado
    imc = peso / (altura_metros ** 2)
    resultado = imc

    # Classificar o IMC em categorias e imprimir mensagem correspondente
    if imc <= 18.5:
        print(f"{nome}, você está abaixo do peso, com {resultado:.2f} de IMC, e precisa ganhar massa muscular de forma saudável.")
    elif 18.5 < imc <= 24.9:
        print(f"{nome}, você está com o peso ideal, com {resultado:.2f} de IMC, continue assim!")
    elif 25 <= imc <= 29.9:
        print(f"{nome}, você está com sobrepeso, com {resultado:.2f} de IMC, cuidado para não desenvolver doenças relacionadas.")
    else:
        print(f"{nome}, você está com obesidade, com {resultado:.2f} de IMC, procure um médico para uma avaliação detalhada.")

    # Perguntar se deseja sair ou reiniciar
    sair = input("\nDeseja sair? (sim/não): ").strip().lower()
    if sair in ['sim', 's']:
        print("Programa encerrado. Até logo!")
        break
    else:
        print("\nReiniciando o programa...\n")
