import spacy 
from regras.oracoes import segmentar_por_verbos
from regras.interiores import segmentacao_interior
from regras.sinais import segmentar_sinais
from util.utils import printar_segmentacao
from util.utils import pre_processamento
from util.utils import salvar_segmentacao
model = spacy.load("pt_core_news_sm")

# Função principal para segmentar o texto, já realiza a segmentação por ponto, ponto de exclamação e interrogação, depois segmenta por verbos, depois segmenta por regras de segmentação interior e por fim segmenta por sinais de pontuação.   
def segmentar_texto(texto):
    texto = pre_processamento(texto)
    doc = model(texto)
    # 1) Segmentar sentenças terminadas por ponto, ponto de exclamação e de interrogação. 
    tokenized_sents = []
    for sent in doc.sents:
        current_sent = []
        for token in sent:
           current_sent.append([token.text, token.lemma_, token.pos_, token.dep_, token.morph.get("VerbForm")])
        if current_sent[-1][0] in [".", "!", "?"]:
            current_sent.append(['|', '|', 'PUNCT', 'segment', False])
        tokenized_sents.append(current_sent)
    verbos_segmentados = segmentar_por_verbos(tokenized_sents)
    interior = segmentacao_interior(verbos_segmentados)
    sinais = segmentar_sinais(interior)
    printar_segmentacao(sinais)
    salvar_segmentacao(sinais)
    return sinais


with open("texto.txt", "r") as file:
    texto = file.read()
segmentar_texto(texto)

