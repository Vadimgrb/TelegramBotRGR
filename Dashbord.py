import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Дашборд киностудии", style={'textAlign': 'center'}),
    html.Div("Интерактивный дашборд для анализа данных киностудии.", style={'textAlign': 'center'}),

    dcc.Dropdown(
        id='genre-dropdown',
        options=[
            {'label': 'Драма', 'value': 'Drama'},
            {'label': 'Комедия', 'value': 'Comedy'},
            {'label': 'Экшен', 'value': 'Action'},
            {'label': 'Ужасы', 'value': 'Horror'}
        ],
        value='Drama',
        clearable=False
    ),
    dcc.Graph(id='revenue-graph'),
    dcc.Slider(
        id='year-slider',
        min=2000,
        max=2023,
        value=2023,
        marks={i: str(i) for i in range(2000, 2024)},
        step=1
    ),
    dcc.Checklist(
        id='award-checklist',
        options=[
            {'label': 'Оскар', 'value': 'Oscar'},
            {'label': 'Золотой глобус', 'value': 'Golden Globe'}
        ],
        value=['Oscar']
    ),
    html.Button('Обновить', id='update-button', n_clicks=0),
    html.Div(id='output-container')
])


@app.callback(
    Output('revenue-graph', 'figure'),
    Input('genre-dropdown', 'value'),
    Input('year-slider', 'value'),
    Input('award-checklist', 'value')
)
def update_graph(selected_genre, selected_year, selected_awards):
    # Здесь должна быть логика для обновления графика
    return {
        'data': [],  # Здесь будет ваш график
        'layout': {'title': 'Выручка по жанрам'}
    }


if __name__ == '__main__':
    app.run_server(debug=True)

