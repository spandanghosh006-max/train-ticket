import random
random= random.randint(5454864,65568585)
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"from {fro} to {to} has been booked on train number {self.trainNo}.")

    def getStatus(self, fro, to):
        print(f"Train {self.trainNo} is on time.")

    def getFares(self, fro, to):
        print(f"The fare from {fro} to {to} is Rs. {random}")

train = Train(12345)
train.book("Delhi", "Mumbai")
train.getStatus("Delhi", "Mumbai")
train.getFares("Delhi", "Mumbai")        