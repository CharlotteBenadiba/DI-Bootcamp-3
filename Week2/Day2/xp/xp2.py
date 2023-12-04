# from xp1 import Dog 
# import random

#class PetDog(Dog): 
#    def __init__(self, name, age, weight):
#        super().__init__(name, age, weight)
#        self.trained = False

#    def train(self):
#        bark_result = super().bark()
#        print(bark_result)
#        self.trained = True

#    def play(self, *dog_names):
#        all_dogs = ', '.join(dog_names)
#        print(f"{all_dogs} all play together")

#    def do_a_trick(self):
#        if self.trained:
#            tricks = [
#                f"{self.name} does a barrel roll",
#                f"{self.name} stands on his back legs",
#                f"{self.name} shakes your hand",
#                f"{self.name} plays dead"
#            ]
#            selected_trick = random.choice(tricks)
#            print(selected_trick)
#        else:
#            print(f"{self.name} is not trained yet. Train first!")

# pet_dog = PetDog('Maximus', 7, 21)
# pet_dog.train()
# pet_dog.play()
# pet_dog.do_a_trick()
