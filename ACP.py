from Arquivo import Arquivo

class ACP:
    def __init__(self):
        self.stack = []

    #computa a cadeia de entrada de acordo com as produções informadas 
    def computacao(self, cadeiaEntrada, parsedLines):
        cadeiaEntrada += 'e'
        simboloInicioPilha = parsedLines['inicio_pilha']
        self.stack.append(simboloInicioPilha)
        estadosFinais = parsedLines['estados_finais']
        estadoInicial = parsedLines['estado_inicial']
        alfabetoPilha = parsedLines['alfabeto_pilha']
        producoes = parsedLines['producoes']

        simboloPilhaAtual = simboloInicioPilha
        estadoAtual = estadoInicial

        print('Estado\tEntrada\tTopo\tPilha Atual')
        print('{}\t {}\t {}\t ({}, {})'.format(estadoAtual, '_', 'Z', simboloPilhaAtual, self.stack))
        for char in cadeiaEntrada:
            for producao in producoes:
                if ((producao[0] == estadoAtual) and (producao[1] == char) and (producao[2] == simboloPilhaAtual)):
                    estadoAtual = producao[3]
                    if(len(producao[4]) == 2):
                        self.stack.append(char)
                    elif(len(producao[4]) == 3):
                        self.stack.append(char)
                        self.stack.append(char)
                    elif ((producao[4] == 'e') and (len(self.stack) != 1)):
                        self.stack.pop()
                        break
            simboloPilhaAntigo = simboloPilhaAtual
            simboloPilhaAtual = self.stack[len(self.stack)-1]
            print('{}\t {}\t {}\t ({}, {})'.format(estadoAtual, char, simboloPilhaAntigo, simboloPilhaAtual, self.stack))

        if(estadoAtual in estadosFinais):
            print('\nCadeia aceita pelo ACP!')
        else:
            print('\nCadeia rejeitada pelo ACP!')

def main():
    arq = Arquivo()
    acp = ACP()
    filePath = input('Digite o caminho do arquivo: ')
    linhas = arq.readFile(filePath)
    print('Arquivo lido com sucesso.\n')
    cadeiaEntrada = input('Digite a cadeia a ser testada: ')
    cadeiaEntrada = cadeiaEntrada.rstrip()

    parsedLines = arq.parseFile(linhas)
    print('\nEstados: ', parsedLines['estados'])
    print('Alfabeto do Autômato: ', parsedLines['alfabeto_acp'])
    print('Alfabeto da Pilha: ', parsedLines['alfabeto_pilha'])
    print('Estado inicial: ', parsedLines['estado_inicial'])
    print('Símbolo Inicial da Pilha: ', parsedLines['inicio_pilha'])
    print('Estados Finais: ', parsedLines['estados_finais'])
    print('Produções:')
    for producoes in parsedLines['producoes']:
        print('\t', producoes)

    print('\nTabela de Transição:')
    acp.computacao(cadeiaEntrada, parsedLines)

if __name__ == '__main__':
    main()
