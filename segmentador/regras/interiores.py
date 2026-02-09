from util.utils import ja_existe_segmentacao

def check_gatilho_post_virgula(token):
    if token[3] in ['ccomp', 'xcomp', 'csubj']:
        return False
    elif token[2] == "CCONJ" or token[2] == "SCONJ" or token[2] == "ADV":
        return True
    elif token[2] == "PRON" and token[3] == 'relcl': 
        return True
    elif (token[2] in ["AUX", "VERB"]) and (token[4] in ["Ger", "Part"]):
            return True
    return False

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