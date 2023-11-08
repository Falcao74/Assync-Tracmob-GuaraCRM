import pandas as pd

class Load:
    def __init__(self, normalized_data, engine):
        self.pd_constituents = pd.json_normalize(normalized_data.constituents, sep='_')
        self.pd_donations = pd.json_normalize(normalized_data.donations, sep='_')
        self.pd_payments = pd.json_normalize(normalized_data.payments, sep='_')
        self.pd_adresses = pd.json_normalize(normalized_data.adresses, sep='_')
        self.engine = engine
        # usando list comprehension, eu retiro dos dados qualquer coluna que tenha um nome maior do que o limite.
        limit = 24
        self.pd_payments = self.pd_payments.loc[:, [x for x in self.pd_payments.columns if len(x) < limit]]
    
    def perform(self):
        self.pd_constituents.to_sql('constituents', self.engine, if_exists='append', index=False)
        self.pd_donations.to_sql('donations', self.engine, if_exists='append', index=False)
        self.pd_payments.to_sql('payments', self.engine, if_exists='append', index=False)
        self.pd_adresses.to_sql('adresses', self.engine, if_exists='append', index=False)
