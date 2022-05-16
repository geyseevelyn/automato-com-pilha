import os

#manipulação do arquivo
class Arquivo:
    def __init__(self):
        pass

    def readFile(self, filePath):
        linhas=[]
        if(os.path.isfile(filePath)):
            try:
                with open(filePath) as file:
                    linhas = [linha.rstrip() for linha in file]
            except IOError as e:
                print("Arquivo não pode ser aberto.")
                exit(0)
        else:
            print('{}: Arquivo não foi encontrado no caminho indicado.'.format(filePath))
            exit(0)
        return linhas

    def parseFile(self,linhas):
        #atribui cada linha do arquivo às suas respectivas variáveis
        estados = linhas[0].rstrip().split()
        alfabeto_acp = linhas[1].rstrip().split()
        alfabeto_pilha = linhas[2].rstrip().split()
        estado_inicial = linhas[3].rstrip()
        inicio_pilha = linhas[4].rstrip()
        estados_finais = linhas[5].rstrip().split()
        producoes = linhas[6:] #linha 6 em diante

        for i in range(len(producoes)):
            producoes[i] = producoes[i].rstrip().split()

        parsedLines = {'estados':estados,
                        'alfabeto_acp':alfabeto_acp,
                        'alfabeto_pilha':alfabeto_pilha,
                        'estado_inicial':estado_inicial,
                        'inicio_pilha':inicio_pilha,
                        'estados_finais':estados_finais,
                        'producoes':producoes}
                        
        return parsedLines