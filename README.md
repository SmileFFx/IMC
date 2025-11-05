# Calculadora de IMC

Calculadora desenvolvida em Python para calcular o Índice de Massa Corporal (IMC) com base na altura e peso do usuário. O programa classifica o IMC em categorias e fornece mensagens personalizadas, permitindo reiniciar ou encerrar a execução de forma interativa.

---

## Funcionalidades

* Solicita nome, idade, altura (m) e peso (kg) do usuário
* Calcula o IMC usando a fórmula: `IMC = peso / (altura ** 2)`
* Classifica o IMC em categorias:

  * Abaixo do peso (≤ 18.5)
  * Peso ideal (18.5 – 24.9)
  * Sobrepeso (25 – 29.9)
  * Obesidade (≥ 30)
* Exibe mensagens personalizadas de acordo com a classificação
* Validação de entradas inválidas
* Permite reiniciar ou encerrar o programa pelo usuário

---

## Como usar

1. Execute o script no terminal:

```
python IMC.py
```

2. Digite seu nome, idade, altura e peso conforme solicitado.
3. O programa exibirá seu IMC e a classificação correspondente.
4. Ao final, escolha se deseja reiniciar ou encerrar o programa.

---

## Exemplo de execução

```
Nome: João
Idade: 28
Altura em metros: 1.80
Peso em kg: 75
João, você está com o peso ideal, com 23.15 de IMC, continue assim!

Deseja sair? (sim/não): n
```

---

## Tecnologias utilizadas

* Python 3.x

---

