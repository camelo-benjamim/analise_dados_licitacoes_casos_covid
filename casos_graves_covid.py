##analisar os dados dos acidentes automobilisticos em recife-pe
import pandas as pd
from scipy import stats

data = pd.read_csv('casos graves covid.csv',sep=',',on_bad_lines="skip",low_memory=False)
## analisando obitos pela covid-19 em Recife-pe e buscando por padrões
data.dropna(subset=['idade'], inplace=True)
data.dropna(subset=['raca'],inplace=True)
data.dropna(subset=['sexo'],inplace=True)
geral = data
## analisando faixa de idade dos casos graves
geral = pd.to_numeric(geral['idade'],errors="coerce")
mediana = round(geral.median(),2)
media = round(geral.mean(),2)
print("MEDIA E MEDIANA DE IDADE DOS PACIENTES POR CASOS GRAVES DE COVID: ")
print("ESSA ANALISE FOI FEITA USANDO OS SEGUINTES CRITÉRIOS: RAÇA E GENERO ")
print("")
print("A média das idade dos pacientes foi: {}".format(str(media)))
print("A mediana das idades dos pacientes foi {}".format(str(mediana)))
##A média das idade dos pacientes foi: 54.76
##A mediana das idades dos pacientes foi 57.0
print("")
##analisando por grupo étnico-racial:
print("ANALISANDO OS PACIENTES POR GRUPO ÉTNICO RACIAL (BRANCOS, NEGROS, PARDOS E OUTROS) POR CASOS GRAVES DE COVID: ")
print("")
total_pacientes = len(data)
print("O número total de pacientes foi {}".format(str(total_pacientes)))
pacientes_brancos = data[data['raca'] == "Branca"]['idade']
pacientes_pretos = data[data['raca'] == "Preta"]['idade']
pacientes_pardos = data[data['raca'] == "Parda"]['idade']
print(" ")
print("Total de pacientes brancos: ")
print(str(len(pacientes_brancos)))
print("Total de pacientes pretos: ")
print(str(len(pacientes_pretos)))
print("Total de pacientes pardos: ")
print(str(len(pacientes_pardos)))
print("")
## porcentagam
print("ANALISANDO A PORCENTAGEM DE PACIENTES EM ESTADO GRAVE DE COVID POR GRUPO ÉTNICO RACIAL (BRANCOS,PRETOS,PARDOS E OUTROS) ")
porcentagem_brancos = round(((pacientes_brancos.__len__() * 100) / total_pacientes),2)
porcentagem_pretos = round(((pacientes_pretos.__len__() * 100) / total_pacientes),2)
porcentagem_pardos = round(((pacientes_pardos.__len__() * 100)/ total_pacientes),2)
outras_racas = len(data) - len(pacientes_brancos) - len(pacientes_pretos) - len(pacientes_pardos)
porcentagem_outras_racas = round(((outras_racas * 100)/total_pacientes),2)
print("Pacientes brancos: {} %".format(str(porcentagem_brancos)))
print("Pacientes pardos: {} %".format(str(porcentagem_pardos)))
print("Pacientes pretos: {} %".format(str(porcentagem_pretos)))
print("Pacientes de outras raças/etnias ou ignorado : {} %".format(porcentagem_outras_racas))
print("")
##resultados
##Total de pacientes brancos:
##5609
##Total de pacientes pretos:
##1108
##Total de pacientes pardos:
##15040
##O número total de pacientes foi 30106
##A porcentagem com relação a raça/etnia dos pacientes é:
##Pacientes brancos: 18.63 %
##Pacientes pardos: 49.96 %
##Pacientes pretos: 3.68 %
##Pacientes de outras raças/etnias: 27.73 %


##analisando idade média de cada grupo racial
print("ANALISANDO A MÉDIA DE IDADE ENTRE OS PACIENTES EM ESTADO GRAVE DE COVID POR RAÇA (BRANCO,NEGRO E PARDO)")
idade_brancos = pd.to_numeric(pacientes_brancos,errors="coerce")
idade_pretos = pd.to_numeric(pacientes_pretos,errors="coerce")
idade_pardos = pd.to_numeric(pacientes_pardos,errors="coerce")

##testes
t_stat, p_value = stats.ttest_ind(idade_brancos, idade_pretos, equal_var=False)
t_stat, i_value = stats.ttest_ind(idade_brancos, idade_pardos, equal_var=False)
t_stat, y_value = stats.ttest_ind(idade_pardos, idade_pretos, equal_var=False)
alpha = 0.05
if (p_value > alpha) and (i_value > alpha) and (y_value > alpha):
    print("Fail to reject the null hypothesis")
else:
    print("Reject the null hypothesis")
    
