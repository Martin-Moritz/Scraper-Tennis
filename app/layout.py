import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from .figures import *
from .navbar import *

from .data import *

# Couleurs utilisées dans le Dashboard
colors = {
    'background1': '#20B5C8',
    'background2': '#D4E6F1',
    'background3': '#717677',
    'text': 'white'
}

# Disposition des figures et autres composants
layout = html.Div(style={'backgroundColor': colors['background1']}, children=[

    # navbar
    html.Div([navbar]),

    dbc.Row([
        dbc.Col([
            html.Div(children=[
                # Choix entre classement ATP : Singles ou Doubles
                dbc.RadioItems(
                id='singles-doubles',
                options=[
                    {'label': 'Singles', 'value': 'singles'},
                    {'label': 'Doubles', 'value': 'doubles'}
                ],
                value='singles',
                labelStyle={'width':'100%','backgroundColor':colors['background3'],'color':colors['text'],'fontWeight': 'bold',}
                ),
            ]),
        ], width=1),

        dbc.Col([
            html.H2(
                id='text-before-button',
                children='Données scrapées - Classement ATP : Singles',
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontWeight': 'bold',
                    'fontSize':20
                }
            ),
        ], width=3),

        dbc.Col([
            # Lien vers les données utilisées
            dbc.Button("ATP Tour",id="scraper-button", color="success", className="mr-1", href="https://www.atptour.com/en/rankings/singles", style={'fontWeight': 'bold'}),
        ], width=1),
    ], no_gutters=True, justify='around', align = 'center', style={'height':'70px', 'backgroundColor':colors['background3']}),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    html.H2(
        id='titre-classement',
        children='Classement - Singles',
        style={
            'textAlign': 'center',
            'fontWeight': 'bold',
            'fontSize':20
        }
    ),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    dbc.Row([
        dbc.Col([
            html.Div(children=[
                # Menu déroulant pour le choix des joueurs
                dcc.Dropdown(
                id='selection-joueur',
                placeholder='Sélectionner un joueur du TOP 100 (Singles)',
                options=options_selection_joueurs,
                multi=True,
                value=[],
                style={'display': 'inline-block','width':'100%'}
                ),
            ]),
        ], width=7),
    ], no_gutters=True, justify='around', align = 'center'),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    dbc.Row([
        dbc.Col([
            html.Div(id='classement-joueurs', children=[
                dbc.ListGroup([
                    dbc.ListGroupItem("Joueur", color="secondary", style={'textAlign': 'center','width':'300px','fontWeight': 'bold'}),
                    dbc.ListGroupItem("Rang", color="secondary", style={'textAlign': 'center','width':'110px','fontWeight': 'bold'}),
                    dbc.ListGroupItem("Points", color="secondary", style={'textAlign': 'center','width':'140px','fontWeight': 'bold'}),
                    dbc.ListGroupItem("Age", color="secondary", style={'textAlign': 'center','width':'110px','fontWeight': 'bold'}),
                    dbc.ListGroupItem("Tournois joués", color="secondary", style={'textAlign': 'center','width':'200px','fontWeight': 'bold'}),
                    dbc.ListGroupItem("Pays", color="secondary", style={'textAlign': 'center','width':'110px','fontWeight': 'bold'}),
                ],horizontal=True,className="mb-2",),
                dbc.ListGroup([
                    dbc.ListGroupItem(df_singles.joueur[0], style={'textAlign': 'center','width':'300px'}),
                    dbc.ListGroupItem(df_singles.rang[0], style={'textAlign': 'center','width':'110px'}),
                    dbc.ListGroupItem(df_singles.points[0], style={'textAlign': 'center','width':'140px'}),
                    dbc.ListGroupItem(df_singles.age[0], style={'textAlign': 'center','width':'110px'}),
                    dbc.ListGroupItem(df_singles.nb_tournois[0], style={'textAlign': 'center','width':'200px'}),
                    dbc.ListGroupItem(df_singles.pays[0], style={'textAlign': 'center','width':'110px'}),
                ],horizontal=True,className="mb-2",),
            ]),
            ], width=6, align='center'),

    ], no_gutters=True, justify='around', align = 'center', style={'backgroundColor':colors['background1']}),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'60px'}),

    html.H2(
        children='Graphiques',
        style={
            'textAlign': 'center',
            'fontWeight': 'bold',
            'fontSize':20
        }
    ),

    dbc.Row([
        dbc.Col([
            # Figure Histogramme
            html.Div(children=[dcc.Graph(id='histogram', figure=histogramme)]),
        ], width=5),

        dbc.Col([
            # Figure Diagramme en barres
            html.Div(children=[dcc.Graph(id='bar-diagram', figure=diagramme)]),
        ], width=6),
    ], no_gutters=True, justify='center', align = 'center'),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    html.H2(
        children='Carte',
        style={
            'textAlign': 'center',
            'fontWeight': 'bold',
            'fontSize':20
        }
    ),

    dbc.Row([], no_gutters=True, justify='around', align = 'center', style={'height':'30px'}),

    dbc.Row([
        dbc.Col([
                html.Div(children=[
                    # Menu déroulant pour le choix des pays
                    dcc.Dropdown(
                    id='selection-pays',
                    placeholder='Sélectionner un pays',
                    options=options_selection_pays,
                    multi=True,
                    value=[],
                    style={'display': 'inline-block','width':'100%'}
                    ),
                ]),
            ], width=7),
    ], no_gutters=True, justify='around', align = 'center'),

    # Figure Carte
    html.Div(children=[dcc.Graph(id='mapbox', figure=carte)]),

])
