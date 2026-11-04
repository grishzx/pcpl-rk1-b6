class House:
    """Дом."""

    def __init__(self, id, name, floors, street_id):
        self.id = id
        self.name = name
        self.floors = floors
        self.street_id = street_id


class Street:
    """Улица."""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class HouseStreet:
    """Связь дома и улицы: многие-ко-многим."""

    def __init__(self, house_id, street_id):
        self.house_id = house_id
        self.street_id = street_id


streets = [
    Street(1, "Центральная"),
    Street(2, "Лесная"),
    Street(3, "Садовая"),
]

houses = [
    House(1, "Дом купцов", 5, 1),
    House(2, "Дом культуры", 3, 2),
    House(3, "Дом мастеров", 4, 2),
    House(4, "Дом учёных", 9, 3),
]

houses_streets = [
    HouseStreet(1, 1),
    HouseStreet(1, 2),
    HouseStreet(2, 2),
    HouseStreet(3, 2),
    HouseStreet(4, 3),
]


def main():
    # Связь один-ко-многим: у дома одна основная улица.
    one_to_many = [
        (house.name, street.name)
        for house in houses
        for street in streets
        if house.street_id == street.id
    ]

    print("Задание Б1. Дома и улицы, сортировка по названию дома:")
    result_1 = sorted(one_to_many, key=lambda row: row[0])
    for house_name, street_name in result_1:
        print(f"{house_name} - {street_name}")

    print("\nЗадание Б2. Улицы по возрастанию количества домов:")
    result_2 = [
        (street.name, len([h for h in houses if h.street_id == street.id]))
        for street in streets
    ]
    result_2 = sorted(result_2, key=lambda row: row[1])
    for street_name, count in result_2:
        print(f"{street_name}: {count}")

    # Связь многие-ко-многим берётся из списка houses_streets.
    print("\nЗадание Б3. Дома с названием на 'ов' и их улицы:")
    result_3 = {
        house.name: [
            street.name
            for link in houses_streets
            for street in streets
            if link.house_id == house.id and link.street_id == street.id
        ]
        for house in houses
        if house.name.endswith("ов")
    }
    for house_name, street_names in result_3.items():
        print(f"{house_name}: {', '.join(street_names)}")


if __name__ == "__main__":
    main()
