from urllib.parse import quote #Usada para garantir que os termos da URL estejam codificados corretamente.
import requests
import json

def buscar_vagas(vagas):
    todas_as_vagas = []

    for vaga in vagas:
        for offset in range(0, 100, 10):
            vaga_codificada = quote(vaga)
            url = f"https://portal.api.gupy.io/api/job?name={vaga_codificada}&offset=0&limit=10"
            resposta = requests.get(url)

            print(f"Buscando vaga: {vaga}")
            print(f"Status code: {resposta.status_code}")
            print(f"Resposta: {resposta.text[:200]}")

            if resposta.status_code == 200:
                dados = resposta.json()
            todas_as_vagas.extend(dados.get("data", []))
        else:
            print(f"Erro ao buscar vaga '{vaga}': {resposta.status_code}")

    caminho = "../dados/vagas/gupy.json"

    with open("dados/vagas/gupy.json", "w", encoding="utf-8") as f:
        json.dump(todas_as_vagas, f, indent=4, ensure_ascii=False)




                
    