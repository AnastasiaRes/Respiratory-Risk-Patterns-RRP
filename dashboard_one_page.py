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

# Layout для дашборда с выровненными графиками
app.layout = html.Div([
    html.H1('Dashboard: Respiratory Risk Patterns', style={'textAlign': 'center'}),
    html.Div([
        html.Div([
            html.H3('Age Distribution', style={'marginBottom': '5px'}),
            html.Img(src=encoded_graphs['age_distribution'], style={'width': '85%', 'height': '200px', 'marginBottom': '10px'}),

            html.H3('Gender Distribution', style={'marginBottom': '5px'}),
            html.Img(src=encoded_graphs['gender_distribution'], style={'width': '85%', 'height': '200px', 'marginBottom': '10px'}),

            html.H3('Smoking Distribution', style={'marginBottom': '5px'}),
            html.Img(src=encoded_graphs['smoking_distribution'], style={'width': '85%', 'height': '200px', 'marginBottom': '10px'})
        ], style={'flex': '1', 'textAlign': 'center', 'padding': '10px'}),

        html.Div([
            html.H3('Alcohol Consumption', style={'marginBottom': '5px'}),
            html.Img(src=encoded_graphs['alcohol_distribution'], style={'width': '85%', 'height': '200px', 'marginBottom': '10px'}),

            html.H3('Diabetes Distribution', style={'marginBottom': '5px'}),
            html.Img(src=encoded_graphs['diabetes_distribution'], style={'width': '85%', 'height': '200px', 'marginBottom': '10px'}),

            html.H3('Boxplots', style={'marginBottom': '5px'}),
            html.Img(src=encoded_graphs['boxplot'], style={'width': '85%', 'height': '200px', 'marginBottom': '10px'})
        ], style={'flex': '1', 'textAlign': 'center', 'padding': '10px'}),

        html.Div([
            html.H3('Correlation Heatmap', style={'marginBottom': '5px'}),
            html.Img(src=encoded_graphs['correlation_heatmap'], style={'width': '85%', 'height': '200px', 'marginBottom': '10px'}),

            html.H3('ROC Curve', style={'marginBottom': '5px'}),
            html.Img(src=encoded_graphs['roc_curve'], style={'width': '85%', 'height': '200px', 'marginBottom': '10px'}),

            html.H3('Feature Importance', style={'marginBottom': '5px'}),
            html.Img(src=encoded_graphs['feature_importance'], style={'width': '85%', 'height': '200px', 'marginBottom': '10px'})
        ], style={'flex': '1', 'textAlign': 'center', 'padding': '10px'})
    ], style={'display': 'flex', 'flexWrap': 'wrap'})
])

# Запуск дашборда
if __name__ == '__main__':
    app.run_server(debug=True)
