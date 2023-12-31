class Normalize:
    def __init__(self, raw_data):
        self.constituents, self.donations, self.payments, self.adresses = self.normalize(raw_data)

    def normalize(self, raw_data):
        constituents = []
        donations = []
        payments = []
        adresses = []

        for donor in raw_data:
            constituent = donor.copy()

            if 'address' in constituent:
                if constituent['address']:
                    constituent['address']['constituent_id'] = constituent['id']
                    adresses += [constituent['address']]
                del constituent['address']

            if 'donations' in constituent:
                if constituent['donations']:
                    donations += constituent['donations']
                del constituent['donations']

            if 'payments' in constituent:
                if constituent['payments']:
                    payments += constituent['payments']
                del constituent['payments']

            constituents += [constituent]

        return constituents, donations, payments, adresses
