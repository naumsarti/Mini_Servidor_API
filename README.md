# Mini Projeto 3 - Mini Servidor de API

Projeto desenvolvido para a Fatec Rio Claro que demonstra a implementação de um **servidor de APIs** utilizando FastAPI e um **cliente** que consome dados dessa API através da biblioteca requests.

O objetivo é entender como diferentes sistemas se comunicam de forma padronizada através de APIs (Application Programming Interfaces), permitindo a integração de serviços de forma ágil e escalável.

### Tecnologias Utilizadas

- **Python 3.x**
- **FastAPI** - Framework web moderno e rápido para criar APIs
- **Uvicorn** - Servidor ASGI para executar a aplicação FastAPI
- **Requests** - Biblioteca para fazer requisições HTTP

---

## Estrutura do Projeto

```
Mini_Servidor_API/
│
├── README.md                    # Este arquivo
├── requirements.txt             # Dependências do projeto
│
├── server/                      # Servidor da API (backend)
│   └── app/
│       ├── __init__.py
│       └── main.py             # Servidor FastAPI
│
└── client/                      # Cliente que consome a API
    └── main.py                  # Script cliente 
```

---

## Como Executar

### Pré-requisitos

- Python 3.7 ou superior instalado

---

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/naumsarti/Mini_Servidor_API.git
cd Mini_Servidor_API
```

---

### Passo 2: Criar o Ambiente Virtual (venv)

#### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Passo 3: Instalar as Dependências

```bash
pip install -r requirements.txt
```

---

### Passo 4: Executar o Servidor

Abra um **primeiro terminal** e execute:

```bash
uvicorn server.app.main:app --reload
```

Servidor rodando! **Deixe esse terminal aberto.**

---

### Passo 5: Executar o Cliente

Abra um **segundo terminal** e execute:

```bash
python client/main.py
```

---

## Parar a Execução

Para parar o servidor, pressione `CTRL+C` no terminal onde está rodando.

---
