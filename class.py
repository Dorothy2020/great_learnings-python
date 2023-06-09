# creating the class
class Phone:
    def make_call(self):
        print("phones can make calls")

    def play_game(self):
        print("Phones can play games")


# Instantiate the p1 object
p1 = Phone()
# invoke methods through objects
p1.make_call()
p1.play_game()


# Adding Parameters to Class
class Phone:
    def make_call(self):
        print("phones can make calls")

    def play_game(self):
        print("Phones can play games")

    def assign_cost(self, cost):
        self.cost = cost

    def assign_color(self, color):
        self.color = color


    def show_cost(self,cost):
        return self.cost
    def show_color(self,color):
        return self.color


p2 = Phone()
p2.assign_cost(555)
p2.show_color("orange")
