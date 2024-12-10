import os
import shutil
import pandas as pd
import numpy as np

# Текущая директория скрипта
current_dir = os.path.dirname(os.path.abspath(__file__))

# Путь к папке с оригинальными данными
original_data_dir = os.path.join(current_dir, 'datasets')

# Путь для копии папки
copied_data_dir = os.path.join(current_dir, 'datasets_copy')

# Проверяем, существует ли уже копия папки
if not os.path.exists(copied_data_dir):
    shutil.copytree(original_data_dir, copied_data_dir)
    print(f"Папка 'datasets' успешно скопирована в 'datasets_copy'.")

    # Добавление слова 'copy' к файлам в копии
    for filename in os.listdir(copied_data_dir):
        old_file = os.path.join(copied_data_dir, filename)
        new_file = os.path.join(copied_data_dir, f"{os.path.splitext(filename)[0]}_copy{os.path.splitext(filename)[1]}")
        os.rename(old_file, new_file)
    print("Файлам в 'datasets_copy' добавлено слово 'copy'.")
else:
    print(f"Папка 'datasets_copy' уже существует.")

# Загрузка данных из копии
brfss = pd.read_csv(os.path.join(copied_data_dir, 'brfss2020_copy.csv'))
copd = pd.read_csv(os.path.join(copied_data_dir, 'COPD_copy.csv'))
lung_cancer = pd.read_csv(os.path.join(copied_data_dir, 'survey lung cancer_copy.csv'))


# Касательно пола
# Изменение значений в столбце GENDER в файле lung_cancer
if 'GENDER' in lung_cancer.columns:
    lung_cancer['GENDER'] = lung_cancer['GENDER'].replace({'M': 1, 'F': 0})
    print("Значения в столбце 'GENDER' успешно изменены (M → 1, F → 0).")

    # Сохранение измененного файла обратно
    lung_cancer.to_csv(os.path.join(copied_data_dir, 'survey lung cancer_copy.csv'), index=False)
    print("Изменения сохранены в 'survey lung cancer_copy.csv'.")
else:
    print("Столбец 'GENDER' не найден в файле 'survey lung cancer_copy.csv'.")


# Изменение значений в столбце _SEX в файле brfss2020_copy.csv
if '_SEX' in brfss.columns:
    brfss['_SEX'] = brfss['_SEX'].replace({2: 0})
    print("Значения в столбце '_SEX' успешно изменены (2 → 0).")

    # Сохранение измененного файла обратно
    brfss.to_csv(os.path.join(copied_data_dir, 'brfss2020_copy.csv'), index=False)
    print("Изменения сохранены в 'brfss2020_copy.csv'.")
else:
    print("Столбец '_SEX' не найден в файле 'brfss2020_copy.csv'.")


# Переименование колонок пола в файлах:

# Переименование столбцов в файле lung_cancer
if 'GENDER' in lung_cancer.columns:
    lung_cancer.rename(columns={'GENDER': 'gender'}, inplace=True)
    print("Столбец 'GENDER' переименован в 'gender' в файле 'survey lung cancer_copy.csv'.")

    # Сохранение изменений
    lung_cancer.to_csv(os.path.join(copied_data_dir, 'survey lung cancer_copy.csv'), index=False)
    print("Изменения сохранены в 'survey lung cancer_copy.csv'.")

# Переименование столбцов в файле brfss
if '_SEX' in brfss.columns:
    brfss.rename(columns={'_SEX': 'gender'}, inplace=True)
    print("Столбец '_SEX' переименован в 'gender' в файле 'brfss2020_copy.csv'.")

    # Сохранение изменений
    brfss.to_csv(os.path.join(copied_data_dir, 'brfss2020_copy.csv'), index=False)
    print("Изменения сохранены в 'brfss2020_copy.csv'.")

# Касательно возраста
# Переименование колонок возраста в файлах:

# Переименование столбцов в файле lung_cancer
if 'AGE' in lung_cancer.columns:
    lung_cancer.rename(columns={'AGE': 'age'}, inplace=True)
    print("Столбец 'AGE' переименован в 'age' в файле 'survey lung cancer_copy.csv'.")

    # Сохранение изменений
    lung_cancer.to_csv(os.path.join(copied_data_dir, 'survey lung cancer_copy.csv'), index=False)
    print("Изменения сохранены в 'survey lung cancer_copy.csv'.")

