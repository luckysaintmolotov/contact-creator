import random
class Contact:
    def __init__(self,firstname,lastname,dateofbirth):
        self.firstname = firstname
        self.lastname = lastname 
        self.dateofbirth = dateofbirth

class Names:
    
    female_names = [
        "Anya", "Darya", "Elena", "Irina", "Katya", "Lilia", "Mila", "Nadia", "Oksana", "Polina",
        "Radmila", "Svetlana", "Tatiana", "Valentina", "Yelena", "Zinaida", "Alina", "Anastasia",
        "Danica", "Ekaterina", "Galina", "Inna", "Ksenia", "Lyudmila", "Marina", "Nadezhda", "Olga",
        "Renata", "Tatyana", "Vasilisa", "Yulia", "Zlata", "Amina", "Darina", "Elizaveta", "Faina",
        "Iryna", "Kira", "Masha", "Nika", "Raisa", "Sonya", "Ulyana", "Vika", "Xenia",
        "Amelia", "Beatrice", "Clara", "Delphine", "Freya", "Greta", "Helena", "Julia", "Livia", "Mia",
        "Ophelia", "Penelope", "Quinn", "Rosa", "Sofia", "Tessa", "Viola", "Willa", "Zara", "Aisling",
        "Brigitte", "Cosima", "Elysia", "Genevieve", "Heloise", "Jessamine", "Kaia", "Liora", "Maren",
        "Nella", "Pippa", "Rhea", "Sienna", "Thalia", "Una", "Violetta", "Wilhelmina", "Yvonne", "Zinnia",
        "Aveline", "Celeste", "Faye", "Hilda", "Isadora", "Jovana", "Klara", "Lila", "Mireille", "Orla",
        "Paloma", "Quinlan", "Selene", "Talia", "Ulla", "Wren"    ]

    male_names = [
        "Alexander", "Benjamin", "Charles", "Daniel", "Edward", "Felix", "Gabriel", "Henry", "Isaac", "Julian",
        "Leo", "Maximilian", "Nathan", "Oliver", "Paul", "Quentin", "Raphael", "Samuel", "Thomas", "Victor",
        "William", "Adrian", "Bruno", "Christoph", "David", "Emil", "Florian", "Georg", "Hugo", "Ivan", "Jan",
        "Klaus", "Lars", "Marco", "Niklas", "Oskar", "Petr", "Rasmus", "Stefan", "Tobias", "Uwe", "Viktor",
        "Anton", "Boris", "Cedric", "Darius", "Erik", "Filip", "Gregor", "Henrik", "Ivo", "Jannik", "Kieran",
        "Leif", "Milan", "Niko", "Otto", "Pavel", "Quentin", "Rocco", "Silas", "Teodor", "Ulrich", "Vasile",
        "Wenzel", "Xander", "Yves", "Zoran", "Alaric", "Bartosz", "Cosimo", "Dario", "Eamon", "Fintan", "Goran",
        "Hannes", "Ignatius", "Jovan", "Kacper", "Loris", "Marius", "Niall", "Orson", "Piero", "Quirin",
        "Rinaldo", "Soren", "Tadeusz", "Urban", "Vito", "Wilfred", "Xavi", "Yannis", "Zdenek", "Arvid",
        "Bastian", "Cillian", "Dorian", "Ewan", "Finn"
    ]

    first_names = [
        "Alex", "Taylor", "Jordan", "Morgan", "Casey", "Riley", "Jamie", "Quinn", "Dakota",
        "Skylar", "Cameron", "Finley", "Parker", "Reese", "Sydney","Drew", "Sam", "Jessie",
        "Blair", "Robin","Sage", "Ash", "Kiran", "Jaden", "Rowan", "Phoenix", "Tatum",
        "Emery", "Lennox", "Marlowe", "Remy", "Sloane","River", "Alexi",
        "Casey", "Jordan", "Sky", "Sam", "Avery", "Charlie", "Jamie", "Riley"
    ]
    
    last_names = [
    "Smith", "Johnson", "Williams", "Jones", "Brown",
    "Davis", "Miller", "Wilson", "Moore","Anderson", 
    "Thomas", "Jackson", "White", "Harris",
    "Martin", "Thompson", "Clark", "Lewis", "Walker",
    "Hall", "Allen", "Young", "King", "Wright",
    "Adams", "Baker", "Mitchell", "Roberts", "Turner",
    "Phillips", "Campbell", "Parker", "Evans", "Collins",
    "Stewart", "Cook", "Morgan", "Bell", "Murphy",
    "Bailey", "Ward", "Howard", "Price", "Bennett",
    "Reed", "Cox", "James", "Watson", "Brooks",
    "Kelly", "Sanders", "Foster", "Bryant", "Alexander",
    "Russell", "Griffin", "Diaz", "Hayes", "Hughes",
    "Harrison", "Graham", "Holland", "Hunt", "Mason",
    "Perry", "Powell", "Long","Hodge",
    "Ivanov", "Petrov", "Sidorov", "Kovalenko", "Smirnov",
    "Popov", "Vasiliev", "Morozov", "Fedorov", "Nikolaev",
    "Sokolov", "Lebedev", "Kuznetsov", "Mikhailov", "Orlov",
    "Romanov", "Borisov", "Dmitriev", "Gavrilov", "Tikhonov",
    "Zaitsev", "Karpov", "Semenov", "Frolov", "Gusev",
    "Kovalchuk", "Zhuravlev", "Belyakov", "Semyonov", "Kolesnikov",
    "Vlasov", "Makarov", "Kuzmin", "Svetlov", "Shcherbakov"]
    @classmethod
    def random_name(cls):
        cls.sort_check_list(cls.first_names)
        cls.sort_check_list(cls.last_names)
        return f"{random.choice(cls.first_names)} {random.choice(cls.last_names)}"
    @classmethod
    def random_fe_name(cls):
        return f"{random.choice(cls.female_names)} {random.choice(cls.last_names)}"
    @classmethod
    def random_ma_name(cls):
        return f"{random.choice(cls.male_names)} {random.choice(cls.last_names)}"
    