media_idade_brancos = round(idade_brancos.mean(),2)
mediana_idade_brancos = round(idade_brancos.median(),2)
print("")
##
print("A média de idade entre os pacientes Brancos foi {}".format(str(media_idade_brancos)))
print("A mediana de idade entre os pacientes Brancos foi {}".format(str(mediana_idade_brancos)))
##
media_idade_pardos = round(idade_pardos.mean(),2)
mediana_idade_pardos = round(idade_pardos.median(),2)
##
print("A média de idade entre os pacientes Pardos foi {}".format(str(media_idade_pardos)))
print("A mediana de idade entre os pacientes Pardos foi {}".format(str(mediana_idade_pardos)))
##
media_idade_pretos = round(idade_pretos.mean(),2)
mediana_idade_pretos = round(idade_pretos.median(),2)
##
print("A média de idade entre os pacientes Pretos foi {}".format(str(media_idade_pretos)))
print("A mediana de idade entre os pacientes Pretos foi {}".format(str(mediana_idade_pretos)))
##
print("")
print("Analisando óbitos...")
print("")
obitos = data[data['evolucao'] == 'ÓBITO']
##analisando a porcentagem dos pacientes que vieram a óbito
porcentagem_obitos = round(((len(obitos)* 100) / total_pacientes),2)
print("A porcentagem total dos pacientes que vieram a óbito foi: {}".format(str(porcentagem_obitos)))
obitos_idade = obitos['idade']
obitos_idade = pd.to_numeric(obitos_idade,errors="coerce")
media_idade_obitos = round(obitos_idade.mean(),2)
mediana_idade_obitos = round(obitos_idade.median(),2)
print("A média de idade dos pacientes que vieram a óbito foi {} anos: ".format(str(media_idade_obitos)))
print("A mediana de idade dos pacientes que vieram a óbito foi {} anos: ".format(str(mediana_idade_obitos)))
print("")
##porcentagem de pacientes brancos que vieram a óbito
print("ÓBITOS DE PACIENTES BRANCOS: ")
obito_brancos = obitos[obitos["raca"] == "Branca"]
print(str(len(obito_brancos)))
print("ÓBITOS DE PACIENTES NEGROS: ")
obito_negros = obitos[obitos["raca"] == "Preta"]
print(str(len(obito_negros)))
print("ÓBITOS DE PACIENTES PARDOS: ")
obito_pardos= obitos[obitos["raca"] == "Parda"]
print(str(len(obito_pardos)))
print("")
print("ANALISANDO A MEDIA E MEDIANA DE IDADE ENTRE OS PACIENTES QUE VIERAM A ÓBITO: ")
idade_brancos = obito_brancos['idade']
idade_brancos = pd.to_numeric(idade_brancos,errors="coerce")
media_brancos = round(idade_brancos.mean(),2)
mediana_brancos = round(idade_brancos.median(),2)
idade_negros = obito_negros['idade']
idade_negros = pd.to_numeric(idade_negros,errors="coerce")
media_negros = round(idade_negros.mean(),2)
mediana_negros = round(idade_negros.median(),2)
idade_pardos = obito_pardos['idade']
idade_pardos = pd.to_numeric(idade_pardos,errors="coerce")
media_pardos = round(idade_pardos.mean(),2)
mediana_pardos = round(idade_pardos.median(),2)

print("MÉDIA DE IDADE ENTRE OS PACIENTES BRANCOS QUE VIERAM A ÓBITO {}".format(str(media_brancos)))
print("MÉDIANA DE IDADE ENTRE OS PACIENTES BRANCOS QUE VIERAM A ÓBITO {}".format(str(mediana_brancos)))
print("")
print("MÉDIA DE IDADE ENTRE OS PACIENTES NEGROS QUE VIERAM A ÓBITO {}".format(str(media_negros)))
print("MÉDIANA DE IDADE ENTRE OS PACIENTES NEGROS QUE VIERAM A ÓBITO {}".format(str(mediana_negros)))
print("")
print("MÉDIA DE IDADE ENTRE OS PACIENTES PARDOS QUE VIERAM A ÓBITO {}".format(str(media_pardos)))
print("MÉDIANA DE IDADE ENTRE OS PACIENTES PARDOS QUE VIERAM A ÓBITO {}".format(str(mediana_pardos)))

