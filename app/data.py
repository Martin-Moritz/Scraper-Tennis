import pandas as pd
import plotly.express as px

from data.redis import *


## Data utilisée pour l'ajout de noms de continents et noms de pays dans la dataset principale
# Liste des continents
df_continent=pd.read_csv("https://pkgstore.datahub.io/JohnSnowLabs/country-and-continent-codes-list/country-and-continent-codes-list-csv_csv/data/b7876b7f496677669644f3d1069d3121/country-and-continent-codes-list-csv_csv.csv",sep=",")
# Liste des pays en français
df_pays=pd.read_csv("data/pays.csv",sep=',')

###############################################################################
#                                 TENNIS                                      #
###############################################################################

########### Import des données de la BDD Redis dans des dataframes pandas
# Classement ATP - singles
singles =[]

for i in range(100):
    singles.append(pd.DataFrame(redis_client.hgetall('single '+str(i+1)), index=[i]))

df_singles = pd.concat(singles)

# Classement ATP - doubles
doubles =[]

for i in range(100):
    doubles.append(pd.DataFrame(redis_client.hgetall('double '+str(i+1)), index=[i]))

df_doubles = pd.concat(doubles)


########### DEBUT DU TRAITEMENT DES DONNEES
########### Traitement des données scrapées / Singles

# Correction code Iso3 des pays
for i in range(df_singles.pays.size):
    if df_singles.pays.iloc[i]=='SUI':
        df_singles.pays.iloc[i] = 'CHE'
    elif df_singles.pays.iloc[i]=='URU':
        df_singles.pays.iloc[i] = 'URY'
    elif df_singles.pays.iloc[i]=='SLO':
        df_singles.pays.iloc[i] = 'SVN'
    elif df_singles.pays.iloc[i]=='RSA':
        df_singles.pays.iloc[i] = 'ZAF'
    elif df_singles.pays.iloc[i]=='POR':
        df_singles.pays.iloc[i] = 'PRT'
    elif df_singles.pays.iloc[i]=='GRE':
        df_singles.pays.iloc[i] = 'GRC'
    elif df_singles.pays.iloc[i]=='GER':
        df_singles.pays.iloc[i] = 'DEU'
    elif df_singles.pays.iloc[i]=='CRO':
        df_singles.pays.iloc[i] = 'HRV'
    elif df_singles.pays.iloc[i]=='CHI':
        df_singles.pays.iloc[i] = 'CHL'
    elif df_singles.pays.iloc[i]=='BUL':
        df_singles.pays.iloc[i] = 'BGR'
    elif df_singles.pays.iloc[i]=='ZIM':
        df_singles.pays.iloc[i] = 'ZWE'
    elif df_singles.pays.iloc[i]=='VIE':
        df_singles.pays.iloc[i] = 'VNM'
    elif df_singles.pays.iloc[i]=='TPE':
        df_singles.pays.iloc[i] = 'TWN'
    elif df_singles.pays.iloc[i]=='PHI':
        df_singles.pays.iloc[i] = 'PHL'
    elif df_singles.pays.iloc[i]=='NMI':
        df_singles.pays.iloc[i] = 'MNP'
    elif df_singles.pays.iloc[i]=='NED':
        df_singles.pays.iloc[i] = 'NLD'
    elif df_singles.pays.iloc[i]=='MON':
        df_singles.pays.iloc[i] = 'MCO'
    elif df_singles.pays.iloc[i]=='MAS':
        df_singles.pays.iloc[i] = 'MYS'
    elif df_singles.pays.iloc[i]=='MAD':
        df_singles.pays.iloc[i] = 'MDG'
    elif df_singles.pays.iloc[i]=='LIB':
        df_singles.pays.iloc[i] = 'LBY'
    elif df_singles.pays.iloc[i]=='LAT':
        df_singles.pays.iloc[i] = 'LVA'
    elif df_singles.pays.iloc[i]=='IRI':
        df_singles.pays.iloc[i] = 'IRN'
    elif df_singles.pays.iloc[i]=='INA':
        df_singles.pays.iloc[i] = 'IDN'
    elif df_singles.pays.iloc[i]=='HAI':
        df_singles.pays.iloc[i] = 'HTI'
    elif df_singles.pays.iloc[i]=='GUA':
        df_singles.pays.iloc[i] = 'GTM'
    elif df_singles.pays.iloc[i]=='ESA':
        df_singles.pays.iloc[i] = 'SLV'
    elif df_singles.pays.iloc[i]=='DEN':
        df_singles.pays.iloc[i] = 'DNK'
    elif df_singles.pays.iloc[i]=='CRC':
        df_singles.pays.iloc[i] = 'CRI'
    elif df_singles.pays.iloc[i]=='BAR':
        df_singles.pays.iloc[i] = 'BRB'
    elif df_singles.pays.iloc[i]=='BAH':
        df_singles.pays.iloc[i] = 'BHS'
    elif df_singles.pays.iloc[i]=='ANT':
        df_singles.pays.iloc[i] = 'ATG'
    elif df_singles.pays.iloc[i]=='ALG':
        df_singles.pays.iloc[i] = 'DZA'

