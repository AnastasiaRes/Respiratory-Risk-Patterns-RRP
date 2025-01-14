import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# Определение текущей директории скрипта
current_dir = os.path.dirname(os.path.abspath(__file__))

# Путь к файлу combined_dataset.csv
dataset_path = os.path.join(current_dir, 'datasets_copy', 'combined_dataset.csv')

# Создание папки для сохранения результатов
results_dir = os.path.join(current_dir, 'results')
os.makedirs(results_dir, exist_ok=True)
print("Создана папка 'results' для сохранения результатов.")

# Загрузка датасета
combined_dataset = pd.read_csv(dataset_path)

# Преобразование всех числовых колонок в целые значения
numeric_columns = combined_dataset.select_dtypes(include=['float64']).columns
combined_dataset[numeric_columns] = combined_dataset[numeric_columns].astype('Int64')

# Сохранение основной информации о датасете
with open(os.path.join(results_dir, 'dataset_info.txt'), 'w') as f:
    f.write("Информация о датасете до удаления пропусков:\n")
    combined_dataset.info(buf=f)
    f.write("\nКоличество пропущенных значений в каждой колонке до удаления пропусков:\n")
    f.write(f"{combined_dataset.isnull().sum()}\n")
print("Информация о датасете до удаления пропусков сохранена в 'dataset_info.txt'.")

# Удаление строк с пропусками
cleaned_dataset = combined_dataset.dropna()

# Сохранение информации о датасете после удаления пропусков
with open(os.path.join(results_dir, 'dataset_info.txt'), 'a') as f:
    f.write("\nИнформация о датасете после удаления пропусков:\n")
    cleaned_dataset.info(buf=f)
    f.write("\nКоличество пропущенных значений в каждой колонке после удаления пропусков:\n")
    f.write(f"{cleaned_dataset.isnull().sum()}\n")
print("Информация о датасете после удаления пропусков добавлена в 'dataset_info.txt'.")

# Сохранение очищенного датасета
output_path_cleaned = os.path.join(current_dir, 'datasets_copy', 'cleaned_dataset.csv')
cleaned_dataset.to_csv(output_path_cleaned, index=False)
print(f"\nОчищенный датасет сохранён в файл: {output_path_cleaned}")

# Расчет основных метрик
statistics_summary = cleaned_dataset.describe().T  # Транспонируем для удобства

# Добавление моды для каждой колонки
statistics_summary['mode'] = cleaned_dataset.mode().iloc[0]

# Добавление количества уникальных значений
statistics_summary['unique_values'] = cleaned_dataset.nunique()

# Добавление количества пропусков (для проверки)
statistics_summary['missing_values'] = round(combined_dataset.isnull().sum()/len(combined_dataset)*100, 2)

# Сохранение сводной таблицы
output_path_summary = os.path.join(results_dir, 'statistics_summary.csv')
statistics_summary.to_csv(output_path_summary)
print(f"\nСводная таблица сохранена в файл: {output_path_summary}")

# Вывод сводной таблицы
print("\nСводная таблица с основными метриками:")
print(statistics_summary)

# Распределение по колонкам
columns_to_analyze = ['gender', 'age', 'smoking', 'Diabetes', 'chronic_disease', 'alcohol', 'pulmonary_diseases']

# Визуализация распределения данных
plt.style.use('Solarize_Light2')  # Устанавливаем стиль графиков

for column in columns_to_analyze:
    if column in cleaned_dataset.columns and column != 'age':  # Исключаем 'age'
        plt.figure(figsize=(10, 6))
        ax = sns.countplot(
            data=cleaned_dataset,
            x=column,
            hue=column,  # Указываем ту же переменную, что и для x
            palette='viridis',
            legend=False
        )

        # Добавление значений над столбцами
        for bar in ax.patches:
            ax.annotate(
                format(int(bar.get_height()), ','),
                (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                ha='center', va='bottom', fontsize=10, color='black'
            )

        plt.title(f'Распределение значений в колонке "{column}"', fontsize=14)
        plt.xlabel(column, fontsize=12)
        plt.ylabel('Количество', fontsize=12)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)

        # Сохранение графика
        plt.savefig(os.path.join(results_dir, f'{column}_distribution.png'))
        plt.close()
        print(f"График распределения для '{column}' сохранен в 'results/{column}_distribution.png'.")

