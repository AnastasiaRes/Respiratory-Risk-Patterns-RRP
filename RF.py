import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve, auc
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

# Удаление строк с пропусками
combined_dataset = combined_dataset.dropna()

# Разделение на признаки и целевую переменную
X = combined_dataset[['gender', 'age', 'smoking', 'Diabetes', 'chronic_disease', 'alcohol']]
y = combined_dataset['pulmonary_diseases']

# Разделение на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Создание и обучение модели случайного леса
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Предсказание на тестовой выборке
y_pred = rf_model.predict(X_test)
y_pred_proba = rf_model.predict_proba(X_test)

# Расчет точности
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# ROC AUC Score
if len(y_test.unique()) > 2:
    roc_auc = roc_auc_score(y_test, y_pred_proba, multi_class='ovr')
    print("ROC AUC Score (multiclass):", roc_auc)
else:
    roc_auc = roc_auc_score(y_test, y_pred_proba[:, 1])
    print("ROC AUC Score:", roc_auc)

# Построение ROC-кривой
plt.figure(figsize=(10, 8))

if len(y_test.unique()) > 2:
    # Для мультиклассовой задачи
    for i, class_label in enumerate(rf_model.classes_):
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba[:, i], pos_label=class_label)
        plt.plot(fpr, tpr, label=f'Class {class_label} (AUC = {auc(fpr, tpr):.2f})')
else:
    # Для бинарной задачи
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba[:, 1])
    plt.plot(fpr, tpr, label=f'Binary Class (AUC = {roc_auc:.2f})')

plt.plot([0, 1], [0, 1], 'k--', label='Random Guessing')
plt.xlabel('False Positive Rate', fontsize=14)
plt.ylabel('True Positive Rate', fontsize=14)
plt.title('ROC Curve for Pulmonary Disease Prediction', fontsize=16)
plt.legend(loc='lower right', fontsize=12)
plt.grid(alpha=0.3)

# Сохранение ROC-кривой
roc_curve_path = os.path.join(results_dir, 'roc_curve_pulmonary.png')
plt.savefig(roc_curve_path)
plt.close()
print(f"ROC-кривая сохранена в файл: {roc_curve_path}")

print("Все результаты успешно сохранены.")

plt.style.use('Solarize_Light2')

# Анализ важности признаков
importances = rf_model.feature_importances_
feature_names = X.columns
feature_importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

# Визуализация важности признаков
plt.figure(figsize=(10, 6))
sns.barplot(data=feature_importance_df, x='Importance', y='Feature', palette='viridis')
plt.title('Важность признаков для предсказания легочных заболеваний', fontsize=16)
plt.xlabel('Importance', fontsize=14)
plt.ylabel('Feature', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()
