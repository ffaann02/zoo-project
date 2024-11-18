class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12: # add equal underbound
            return 50
        elif 13 <= age <= 20: # add equal upperbound
            return 100
        elif 21 <= age <= 60: # add equal underbound
            return 150
        elif age > 60: # remove equal
            return 100
        else:
            return 0 # add below zero age case