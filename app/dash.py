import flask
import dash
import dash_bootstrap_components as dbc

from . import app

from .callbacks import register_callbacks
from .layout import layout

# Style de page utilisé pour le dashboard -> 'dbc.themes.BOOTSTRAP' permet d'utiliser les dash_bootstrap_components
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Création de l'application Dash
dashapp = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=app,
    routes_pathname_prefix='/')

dashapp.layout = layout
register_callbacks(dashapp)