# Ajout d'une colonne "continent"
continents=[]

for i in range(df_singles.pays.size):
    found = False
    j=0
    while j<df_continent.Three_Letter_Country_Code.size and found==False:
        if df_singles.pays.iloc[i]==df_continent.Three_Letter_Country_Code.iloc[j]:
            continents.append(df_continent.Continent_Name.iloc[j])
            found=True
        else:
            j=j+1
    if found==False:
        continents.append('NA')

# Renommage des continents en français
for i in range(len(continents)):
    if continents[i]=="Asia":
        continents[i]="Asie"
    elif continents[i]=="Oceania":
        continents[i]="Océanie"
    elif continents[i]=="North America":
        continents[i]="Amérique du Nord"
    elif continents[i]=="South America":
        continents[i]="Amérique du Sud"
    elif continents[i]=="Africa":
        continents[i]="Afrique"

df_singles['continent'] = continents

# Ajout d'une colonne "nom_pays"
pays=[]

for i in range(df_singles.pays.size):
    found = False
    j=0
    while j<df_pays.AFG.size and found==False:
        if df_singles.pays.iloc[i]==df_pays.AFG.iloc[j]:
            pays.append(df_pays.Afghanistan.iloc[j])
            found=True
        else:
            j=j+1
    if found==False:
        pays.append(df_singles.pays.iloc[i])

df_singles['nom_pays']=pays

#Ajout d'une colonne "nb_joueurs_pays"

nb_joueurs_pays = [0 for i in range(100)]

df_singles['nb_joueurs_pays'] = nb_joueurs_pays

for pays in df_singles.pays:
    total = 0
    for i in range(df_singles.pays.size):
        if df_singles.pays.iloc[i]==pays:
            total += 1
    df_singles.loc[df_singles["pays"]==pays,'nb_joueurs_pays'] = total

########### Traitement des données scrapées / Doubles

#Correction code Iso3 des pays
for i in range(df_doubles.pays.size):
    if df_doubles.pays.iloc[i]=='SUI':
        df_doubles.pays.iloc[i] = 'CHE'
    elif df_doubles.pays.iloc[i]=='URU':
        df_doubles.pays.iloc[i] = 'URY'
    elif df_doubles.pays.iloc[i]=='SLO':
        df_doubles.pays.iloc[i] = 'SVN'
    elif df_doubles.pays.iloc[i]=='RSA':
        df_doubles.pays.iloc[i] = 'ZAF'
    elif df_doubles.pays.iloc[i]=='POR':
        df_doubles.pays.iloc[i] = 'PRT'
    elif df_doubles.pays.iloc[i]=='GRE':
        df_doubles.pays.iloc[i] = 'GRC'
    elif df_doubles.pays.iloc[i]=='GER':
        df_doubles.pays.iloc[i] = 'DEU'
    elif df_doubles.pays.iloc[i]=='CRO':
        df_doubles.pays.iloc[i] = 'HRV'
    elif df_doubles.pays.iloc[i]=='CHI':
        df_doubles.pays.iloc[i] = 'CHL'
    elif df_doubles.pays.iloc[i]=='BUL':
        df_doubles.pays.iloc[i] = 'BGR'
    elif df_doubles.pays.iloc[i]=='ZIM':
        df_doubles.pays.iloc[i] = 'ZWE'
    elif df_doubles.pays.iloc[i]=='VIE':
        df_doubles.pays.iloc[i] = 'VNM'
    elif df_doubles.pays.iloc[i]=='TPE':
        df_doubles.pays.iloc[i] = 'TWN'
    elif df_doubles.pays.iloc[i]=='PHI':
        df_doubles.pays.iloc[i] = 'PHL'
    elif df_doubles.pays.iloc[i]=='NMI':
        df_doubles.pays.iloc[i] = 'MNP'
    elif df_doubles.pays.iloc[i]=='NED':
        df_doubles.pays.iloc[i] = 'NLD'
    elif df_doubles.pays.iloc[i]=='MON':
        df_doubles.pays.iloc[i] = 'MCO'
    elif df_doubles.pays.iloc[i]=='MAS':
        df_doubles.pays.iloc[i] = 'MYS'
    elif df_doubles.pays.iloc[i]=='MAD':
        df_doubles.pays.iloc[i] = 'MDG'
    elif df_doubles.pays.iloc[i]=='LIB':
        df_doubles.pays.iloc[i] = 'LBY'
    elif df_doubles.pays.iloc[i]=='LAT':
        df_doubles.pays.iloc[i] = 'LVA'
    elif df_doubles.pays.iloc[i]=='IRI':
        df_doubles.pays.iloc[i] = 'IRN'
    elif df_doubles.pays.iloc[i]=='INA':
        df_doubles.pays.iloc[i] = 'IDN'
    elif df_doubles.pays.iloc[i]=='HAI':
        df_doubles.pays.iloc[i] = 'HTI'
    elif df_doubles.pays.iloc[i]=='GUA':
        df_doubles.pays.iloc[i] = 'GTM'
    elif df_doubles.pays.iloc[i]=='ESA':
        df_doubles.pays.iloc[i] = 'SLV'
    elif df_doubles.pays.iloc[i]=='DEN':
        df_doubles.pays.iloc[i] = 'DNK'
    elif df_doubles.pays.iloc[i]=='CRC':
        df_doubles.pays.iloc[i] = 'CRI'
    elif df_doubles.pays.iloc[i]=='BAR':
        df_doubles.pays.iloc[i] = 'BRB'
    elif df_doubles.pays.iloc[i]=='BAH':
        df_doubles.pays.iloc[i] = 'BHS'
    elif df_doubles.pays.iloc[i]=='ANT':
        df_doubles.pays.iloc[i] = 'ATG'
    elif df_doubles.pays.iloc[i]=='ALG':
        df_doubles.pays.iloc[i] = 'DZA'

