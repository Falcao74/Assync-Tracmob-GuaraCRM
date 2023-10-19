import os
from datetime import datetime
import time
from typing import Optional

class Log:
    def __init__(self):
        self.log_entries = []
        self.start_time = None

    def start_log(self):
        self.start_time = time.time()
        current_time = datetime.now()
        self.log_entries.append(f'Início do log em {current_time.hour:02d}:{current_time.minute:02d}')

    def add_event(self, event):
        if self.start_time is not None:
            current_time = datetime.now()
            elapsed_time = time.time() - self.start_time
            hours, rem = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(rem, 60)
            time_str = f'{int(hours)}h {int(minutes)}m {seconds:.2f}s'
            self.log_entries.append(f'{current_time.hour:02d}:{current_time.minute:02d} ({time_str}): {event}')

    def write_log(self, param: Optional[str] = None):  # Parâmetro param é opcional
        log_directory = 'C:/bi/logs'
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        current_time = datetime.now()
        current_time = current_time.strftime('%Y%m%d-%H%M%S')
        log_file_name = f'{current_time}_{param}log.txt' if param else f'{current_time}_log.txt'  # Se param for None, não adiciona
        log_file = os.path.join(log_directory, log_file_name)

        with open(log_file, 'a') as file:
            for entry in self.log_entries:
                file.write(entry + '\n')

if __name__ == "__main__":
    log = Log()
    log.start_log()
    log.add_event("Acontecimento 1")
    time.sleep(1)
    log.add_event("Acontecimento 2")
    time.sleep(3)
    log.add_event("Acontecimento 3")
    log.write_log()
