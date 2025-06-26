import os
from typing import Any, Dict
from config.settings import SETTINGS  

os.makedirs(os.path.dirname(SETTINGS["file_path"]), exist_ok=True)

import requests  # se estiver usando
import json

Json_fisico = Dict[str, Any]


def finding_jobs(role: str) -> None:
    all_jobs = []

    for offset in SETTINGS["offsets"]:
        url = f"https://portal.api.gupy.io/api/job?name={role}&offset={offset}&limit=10"
        response = requests.get(url)

        print(f"Buscando vaga: {role}")
        print(f"Status code: {response.status_code}")
        print(f"Resposta: {response.text[:200]}")

        if response.status_code == 200:
            data = response.json()
            all_jobs.extend(data.get("data", []))

    #  Garante que a pasta onde o arquivo será salvo exista
    os.makedirs(os.path.dirname(SETTINGS["file_path"]), exist_ok=True)

    with open(SETTINGS["file_path"], "w", encoding="utf-8") as f:
        json.dump(all_jobs, f, indent=2, ensure_ascii=False)

