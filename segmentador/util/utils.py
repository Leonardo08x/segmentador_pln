import re
def ja_existe_segmentacao(sent):
    segmentos = 0
    for token in sent:
        if token[3] == "segment":
            segmentos+=1
    if segmentos > 1:
        return True
    return False
def printar_segmentacao(segmentacao):
    #print(segmentacao)
    for sent in segmentacao:
        texto_sentenca = ""
        for token in sent:
            texto_sentenca += token[0] + " "
        print(texto_sentenca)

def pre_processamento(texto):
    texto_separa_sinais = re.sub(r'([:/\|\-\_\(\)\[\]])', r' \1 ', texto)
    texto_unifica_espacos = re.sub(r'\s+', ' ', texto_separa_sinais)
    return texto_unifica_espacos.strip()

def salvar_segmentacao(texto_tokenize):
    try:
        with open("texto_segmentado.txt", "x") as file:
            for sent in texto_tokenize:
                for token in sent:
                    file.write(token[0] + " ")
                file.write("\n")
    except Exception as e:
        with open("texto_segmentado.txt", "w") as file:
            for sent in texto_tokenize:
                for token in sent:
                    file.write(token[0] + " ")
                file.write("\n")

def lista_verbos_atributivos():
    verbos = ["dizer", "afirmar", "falar", "declarar", "comentar", "perguntar", "responder"]