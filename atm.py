class Atm(object):
    def __init__(self, user, atmCardNumber, pinNumber):
        self.user = user
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber

    def cashWithDrawal(self):
        print("WithDrawing Cash")

    def balanceEnquiry(self):
        print("Balance Enquiry")

sam = Atm("Sam", 1234567812345678, 12345678)
print(sam.cashWithDrawal())
print(sam.balanceEnquiry())