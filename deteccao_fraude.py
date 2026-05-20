# ============================================================
# PROJETO: DETECÇÃO DE ANOMALIAS EM TRANSAÇÕES (VERSÃO FINAL)
# ============================================================

# ============================================================
# 1. INSTALAÇÃO E IMPORTAÇÃO DAS BIBLIOTECAS
# ============================================================
# Instalando pacotes necessários silenciosamente
import subprocess
import sys

def install_packages():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "xgboost", "shap", "joblib"])

install_packages()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib  # Biblioteca essencial para salvar/exportar o modelo

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from xgboost import XGBClassifier, plot_importance
import shap

# ============================================================
# 2. CARREGAMENTO DOS DADOS
# ============================================================
url = "https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"

print("Carregando base de dados...")
df = pd.read_csv(url)
print("Dataset carregado com sucesso!")

# ============================================================
# 3. FEATURE ENGINEERING
# ============================================================
# Normalizando apenas a coluna Amount, pois as outras (V1-V28) já estão normalizadas
scaler = StandardScaler()
df["Amount_scaled"] = scaler.fit_transform(df["Amount"].values.reshape(-1, 1))

# Removendo as colunas originais que não usaremos no modelo
df = df.drop(["Time", "Amount"], axis=1)

# ============================================================
# 4. SEPARAÇÃO DE VARIÁVEIS E DIVISÃO TREINO/TESTE
# ============================================================
X = df.drop("Class", axis=1)
y = df["Class"]

# O parâmetro stratify garante que a mesma proporção de fraudes exista no treino e no teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.3, random_state=42
)

print(f"\nTamanho treino: {X_train.shape}")
print(f"Tamanho teste: {X_test.shape}")

# ============================================================
# 5. TREINAMENTO DO MODELO AVANÇADO (XGBOOST)
# ============================================================
# Em vez de criar dados sintéticos (SMOTE), usamos a matemática a nosso favor
# Calculamos a proporção exata entre transações normais e fraudes para o peso
peso_fraude = len(y_train[y_train == 0]) / len(y_train[y_train == 1])

# Instanciando o modelo com os melhores hiperparâmetros (evitando overfitting)
xgb_model = XGBClassifier(
    n_estimators=100,
    max_depth=3,  # Árvores rasas para focar nos padrões mais fortes
    learning_rate=0.1,
    scale_pos_weight=peso_fraude,  # Penaliza fortemente se errar uma fraude
    random_state=42,
    n_jobs=-1  # Usa todos os processadores disponíveis
)

print("\nTreinando o modelo XGBoost (isso pode levar alguns segundos)...")
xgb_model.fit(X_train, y_train)
print("Modelo treinado com sucesso!")

# ============================================================
# 6. AVALIAÇÃO DO MODELO
# ============================================================
y_pred = xgb_model.predict(X_test)

print("\n" + "="*50)
print("RELATÓRIO DE CLASSIFICAÇÃO (XGBOOST)")
print("="*50)
print(classification_report(y_test, y_pred))

# Matriz de Confusão
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title("Matriz de Confusão - XGBoost")
plt.xlabel("Previsto")
plt.ylabel("Real")
plt.savefig('confusion_matrix.png')
plt.show()

# ============================================================
# 7. IMPORTÂNCIA DAS VARIÁVEIS E EXPLICABILIDADE (SHAP)
# ============================================================
print("\nGerando Gráfico de Importância de Variáveis...")
plt.rcParams["figure.figsize"] = (10, 6)
plot_importance(xgb_model, max_num_features=10, importance_type='weight', 
                title='Top 10 Variáveis mais Importantes - XGBoost')
plt.savefig('feature_importance.png')
plt.show()

print("\nGerando análise SHAP para explicabilidade de negócios...")
shap.initjs()
explainer = shap.TreeExplainer(xgb_model)

# Usamos uma amostra de 1000 transações do teste para o SHAP processar rapidamente
X_test_sample = X_test.sample(1000, random_state=42)
shap_values = explainer.shap_values(X_test_sample)

shap.summary_plot(shap_values, X_test_sample)
plt.savefig('shap_summary.png')
plt.show()

# ============================================================
# 8. EXPORTAÇÃO DO MODELO (DEPLOY)
# ============================================================
# Salvando o "cérebro" treinado e o normalizador em arquivos físicos
joblib.dump(xgb_model, 'modelo_xgboost_fraude.pkl')
joblib.dump(scaler, 'scaler_amount.pkl')

print("\n" + "="*50)
print("DEPLOY PREPARADO!")
print("="*50)
print("Os arquivos 'modelo_xgboost_fraude.pkl' e 'scaler_amount.pkl' foram salvos.")
print("Eles estão prontos para serem integrados via API em sistemas de gestão, apps")
print("financeiros ou conectados a rotinas de atualização de planilhas e dashboards.")
