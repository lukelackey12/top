class Cell:

    def _init_(self, ma, mo, re):
        self._manufact = ma
        self._model = mo
        self._retail_price = re


    def set_manufact(self, ma):
        self._manufact = ma

    def set_model(self, mo):
        self._model = mo

    def set_retail_price(self, re):
        self._retail_price = re

    def get_manufact(self):
        return self._manufact
    
    def get_model(self):
        return self._model
    
    def get_retail_price(self):
        return self._retail_price
    

        