##por genero
print("")
mulheres = data[data['sexo'] == 'Feminino']
homens = data[data['sexo'] == 'Masculino']
print("POR GÊNERO: ")
print("")
print("Total de mulheres em estado grave pelo covid: {}".format(str(len(mulheres))))
print("Total de homens em estado grave pelo covid {}".format(str(len(homens))))
mulheres_negras = mulheres[mulheres['raca'] == 'Preta']['idade']
mulheres_negras = pd.to_numeric(mulheres_negras,errors="coerce")
media_mnegras = mulheres_negras.mean()
mediana_mnegras = mulheres_negras.median()
mulheres_brancas = mulheres[mulheres['raca'] == 'Branca']['idade']
mulheres_brancas = pd.to_numeric(mulheres_brancas,errors="coerce")
media_mbrancas = mulheres_brancas.mean()
mediana_mbrancas = mulheres_brancas.median()
mulheres_pardas = mulheres[mulheres['raca'] == 'Parda']['idade']
mulheres_pardas = pd.to_numeric(mulheres_pardas,errors="coerce")
media_mpardas =  mulheres_pardas.mean()
mediana_mpardas = mulheres_pardas.median()
print("Por raça/etnia")
print("")
print("Media de idade de mulheres negras em estado grave é: {}".format(str(media_mnegras)))
print("Mediana de idade de mulheres negras em estado grave é: {}".format(str(mediana_mnegras)))
print("Media de idade de mulheres brancas em estado grave é: {}".format(str(media_mbrancas)))
print("Mediana de idade de mulheres brancas em estado grave é: {}".format(str(mediana_mnegras)))
print("Media de idade de mulheres pardas em estado grave é: {}".format(str(media_mpardas)))
print("Mediana de idade de mulheres pardas em estado grave é: {}".format(str(media_mpardas)))
homens_negros = homens[homens['raca'] == "Preta"]['idade']
homens_negros = pd.to_numeric(homens_negros,errors="coerce")
media_hnegros = homens_negros.mean()
mediana_hnegros = homens_negros.median()
homens_brancos = homens[homens['raca'] == "Branca"]['idade']
homens_brancos = pd.to_numeric(homens_brancos,errors="coerce")
media_hbrancos = homens_brancos.mean()
mediana_hbrancos = homens_brancos.median()
homens_pardos = homens[homens['raca'] == "Parda"]['idade']
homens_pardos = pd.to_numeric(homens_pardos,errors="coerce")
media_hpardos = homens_pardos.mean()
mediana_hpardos = homens_pardos.median()
print("")
print("A média de idade de homens negros em estado grave é {}".format(str(media_hnegros)))
print("A mediana de idade de homens negros em estado grave é {}".format(str(mediana_hnegros)))
print("A média de idade de homens brancos em estado grave é {}".format(str(media_hbrancos)))
print("A mediana de idade de homens brancos em estado grave é {}".format(str(mediana_hbrancos)))
print("A média de idade de homens pardos em estado grave é {}".format(str(media_hpardos)))
print("A mediana de idade de homens pardos em estado grave é {}".format(str(mediana_hpardos)))
print("")
print("")
print("ÓBITO")
print("")
mulheres = data[data['evolucao'] == 'ÓBITO']
homens = data[data['evolucao'] == 'ÓBITO']
print("")
print("Total de mulheres que vieram a óbito pelo covid: {}".format(str(len(mulheres))))
print("Total de homens que vieram a óbito  pelo covid {}".format(str(len(homens))))
print("")
mulheres_negras = mulheres[mulheres['raca'] == 'Preta']['idade']
mulheres_negras = pd.to_numeric(mulheres_negras,errors="coerce")
media_mnegras = mulheres_negras.mean()
mediana_mnegras = mulheres_negras.median()
mulheres_brancas = mulheres[mulheres['raca'] == 'Branca']['idade']
mulheres_brancas = pd.to_numeric(mulheres_brancas,errors="coerce")
media_mbrancas = mulheres_brancas.mean()
mediana_mbrancas = mulheres_brancas.median()
mulheres_pardas = mulheres[mulheres['raca'] == 'Parda']['idade']
mulheres_pardas = pd.to_numeric(mulheres_pardas,errors="coerce")
media_mpardas =  mulheres_pardas.mean()
mediana_mpardas = mulheres_pardas.median()
print("POR ETNIA")
print("")
print("Media de idade de mulheres negras que vieram a óbito  é: {}".format(str(media_mnegras)))
print("Mediana de idade de mulheres negras que vieram a óbito  é: {}".format(str(mediana_mnegras)))
print("Media de idade de mulheres brancas que vieram a óbito  é: {}".format(str(media_mbrancas)))
print("Mediana de idade de mulheres brancas que vieram a óbito  é: {}".format(str(mediana_mnegras)))
print("Media de idade de mulheres pardas que vieram a óbito  é: {}".format(str(media_mpardas)))
print("Mediana de idade de mulheres pardas que vieram a óbito  é: {}".format(str(media_mpardas)))
print("")
homens_negros = homens[homens['raca'] == "Preta"]['idade']
homens_negros = pd.to_numeric(homens_negros,errors="coerce")
media_hnegros = homens_negros.mean()
mediana_hnegros = homens_negros.median()
homens_brancos = homens[homens['raca'] == "Branca"]['idade']
homens_brancos = pd.to_numeric(homens_brancos,errors="coerce")
media_hbrancos = homens_brancos.mean()
mediana_hbrancos = homens_brancos.median()
homens_pardos = homens[homens['raca'] == "Parda"]['idade']
homens_pardos = pd.to_numeric(homens_pardos,errors="coerce")
media_hpardos = homens_pardos.mean()
mediana_hpardos = homens_pardos.median()

print("A média de idade de homens negros que vieram a óbito  é {}".format(str(media_hnegros)))
print("A mediana de idade de homens negros que vieram a óbito  é {}".format(str(mediana_hnegros)))
print("A média de idade de homens brancos que vieram a óbito  é {}".format(str(media_hbrancos)))
print("A mediana de idade de homens brancos que vieram a óbito  é {}".format(str(mediana_hbrancos)))
print("A média de idade de homens pardos que vieram a óbito  é {}".format(str(media_hpardos)))
print("A mediana de idade de homens pardos que vieram a óbito  é {}".format(str(mediana_hpardos)))