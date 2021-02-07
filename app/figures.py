import plotly.express as px
import plotly.graph_objects as go

from .data import *

# Couleurs utilisées dans le Dashboard
colors = {
    'background1': '#20B5C8',
    'background2': '#D4E6F1',
    'background3': '#717677',
    'text': 'white'
}

## Figure Carte

# fonction pour créer la carte
def create_carte(df,pays,values,focus='world',type='Singles'):
    """
    Retourne une carte choroplèthe.

    Parameters:
        df : DataFrame or array-like or dict
        pays : Column DataFrame
        values : Column DataFrame
        focus : str
        type : str

    Returns:
        Return type : plotly.graph_objects.Figure
    """

    carte = px.choropleth(df,locations=pays, color=values,
                                    color_continuous_scale="burgyl",
                                    range_color=(1,12),
                                    scope=focus,
                                    labels={pays:"Pays",values:"Nombre de joueurs / Pays"},
                                    hover_name="nom_pays",
                                    template="ggplot2",
                                    title="Nombre de joueurs par pays dans le TOP 100 - Classement ATP / " + type,
                                    height=700)
    carte.update_layout(title={'font':{'color':colors['text']}}, paper_bgcolor=colors['background1'])
    return carte

# création de la carte
carte = create_carte(df_singles,'pays','nb_joueurs_pays')


## Figure Histogramme

# fonction pour créer l'histogramme
def create_histogramme(df,x,type='Singles'):
    """
    Retourne un histogramme.

    Parameters:
        df : DataFrame or array-like or dict
        year : str

    Returns:
        Return type : plotly.graph_objects.Figure
    """

    histogramme = px.histogram(df, title="Répartition de l'âge des joueurs du TOP 100 - Classement ATP / " + type,
                               x=x, labels={'pays':'Pays','age':'Age'},
                               template='plotly', nbins=6, range_x=(15,45), range_y=(0,40), color_discrete_sequence=['indianred'])
    histogramme.update_layout(title={'font':{'size':15, 'color':colors['text']}},
                              yaxis={'title':{'text':'Nombre de joueurs'}}, paper_bgcolor=colors['background1'])
    return histogramme

# création de l'histogramme
histogramme = create_histogramme(df_singles,'age')


## Figure Diagramme en barres

# fonction pour créer le diagramme
def create_diagramme(df,x,y,type='Singles'):
    """
    Retourne un diagramme.

    Parameters:
        df : DataFrame or array-like or dict
        year : str

    Returns:
        Return type : plotly.graph_objects.Figure
    """

    diagramme = px.bar(df, title="Points des joueurs du TOP 10 - Classement ATP / " + type, x=x, y=y,
                             color=x, labels={x:'Joueur', y:"Points"},
                             template='plotly', range_y=(0,15000))
    diagramme.update_layout(title={'font':{'size':15, 'color':colors['text']}}, xaxis={'title':{'text':''}},
                            yaxis={'title':{'text':'Points'}}, paper_bgcolor=colors['background1'])
    return diagramme

# création du diagramme
diagramme = create_diagramme(df_singles,'joueur','points')
