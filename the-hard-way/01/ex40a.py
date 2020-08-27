class MyStuff(object):

    def __init__(self):
        self.const_var = "Algo constante"

    def fc_uno(self):
        print('Soy una función')

ejemplo = MyStuff()
ejemplo.fc_uno()
print(ejemplo.const_var)