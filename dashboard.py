import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dash import Dash, dcc, html
import base64

# Создание экземпляра приложения Dash
app = Dash(__name__)

# Определение директорий
current_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(current_dir, 'results')
datasets_dir = os.path.join(current_dir, 'datasets_copy')
combined_dataset_path = os.path.join(datasets_dir, 'combined_dataset.csv')

# Загрузка данных
combined_dataset = pd.read_csv(combined_dataset_path)

# Сохранение графиков из results в виде base64
def encode_image(image_file):
    with open(image_file, 'rb') as file:
        encoded = base64.b64encode(file.read()).decode('utf-8')
    return f'data:image/png;base64,{encoded}'

graph_paths = {
    'age_distribution': os.path.join(results_dir, 'age_distribution.png'),
    'gender_distribution': os.path.join(results_dir, 'gender_vs_pulmonary_diseases.png'),
    'smoking_distribution': os.path.join(results_dir, 'smoking_vs_pulmonary_diseases.png'),
    'alcohol_distribution': os.path.join(results_dir, 'alcohol_distribution.png'),
    'diabetes_distribution': os.path.join(results_dir, 'diabetes_distribution.png'),
    'boxplot': os.path.join(results_dir, 'boxplots.png'),
    'correlation_heatmap': os.path.join(results_dir, 'correlation_heatmap.png'),
    'roc_curve': os.path.join(results_dir, 'roc_curve_pulmonary.png'),
    'feature_importance': os.path.join(results_dir, 'feature_importance.png')
}

encoded_graphs = {name: encode_image(path) for name, path in graph_paths.items()}

# Layout для дашборда с вкладками для улучшенной навигации
app.layout = html.Div([
    html.H1('Dashboard: Respiratory Risk Patterns', style={'textAlign': 'center'}),
    dcc.Tabs(id='tabs', children=[
        dcc.Tab(label='Age Distribution', children=[html.Img(src=encoded_graphs['age_distribution'], style={'width': '80%', 'margin': 'auto'})]),
        dcc.Tab(label='Gender Distribution', children=[html.Img(src=encoded_graphs['gender_distribution'], style={'width': '80%', 'margin': 'auto'})]),
        dcc.Tab(label='Smoking Distribution', children=[html.Img(src=encoded_graphs['smoking_distribution'], style={'width': '80%', 'margin': 'auto'})]),
        dcc.Tab(label='Alcohol Consumption', children=[html.Img(src=encoded_graphs['alcohol_distribution'], style={'width': '80%', 'margin': 'auto'})]),
        dcc.Tab(label='Diabetes Distribution', children=[html.Img(src=encoded_graphs['diabetes_distribution'], style={'width': '80%', 'margin': 'auto'})]),
        dcc.Tab(label='Boxplots', children=[html.Img(src=encoded_graphs['boxplot'], style={'width': '80%', 'margin': 'auto'})]),
        dcc.Tab(label='Correlation Heatmap', children=[html.Img(src=encoded_graphs['correlation_heatmap'], style={'width': '80%', 'margin': 'auto'})]),
        dcc.Tab(label='ROC Curve', children=[
            html.Img(src=encoded_graphs['roc_curve'], style={'width': '80%', 'margin': 'auto'}),
            html.P('Class 0: Отсутствие респираторных заболеваний.'),
            html.P('Class 2: Хроническая обструктивная болезнь легких (COPD).'),
            html.P('Class 3: Астма.'),
            html.P('Class 4: Рак легких.')
        ]),
        dcc.Tab(label='Feature Importance', children=[html.Img(src=encoded_graphs['feature_importance'], style={'width': '80%', 'margin': 'auto'})])
    ])
])

# Запуск дашборда
if __name__ == '__main__':
    app.run_server(debug=True)
