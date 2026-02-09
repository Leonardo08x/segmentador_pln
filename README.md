# Segmentador RST para o Português Brasileiro

Repositório destinado ao desenvolvimento de um segmentador automático de unidades discursivas elementares (EDUs), fundamentado na **Rhetorical Structure Theory (RST)**. Este trabalho integra o projeto de pesquisa **"Relações retóricas para além de marcadores discursivos: revisitando a anotação RST para o português brasileiro"**.

**Bolsista de IC:** Leonardo Cunha da Rocha  
**Orientadora:** Profa. Dra. Paula Christina Figueira Cardoso  
**Instituição:** Universidade Federal do Pará (UFPA) - ICEN - FACOMP

---

## 📌 Descrição do Projeto
O objetivo deste sistema é realizar a segmentação automática de textos em unidades elementares, respeitando diretrizes linguísticas específicas para a anotação RST. O sistema utiliza a biblioteca **spaCy** para análise sintática e morfológica, implementando um pipeline de regras que identificam fronteiras discursivas em diferentes níveis (gramatical, pontuação e semântico-atributivo).

## 🚀 Funcionalidades e Regras Implementadas

O segmentador obedece a um conjunto rigoroso de diretrizes de segmentação:

### 1. Regras Básicas e de Sentença
* **Pontuação Terminal:** Segmentação obrigatória em `.`, `!` e `?`.
* **Orações com Verbo:** Identificação de orações completas e segmentos sem verbo que contenham marcadores discursivos fortes (ex: *porque, mas, embora, até*).
* **Interiores de Falas:** Segmentação de unidades dentro de citações e diálogos.

### 2. Regras Específicas (Sintáticas)
* **Orações Coordenadas:** Segmentação de orações com sujeito explícito ou inferido.
* **Orações Relativas:** Isolamento de relativas explicativas ou restritivas (uso de tag `relcl`).
* **Formas Nominais:** Segmentação de orações reduzidas de particípio ou gerúndio, especialmente quando demarcadas por vírgulas.
* **Não-Segmentação:** O sistema é configurado para **não** separar sujeitos e objetos oracionais da oração principal.

### 3. Regras de Atribuição e Sinais
* **Verbos Atributivos/Públicos:** Segmentação diante de verbos como *dizer, afirmar, declarar*, desde que o sujeito seja animado (pessoa ou instituição).
* **Sinais Gráficos:** Identificação de fronteiras em parênteses `()`, colchetes `[]`, hífens `-`, barras `/` e dois-pontos `:`.

---

## 🛠 Estrutura do Código

O projeto está organizado em módulos para facilitar a manutenção e expansão das regras:

* **`segmentador.py`**: Orquestrador principal do pipeline. Realiza a carga do modelo spaCy (`pt_core_news_sm`) e coordena a execução das regras.
* **`regras/oracoes.py`**: Implementa a lógica de segmentação baseada em verbos, orações relativas e conjunções coordenadas.
* **`regras/interiores.py`**: Gerencia a segmentação interior de falas e gatilhos pós-vírgula.
* **`regras/sinais.py`**: Trata a segmentação baseada em sinais de pontuação e caracteres especiais.
* **`util/utils.py`**: Contém funções auxiliares de pré-processamento (Regex para limpeza e separação de tokens) e utilitários de exibição.

## 🔧 Pré-processamento
Para garantir a precisão, o sistema aplica uma limpeza inicial via Expressões Regulares que assegura a correta separação de tokens grudados (ex: `palavra(parêntese)` -> `palavra ( parêntese )`), permitindo que o modelo spaCy identifique corretamente as etiquetas POS e dependências.

---
*Este repositório é parte integrante de atividades de pesquisa acadêmica e está em constante atualização.*
