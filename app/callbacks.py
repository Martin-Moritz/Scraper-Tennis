import dash
from dash.dependencies import *
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from .figures import *
from .data import *

# Callbacks pour rafraichir et mettre à jour les différentes figures et composants
def register_callbacks(dashapp):
    @dashapp.callback(
        Output('mapbox', 'figure'),
        [Input('selection-pays', 'value'), Input('singles-doubles','value')])
    def update_carte(selected_countries, selected_classement):
        """
        Retourne une carte choroplèthe.

        Parameters:
            selected_countries : list of str
            selected_classement : str

        Returns:
            Return type : plotly.graph_objects.Figure
        """

        # focus de la carte
        focus = 'world'

        # filtrage des données : classement ATP singles ou doubles
        if selected_classement=='singles':
            filtered_df = df_singles
            type = 'Singles'
        else:
            filtered_df = df_doubles
            type = 'Doubles'

        # choix des pays affichés sur la carte ?
        if selected_countries!=[]:
            # Mise à jour de la carte en fonction des pays sélectionnés
            frames = []
            for i in selected_countries:
                frames.append(filtered_df[filtered_df["pays"]==i])
            filtered_df = pd.concat(frames)

            # Détermine si les pays sélectionnés se situent sur le même continent
            cont = filtered_df.continent.iloc[0]
            unique_continent = True
            i = 1
            while unique_continent==True and i<len(filtered_df):
                if filtered_df.continent.iloc[i]==cont:
                    i=i+1
                else:
                    unique_continent=False

            # Ajuste le focus de la carte si les pays sélectionnés sont sur le même continent
            if unique_continent==True:
                if cont=="Asie":
                    focus='asia'
                elif cont=="Europe":
                    focus='europe'
                elif cont=="Amérique du Nord":
                    focus='north america'
                elif cont=="Amérique du Sud":
                    focus='south america'
                elif cont=="Afrique":
                    focus='africa'

        # Création de la figure
        carte = create_carte(filtered_df,'pays','nb_joueurs_pays',focus,type)

        return carte


    @dashapp.callback(
        [Output('selection-pays', 'options'), Output('selection-joueur', 'options'), Output('selection-joueur', 'placeholder'), Output('titre-classement', 'children')],
        [Input('singles-doubles','value')])
    def update_dropdown(selected_classement):
        """
        Retourne un paramètre d'un dcc.Dropdown

        Parameters:
            selected_classement : str

        Returns:
            Return type : dict
        """

        # Mise à jour des pays sélectionnables dans le menu déroulant
        if selected_classement == "singles":
            options_pays = options_selection_pays_singles
            options_joueurs = options_selection_joueurs_singles
            placeholder = 'Sélectionner un joueur du TOP 100 (Singles)'
            titre = 'Classement - Singles'
        else:
            options_pays = options_selection_pays_doubles
            options_joueurs = options_selection_joueurs_doubles
            placeholder = 'Sélectionner un joueur du TOP 100 (Doubles)'
            titre = 'Classement - Doubles'

        return options_pays, options_joueurs, placeholder, titre


    @dashapp.callback(
        Output('histogram', 'figure'),
        [Input('singles-doubles','value')])
    def update_histogramme(selected_classement):
        """
        Retourne un histogramme.

        Parameters:
            selected_classement : str

        Returns:
            Return type : plotly.graph_objects.Figure
        """
        # Filtrage des données
        if selected_classement=='singles':
            filtered_df = df_singles
            type = 'Singles'
        else:
            filtered_df = df_doubles
            type = 'Doubles'

        # Création de la figure
        histogramme = create_histogramme(filtered_df, 'age',type)

        return histogramme


    @dashapp.callback(
        Output('bar-diagram', 'figure'),
        [Input('singles-doubles', 'value')])
    def update_diagramme(selected_classement):
        """
        Retourne un diagramme.

        Parameters:
            selected_classement : str

        Returns:
            Return type : plotly.graph_objects.Figure
        """

        # Filtrage des données
        if selected_classement=='singles':
            filtered_df = df_singles
            type = 'Singles'
        else:
            filtered_df = df_doubles
            type = 'Doubles'

        # TOP 10 du classement
        filtered_df = filtered_df.iloc[:10]

        # Création de la figure
        diagramme = create_diagramme(filtered_df,'joueur','points',type)

        return diagramme


    @dashapp.callback([Output("scraper-button","color"), Output("scraper-button","href"), Output("text-before-button","children")],
    [Input("singles-doubles", "value")])
    def update_link(selected_classement):
        """
        Met à jour le lien vers les données scrapées.

        Parameters:
            selected_classement : str
        """

        if selected_classement=='singles':
            couleur = "success"
            href = "https://www.atptour.com/en/rankings/singles"
            texte = "Données scrapées - Classement ATP : Singles"
        else:
            couleur = "warning"
            href = "https://www.atptour.com/en/rankings/doubles"
            texte = "Données scrapées - Classement ATP : Doubles"

        return couleur, href, texte


    @dashapp.callback(
        Output('classement-joueurs', 'children'),
        [Input('selection-joueur', 'value'), Input('singles-doubles','value')])
    def update_classement(selected_players, selected_classement):
        """
        Change l'affichage du classement avec les joueurs sélectionnés.

        Parameters:
            selected_players : list of str
            selected_classement : str
        """

        # Le classement à afficher
        children = [
        dbc.ListGroup([
            dbc.ListGroupItem("Joueur", color="secondary", style={'textAlign': 'center','width':'300px','fontWeight': 'bold'}),
            dbc.ListGroupItem("Rang", color="secondary", style={'textAlign': 'center','width':'110px','fontWeight': 'bold'}),
            dbc.ListGroupItem("Points", color="secondary", style={'textAlign': 'center','width':'140px','fontWeight': 'bold'}),
            dbc.ListGroupItem("Age", color="secondary", style={'textAlign': 'center','width':'110px','fontWeight': 'bold'}),
            dbc.ListGroupItem("Tournois joués", color="secondary", style={'textAlign': 'center','width':'200px','fontWeight': 'bold'}),
            dbc.ListGroupItem("Pays", color="secondary", style={'textAlign': 'center','width':'110px','fontWeight': 'bold'}),
        ],horizontal=True,className="mb-2",)
        ]

        # filtrage des données : classement ATP singles ou doubles
        if selected_classement=='singles':
            filtered_df = df_singles
        else:
            filtered_df = df_doubles


        if selected_players==[]:
            selected_players=[0,1,2,3,4]

        # Mise à jour du classement
        for i in selected_players:
            children.append(dbc.ListGroup([
                dbc.ListGroupItem(filtered_df.joueur[i], style={'textAlign': 'center','width':'300px'}),
                dbc.ListGroupItem(filtered_df.rang[i], style={'textAlign': 'center','width':'110px'}),
                dbc.ListGroupItem(filtered_df.points[i], style={'textAlign': 'center','width':'140px'}),
                dbc.ListGroupItem(filtered_df.age[i], style={'textAlign': 'center','width':'110px'}),
                dbc.ListGroupItem(filtered_df.nb_tournois[i], style={'textAlign': 'center','width':'200px'}),
                dbc.ListGroupItem(filtered_df.pays[i], style={'textAlign': 'center','width':'110px'}),
            ],horizontal=True,className="mb-2",))

        return children
