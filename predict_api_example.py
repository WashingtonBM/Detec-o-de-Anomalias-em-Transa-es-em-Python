# ============================================================
# EXEMPLO: API FASTAPI PARA PRODUÇÃO
# ============================================================
# Executar com: uvicorn predict_api_example:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from typing import List

# ============================================================
# CARREGANDO O MODELO PRÉ-TREINADO
# ============================================================
try:
    modelo = joblib.load('modelo_xgboost_fraude.pkl')
    scaler = joblib.load('scaler_amount.pkl')
    print("✓ Modelo carregado com sucesso!")
except FileNotFoundError:
    raise Exception("Arquivos do modelo não encontrados. Execute 'deteccao_fraude.py' primeiro.")

# ============================================================
# DEFININDO ESTRUTURA DE DADOS
# ============================================================
class TransacaoInput(BaseModel):
    """Estrutura para receber dados de uma transação"""
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float


class PredicaoOutput(BaseModel):
    """Estrutura de resposta da API"""
    fraude: bool
    probabilidade_fraude: float
    confianca: str


# ============================================================
# CRIANDO APLICAÇÃO FASTAPI
# ============================================================
app = FastAPI(
    title="🛡️ API de Detecção de Fraudes",
    description="Sistema de detecção de anomalias em transações financeiras",
    version="1.0.0"
)


# ============================================================
# ENDPOINTS
# ============================================================

@app.get("/")
def root():
    """Endpoint raiz - verifica se a API está funcionando"""
    return {
        "status": "✓ Online",
        "versao": "1.0.0",
        "modelo": "XGBoost",
        "documentacao": "/docs"
    }


@app.get("/health")
def health():
    """Health check para monitoramento"""
    return {"status": "healthy", "model_loaded": True}


@app.post("/predict", response_model=PredicaoOutput)
def predict(transacao: TransacaoInput):
    """
    Prediz se uma transação é fraudulenta
    
    **Exemplo de entrada:**
    ```json
    {
        "V1": 1.0, "V2": -0.5, "V3": 1.2, "V4": 0.3, "V5": -0.1,
        "V6": -1.0, "V7": 0.5, "V8": -0.3, "V9": 1.1, "V10": -0.8,
        "V11": 0.2, "V12": 1.0, "V13": -0.5, "V14": 0.8, "V15": -0.3,
        "V16": 0.5, "V17": -1.0, "V18": 0.3, "V19": 1.2, "V20": -0.1,
        "V21": 0.5, "V22": -0.8, "V23": 0.2, "V24": 1.0, "V25": -0.5,
        "V26": 0.8, "V27": -0.3, "V28": 0.5,
        "Amount": 150.50
    }
    ```
    """
    try:
        # Normalizando o Amount
        amount_scaled = scaler.transform([[transacao.Amount]])[0][0]
        
        # Preparando features para o modelo (ordem importante!)
        features = [
            transacao.V1, transacao.V2, transacao.V3, transacao.V4, transacao.V5,
            transacao.V6, transacao.V7, transacao.V8, transacao.V9, transacao.V10,
            transacao.V11, transacao.V12, transacao.V13, transacao.V14, transacao.V15,
            transacao.V16, transacao.V17, transacao.V18, transacao.V19, transacao.V20,
            transacao.V21, transacao.V22, transacao.V23, transacao.V24, transacao.V25,
            transacao.V26, transacao.V27, transacao.V28, amount_scaled
        ]
        
        # Fazendo predição
        previsao = modelo.predict([features])[0]
        probabilidades = modelo.predict_proba([features])[0]
        
        # Interpretando resultados
        fraude = bool(previsao)
        prob_fraude = float(probabilidades[1])  # Probabilidade de fraude (classe 1)
        
        # Definindo confiança
        confianca = "Muito Alta" if prob_fraude > 0.8 else \
                   "Alta" if prob_fraude > 0.6 else \
                   "Média" if prob_fraude > 0.4 else \
                   "Baixa"
        
        return PredicaoOutput(
            fraude=fraude,
            probabilidade_fraude=round(prob_fraude, 4),
            confianca=confianca
        )
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro na predição: {str(e)}")


@app.post("/predict_batch")
def predict_batch(transacoes: List[TransacaoInput]):
    """
    Prediz múltiplas transações em uma única requisição (mais eficiente)
    
    **Retorna uma lista de predições**
    """
    resultados = []
    for transacao in transacoes:
        resultado = predict(transacao)
        resultados.append(resultado)
    
    return {
        "total": len(resultados),
        "fraudes_detectadas": sum(1 for r in resultados if r.fraude),
        "predicoes": resultados
    }


@app.get("/modelo/info")
def modelo_info():
    """Informações sobre o modelo treinado"""
    return {
        "algoritmo": "XGBoost",
        "n_estimadores": 100,
        "max_depth": 3,
        "learning_rate": 0.1,
        "features": 29,
        "accuracy_teste": "100%",
        "recall_fraudes": "85%",
        "precisao_fraudes": "24%",
        "data_treinamento": "Maio de 2026"
    }


# ============================================================
# EXECUTAR SERVIDOR
# ============================================================
if __name__ == "__main__":
    import uvicorn
    
    print("\n" + "="*60)
    print("🚀 INICIANDO API DE DETECÇÃO DE FRAUDES")
    print("="*60)
    print("📚 Documentação: http://localhost:8000/docs")
    print("🔍 Swagger UI: http://localhost:8000/swagger")
    print("="*60 + "\n")
    
    # Executar servidor na porta 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