# Переименование столбцов в файле brfss
if '_AGE80' in brfss.columns:
    brfss.rename(columns={'_AGE80': 'age'}, inplace=True)
    print("Столбец '_AGE80' переименован в 'age' в файле 'brfss2020_copy.csv'.")

    # Сохранение изменений
    brfss.to_csv(os.path.join(copied_data_dir, 'brfss2020_copy.csv'), index=False)
    print("Изменения сохранены в 'brfss2020_copy.csv'.")

# Переименование столбцов в файле copd
if 'AGE' in copd.columns:
    copd.rename(columns={'AGE': 'age'}, inplace=True)
    print("Столбец 'AGE' переименован в 'age' в файле 'COPD_copy.csv'.")

    # Сохранение изменений
    copd.to_csv(os.path.join(copied_data_dir, 'COPD_copy.csv'), index=False)
    print("Изменения сохранены в 'COPD_copy.csv'.")


# Касательно курения:

# Переименование столбцов в файле lung_cancer
if 'SMOKING' in lung_cancer.columns:
    lung_cancer.rename(columns={'SMOKING': 'smoking'}, inplace=True)
    print("Столбец 'SMOKING' переименован в 'smoking' в файле 'survey lung cancer_copy.csv'.")

    # Сохранение изменений
    lung_cancer.to_csv(os.path.join(copied_data_dir, 'survey lung cancer_copy.csv'), index=False)
    print("Изменения сохранены в 'survey lung cancer_copy.csv'.")

# Переименование столбцов в файле brfss
if '_SMOKER3' in brfss.columns:
    brfss.rename(columns={'_SMOKER3': 'smoke_status'}, inplace=True)
    print("Столбец '_SMOKER3' переименован в 'smoke_status' в файле 'brfss2020_copy.csv'.")

    # Сохранение изменений
    brfss.to_csv(os.path.join(copied_data_dir, 'brfss2020_copy.csv'), index=False)
    print("Изменения сохранены в 'brfss2020_copy.csv'.")

# Создание новой колонки 'smoking' на основе 'smoke_status' в файле brfss
if 'smoke_status' in brfss.columns:
    brfss['smoking'] = brfss['smoke_status'].replace({1: 2, 4: 1, 9: np.nan}) # есть 1 - нет, 2 - да, 3 - бывший
    print("Новая колонка 'smoking' создана в файле 'brfss2020_copy.csv'.")

    # Сохранение изменений
    brfss.to_csv(os.path.join(copied_data_dir, 'brfss2020_copy.csv'), index=False)
    print("Изменения сохранены в 'brfss2020_copy.csv'.")
else:
    print("Колонка 'smoke_status' не найдена в файле 'brfss2020_copy.csv'.")


# Касательно диабета

# Создание новой колонки 'Diabetes' на основе 'DIABETE4' в файле brfss
if 'DIABETE4' in brfss.columns:
    # Преобразование значений в колонке 'DIABETE4'
    chg = {1: 1, 2: 1, 3: 0, 4: 1, 7: np.nan, 9: np.nan}
    brfss['Diabetes'] = brfss['DIABETE4'].replace(to_replace=chg)
    print("Новая колонка 'Diabetes' создана в файле 'brfss2020_copy.csv'.")

    # Сохранение изменений
    brfss.to_csv(os.path.join(copied_data_dir, 'brfss2020_copy.csv'), index=False)
    print("Изменения сохранены в 'brfss2020_copy.csv'.")
else:
    print("Колонка 'DIABETE4' не найдена в файле 'brfss2020_copy.csv'.")


# Проверяем, есть ли колонка 'diabetes' в каждом датасете
if 'Diabetes' not in lung_cancer.columns:
    lung_cancer['Diabetes'] = np.nan  # Добавляем колонку с пропусками
    print("Добавлена колонка 'Diabetes' с пропусками в датасет 'lung_cancer'.")

# Сохранение изменений
lung_cancer.to_csv(os.path.join(copied_data_dir, 'survey lung cancer_copy.csv'), index=False)

# Касательно алкоголя
# Касательно алкоголя

