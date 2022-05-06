#
# Escrevendo arquivos com funções do Python

def Escrevearquivo():
    arquivo = open("NovoArquivo.txt", "w+")
    
    arquivo.write("Linha gerada com a funcao 'Escrevearquivo' \r\n")
    
    arquivo.close()
    
Escrevearquivo()

def Alteraarquivo():
    arquivo = open("NovoArquivo.txt", "a+")
    
    arquivo.write("Linha gerada com a funcao 'Alteraarquivo' \r\n")
    
    arquivo.close()
    
Alteraarquivo()
