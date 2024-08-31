# calcValuation
 
## Visão Geral

A classe calcValuation é uma implementação de métodos de valuation e análise financeira. Ela permite calcular diversos indicadores financeiros como ROI, NOPAT, EBITDA, Goodwill, entre outros, para análises gerenciais simples e completas, além de avaliar o retorno de campanhas de marketing.
Métodos Disponíveis

1. `analiseGerencialSimples`: Realiza uma análise financeira básica calculando lucro bruto, lucro operacional, ROI, lucro econômico e Goodwill.
2. `calcROICampanha`: Calcula o ROI de uma campanha de marketing, considerando fatores como cliques, erros, vendas e capital investido.
3. `analiseGerencialCompleta`: Realiza uma análise financeira mais completa, incorporando elementos como fluxo de caixa, EBITDA, NOPAT, e valor da empresa.

## Métodos

### analiseGerencialSimples
```
def analiseGerencialSimples(self, investimento, capital_proprio, receita, custo_mercadorias, despesas_operacionais, custo_oportunidade, capital_terceiros=None) -> pd.DataFrame:
```
**Descrição**: Este método realiza uma análise gerencial simples, calculando indicadores como lucro bruto, lucro operacional, ROI, lucro econômico e Goodwill.

**Parâmetros**:

1. `investimento`: Valor total investido na operação.
2. `capital_proprio`: Capital próprio investido.
3. `receita`: Receita total gerada.
4. `custo_mercadorias`: Custo das mercadorias vendidas.
5. `despesas_operacionais`: Despesas operacionais incorridas.
6. `custo_oportunidade`: Custo de oportunidade do capital investido.
7. `capital_terceiros (opcional)`: Capital de terceiros envolvido.

**Retorno**:

`pd.DataFrame`: DataFrame contendo as métricas da campanha e seus respectivos valores.

### calcROICampanha
```
def calcROICampanha(self, quantidade_emails, erros, cliques, vendas, ticket_medio, capital_investido, margem_bruta) -> pd.DataFrame:
```

**Descrição**: Este método calcula o ROI de uma campanha de marketing, levando em consideração métricas como número de emails enviados, cliques, vendas realizadas e o capital investido.

**Parâmetros**:

1. `quantidade_emails`: Número total de emails enviados.
2. `erros`: Número de emails que não foram entregues corretamente.
3. `cliques`: Número de cliques nos emails.
4. `vendas`: Número de vendas realizadas.
5. `ticket_medio`: Valor médio do ticket de vendas.
6. `capital_investido`: Capital investido na campanha.
7. `margem_bruta`: Margem bruta esperada.

**Retorno**:

`pd.DataFrame`: DataFrame contendo as métricas da campanha e seus respectivos valores.

### analiseGerencialCompleta
```
def analiseGerencialCompleta(self, capital_investido, preco_vendas, preco_custo, despesas_fixas, depreciacao, ir, custo_oportunidade, unidades_vendidas, parcela_financiamento=0.00) -> pd.DataFrame:
```

**Descrição**: Este método realiza uma análise financeira completa, considerando múltiplos fatores como EBITDA, NOPAT, fluxo de caixa, Goodwill e valor da empresa.

**Parâmetros**:

1. `capital_investido`: Capital total investido no negócio.
2. `preco_vendas`: Preço de venda por unidade.
3. `preco_custo`: Custo por unidade vendida.
4. `despesas_fixas`: Despesas fixas mensais.
5. `depreciacao`: Valor da depreciação.
6. `ir`: Alíquota do imposto de renda.
7. `custo_oportunidade`: Custo de oportunidade do capital investido.
8. `unidades_vendidas`: Número de unidades vendidas.
9. `parcela_financiamento (opcional)`: Valor da parcela do financiamento.

**Retorno**:

`pd.DataFrame`: DataFrame contendo as métricas da campanha e seus respectivos valores.

## Exemplo de Uso

```
### Instanciando a classe
valuation = calcValuation()

### Análise Gerencial Simples
df_gerencial_simples = valuation.analiseGerencialSimples(
    investimento=100000, 
    capital_proprio=80000, 
    receita=200000, 
    custo_mercadorias=120000, 
    despesas_operacionais=50000, 
    custo_oportunidade=0.05
)

### ROI de Campanha
df_roi_campanha = valuation.calcROICampanha(
    quantidade_emails=10000, 
    erros=500, 
    cliques=3000, 
    vendas=150, 
    ticket_medio=100, 
    capital_investido=5000, 
    margem_bruta=0.2
)

### Análise Gerencial Completa
df_gerencial_completa = valuation.analiseGerencialCompleta(
    capital_investido=150000, 
    preco_vendas=50, 
    preco_custo=30, 
    despesas_fixas=20000, 
    depreciacao=5000, 
    ir=0.15, 
    custo_oportunidade=0.08, 
    unidades_vendidas=5000, 
    parcela_financiamento=1000
)
```

## Observações

1. Os métodos retornam DataFrames pandas, facilitando a visualização dos resultados.
2. As métricas calculadas nos métodos oferecem uma visão detalhada dos aspectos financeiros e operacionais do negócio ou campanha analisada.
3. É importante fornecer os parâmetros corretos para garantir cálculos precisos.