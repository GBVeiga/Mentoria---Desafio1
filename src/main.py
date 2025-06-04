from gupy import buscar_vagas  # ✅ Correto, já que está no mesmo diretório


def main():
    vagas = [
        "analista de dados senior",
        "engenheiro de software" ,
        "analista de dados jr",
        "analise de dados pleno",
    ]

    buscar_vagas(vagas)

if __name__ == "__main__":
    main()


    