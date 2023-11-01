cores = {
    'limpa':'\033[m',
    'verde':'\033[32m',
    'vermelho':'\033[31m',
    'branco':'\033[97m'
}

print('Bem-vindo(a) ao Controle de {}Finanças{}'.format(cores['verde'], cores['limpa']))
print('{}Desenvolvido por guigas{}'.format(cores['branco'], cores['limpa']))

opcao = int(input('''O que você deseja registrar?
[1] Entradas
[2] Saídas
[3] Fechar programa
Opção: '''))

while opcao != 3:
    if opcao == 1:
        entrada = float(input('Adicione o valor de entrada: R$'))
        continuar = str(input('Deseja adicionar mais valores? [S/N]')).strip().upper()
    if continuar == 'S':
        entrada = float(input('Adicione o valor da entrada: R$'))
        continuar = str(input('Deseja adicionar mais valores? [S/N]')).strip().upper()
    elif continuar == 'N':
        print('Valores recebidos com sucesso!')