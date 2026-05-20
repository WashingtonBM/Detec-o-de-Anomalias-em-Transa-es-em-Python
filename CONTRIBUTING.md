# 🤝 Guia de Contribuição

Primeiro, muito obrigado por considerar contribuir para este projeto! É pessoas como você que tornam este projeto uma ótima ferramenta.

## 📋 Código de Conduta

Este projeto e todos os participantes estão sujeitos ao nosso [Código de Conduta](CODE_OF_CONDUCT.md). Ao participar, você concorda em respeitar essas diretrizes.

## Como Contribuir

### 🐛 Reportando Bugs

Antes de criar um relatório de bug, faça uma pesquisa rápida nas issues existentes, pois o problema pode já ter sido relatado.

**Como enviar um bom relatório de bug:**

- Use um **título claro e descritivo**
- Forneça uma **descrição passo-a-passo** para reproduzir o problema
- Forneça **exemplos específicos** para demonstrar os passos
- Descreva o **comportamento observado** e qual era o **comportamento esperado**
- Inclua **screenshots** ou **outputs de erro** se possível
- Mencione sua **versão do Python, SO e versões das bibliotecas**

### 💡 Sugerindo Enhancements

**Como enviar uma boa sugestão de melhoria:**

- Use um **título claro e descritivo**
- Forneça uma **descrição clara** do enhancement proposto
- Explique **por que** isso seria útil (casos de uso)
- Liste **exemplos de como outras ferramentas** resolvem este problema

### 🔧 Pull Requests

- Preencha o **template de PR** completamente
- Siga o **estilo de código Python** (PEP 8)
- Inclua **testes** quando apropriado
- Atualize a **documentação** se necessário
- Termine todos os arquivos com uma **newline**

## 📝 Processo de Desenvolvimento

1. **Fork o repositório** e clone localmente:
   ```bash
   git clone https://github.com/seu-usuario/Detec-o-de-Anomalias-em-Transa-es-em-Python.git
   cd Detec-o-de-Anomalias-em-Transa-es-em-Python
   ```

2. **Crie uma virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # dependências de desenvolvimento
   ```

4. **Crie uma branch para sua feature**:
   ```bash
   git checkout -b feature/seu-feature-name
   ```

5. **Faça suas mudanças e commit**:
   ```bash
   git commit -am "Adiciona novo feature XYZ"
   ```

6. **Push para sua branch**:
   ```bash
   git push origin feature/seu-feature-name
   ```

7. **Abra um Pull Request** no GitHub

## ✅ Checklist para Pull Request

Antes de enviar seu PR, certifique-se de:

- [ ] Sua branch está atualizada com `main`
- [ ] Você testou seu código localmente
- [ ] Seu código segue o PEP 8
- [ ] Você atualizou a documentação
- [ ] Você não quebrou nenhum teste existente
- [ ] Você adicionou testes para novas funcionalidades

## 📖 Padrões de Código

### Python (PEP 8)

```python
# ✓ Bom
def calcular_risco_fraude(valor, historial):
    """Calcula o risco de fraude baseado no histórico."""
    if valor > 1000:
        return "alto"
    return "baixo"


# ✗ Ruim
def calc(v, h):
    if v > 1000:
        return "alto"
    return "baixo"
```

### Docstrings

```python
def predict_fraud(transaction_data):
    """
    Prediz se uma transação é fraudulenta.
    
    Args:
        transaction_data (dict): Dados da transação com features normalizadas
        
    Returns:
        dict: Contém 'prediction' (bool) e 'confidence' (float)
        
    Raises:
        ValueError: Se transaction_data for inválido
        
    Example:
        >>> result = predict_fraud({'V1': 1.0, 'V2': -0.5})
        >>> print(result['prediction'])
        False
    """
    pass
```

## 🔄 Processo de Review

1. Pelo menos **um maintainer** irá revisar seu PR
2. Mudanças podem ser solicitadas
3. Uma vez aprovado, seu PR será **merged**
4. Você receberá crédito no [CHANGELOG](CHANGELOG.md)

## 🏆 Reconhecimento

Contribuidores são reconhecidos no:
- Arquivo [CONTRIBUTORS.md](CONTRIBUTORS.md)
- README.md (para grandes contribuições)
- Releases notes

## 📚 Recursos Adicionais

- [Documentação Python](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

## 💬 Precisa de Ajuda?

- 📧 Email: seu-email@exemplo.com
- 💬 Discord: [Link para servidor]
- 🐛 Issues: [Abra uma issue](https://github.com/WashingtonBM/Detec-o-de-Anomalias-em-Transa-es-em-Python/issues)

---

**Obrigado por contribuir! 🎉**
