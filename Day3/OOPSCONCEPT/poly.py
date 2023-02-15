# one method is same output is diff one indecate srting len and anather is int value len


# print(len("sonalikadlag"))
#
# print(len([10,20,30]))

class Polygon:

    def render(self):
        print("Rendering Polygon...")


class Square(Polygon):

    def render(self):
        print("Rendering Square...")


class Circle(Polygon):

        print("Rendering Circle...")



s1 = Square()
s1.render()


c1 = Circle()
c1.render()