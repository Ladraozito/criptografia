# criptografia chr(ord())


def criptografar(texto, chave=1):
    encript = ''
    try:
        for letra in texto:
            encript += chr(ord(letra)+chave)
    except OverflowError:
        msg_erro('ERRO! Não foi possível criptografar sua mensagem!')
    return encript


def descriptografar(texto, chave=1):
    descript = ''
    for letra in texto:
        descript += chr(ord(letra)-chave)
    return descript


def chutar_chaves(texto, limite=0):
    cont = chute = 0
    continua = False
    if limite == 0:
        while True:
            chute += 1
            cont += 1
            try:
                print(f'{cont}. {descriptografar(texto, chute)}')
            except ValueError:
                chute = 0
                cont -= 1
                continua = True
                break
            except KeyboardInterrupt:
                msg_erro('Operação interrompida!')
                break
        while continua:
            chute -= 1
            cont += 1
            try:
                print(f'{cont}. {descriptografar(texto, chute)}')
            except ValueError:
                msg_erro('Não foi possível chutar mais chaves!')
                break
            except KeyboardInterrupt:
                msg_erro('Operação interrompida!')
                break
    else:
        while limite > 0:
            chute += 1
            cont += 1
            try:
                print(f'{cont}. {descriptografar(texto, chute)}')
            except ValueError:
                chute = 0
                cont -= 1
                continua = True
                break
            except KeyboardInterrupt:
                msg_erro('Operação interrompida!')
            limite -= 1
        while limite > 0 and continua:
            chute -= 1
            cont += 1
            try:
                print(f'{cont}. {descriptografar(texto, chute)}')
            except ValueError:
                msg_erro('Não foi possível chutar mais chaves!')
            except KeyboardInterrupt:
                msg_erro('Operação interrompida!')
            limite -= 1


# criptografia vigenere


def tabelaVigenere():
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tabela = {}
    contador1 = 0
    for linha in alfabeto:
        tabela[linha] = {}
        linhaDaTabela = alfabeto[contador1:len(alfabeto)] + alfabeto[0:contador1]
        contador2 = 0
        for coluna in alfabeto:
            tabela[linha][coluna] = linhaDaTabela[contador2]
            contador2 += 1
        contador1 += 1
    return tabela


def codificar(msg, chave='A'):
    msg = msg.upper()
    chave = chave.upper()
    chave_nova = chave
    while len(chave_nova) < len(msg):
        chave_nova += chave
    chave_nova = chave_nova[0:len(msg)]
    contador = 0
    mensagem = ''
    for letra in msg:
        mensagem += Tabela[letra][chave_nova[contador]]
        contador += 1
    return mensagem


def decodificar(msg, chave='A'):
    msg = msg.upper()
    chave = chave.upper()
    chave_nova = chave
    while len(chave_nova) < len(msg):
        chave_nova += chave
    chave_nova = chave_nova[0:len(msg)]
    contador = 0
    mensagem = ''
    for letra in msg:
        for chave, item in Tabela[chave_nova[contador]].items():
            if item == letra:
                mensagem += chave
        contador += 1
    return mensagem



Tabela = tabelaVigenere()

# utilitarios


def receba_int(texto):
    while True:
        num = input(texto)
        if num.isdigit():
            return int(num)
        msg_erro('Isto não é um número!')


def msg_erro(texto):
    print(f'\033[31m{texto}\033[m')


def limpar():
    import os
    return os.system('cls' if os.name == 'nt' else 'clear')


def titulo(texto):
    texto = texto.upper()
    print('='*40)
    print(f'{texto:^40}')
    print('='*40)


def texto(texto):
    while True:
        mensagem = input(texto).strip()
        if not mensagem:
            msg_erro('Erro! Não foi digitado texto algum!')
        else:
            break
    return mensagem


def leia_arquivo(texto):
    while True:
        arquivo = input(texto)
        try:
            tente = open(arquivo, 'r', encoding='UTF-8').close()
            break
        except FileNotFoundError:
            msg_erro('Erro! Verifique o nome do arquivo!')
    return arquivo
