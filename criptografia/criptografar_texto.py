from criptografia.utilitarios import codificador

while True:
    codificador.limpar()
    codificador.titulo('programa de criptografia')
    print('[1] Criptografar')
    print('[2] Descriptografar')
    print('[3] Sair')
    escolha = codificador.receba_int('Escolha: ')
    codificador.limpar()
    if escolha == 1:
        codificador.titulo('criptografar')
        mensagem = codificador.texto('Mensagem a criptografar: ')
        chave = codificador.receba_int('Chave para criptografar: ')
        print('[apenas Enter para não salvar]')
        nome = input('Nome do arquivo [Incluir extensão!]: ').strip()
        if not nome:
            print(f'Mensagem criptografada: {codificador.criptografar(mensagem, chave)}')
        else:
            print('Criptografando...', end='')
            mensagem_nova = codificador.criptografar(mensagem, chave)
            print('Pronto!')
            print('Gravando...', end='')
            arquivo = open(nome, 'w', encoding='UTF-8')
            arquivo.write(mensagem_nova)
            arquivo.close()
            print('Pronto!')
    elif escolha == 2:
        while True:
            codificador.limpar()
            codificador.titulo('descriptografar')
            print('[1] Escrever a mensagem')
            print('[2] Escrever o nome do arquivo')
            print('[3] Voltar')
            escolha = codificador.receba_int('Escolha: ')
            codificador.limpar()
            if escolha == 1:
                codificador.titulo('escrever mensagem')
                mensagem = codificador.texto('Mensagem a decifrar: ')
                chave = codificador.receba_int('Chave [0 para chutar várias chaves]: ')
                if chave == 0:
                    print('[0 para chutar o máximo de chaves possível]')
                    qtd_chutes = codificador.receba_int('Quantos chutes fazer? ')
                    print('='*40)
                    codificador.chutar_chaves(mensagem, qtd_chutes)
                else:
                    print(f'Descriptografada: {codificador.descriptografar(mensagem, chave)}')
                print('='*40)
            elif escolha == 2:
                codificador.limpar()
                codificador.titulo('escrever nome do arquivo')
                nome = codificador.leia_arquivo('Nome do arquivo [Incluir extensão!]: ')
                chave = codificador.receba_int('Chave [0 para chutar varias chaves]: ')
                arquivo = open(nome, 'r', encoding='UTF-8')
                mensagem = arquivo.read()
                if chave == 0:
                    qtd_chutes = codificador.receba_int('Quantos chutes fazer? ')
                    print('='*40)
                    codificador.chutar_chaves(mensagem, qtd_chutes)
                else:
                    print(codificador.descriptografar(mensagem, chave))
                arquivo.close()
                print('='*40)
            elif escolha == 3:
                break
            else:
                codificador.msg_erro('Erro! Tente novamente!')
            input('Tecle Enter para seguir!')
    elif escolha == 3:
        break
    else:
        codificador.msg_erro('Erro! Tente de novo!')
    input('Tecle Enter para seguir!')
