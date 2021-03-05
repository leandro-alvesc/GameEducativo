from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado (1, 2, 3 ou 4): '))

    calc = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(calc.mostrar_resultado())
        print('Acertou!')
        print(f'Você tem {pontos} ponto(s).')
    else:
        print(calc.mostrar_resultado())
        print('Errou!')

    continuar: int = int(input('Deseja continuar? (1 - Sim, 0 - Não) '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você fez {pontos} pontos!')
        print('Até a próxima!')


if __name__ == '__main__':
    main()
