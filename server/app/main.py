from fastapi import FastAPI

app = FastAPI(
    title="Minha API Fatec",
    description="API desenvolvida para o Terceiro Mini Projeto",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """Rota raiz que retorna mensagem de boas-vindas"""
    return {"mensagem": "Bem-vindo à API do Mini Projeto 3!"}

@app.get("/dados")
def get_dados():
    """Retorna dados simulados do projeto"""
    return {
        "id": 1,
        "tema": "Consumo de APIs",
        "tecnologias": ["Python", "FastAPI"],
        "status": "Ativo"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)