class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(person["name"], person["age"]) for person in people]

    for num, person in enumerate(people):
        if "wife" in person and person["wife"] is not None:
            result_list[num].wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            result_list[num].husband = Person.people[person["husband"]]
    return result_list
