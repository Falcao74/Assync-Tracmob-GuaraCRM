import json
from log import Log
from asyncio import gather
from typing import Dict, List
from httpx import AsyncClient, ConnectError, ConnectTimeout

class Guara:
    
    def __init__(self, token):
        self._endpoint: str = "https://guaracrm.com.br/api/v1/constituents"
        self._headers: Dict = {'Content-Type': 'application/json'}
        self._result_per_page: int = 50
        self._token: str = token
        self._start_page: int = 1
        self._total_pages: int = 0
        self._lista: List = []
        
    @property
    def url(self):
        return f'{self._endpoint}?access_token={self._token}&per_page={self._result_per_page}&page=1'
    
    async def set_total_pages(self) -> None:
        async with AsyncClient() as client:
            response = await client.get(self.url)
            result = response.json()
            self._total_pages = result['metadata']['pagination']['total_pages']
    
    def mount_requests(self, param: int) -> str:
        return f'{self._endpoint}?access_token={self._token}&per_page=50&page={param}'
    
    async def create_tasks(self):
        return [self.mount_requests(page) for page in range(self._start_page, self._total_pages + 1)]
    
    async def fetch_responses(self, tasks, retries = 3):
        log = Log()
        log.start_log()
        for retry in range(retries):
            try:
                async with AsyncClient() as client:
                    responses = await gather(*[client.get(task) for task in tasks])
                    return responses
            except (ConnectTimeout, ConnectError) as e:
                log.add_event(f'Erro na tentativa {retry + 1}: {e}')
            except Exception as e:
                log.add_event(f'\n Surgiu um erro desconhecido no momento: tentativa {retry + 1 } \n  Requisitando os dados novamente: {e}')
        log.add_event(f"Atingiu o número máximo de tentativas. Falha na solicitação.")
        log.write_log(param = "requests_errors")
        return []
            
    def process_data(self, responses):
        for response in responses:
            data = response.json()['constituents']
            self._lista.extend(data)
            
    async def listagem(self):
        tasks = await self.create_tasks()
        responses = await self.fetch_responses(tasks)
        self.process_data(responses)
        return self._lista