# Проверяем наличие колонки 'DRNKANY5' в brfss
if 'DRNKANY5' in brfss.columns:
    # Преобразование значений в колонке 'DRNKANY5' для создания колонки 'alcohol'
    chg = {1: 2, 2: 1, 7: np.nan, 9: np.nan}
    brfss['alcohol'] = brfss['DRNKANY5'].replace(to_replace=chg)
    print("Колонка 'alcohol' успешно создана в файле 'brfss2020_copy.csv'.")

    # Сохранение изменений
    brfss.to_csv(os.path.join(copied_data_dir, 'brfss2020_copy.csv'), index=False)
    print("Изменения сохранены в 'brfss2020_copy.csv'.")
else:
    print("Колонка 'DRNKANY5' не найдена в файле 'brfss2020_copy.csv'.")

# Проверяем наличие колонки 'ALCOHOL CONSUMING' в lung_cancer
if 'ALCOHOL CONSUMING' in lung_cancer.columns:
    # Преобразование значений в колонке для создания колонки 'alcohol'
    # 'YES' -> 1, 'NO' -> 0
    lung_cancer['alcohol'] = lung_cancer['ALCOHOL CONSUMING'].replace({'YES': 2, 'NO': 1})
    print("Колонка 'alcohol' успешно создана в файле 'survey lung cancer_copy.csv'.")

    # Сохранение изменений
    lung_cancer.to_csv(os.path.join(copied_data_dir, 'survey lung cancer_copy.csv'), index=False)
    print("Изменения сохранены в 'survey lung cancer_copy.csv'.")
else:
    print("Колонка 'ALCOHOL CONSUMING' не найдена в файле 'survey lung cancer_copy.csv'.")

# Проверяем, есть ли колонка 'alcohol' в файле copd
if 'alcohol' not in copd.columns:
    copd['alcohol'] = 3  # Добавляем колонку с фиксированным значением 3
    print("Добавлена колонка 'alcohol' со значением 3 в датасет 'copd'.")

    # Сохранение изменений
    copd.to_csv(os.path.join(copied_data_dir, 'COPD_copy.csv'), index=False)
    print("Изменения сохранены в 'COPD_copy.csv'.")



# Касательно хронических заболеваний
# Переименование столбцов в файле lung_cancer
if 'CHRONIC DISEASE' in lung_cancer.columns:
    lung_cancer.rename(columns={'CHRONIC DISEASE': 'chronic_disease'}, inplace=True)
    print("Столбец 'CHRONIC DISEASE' переименован в 'chronic_disease' в файле 'survey lung cancer_copy.csv'.")

    # Сохранение изменений
    lung_cancer.to_csv(os.path.join(copied_data_dir, 'survey lung cancer_copy.csv'), index=False)
    print("Изменения сохранены в 'survey lung cancer_copy.csv'.")

# Изменение значений в столбце chronic disease в файле lung_cancer
if 'chronic_disease' in lung_cancer.columns:
    lung_cancer['chronic_disease'] = lung_cancer['chronic_disease'].replace({2: 1, 1: 0})
    print("Значения в столбце 'chronic disease' успешно изменены (2 → 1, 1 → 0).")

    # Сохранение измененного файла обратно
    lung_cancer.to_csv(os.path.join(copied_data_dir, 'survey lung cancer_copy.csv'), index=False)
    print("Изменения сохранены в 'survey lung cancer_copy.csv'.")
else:
    print("Столбец 'chronic disease' не найден в файле 'survey lung cancer_copy.csv'.")


# Список колонок, связанных с хроническими заболеваниями
chronic_columns = ['copd', 'Diabetes', 'hypertension', 'AtrialFib', 'IHD']

# Проверяем, что все указанные колонки существуют в датасете
missing_columns = [col for col in chronic_columns if col not in copd.columns]
if missing_columns:
    print(f"Следующие колонки отсутствуют в датасете: {missing_columns}")
else:
    # Создание новой колонки 'chronic_disease'
    copd['chronic_disease'] = (copd[chronic_columns] == 1).any(axis=1).astype(int)
    print("Колонка 'chronic_disease' успешно создана.")

    # Сохранение изменений в файл
    copd.to_csv(os.path.join(copied_data_dir, 'COPD_copy.csv'), index=False)
    print("Изменения сохранены в 'COPD_copy.csv'.")

    # Проверка распределения значений в новой колонке
    print("Распределение значений в 'chronic_disease':")
    print(copd['chronic_disease'].value_counts())

