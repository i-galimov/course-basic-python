class Circle:
    pi = 3.14

    def calculate_area(self, radius):
        self.radius = radius
        s = self.radius ** 2 * self.pi
        return s

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)