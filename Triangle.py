#Problem 1
class Triangle():

    number_of_sides = 3
    
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        return False

my_triangle = Triangle(90, 30, 60)
print(my_triangle.check_angles())

#Problem 2
class Song():
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for lyline in self.lyrics:
            print(lyline)
happy_bday = Song(["May god bless you,","Have a sunshine on you", "Happy Birthday to you!"])
happy_bday.sing_me_a_song()

#Problem 3
class Lunch():
    def __init__(self, menu):
        self.menu = menu
    def menu_price(self):
        if self.menu == "menu 1":
            print("Your choice:" + str(self.menu) + ", Price 12.00")
        elif self.menu == "menu 2":
            print("Your choice:" + str(self.menu) + ", Price 13.40")
        else:
            print("Error in menu")
Paul = Lunch("menu 1")
Paul.menu_price()

#Problem 4
