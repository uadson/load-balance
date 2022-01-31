"""
Problema

Balanceamento de carga é muito importante em ambientes Cloud. Estamos sempre
tentando minimizar os custos para que possamos manter o número de servidores o
menor possível. Em contrapartida a capacidade e performance aumenta quando
adicionamos mais servidores. Em nosso ambiente de simulação, em cada tick
(unidade básica de tempo da simulação), os usuários conectam aos servidores
disponíveis e executam uma tarefa. Cada tarefa leva um número de ticks para
ser ﬁnalizada (o número de ticks de uma tarefa é representado por ttask ), e
após isso o usuário se desconecta automaticamente.

Os servidores são máquinas virtuais que se auto criam para acomodar novos
usuários. Cada servidor custa R$ 1,00 por tick e suporta no máximo umax
usuários simultaneamente. Você deve ﬁnalizar servidores que não estão sendo
mais usados. O desaﬁo é fazer um programa em Python que recebe usuários e os
aloca nos servidores tentando manter o menor custo possível."""


class LoadBalance:

    def __init__(self):
        self.input_file = str()
        self.users = []
        self.tick = int()
        self.ttask = int()
        self.umax = int()
        self.servers = []
        self.cost = int()

    def read_file(self, file_path):
        """[Método para 'ler' o arquivo com os dados de ttask, umax e inputs. E
        salvá-los em uma lista no atributo self.input_file]

        Args:
            file_path ([str]): [input.txt]

        Returns:
            [list]: [4, 2, 1, 3, 0, 1, 0, 1]
        """
        with open(file_path, 'r') as f:
            context = f.readlines()
            self.input_file = [int(context[index].rstrip('\n')) for index in range(len(context))]
        return self.input_file

    def get_ttask(self):
        """[Método para 'recuperar' o valor da ttaks (números de ticks de uma
        tarefa) que está posicionado na primeira linha do arquivo, e salvá-lo
        no atributo self.ttask.
        Antes checa se o valor estão entre os critérios estabelecidos:
        1 <= ttaks <= 10]

        Returns:
            [int]: [4]
        """
        if self.input_file[0] < 0 and self.input_file[0] > 10:
            self.input_file[0] = 4
        self.ttask = self.input_file[0]
        return self.ttask

    def get_umax(self):
        """[Método para 'recuperar' o valor da umax (número máximo de usuários
        simultaneamente conectados por servidor) que está posicionado na
        segunda linha do arquivo, e salvá-lo no atributo self.umax.
        Antes checa se o valor estão entre os critérios estabelecidos:
        1 <= umax <= 10]

        Returns:
            [int]: [2]
        """
        if self.input_file[1] < 0 and self.input_file[1] > 10:
            self.input_file[1] = 2
        self.umax = self.input_file[1]
        return self.umax

    def get_users(self):
        """[Os demais dados são os números de novos usuários para cada tick,
        e serão salvos em uma lista - self.users]

        Returns:
            [list]: [1, 3, 0, 1, 0, 1]
        """
        for user in self.input_file[2:]:
            self.users.append(user)
        return self.users

    def balance(self):
        """[
            1ª Passo
            Verificação da quantidade usuários na primeira posição da fila
            [1, 3, 0, 1] e em seguida fazer a 'distribuição de usuários
            por servidor conforma sua capacidade além da contagem de ticks
        ]

        Returns:
            [type]: [description]
        """
        start = 0
        end = self.ttask
        diff = 0

        # 1ª Passo - ttask 1 - [1, 3, 0, 1]
        # Verifica quantidade de usuários na primeira posição da fila
        first = self.users[0]
        self.tick = sum(self.users[start: end])
        self.cost = self.tick

        #
        if first < self.umax:
            self.servers.append(1)
        #
        if first == self.umax:
            self.servers.append(self.umax)
        #
        if first > self.umax:
            self.servers.append(self.umax)
            diff = (first - self.umax)
            #
            if diff > self.umax:
                self.servers.append(self.umax)
                diff = (diff - self.umax)
            #
            if diff == self.umax:
                self.servers.append(self.umax)
            #
            if diff < self.umax:
                self.servers.append(1)
        #
        # Após verificação a alocação do primeiro(s) usuários da primeira posição,
        # alocar os demais. [3, 0, 1]
        start += 1
        for user in self.users[start: end]:
            if (user + first) > self.umax:
                self.servers.append(self.umax)
                diff = (user + first) - self.umax
            #
            if diff > self.umax:
                self.servers.append(self.umax)
                diff = diff - self.umax
            #
            if diff == self.umax:
                self.servers.append(self.umax)
            #
            if diff < self.umax:
                self.servers.append(1)
            #
            first = user + first

        # Fim do 1ª Passo
        #
        # 2º Passo - ttask 2 - [3, 0, 1, 0]
        # Verifica quantidade de usuários na fila e realiza a alocação dos mesmos
        end += 1
        self.tick = self.tick + sum(self.users[start: end])
        self.cost = self.tick

        for _ in range(1):
            user = sum(self.users[start: end])
            self.servers.append(1)
            if (user - 1) > self.umax:
                self.servers.append(self.umax)
                diff = (user - 1) - self.umax
            #
            if diff > self.umax:
                self.servers.append(self.umax)
                diff = diff - self.umax
            #
            if diff == self.umax:
                self.servers.append(self.umax)
            #
            if diff < self.umax:
                self.servers.append(1)

        # Fim do 2º Passo
        #
        # 3º Passo - ttask 3 - [0, 1, 0, 1]
        # Verifica quantidade de usuários na fila e realiza a alocação dos mesmos
        start += 1
        self.tick = self.tick + sum(self.users[start:])
        self.cost = self.tick

        for _ in range(1):
            user = sum(self.users[start:])
            if user == self.umax:
                self.servers.append(self.umax)
            #
            if user < self.umax:
                self.servers.append(1)
            #
            if user > self.umax:
                self.servers.append(self.umax)
                diff = user - self.umax
            #
            if diff > self.umax:
                self.servers.append(self.umax)
                diff = diff - self.umax
            #
            if diff == self.umax:
                self.servers.append(self.umax)

        # Fim do 3º Passo
        #
        # 4º Passo - ttask 4 - [1, 0, 1, -]
        # Verifica quantidade de usuários na fila e realiza a alocação dos mesmos
        start += 1
        self.tick = self.tick + sum(self.users[start:])
        self.cost = self.tick

        for _ in range(1):
            user = sum(self.users[start:])
            if user == self.umax:
                self.servers.append(self.umax)
            #
            if user < self.umax:
                self.servers.append(1)
            #
            if user > self.umax:
                self.servers.append(self.umax)
                diff = user - self.umax
            #
            if diff > self.umax:
                self.servers.append(self.umax)
                diff = diff - self.umax
            #
            if diff == self.umax:
                self.servers.append(self.umax)
        #
        # Fim do 4º Passo
        #
        # 5º Passo - ttask 5 - [0, 1, -, -]
        start += 1
        self.tick = self.tick + sum(self.users[start:])
        self.cost = self.tick

        for _ in range(1):
            user = sum(self.users[start:])
            if user == self.umax:
                self.servers.append(self.umax)
            #
            if user < self.umax:
                self.servers.append(1)
            #
            if user > self.umax:
                self.servers.append(self.umax)
                diff = user - self.umax
            #
            if diff > self.umax:
                self.servers.append(self.umax)
                diff = diff - self.umax
            #
            if diff == self.umax:
                self.servers.append(self.umax)
        #
        # Fim do 5º Passo
        #
        # 6º Passo - ttask 6 - [1, -, -, -]
        start += 1
        self.tick = self.tick + sum(self.users[start:])
        self.cost = self.tick
        for _ in range(1):
            user = sum(self.users[start:])
            if user == self.umax:
                self.servers.append(self.umax)
            #
            if user < self.umax:
                self.servers.append(1)
            #
            if user > self.umax:
                self.servers.append(self.umax)
                diff = user - self.umax
            #
            if diff > self.umax:
                self.servers.append(self.umax)
                diff = diff - self.umax
            #
            if diff == self.umax:
                self.servers.append(self.umax)
        # Fim do 6º Passo
        #
        # 7º Passo - ttask 7 - [-, -, -, -]
        start += 1
        self.tick = self.tick + sum(self.users[start:])
        self.cost = self.tick

        for _ in range(1):
            user = sum(self.users[start:])
            if user == self.umax:
                self.servers.append(self.umax)
            #
            if user < self.umax and user > 0:
                self.servers.append(1)
            #
            if user == 0:
                self.servers.append(0)
            #
            if user > self.umax:
                self.servers.append(self.umax)
                diff = user - self.umax
            #
            if diff > self.umax:
                self.servers.append(self.umax)
                diff = diff - self.umax
            #
            if diff == self.umax:
                self.servers.append(self.umax)
        # Fim do 7º Passo
        #
        self.servers.append(self.cost)

        return self.servers


