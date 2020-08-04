class Animal:
    noise = 'Rawr'  # propiedad/atributo
    color = 'red'

    def make_noise(self):
        print(f'{self.noise}')

    def set_noise(self, new_noise):
        self.noise = new_noise

    def get_noise(self):
        return self.noise

    def set_noise(self, new_value):
        self.noise = new_value
        return self.noise

    def get_color(self):
        return self.color

    def set_color(self, new_value):
        self.color = new_value
        return self.color


class Wolf(Animal):
    noise = 'Grrrr'


class BabyWolf(Wolf):
    color = "yellow"


obj_animal = Animal()  # instanciamos
obj_animal.make_noise()
obj_animal.noise
obj_animal.set_noise("hhhhh")
obj_animal.make_noise()

obj_wolf = Wolf()
obj_wolf.make_noise()
print(obj_wolf.get_color())

ob = BabyWolf()
ob.make_noise()
print(ob.get_color())
