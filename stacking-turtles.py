class Turtle:
    def __init__(self, name, below=None, above=None):
        self.name = name
        self.below = below
        if below:
            self.below.above = self
        self.above = above
        if above:
            self.above.below = self


    def climb_down(self):
            """Cause this turtle to climb down from its current stack of turtles. The
            turtles above this turtle stay in place, and a new stack of turtles is made, where
            this turtle is the bottom turtle. If this turtle is already the bottom turtle, this
            function does nothing.
            """
            if self.below:
                self.below.above = None
            self.below = None

    def climb_up(self, other):
            """Cause this turtle to climb up the stack of turtles containing the other
            turtle, making one stack from two stacks, or two different stacks from two existing
            stacks. (self and other should not be in the same stack of turtles). The turtles
            above this turtle stay in place, and this turtle becomes the first turtle on top of
            the other stack.
            """
            if self.below:
                self.below.above = None
            next = other
            while next.above:
                next = next.above
            self.below = next
            next.above = self

    def stack_height(self):
            """
            Return the height of the stack that includes this turtle (the number of
            turtles in the stack).

            """
            height = 1
            next = self
            while next.below:
                height += 1
                next = next.below
            next = self
            while next.above:
                height += 1
                next = next.above
            return height

    def __repr__(self):
            prev = "" if not self.behind else f",below={self.below}"
            nxt = "" if not self.in_front else f",above={self.in_above}"
            return f"Turtle('{self.name}'{prev}{nxt})"

    def __str__(self):
            return self.name

bowser = Turtle("Bowser")
franklin = Turtle("Franklin", below=bowser)
michelangelo = Turtle("Michelangelo", below=franklin)
yertle = Turtle("Yertle", below=michelangelo)
# >>> yertle
# Turtle('Yertle',below=Michelangelo)

# >>> michelangelo
# Turtle('Michelangelo',below=Franklin,above=Yertle)
michelangelo.above = yertle
# >>> franklin
# Turtle('Franklin',below=Bowser,above=Michelangelo)
franklin.above = michelangelo
# >>> Bowser
# Turtle('Bowser',above=Franklin)
bowser.above = franklin

# current stack 
# Yertle
# Michelangelo
# Franklin
# Bowser
# 

# insert code here to make the stack look like this:



# new stack split into two stacks
# Michelangelo
# Franklin
# Yertle


# Bowser
