from random import randint


class Calcular:

    def __init__(self, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # 1 - somar, 2 - subtrair, 3 - multiplicar
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self) -> int:
        return self.__dificuldade

    @property
    def valor1(self) -> int:
        return self.__valor1

    @property
    def valor2(self) -> int:
        return self.__valor2

    @property
    def operacao(self) -> int:
        return self.__operacao

    @property
    def resultado(self) -> float:
        return self.__resultado

    def __str__(self) -> str:
        if self.operacao == 1:
            op = 'somar'
        elif self.operacao == 2:
            op = 'subtrair'
        elif self.operacao == 3:
            op = 'multiplicar'
        else:
            op = 'operação desonhecida'
        return f'Valor 1: {self.valor1}\nValor 2: {self.valor2}\nDificuldade:{self.dificuldade}\n' \
               f'Operação: {op.title()}'

    @property
    def _gerar_valor(self) -> int:
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(1000, 100000)

    @property
    def _gerar_resultado(self) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2

    @property
    def _op_simbolo(self) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return '*'
        else:
            return ''

    def checar_resultado(self, resposta: int) -> bool:
        if self.resultado == resposta:
            return True
        else:
            return False

    def mostrar_operacao(self) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2}')

    def mostrar_resultado(self) -> str:
        return f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}'
