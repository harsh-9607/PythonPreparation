from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print("Its running")

com1 =laptop()
com1.process() 

com=computer()
com.process()