# хронические для brfss
# Список колонок, связанных с хроническими заболеваниями
chronic_columns = [
    'CVDCRHD4', 'ASTHMA3', 'ASTHNOW', 'CHCSCNCR',
    'CHCOCNCR', 'CHCCOPD2', 'HAVARTH4', 'CHCKDNY2', 'Diabetes'
]

# Проверяем наличие всех колонок в датасете
missing_columns = [col for col in chronic_columns if col not in brfss.columns]
if missing_columns:
    print(f"Следующие колонки отсутствуют в датасете: {missing_columns}")
else:
    # Создание новой колонки 'chronic_disease'
    brfss['chronic_disease'] = (brfss[chronic_columns] == 1).any(axis=1).astype(int)
    print("Колонка 'chronic_disease' успешно создана.")

    # Сохранение изменений в файл
    brfss.to_csv(os.path.join(copied_data_dir, 'brfss2020_copy.csv'), index=False)
    print("Изменения сохранены в 'brfss2020_copy.csv'.")

    # Проверка распределения значений в новой колонке
    print("Распределение значений в 'chronic_disease':")
    print(brfss['chronic_disease'].value_counts())


# Новая колонка для всех pulmonary diseases

# Для файла lung_cancer.csv
if 'LUNG_CANCER' in lung_cancer.columns:
    lung_cancer['pulmonary_diseases'] = lung_cancer['LUNG_CANCER'].apply(lambda x: 1 if x == 'YES' else 0)
    print("Колонка 'pulmonary_diseases' добавлена в файле 'lung_cancer'.")
    lung_cancer.to_csv(os.path.join(copied_data_dir, 'survey lung cancer_copy.csv'), index=False)

# Для файла COPD.csv
if 'COPDSEVERITY' in copd.columns:
    copd['pulmonary_diseases'] = copd['COPDSEVERITY'].apply(lambda x: 2 if pd.notna(x) else 0)
    print("Колонка 'pulmonary_diseases' добавлена в файле 'COPD'.")
    copd.to_csv(os.path.join(copied_data_dir, 'COPD_copy.csv'), index=False)

# Для файла brfss2020_copy.csv
if 'CHCCOPD2' in brfss.columns and 'ASTHMA3' in brfss.columns:
    def assign_pulmonary(row):
        if row['CHCCOPD2'] == 1 and row['ASTHMA3'] == 1:
            return 4  # Астма + ХОБЛ
        elif row['CHCCOPD2'] == 1:
            return 2  # ХОБЛ
        elif row['ASTHMA3'] == 1:
            return 3  # Астма
        else:
            return 0  # Отсутствие заболевания

    brfss['pulmonary_diseases'] = brfss.apply(assign_pulmonary, axis=1)
    print("Колонка 'pulmonary_diseases' добавлена в файле 'brfss2020_copy.csv'.")
    brfss.to_csv(os.path.join(copied_data_dir, 'brfss2020_copy.csv'), index=False)




# Проверка и вывод уникальных значений для файла brfss
if 'alcohol' in brfss.columns:
    print("Уникальные значения в колонке 'alcohol' для файла 'brfss':")
    print(brfss['alcohol'].value_counts(dropna=False))
else:
    print("Колонка 'alcohol' отсутствует в файле 'brfss'.")

print("\n" + "-" * 50 + "\n")

# Проверка и вывод уникальных значений для файла COPD
if 'alcohol' in copd.columns:
    print("Уникальные значения в колонке 'alcohol' для файла 'COPD':")
    print(copd['alcohol'].value_counts(dropna=False))
else:
    print("Колонка 'alcohol' отсутствует в файле 'COPD'.")

print("\n" + "-" * 50 + "\n")

# Проверка и вывод уникальных значений для файла lung_cancer
if 'alcohol' in lung_cancer.columns:
    print("Уникальные значения в колонке 'alcohol' для файла 'lung_cancer':")
    print(lung_cancer['alcohol'].value_counts(dropna=False))
else:
    print("Колонка 'alcohol' отсутствует в файле 'lung_cancer'.")
