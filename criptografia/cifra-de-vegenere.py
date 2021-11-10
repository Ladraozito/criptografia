from utilitarios import codificador

print('[Cifra de Vènere]')
while True:
    print('-' * 30)
    print('[1] Criptografar')
    print('[2] Descriptografar')
    print('[3] Limpar')
    print('[4] Sair')
    print('-' * 30)
    escolha = int(input('[Escolha]: '))
    print('-' * 30)
    if escolha == 1:
        msg = input('Mensagem: ')
        chave = input('Chave: ')
        print(f'Criptografado: {codificador.codificar(msg, chave)}')
    elif escolha == 2:
        msg = input('Mensagem: ')
        chave = input('Chave: ')
        print(f'descriptografado: {codificador.decodificar(msg, chave)}')
    elif escolha == 3:
        codificador.limpar()
    elif escolha == 4:
        print('--<VOLTE SEMPRE!>--')
        break
    else:
        print('\033[31mErro! Valor Inválido!\033[m')
