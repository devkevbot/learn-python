class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, o: object) -> bool:
        return self.name == o.name


bob = Person("Bob")
tim = Person("time")
bob2 = Person("Bob")

print(bob == tim)
print(bob == bob2)
