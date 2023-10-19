import time
from log import Log
from load import Load
from guara import Guara
from normalize import Normalize
from settings import user_token
from asyncio import gather, run
from datetime import datetime

class APP:
        
    async def main(self):
        guara = Guara(user_token)
        await guara.set_total_pages()
        normalizer = Normalize()
        load = Load()
        log = Log() 
        
        try:
            log.start_log()
            tasks = await guara.create_tasks()
            num_requests = len(tasks)
            log.add_event(f'Quantidade de requests a serem feitas: {num_requests}')

            counter = 0

            for task in tasks:   
                response = await guara.fetch_responses([task])
                raw_data = response[0].json()['constituents']
                normalizer.normalize_data(raw_data)  # Use o método da instância normalizer
                load.prepare_to_load(normalizer)  # Use a instância normalizer
                load.perform() 
                counter += 1
                print(f'Requisições: {counter}')
             
            log.add_event(f'Processo finalizado')
                  
        except Exception as e:
            # Em caso de erro, registre o erro no log
            log.add_event(f'Ocorreu um erro: {str(e)}\n O processo não finalizou')

        # Ao final da rotina, escreva o log
        log.write_log()

if __name__ == "__main__":
    app = APP()
    run(app.main())