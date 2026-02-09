def segmentar_sinais(tokenized_sents):
    segmentacoes = []
    for sent in tokenized_sents:
        sub_sentencas_segmentadas = []
        for token_index in range(len(sent)):
            if sent[token_index][0] in [":", "/","-","_"]:
                sub_sentencas_segmentadas.append(sent[token_index])
                sub_sentencas_segmentadas.append(['|', '|', 'PUNCT', 'segment', False])
            elif sent[token_index][0] in ["|"] and not sent[token_index][3] == "segment":
                sub_sentencas_segmentadas.append(sent[token_index])
                sub_sentencas_segmentadas.append(['|', '|', 'PUNCT', 'segment', False])
            elif sent[token_index][0] in ["(","["]:
                sub_sentencas_segmentadas.append(['|', '|', 'PUNCT', 'segment', False])
                sub_sentencas_segmentadas.append(sent[token_index])
            elif sent[token_index][0] in [")","]"]:
                sub_sentencas_segmentadas.append(sent[token_index])
                sub_sentencas_segmentadas.append(['|', '|', 'PUNCT', 'segment', False])
            else:
                sub_sentencas_segmentadas.append(sent[token_index])
        segmentacoes.append(sub_sentencas_segmentadas)
    return segmentacoes