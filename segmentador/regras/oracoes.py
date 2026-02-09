from util.utils import ja_existe_segmentacao

def tem_verbos(sentenca):
    for token in sentenca:
        if token[2] == "VERB":
            return True
        elif token[3] == "orphan":
            return True
    return False

def segmentar_por_verbos(tokenized_sents):
    segmentacoes = []
    for sent in tokenized_sents:
        if ja_existe_segmentacao(sent):
            segmentacoes.append(sent)
            continue
        sub_sentencas_segmentadas = []
        if tem_verbos(sent):
            for token_index in range(len(sent)):
                if  sent[token_index][3] == 'relcl':
                    sub_sentencas_segmentadas.append(['|', '|', 'PUNCT', 'segment', False])
                    sub_sentencas_segmentadas.append(sent[token_index])
                elif sent[token_index][2] == "CCONJ" and token_index > 0 and token_index < len(sent) - 1:
                    sub_sentencas_segmentadas.append(['|', '|', 'PUNCT', 'segment', False])
                    sub_sentencas_segmentadas.append(sent[token_index])
                else:
                    sub_sentencas_segmentadas.append(sent[token_index])
        else:
            segmentacoes.append(sent)
        segmentacoes.append(sub_sentencas_segmentadas)
    return segmentacoes