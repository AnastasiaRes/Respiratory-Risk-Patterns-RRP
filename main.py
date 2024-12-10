import pandas as pd
import os

# Получение текущего пути к скрипту
current_dir = os.path.dirname(os.path.abspath(__file__))

# Путь к папке с данными
data_dir = os.path.join(current_dir, 'datasets')

# Путь для копии папки
copied_data_dir = os.path.join(current_dir, 'datasets_copy')


# Список колонок для объединения
columns_to_merge = ['gender', 'age', 'smoking', 'Diabetes', 'chronic_disease', 'alcohol', 'pulmonary_diseases']

# Загрузка всех файлов
lung_cancer_path = os.path.join(copied_data_dir, 'survey lung cancer_copy.csv')
copd_path = os.path.join(copied_data_dir, 'COPD_copy.csv')
brfss_path = os.path.join(copied_data_dir, 'brfss2020_copy.csv')

# Загружаем датасеты
lung_cancer = pd.read_csv(lung_cancer_path)
copd = pd.read_csv(copd_path)
brfss = pd.read_csv(brfss_path)

# Оставляем только необходимые колонки (игнорируя отсутствующие)
lung_cancer_filtered = lung_cancer[[col for col in columns_to_merge if col in lung_cancer.columns]]
copd_filtered = copd[[col for col in columns_to_merge if col in copd.columns]]
brfss_filtered = brfss[[col for col in columns_to_merge if col in brfss.columns]]

# Объединение датасетов
combined_dataset = pd.concat([lung_cancer_filtered, copd_filtered, brfss_filtered], ignore_index=True)

# Сохранение итогового датасета
output_path = os.path.join(copied_data_dir, 'combined_dataset.csv')
combined_dataset.to_csv(output_path, index=False)

print(f"Общий датасет сохранен в '{output_path}'.")
print("Размер объединенного датасета:", combined_dataset.shape)


