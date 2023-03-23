class Programmer:
    def __init__(self, name, typing_speed, experience):
        self.name = name
        self.typing_speed = typing_speed
        self.experience = experience

    def __str__(self):
        return f"{self.name}: typing_speed {self.typing_speed}, and experience {self.experience}"

    def action(self):
        """The action performed by the programmer."""
        print(f"{self.name} is writing code at a speed of {self.typing_speed} lines per minute.")

class CS111Student(Programmer):
    recharge_speed = 10

    def __init__(self, name, typing_speed, ta, experience=1):
        super().__init__(name, typing_speed, experience)
        self.ta = ta
        ta.add_student(self)
        self.energy_supply = 10

    def action(self, problem_difficulty):
        if self.energy_supply > 0:
            if self.experience >= problem_difficulty:
                self.energy_supply -= 1
                print(f"All right! {self.name} added {self.typing_speed} lines of code.")
            else:
                print("We need to ask a TA for help")
                self.ta.give_help(self)
        else:
            print("We need to take a rest")
            self.energy_supply += self.recharge_speed

    def receive_help(self, helper):
        if helper.experience > self.experience:
            self.experience += 1
            print("Thanks for the help! I’ll keep trying on this problem.")
        else:
            self.experience += .5
            helper.experience += .5
            print("Two heads are better than one! Let’s keep trying on this problem.")

    def give_help(self, other):
        if self.energy_supply > 0:
            self.energy_supply -= 1
            other.receive_help(self)
            print("Thanks for letting me help you!")
        else:
            print("Sorry, I need to take a rest first.")
            self.energy_supply += self.recharge_speed

class TA(Programmer):
    recharge_speed = 10
    lines_per_project = 15

    def __init__(self, name, typing_speed, experience=3, students=None):
        super().__init__(name, typing_speed, experience)
        self.students = students if students is not None else []
        self.lines_left = self.lines_per_project
        self.energy_supply = 10

    def add_student(self, student):
        self.students.append(student)

    def action(self, problem_difficulty):
        if self.energy_supply > 0:
            if self.experience >= problem_difficulty:
                self.energy_supply -= 1
                self.lines_left -= self.typing_speed
                print(f"All right! {self.name} added {self.typing_speed} lines of code.")
            else:
                print("We need to do some reading")
                self.read_textbook()
        else:
            print("We need to take a rest")
            self.energy_supply += self.recharge_speed

        if self.lines_left <= 0:
            print("Let’s help some students!")
            self.lines_left = self.lines_per_project
            for student in self.students:
                self.give_help(student)

    def give_help(self, other):
        other.receive_help(self)
        print("Thanks for letting me help you!")

    def read_textbook(self):
        self.experience += 1
