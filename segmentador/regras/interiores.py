from util.utils import ja_existe_segmentacao

def check_gatilho_post_virgula(token):
    # não segmenta sujeitos e objetos oracionais 
    if token[3] in ['ccomp', 'xcomp', 'csubj']:
        return False
    # segmenta orações coordenadas introduzidas por conjunções coordenativas, como "e", "mas", "ou", "nem", "porém", "todavia", "contudo", "entretanto", "no entanto", "logo", "portanto", "assim", "consequentemente", "por isso", "por conseguinte", "de modo que", "de forma que", "de maneira que", entre outras.
    elif token[2] == "CCONJ" or token[2] == "SCONJ" or token[2] == "ADV":
        return True
    # segmenta orações relativas introduzidas por pronomes relativos 
    elif token[2] == "PRON" and token[3] == 'relcl': 
        return True
    # segmenta orações reduzidas de gerúndio ou particípio
    elif (token[2] in ["AUX", "VERB"]) and (token[4] in ["Ger", "Part"]):
            return True
    return False
# segmenta interiores de falas
def segmentacao_interior(tokenized_sents):
    segmentacoes = []
    for sent in tokenized_sents:
        if ja_existe_segmentacao(sent):
            segmentacoes.append(sent)
            continue
        sub_sentencas_segmentadas = []
        for token_index in range(len(sent)):
            print(sent[token_index])
            if token_index < len(sent) - 1:
                if sent[token_index][1] == "," and check_gatilho_post_virgula(sent[token_index+1]) :
                        sub_sentencas_segmentadas.append(sent[token_index])
                        sub_sentencas_segmentadas.append(['|', '|', 'PUNCT', 'segment', False])
                else:
                    sub_sentencas_segmentadas.append(sent[token_index])
            else:
                sub_sentencas_segmentadas.append(sent[token_index])
        segmentacoes.append(sub_sentencas_segmentadas)
    return segmentacoes