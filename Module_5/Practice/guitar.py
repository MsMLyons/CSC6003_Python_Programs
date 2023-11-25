class Guitar:
    def __init__(self, model, style):
        self.model = model
        self.style = style

    def play(self):
        print(f"I am playing my {self.model} and {self.style}")

guitar1 = Guitar("Gibson", "strumming")
guitar1.play()
guitar2 = Guitar("Fender", "shredding")
guitar2.play()

# output -->
    # I am playing my Gibson and strumming
    # I am playing my Fender and shredding