# Projeto Python

Bem-vindo ao projeto Python básico!

## Estrutura do Projeto

```
.
├── src/                    # Código fonte principal
├── tests/                  # Testes unitários
├── docs/                   # Documentação
├── requirements.txt        # Dependências do projeto
├── .gitignore             # Arquivos a ignorar no git
└── README.md              # Este arquivo
```

## Instalação

1. Crie um ambiente virtual:
```bash
python -m venv venv
```

2. Ative o ambiente virtual:
- **Windows**: `venv\Scripts\activate`
- **Linux/macOS**: `source venv/bin/activate`

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

Para executar a aplicação:
```bash
python src/main.py
```

## Testes

Para executar os testes:
```bash
pytest tests/
```

## Desenvolvimento

- Mantenha o código em `src/`
- Escreva testes em `tests/`
- Documente em `docs/`
