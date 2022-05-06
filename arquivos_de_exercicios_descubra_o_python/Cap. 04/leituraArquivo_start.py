#
# Lendo arquivos com funções do Python
#
def LeituraArquivo():
    arquivo = open("NovoArquivo.txt", "r")
    if (arquivo.mode == "r"):
        conteudo = arquivo.read()
        print (conteudo)

    arquivo.close()


LeituraArquivo()

def LeituraArquivoGrande():
    arquivo = open("NovoArquivo.txt", "r")
    if (arquivo.mode == "r"):
        conteudoTotal = arquivo.readlines()

        for conteudo in conteudoTotal:
            print(conteudo)
    
        arquivo.close()


    LeituraArquivoGrande()

