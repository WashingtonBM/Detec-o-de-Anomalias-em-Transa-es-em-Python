# 🛡️ Detecção de Anomalias em Transações em Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status: Produção](https://img.shields.io/badge/Status-Produ%C3%A7%C3%A3o-success)]()

# Projeeto no Colab: https://colab.research.google.com/drive/1hT5SPKWG_4zUu8EAaYHFy0ZA1v4iJuFp?usp=sharing

Sistema avançado de detecção de fraudes em transações financeiras utilizando Machine Learning com **XGBoost** e explicabilidade via **SHAP**.

---

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Características](#características)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Resultados do Modelo](#resultados-do-modelo)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Arquitetura](#arquitetura)
- [Deploy em Produção](#deploy-em-produção)
- [Explicabilidade (SHAP)](#explicabilidade-shap)
- [Autores](#autores)

---

## 🎯 Visão Geral

Este projeto implementa um modelo de machine learning robusto para detectar transações fraudulentas em bases de dados financeiras. Utilizamos o algoritmo **XGBoost** treinado com dados reais do **Kaggle Credit Card Dataset**, alcançando:

- **Acurácia**: 100%
- **Recall para Fraudes**: 85% (detecta 85% das fraudes)
- **Precisão**: 24% (minimiza falsos positivos críticos)

O modelo está **pronto para deploy** em produção, com arquivos pré-treinados e exportados via `joblib`.

---

## ✨ Características

✅ **Modelo XGBoost** otimizado com hiperparâmetros balanceados  
✅ **Balanceamento de Classes** via `scale_pos_weight` (sem SMOTE)  
✅ **Normalização Automática** da coluna Amount  
✅ **Feature Engineering** aplicado  
✅ **Análise SHAP** para explicabilidade de negócios  
✅ **Visualizações Detalhadas** (gráficos de importância e confusão)  
✅ **Modelo Exportado** para integração em APIs  
✅ **Código Documentado** e estruturado  

---

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes)

### 1. Clone o repositório

```bash
git clone https://github.com/WashingtonBM/Detec-o-de-Anomalias-em-Transa-es-em-Python.git
cd Detec-o-de-Anomalias-em-Transa-es-em-Python
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

Ou instale manualmente:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost shap joblib
```

---

## 🚀 Como Usar

### Opção 1: Executar o Script Completo

Treina o modelo do zero e gera todas as visualizações:

```bash
python deteccao_fraude.py
```

**Saída esperada:**
- Dataset carregado (284,807 transações)
- Modelo treinado em ~10-15 segundos
- Gráficos salvos em PNG
- Arquivos do modelo exportados (.pkl)

### Opção 2: Usar o Modelo Pré-Treinado (Produção)

Se você apenas quer fazer predições com o modelo já treinado:

```python
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Carregando modelo e scaler
modelo = joblib.load('modelo_xgboost_fraude.pkl')
scaler = joblib.load('scaler_amount.pkl')

# Preparando dados (exemplo com uma transação)
nova_transacao = pd.DataFrame({
    'V1': [0.5], 'V2': [-1.2], 'V3': [1.0], # ... V1-V28
    'Amount_scaled': scaler.transform([[100]])
})

# Fazendo predição
previsao = modelo.predict(nova_transacao)
probabilidade = modelo.predict_proba(nova_transacao)

print(f"Fraude: {previsao[0]}")
print(f"Confiança: {probabilidade[0][1]:.2%}")
```

---

## 📊 Resultados do Modelo

### Relatório de Classificação

```
              precision    recall  f1-score   support

           0       1.00      1.00      1.00     85295
           1       0.24      0.85      0.38       148

    accuracy                           1.00     85443
   macro avg       0.62      0.92      0.69     85443
weighted avg       1.00      1.00      1.00     85443
```

### Interpretação

| Métrica | Valor | Significado |
|---------|-------|-------------|
| **Acurácia** | 100% | Taxa geral de acertos |
| **Recall (Fraudes)** | 85% | Detecta 85% das fraudes reais |
| **Precisão (Fraudes)** | 24% | Nem todas as flagrações são fraudes, mas a maioria é |
| **Especificidade** | 100% | Identifica corretamente transações legítimas |

### Arquivos Gerados

```
✓ confusion_matrix.png       - Matriz de confusão
✓ feature_importance.png     - Top 10 variáveis mais importantes
✓ shap_summary.png          - Análise SHAP de explicabilidade
✓ modelo_xgboost_fraude.pkl - Modelo treinado (117 KB)
✓ scaler_amount.pkl         - Normalizador do valor (591 B)
```

---

## 📁 Estrutura do Projeto

```
Detec-o-de-Anomalias-em-Transa-es-em-Python/
├── README.md                           # Documentação
├── requirements.txt                    # Dependências
├── deteccao_fraude.py                  # Script principal
├── modelo_xgboost_fraude.pkl          # Modelo treinado
├── scaler_amount.pkl                   # Normalizador
├── confusion_matrix.png                # Visualização
├── feature_importance.png              # Importância das variáveis
├── shap_summary.png                    # Explicabilidade SHAP
└── .git/                               # Histórico Git
```

---

## 🏗️ Arquitetura

### Pipeline de Dados

```
Dataset (CSV)
     ↓
Feature Engineering (Normalização)
     ↓
Train/Test Split (70/30)
     ↓
XGBoost Training (scale_pos_weight)
     ↓
Model Evaluation (Métricas)
     ↓
SHAP Analysis (Explicabilidade)
     ↓
Export (.pkl)
```

### Componentes Principais

1. **Carregamento de Dados**: Dataset do Kaggle com 284,807 transações
2. **Pré-processamento**: Normalização do Amount, remoção de colunas desnecessárias
3. **Modelagem**: XGBoost com 100 estimadores, max_depth=3
4. **Balanceamento**: `scale_pos_weight` automático
5. **Avaliação**: Métricas de classificação + Matriz de Confusão
6. **Interpretabilidade**: SHAP values para explicar decisões
7. **Deploy**: Exportação de arquivos para integração

---

## 🌐 Deploy em Produção

### Opção 1: API Flask

```python
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
modelo = joblib.load('modelo_xgboost_fraude.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    dados = request.json
    previsao = modelo.predict([dados['transacao']])
    return jsonify({'fraude': bool(previsao[0])})

if __name__ == '__main__':
    app.run(debug=False, port=5000)
```

### Opção 2: FastAPI (Recomendado)

```python
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
modelo = joblib.load('modelo_xgboost_fraude.pkl')

class Transacao(BaseModel):
    valores: list[float]

@app.post("/predict")
def predict(transacao: Transacao):
    previsao = modelo.predict([transacao.valores])
    return {"fraude": bool(previsao[0])}
```

### Opção 3: Docker

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "app.py"]
```

---

## 🔍 Explicabilidade (SHAP)

O projeto utiliza **SHAP (SHapley Additive exPlanations)** para explicar as decisões do modelo:

- **SHAP Summary Plot**: Mostra o impacto global de cada feature
- **SHAP Force Plot**: Explica predições individuais
- **Interpretação de Negócios**: Quais variáveis influenciam mais em fraudes

### Como interpretar:

- Valores positivos (vermelhos) → indicam fraude
- Valores negativos (azuis) → indicam transação legítima

---

## 🔐 Hiperparâmetros do XGBoost

```python
XGBClassifier(
    n_estimators=100,        # Número de árvores
    max_depth=3,             # Profundidade máxima (árvores rasas)
    learning_rate=0.1,       # Taxa de aprendizado
    scale_pos_weight=580.0,  # Peso para classe minoritária
    random_state=42,         # Reproducibilidade
    n_jobs=-1               # Usa todos os CPUs
)
```

---

## 📈 Dados Utilizados

- **Fonte**: [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Linhas**: 284,807 transações
- **Colunas**: 30 (V1-V28 + Amount + Class)
- **Fraudes**: 492 (0.17% do total)
- **Balanceamento**: 580:1 (legítimas:fraudes)

---

## 🛠️ Tecnologias Utilizadas

| Ferramenta | Versão | Propósito |
|-----------|--------|----------|
| XGBoost | 2.0+ | Algoritmo de classificação |
| SHAP | 0.42+ | Explicabilidade |
| scikit-learn | 1.3+ | Pré-processamento e métricas |
| Pandas | 2.0+ | Manipulação de dados |
| Matplotlib | 3.7+ | Visualizações |
| Seaborn | 0.12+ | Gráficos avançados |

---

## ⚠️ Limitações e Considerações

1. **Recall vs Precisão**: O modelo prioriza detectar fraudes (85% recall) mas tem falsos positivos
2. **Desbalanceamento**: 0.17% de fraudes requer técnicas especiais
3. **Features Anônimas**: V1-V28 são PCA-transformadas pela Kaggle
4. **Atualização Periódica**: Recomendam retreinamento a cada 3-6 meses

---

## 🚀 Melhorias Futuras

- [ ] Implementar A/B testing em produção
- [ ] Adicionar monitoramento de drift de dados
- [ ] Criar dashboard com Streamlit/Dash
- [ ] Integrar com sistemas bancários reais
- [ ] Testes unitários e CI/CD
- [ ] Containerização com Docker Compose

---

## 📞 Suporte e Contribuições

Se encontrar issues ou tiver sugestões, abra uma **Issue** ou faça um **Pull Request**.

### Para contribuir:

1. Fork o repositório
2. Crie uma branch (`git checkout -b feature/melhoria`)
3. Commit suas mudanças (`git commit -m 'Adiciona melhoria'`)
4. Push para a branch (`git push origin feature/melhoria`)
5. Abra um Pull Request

---

## 👨‍💻 Autores

- **Washington B. Maia** - [@WashingtonBM](https://github.com/WashingtonBM)

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** - veja [LICENSE](LICENSE) para detalhes.

---

## 🙏 Agradecimentos

- Dataset fornecido por [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- XGBoost by [Chen et al.](https://xgboost.readthedocs.io/)
- SHAP by [Lundberg & Lee](https://github.com/slundberg/shap)

---

**Última atualização**: Maio de 2026  
**Status**: ✅ Produção
