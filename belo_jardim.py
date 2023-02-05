import pandas as pd
from scipy import stats as stats
print("ANALISE DE DADOS LICITAÇÕES BELO JARDIM 2020:")
data_2020 = pd.read_csv('licitacoes-2020_23-02-2021_13-01-47.csv',sep=',',
                   on_bad_lines='skip', low_memory=False)
data_2020.dropna(subset=['TOTALADJUDICADOLICITACAO'],inplace=True)
data_2020 = data_2020['TOTALADJUDICADOLICITACAO']
data_2020 = pd.to_numeric(data_2020,errors="coerce")
mediana = data_2020.median()
media = round(data_2020.mean(),2)

print("A mediana foi {}".format(str(mediana)))
print("A media foi {}".format(str(media)))

print("ANALISE DE DADOS DE LICITAÇÕES 2021:")
data_2021 = pd.read_csv('licitacoes-2021_04-01-2023_11-43-21.csv',sep=',',
                   on_bad_lines='skip', low_memory=False)
data_2021.dropna(subset=["VALORESTIMADO"],inplace=True)
data_2021 = data_2021['VALORESTIMADO']
data_2021 = pd.to_numeric(data_2021,errors="coerce")
mediana = data_2021.median()
media = round(data_2021.mean(),2)
print("A media foi {}".format(str(media)))
print("A mediana foi {}".format(str(mediana)))

##teste estatístico

t_stat, p_value = stats.ttest_ind(
    data_2021, data_2020, equal_var=False)

# # Print results
print("t-statistic:", t_stat)
print("p-value:", p_value)
# p-value de 0.05

