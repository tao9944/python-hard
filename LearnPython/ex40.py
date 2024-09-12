class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

ode_to_joy = Song(["Joy, beautiful spark of Divinity",
                    "We enter, drunk with fire"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

ode_to_joy.sing_me_a_song()

new_words = "On top of old smokey, all covered in cheese"