# Ajout d'une colonne "continent"
continents=[]

for i in range(df_doubles.pays.size):
    found = False
    j=0
    while j<df_continent.Three_Letter_Country_Code.size and found==False:
        if df_doubles.pays.iloc[i]==df_continent.Three_Letter_Country_Code.iloc[j]:
            continents.append(df_continent.Continent_Name.iloc[j])
            found=True
        else:
            j=j+1
    if found==False:
        continents.append('NA')

# Renommage des continents en français
for i in range(len(continents)):
    if continents[i]=="Asia":
        continents[i]="Asie"
    elif continents[i]=="Oceania":
        continents[i]="Océanie"
    elif continents[i]=="North America":
        continents[i]="Amérique du Nord"
    elif continents[i]=="South America":
        continents[i]="Amérique du Sud"
    elif continents[i]=="Africa":
        continents[i]="Afrique"

df_doubles['continent'] = continents

# Ajout d'une colonne "nom_pays"
pays=[]

for i in range(df_doubles.pays.size):
    found = False
    j=0
    while j<df_pays.AFG.size and found==False:
        if df_doubles.pays.iloc[i]==df_pays.AFG.iloc[j]:
            pays.append(df_pays.Afghanistan.iloc[j])
            found=True
        else:
            j=j+1
    if found==False:
        pays.append(df_doubles.pays.iloc[i])

df_doubles['nom_pays']=pays

# Ajout d'une colonne "nb_joueurs_pays"

nb_joueurs_pays = [0 for i in range(100)]

df_doubles['nb_joueurs_pays'] = nb_joueurs_pays

for pays in df_doubles.pays:
    total = 0
    for i in range(df_doubles.pays.size):
        if df_doubles.pays.iloc[i]==pays:
            total += 1
    df_doubles.loc[df_doubles["pays"]==pays,'nb_joueurs_pays'] = total


########## FIN DU TRAITEMENT DES DONNEES

########## OPTIONS DES PAYS SELECTIONNABLES / SINGLES
# nombre total de pays différents dans la dataset
nb_pays_singles = df_singles.drop_duplicates(subset=['pays']).shape[0]
# liste des codes à trois lettres (iso3) des différents pays de la dataset
liste_code_pays_singles = df_singles.drop_duplicates(subset=['pays']).pays
# liste des noms en français des différents pays
liste_noms_pays_singles = df_singles.drop_duplicates(subset=['pays']).nom_pays

## liste des pays à sélectionner dans le menu déroulant
options_selection_pays_singles = []
for i in range(liste_code_pays_singles.size):
    option = {}
    option['label']=liste_noms_pays_singles.iloc[i]
    option['value']=liste_code_pays_singles.iloc[i]
    options_selection_pays_singles.append(option)

########## OPTIONS DES PAYS SELECTIONNABLES / DOUBLES
# nombre total de pays différents dans la dataset
nb_pays_doubles = df_doubles.drop_duplicates(subset=['pays']).shape[0]
# liste des codes à trois lettres (iso3) des différents pays de la dataset
liste_code_pays_doubles = df_doubles.drop_duplicates(subset=['pays']).pays
# liste des noms en français des différents pays
liste_noms_pays_doubles = df_doubles.drop_duplicates(subset=['pays']).nom_pays

## liste des pays à sélectionner dans le menu déroulant
options_selection_pays_doubles = []
for i in range(liste_code_pays_doubles.size):
    option = {}
    option['label']=liste_noms_pays_doubles.iloc[i]
    option['value']=liste_code_pays_doubles.iloc[i]
    options_selection_pays_doubles.append(option)

##########
# Options de base
options_selection_pays = options_selection_pays_singles

########## OPTIONS DES JOUEURS SELECTIONNABLES

# singles
options_selection_joueurs_singles = []
for i in range(len(df_singles.joueur)):
    option = {}
    option['label']=df_singles.joueur.iloc[i]
    option['value']=i
    options_selection_joueurs_singles.append(option)

# doubles
options_selection_joueurs_doubles = []
for i in range(len(df_doubles.joueur)):
    option = {}
    option['label']=df_doubles.joueur.iloc[i]
    option['value']=i
    options_selection_joueurs_doubles.append(option)

# Options de base
options_selection_joueurs = options_selection_joueurs_singles
###########################################################################
