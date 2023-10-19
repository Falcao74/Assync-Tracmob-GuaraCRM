class Normalize:
    
    def __init__(self):
        self.constituents = []
        self.donations = []
        self.payments = []
        self.adresses = []
        
    def normalize_data(self, data):
        for donor in data:
            constituent = donor.copy()

            if 'address' in constituent:
                if constituent['address']:
                    constituent['address']['constituent_id'] = constituent['id']
                    self.adresses += [constituent['address']]
                del constituent['address']

            if 'donations' in constituent:
                if constituent['donations']:
                    self.donations += constituent['donations']
                del constituent['donations']

            if 'payments' in constituent:
                if constituent['payments']:
                    self.payments += constituent['payments']
                del constituent['payments']

            self.constituents += [constituent]
    
        