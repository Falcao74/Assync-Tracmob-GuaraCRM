import datetime
from retry import retry
import requests

class GuaraCRM:
    def __init__(self, token):
        self._endpoint = "https://guaracrm.com.br/api/v1/constituents"
        self._headers = {'Content-Type': 'application/json'}
        self._page = 1
        self._result_per_page = 60
        self._token = token
        self._total_pages = 0
        self._chunk = 20
    
    @property
    def url(self):
        return f'{self._endpoint}?access_token={self._token}&per_page={self._result_per_page}&page={self._page}'
    
    def has_next_page(self):
        return False if self._page is None else True

    @retry(exceptions=IOError, delay=30.0, tries=5)
    def hit(self):
        try:
            with requests.Session() as client:
                response = client.get(self.url, headers=self._headers)
            if response.status_code != 200:
                raise IOError
            json = response.json()
            self._page = json['metadata']['pagination']['next_page']
            self._total_pages = json['metadata']['pagination']['total_pages']
            return json['constituents']
        
        except Exception as error:
            msg = f'Houve um erro no hit {str(error)} '
            f = open("hit_erros.txt", "a")
            tempo = datetime.datetime.now()
            f.write(f'\n{tempo.hour}:{tempo.minute}:{tempo.second} - {msg}')
            f.close()
            raise IOError
    
    def perform(self, chunk_size):
        i = 0
        data = []
        while self.has_next_page() and i < chunk_size:
            print(f'Pagina {self._page} de {self._total_pages} - {self.percentagem(self._page, self._total_pages):.2f} % do processo')
            data += self.hit()
            i += 1
        return data

    def percentagem(self, divisor, dividendo):
        try:
            _divisor = float(divisor)
            _dividendo = float(dividendo)
            result = 100 * _divisor / _dividendo
            return result if isinstance(result, float) else 0.00
        except ZeroDivisionError:
            return 0.00
