# coding: utf8
import pymysql
import asyncio
import datetime
import requests
import subprocess
import pandas as pd
from load import Load
from guaracrm import GuaraCRM
from normalize import Normalize
from sqlalchemy import create_engine
from settings import IP_SERVER, DB_NAME, DB_USER, DB_PASS, DB_PORT, USER_TOKEN

async def fetch_and_load(token, chunk_size, engine):
    guara = GuaraCRM(token)
    while guara.has_next_page():
        dados_puro = guara.perform(chunk_size=chunk_size)
        dados_normalizados = Normalize(dados_puro)
        Load(dados_normalizados, engine).perform()

def main():
    token = USER_TOKEN  # Substituir pelo token real
    inicio = datetime.datetime.now()
    msg = 'com sucesso'
    
    try:
        engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASS}@{IP_SERVER}:{DB_PORT}/{DB_NAME}?charset=utf8mb4')
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(fetch_and_load(token, chunk_size=20, engine=engine))
        
    except Exception as e:
        f = open("erros.txt", "a")
        msg = 'com erros!'
        f.write(f'\n{datetime.datetime.now()} - {str(e)}')
        f.close()
    
    finally:
        print(f"Processo concluído {msg}!")
        final = datetime.datetime.now()
    
    print(
        f'Processo finalizado em {final.day}/{final.month}'
        f'\n Início em {inicio.hour} : {inicio.minute}: {inicio.second} - Término em '
        f'{final.hour}: {final.minute}: {final.second}\n'
        f'Processo completo no tempo de {final - inicio}'
    )
    input("Aperte enter para encerrar o programa.")

if __name__ == "__main__":
    main()