# Визуализация распределения для 'age'
plt.figure(figsize=(12, 6))
sns.histplot(cleaned_dataset['age'], bins=30, kde=True, color='blue')
plt.title("Распределение по возрасту", fontsize=16)
plt.xlabel("Age", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig(os.path.join(results_dir, 'age_distribution.png'))
plt.close()
print("График распределения для 'age' сохранен в 'results/age_distribution.png'.")

# Визуализация выбросов с использованием boxplot
continuous_columns = ['age']

fig, axes = plt.subplots(1, len(continuous_columns), figsize=(10, 6), sharey=False)

for i, column in enumerate(continuous_columns):
    sns.boxplot(data=cleaned_dataset, y=column, palette='viridis', ax=axes if len(continuous_columns) == 1 else axes[i])
    axes.set_title(f'{column}', fontsize=12)
    axes.set_ylabel('')  # Убираем общую ось Y, чтобы она не дублировалась
    axes.tick_params(axis='x', labelsize=10)
    axes.tick_params(axis='y', labelsize=10)

# Установка общей подписи для графика
plt.suptitle('Boxplots for Continuous Columns', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(os.path.join(results_dir, 'boxplots.png'))
plt.close()
print("Boxplot сохранен в 'results/boxplots.png'.")

# Корреляция между числовыми колонками
numeric_columns = cleaned_dataset.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = cleaned_dataset[numeric_columns].corr()

# Сохранение корреляционной матрицы
with open(os.path.join(results_dir, 'correlation_matrix.txt'), 'w') as f:
    f.write("Корреляция между числовыми колонками:\n")
    f.write(f"{correlation_matrix}\n")
print("Корреляционная матрица сохранена в 'results/correlation_matrix.txt'.")

# Визуализация корреляции
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, cbar_kws={"shrink": 0.8})
plt.title("Корреляция между числовыми колонками", fontsize=16)
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.savefig(os.path.join(results_dir, 'correlation_heatmap.png'))
plt.close()
print("График корреляции сохранен в 'results/correlation_heatmap.png'.")


# Барплот для курения и легочных заболеваний
plt.figure(figsize=(10, 6))
sns.barplot(
    data=cleaned_dataset,
    x='smoking',
    y='pulmonary_diseases',
    estimator=lambda x: sum(x) / len(x),  # Процентное соотношение легочных заболеваний
    ci=None,
    palette='viridis'
)
plt.title('Связь между курением и легочными заболеваниями', fontsize=16)
plt.xlabel('Smoking Status', fontsize=14)
plt.ylabel('Pulmonary Disease Rate', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig(os.path.join(results_dir, 'smoking_vs_pulmonary_diseases.png'))
plt.close()
print("График 'smoking vs pulmonary_diseases' сохранен в results.")

# Барплот для алкоголя и легочных заболеваний
plt.figure(figsize=(10, 6))
sns.barplot(
    data=cleaned_dataset,
    x='alcohol',
    y='pulmonary_diseases',
    estimator=lambda x: sum(x) / len(x),
    ci=None,
    palette='viridis'
)
plt.title('Связь между употреблением алкоголя и легочными заболеваниями', fontsize=16)
plt.xlabel('Alcohol Consumption', fontsize=14)
plt.ylabel('Pulmonary Disease Rate', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig(os.path.join(results_dir, 'alcohol_vs_pulmonary_diseases.png'))
plt.close()
print("График 'alcohol vs pulmonary_diseases' сохранен в results.")

# Барплот для пола и легочных заболеваний
plt.figure(figsize=(10, 6))
sns.barplot(
    data=cleaned_dataset,
    x='gender',
    y='pulmonary_diseases',
    estimator=lambda x: sum(x) / len(x),
    ci=None,
    palette='viridis'
)
plt.title('Связь между полом и легочными заболеваниями', fontsize=16)
plt.xlabel('Gender (1 = Female, 0 = Male)', fontsize=14)
plt.ylabel('Pulmonary Disease Rate', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig(os.path.join(results_dir, 'gender_vs_pulmonary_diseases.png'))
plt.close()
print("График 'gender vs pulmonary_diseases' сохранен в results.")

# Барплот для диабета и легочных заболеваний
plt.figure(figsize=(10, 6))
sns.barplot(
    data=cleaned_dataset,
    x='Diabetes',
    y='pulmonary_diseases',
    estimator=lambda x: sum(x) / len(x),
    ci=None,
    palette='viridis'
)
plt.title('Связь между диабетом и легочными заболеваниями', fontsize=16)
plt.xlabel('Diabetes (1 = yes, 0 = no)', fontsize=14)
plt.ylabel('Pulmonary Disease Rate', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig(os.path.join(results_dir, 'diabetes_vs_pulmonary_diseases.png'))
plt.close()
print("График 'diabetes vs pulmonary_diseases' сохранен в results.")

print('топ неожиданных поворотов')
