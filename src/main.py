from datasources.gupy import finding_jobs
from config.settings import SETTINGS

import json

def main():
    for role in SETTINGS["lista_vagas"]:
        finding_jobs(role)


if __name__ == "__main__":
    main()

    