class student:

    age = 0;
    name = "";

    def __init__(self, tmp_n, tmp_a):
        self.name = tmp_n
        self.age = tmp_a
        print(self.name, 'constructed')

    def inc_age(self):
        self.age += 1
        print(self.name,'is', self.age, 'years old.')


alice = student("Alice", 20)
bob = student("Bob", 21)

alice.inc_age()