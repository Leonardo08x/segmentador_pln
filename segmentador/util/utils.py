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