if __name__ == '__main__':
    # file path input
    file = 'data/input.txt'
    # class object
    obj = LoadBalance()
    # firt method
    print(f'Objetos do arquivo: {obj.read_file(file)}')
    # second method
    print(f'Nº ttask: {obj.get_ttask()}')
    # third method
    print(f'Nº umax: {obj.get_umax()}')
    # four method
    print(f'Usuários: {obj.get_users()}')
    # five  method
    print(f'Resultado: {obj.balance()}')
    print(f'Nº tick: {obj.tick}')
    print(f'Custo: {obj.cost}')

    with open('data/output.txt', 'w') as output:
        for _ in range(1):
            output.write(f'{obj.servers[0]}\n')
            output.write(f'{obj.servers[1]}, {obj.servers[2]}\n')
            output.write(f'{obj.servers[3]}, {obj.servers[3]}\n')
            output.write(f'{obj.servers[5]}, {obj.servers[6]}, {obj.servers[7]}\n')
            output.write(f'{obj.servers[8]}, {obj.servers[9]}, {obj.servers[10]}\n')
            output.write(f'{obj.servers[11]}\n')
            output.write(f'{obj.servers[12]}\n')
            output.write(f'{obj.servers[13]}\n')
            output.write(f'{obj.servers[14]}\n')
            output.write(f'{obj.servers[15]}\n')
            output.write(f'{obj.servers[16]}\n')

    with open('data/output.txt', 'r') as output:
        file = output.readlines()
        for i in file:
            print(i.rstrip('\n'))
