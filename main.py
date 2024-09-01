import pandas as pd

class calcValuation:
    """
    Classe para realizar cálculos de valuation de negócios.

    Esta classe oferece diferentes métodos para calcular métricas financeiras
    importantes para a avaliação de negócios, como ROI, lucro econômico e fluxo de caixa.
    """
    def analiseGerencial(self, investimento, capital_proprio, receita, custo_mercadorias, despesas_operacionais, custo_oportunidade, capital_terceiros=None):
        """
        Realiza uma análise gerencial básica de um negócio.

        Args:
            investimento (float): Valor total investido no negócio.
            capital_proprio (float): Valor do capital próprio investido.
            receita (float): Receita total gerada.
            custo_mercadorias (float): Custo total das mercadorias vendidas.
            despesas_operacionais (float): Despesas operacionais totais.
            custo_oportunidade (float): Taxa de retorno mínima desejada pelo investidor.
            capital_terceiros (float, optional): Valor do capital de terceiros.

        Returns:
            pd.DataFrame: Um DataFrame Pandas com as métricas calculadas.
        """
        # Inputs
        self.investimento = investimento
        self.capital_proprio = capital_proprio
        self.despesas_operacionais = despesas_operacionais
        
        # Retorno Mínimo que o Investidor Espera
        self.custo_oportunidade = custo_oportunidade
        
        lucro_bruto = round(receita - custo_mercadorias, 2)
        lucro_operacional = round(lucro_bruto - self.despesas_operacionais, 2)
        
        # Retorno do Capital Investido
        ROI = round(lucro_operacional*100/self.investimento, 2)
        
        # Lucro Econômico é o Lucro Operacional menos Custo de Oportunidade sobre o Capital Investido
        custo_oportunidade_capital_investido = round(self.custo_oportunidade*self.investimento, 2)

        # Medida de sucesso da empresa - desempenho do negócio. O que sobra para o negócio.
        lucro_economico = lucro_operacional - round(custo_oportunidade_capital_investido, 2)
        
        # Riqueza gerada. Quanto a mais a empresa vale o que foi investido nela. Quanto vale o negócio.
        goodwill = round(lucro_economico/self.custo_oportunidade, 2)

        # Transformando em Dicionário
        dicionario_final_ag = {}

        dicionario_final_ag['Métrica'] = ('Lucro Bruto (R$)', 'Lucro Operacional (R$)', 'ROI (%)', 'Custo de Oportunidade (R$)', 'Lucro Econômico (R$)', 'Goodwill (R$)')
        dicionario_final_ag['Valor'] = (lucro_bruto, lucro_operacional, ROI, custo_oportunidade_capital_investido, lucro_economico, goodwill)

        return pd.DataFrame(dicionario_final_ag)
    

    def calcROICampanha(self, quantidade_emails, erros, cliques, vendas, ticket_medio, capital_investido, margem_bruta):
        """
        Calcula o retorno sobre o investimento (ROI) de uma campanha de marketing.

        Este método calcula o ROI de uma campanha, considerando métricas como taxa de
        abertura, taxa de cliques e taxa de conversão.

        Args:
            quantidade_emails (int): Número total de emails enviados.
            erros (int): Número de emails com erros de entrega.
            cliques (int): Número de cliques nos links dos emails.
            vendas (int): Número de vendas realizadas.
            ticket_medio (float): Valor médio de cada venda.
            capital_investido (float): Valor total investido na campanha.
            margem_bruta (float): Margem bruta das vendas.

        Returns:
            pd.DataFrame: Um DataFrame Pandas com as métricas calculadas, incluindo o ROI.
        """
        # Inputs
        emails_enviados = quantidade_emails
        total_erros = erros
        cliques = cliques
        vendas_realizadas = vendas
        ticket_medio = ticket_medio

        # Resultados
        emails_efetivados = emails_enviados - total_erros
        self.tx_erros = erros/emails_enviados
        self.tx_cliques = cliques/emails_efetivados
        self.tx_conversao = vendas_realizadas/cliques

        # Análise de Resultados
        receita_vendas = round(vendas_realizadas * ticket_medio, 2)
        lucro_bruto = round(receita_vendas * margem_bruta, 2)
        lucro_operacional = round(lucro_bruto - capital_investido, 2)

        ROI = round(lucro_operacional*100/capital_investido, 2)

        # Transformando em Dicionário
        dicionario_final_roi = {}

        dicionario_final_roi['Métrica'] = ('Receita de Vendas (R$)', 'Lucro Bruto (R$)', 'Custo da Campanha (R$)', 'Lucro Operacional (R$)', 'ROI (%)')
        dicionario_final_roi['Valor'] = (receita_vendas, lucro_bruto, capital_investido, lucro_operacional, ROI)

        return pd.DataFrame(dicionario_final_roi)


    def caseDiskPizza(self, capital_investido, preco_vendas, preco_custo, despesas_fixas, depreciacao, ir, custo_oportunidade, unidades_vendidas, parcela_financiamento=None):
        """
        Realiza uma análise financeira detalhada para um negócio de pizza.

        Esta função calcula métricas como EBITDA, EBIT, NOPAT, lucro econômico e fluxo de caixa, 
        considerando diversos fatores como investimento inicial, custos, receitas e despesas.

        Args:
            capital_investido (float): Valor total investido no negócio.
            preco_vendas (float): Preço de venda unitário de uma pizza.
            preco_custo (float): Preço de custo unitário de uma pizza.
            despesas_fixas (float): Despesas fixas mensais.
            depreciacao (float): Depreciação mensal.
            ir (float): Alíquota do imposto de renda.
            custo_oportunidade (float): Taxa de retorno mínima desejada pelo investidor.
            unidades_vendidas (int): Número de pizzas vendidas por mês.
            parcela_financiamento (float, optional): Valor da parcela do financiamento mensal.

        Returns:
            pd.DataFrame: Um DataFrame Pandas com as seguintes métricas:
                * EBITDA
                * EBIT
                * NOPAT
                * Lucro Econômico
                * Fluxo de Caixa Operacional
                * Fluxo de Caixa Líquido

        **Observações:**
            * A função assume que todas as unidades monetárias estão na mesma moeda.
            * A depreciação é considerada como uma despesa fixa mensal.
            * O imposto de renda é calculado sobre o lucro operacional bruto (EBIT).
            * O fluxo de caixa líquido considera o pagamento da parcela do financiamento.
        """

        margem_contribuicao_bruta = preco_vendas - preco_custo
        margem_contribuicao_liquida = margem_contribuicao_bruta * (1 - ir)

        custos_e_despesas_sem_depreciacao = despesas_fixas - depreciacao

        # Resultado Mensal
        receita_vendas = unidades_vendidas * preco_vendas
        custos_e_despesas_variaveis = unidades_vendidas * preco_custo
        margem_contribuicao = receita_vendas - custos_e_despesas_variaveis

        EBITDA = margem_contribuicao - custos_e_despesas_sem_depreciacao

        lucro_operacional_bruto_ebit = EBITDA - depreciacao

        if EBITDA <= 0:
            ir_lucro = 0
        else:
            ir_lucro = lucro_operacional_bruto_ebit * ir

        NOPAT = lucro_operacional_bruto_ebit - ir_lucro

        custo_oportunidade_capital_investido = custo_oportunidade*capital_investido

        lucro_economico = NOPAT - custo_oportunidade_capital_investido

        # Fluxo de Caixa
        fluxo_de_caixa_operacional = NOPAT + depreciacao
        fluxo_de_caixa_liquido = fluxo_de_caixa_operacional - parcela_financiamento

        # Transformando em Dicionário
        dicionario_final_ag = {}

        dicionario_final_ag['Métrica'] = ('EBITDA (R$)', 'EBIT (R$)', 'NOPAT (R$)', 'Lucro Econômico', 'Fluxo de Caixa Operacional (R$)', 'Fluxo de Caixa Operacional (R$)')
        dicionario_final_ag['Valor'] = (EBITDA, lucro_operacional_bruto_ebit, NOPAT, lucro_economico, fluxo_de_caixa_operacional, fluxo_de_caixa_liquido)

        return pd.DataFrame(dicionario_final_ag) 