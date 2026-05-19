import requests
import json

API_URL = "http://127.0.0.1:8000"

def consumir_api():
    """Função que consome os dados da API"""
    print("Iniciando consumo da API...\n")
    
    try:
        resposta_raiz = requests.get(f"{API_URL}/")
        print(f"Status Code da Raiz: {resposta_raiz.status_code}")
        print(f"Resposta da Raiz: {resposta_raiz.json()}\n")
        
        resposta_dados = requests.get(f"{API_URL}/dados")
        print(f"Status Code de Dados: {resposta_dados.status_code}")
        print(f"Resposta de Dados:")
        print(json.dumps(resposta_dados.json(), indent=2))
        
    except requests.exceptions.ConnectionError:
        print("Erro de conexão! O servidor FastAPI está rodando?")
        print("   Execute: uvicorn server.app.main:app --reload")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    consumir_api()