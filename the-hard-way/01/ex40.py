class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


cancion_1 = Song(["Pepe fue a pepelandia", "muy feliz", "llegó a su casa"])
cancion_2 = Song(["Estrofa 1", "Estrofa 2"])

cancion_1.sing_me_a_song()
cancion_2.sing_me_a_song()