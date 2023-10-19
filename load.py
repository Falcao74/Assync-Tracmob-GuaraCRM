import pandas as pd
import pymysql
from sqlalchemy import create_engine
from settings import db_server, db_name, db_user, db_password, db_port

class Load:
    
    def __init__(self):
        self.pd_constituents: pd.DataFrame = pd.DataFrame()
        self.pd_donations: pd.DataFrame = pd.DataFrame()
        self.pd_payments: pd.DataFrame = pd.DataFrame()
        self.pd_adresses: pd.DataFrame = pd.DataFrame()
        self._engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_server}:{db_port	}/{db_name}?charset=utf8mb4')
        
    def prepare_to_load(self, data) -> None:
        self.pd_constituents = pd.json_normalize(data.constituents, sep='_')
        self.pd_donations = pd.json_normalize(data.donations, sep='_')
        self.pd_payments = pd.json_normalize(data.payments, sep='_')
        self.pd_adresses = pd.json_normalize(data.adresses, sep='_')
        # using list comprehension, to avoid bad columns format.
        limit = 40
        self.pd_payments = self.pd_payments.loc[:, [x for x in self.pd_payments.columns if len(x) < limit]]   
        
    def perform(self) -> None:
        self.pd_constituents.to_sql('constituents', self._engine, if_exists='append', index=False)
        self.pd_donations.to_sql('donations', self._engine, if_exists='append', index=False)
        self.pd_payments.to_sql('payments', self._engine, if_exists='append', index=False)
        self.pd_adresses.to_sql('adresses', self._engine, if_exists='append', index=False)