import json

''' PATH: str = "Lezione_15/config.json" #dichiaro il percorso
mode: str = "r" #modalità lettura

with open(PATH, mode=mode) as file: #definisco il file nella funzione open

    config: dict = json.load(file)

    print(config)

    nome_applicazione: str = config["appName"]

    host: str = config["server"]["host"]
    port: str = str(config["server"]["port"])
    timeout: int = config["server"]["timeout"]

    connect(ip=host, port=port, timeout=timeout)

    print(nome_applicazione) '''

''' PATH: str = "Lezione_15/config_1.json"
mode: str = "w"

with open(PATH, mode=mode) as file:

    config: dict = {"nome" : "2048", "versione": "1.1.42", "OS": "Android 16.1.0" }

    json.dump(config, file)''' 

import json

PATH: str = "Lezione_15/config_2.json"
mode:str = "w"

with open(PATH, mode=mode) as file:

    config: dict = {"nome": "ciao", "versione": "2"}

    json.dump(config, file)

    

