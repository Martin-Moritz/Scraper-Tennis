import dash_bootstrap_components as dbc
import dash_html_components as html

# Couleurs utilisées dans le Dashboard
colors = {
    'background1': '#20B5C8',
    'background2': '#D4E6F1',
    'background3': '#717677',
    'text': 'white'
}

logo = "assets/img/logo_ESIEE_blanc.png"

items=[
        dbc.DropdownMenuItem("Moritz Martin",href="https://www.linkedin.com/in/martin-moritz-1944731b1",external_link=True),
        dbc.DropdownMenuItem("Rogissart Vincent",href="https://www.linkedin.com/in/vincent-rogissart-20743a1aa/",external_link=True),
        ]

navbar = dbc.Navbar(
    [
        dbc.Col([
            html.A(html.Img(src=logo, height="50px"),href="https://www.esiee.fr/"),
        ], width=2),
        dbc.Col([
            html.H1(
                children='Projet ESIEE Paris : Scraper - ATP Tour (Classement Tennis)',
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'fontWeight': 'bold',
                    'fontSize':22
                }
            ),
        ], width=8),
        dbc.DropdownMenu(items,label="Auteurs",color="info",className="ml-auto p-2 bd-highlight",in_navbar=True,direction="left", toggle_style={'fontWeight': 'bold'}),
    ],
    color="dark",
    dark=True,
)
