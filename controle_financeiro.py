from time import sleep
cores = {
    'limpa':'\033[m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'branco':'\033[97m'
}

print('Bem-vindo(a) ao Controle de {}$Finanças${}'.format(cores['verde'], cores['limpa']))
print('{}Desenvolvido por guigas{}'.format(cores['branco'], cores['limpa']))
carteira_entrada = 0
carteira_saida = 0
opcao = 0
while opcao != 3:
    opcao = int(input('''O que você deseja registrar?
[1] {}Entradas{}
[2] {}Saídas{}
[3] {}Fechar programa{}
Opção: '''.format(cores['verde'], cores['limpa'], cores['vermelho'], cores['limpa'], cores['branco'], cores['limpa'])))
    if opcao == 1:
        valor_entrada = float(input('Digite o valor que deseja adicionar: R$'))
        repetir_entrada = str(input('Deseja adicionar mais valores? [S/N]: ')).strip().upper()
        carteira_entrada += valor_entrada
        while repetir_entrada == 'S':
            valor_entrada = float(input('Digite o valor que deseja adicionar: R$'))
            carteira_entrada += valor_entrada
            repetir_entrada = str(input('Deseja adicionar mais valores? [S/N]')).strip().upper()
        if repetir_entrada == 'N':
            print('Valor de {}R${}{} adicionado com sucesso!'.format(cores['verde'], carteira_entrada, cores['limpa']))
            sleep(1)
            print('')
        else:
            print('{}ERRO{}! Parece que você digitou algo fora do requisitado, tente novamente!'.format(cores['vermelho'], cores['limpa']))

    if opcao == 2:
        valor_saida = float(input('Digite o valor de suas saídas: R$'))
        repetir_saida = str(input('Deseja adicionar mais valores? [S/N]')).strip().upper()
        carteira_saida -= valor_saida
        while repetir_saida == 'S':
            valor_saida = float(input('Digite o valor de suas saídas: R$'))
            carteira_saida -= valor_saida
            repetir_saida = str(input('Deseja adicionar mais valores? [S/N]')).strip().upper()
        if repetir_saida == 'N':
            print('Valor de {}R${}{} retirado com sucesso!'.format(cores['verde'], carteira_saida, cores['limpa']))
            sleep(1)
            print('')
        else:
            print('{}ERRO{}! Parece que você digitou algo fora do requisitado, tente novamente!'.format(cores['vermelho'], cores['limpa']))

print('Operações realizadas com sucesso! Seu saldo após as movimentações é de {}R${}{}.'.format(cores['verde'], carteira_entrada + carteira_saida, cores['limpa']))
