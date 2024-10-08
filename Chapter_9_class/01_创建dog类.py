class Dog():
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over.")

#实例
my_dog = Dog("wangcai",3)
your_dog = Dog("laifu",5)
my_dog.sit()
my_dog.roll_over()
print("\nMy dog's name is " + my_dog.name.title())
print("My dog age is " + str(my_dog.age) + "years old")

your_dog.sit()
your_dog.roll_over()
print("\nYour dog's name is " + your_dog.name.title())
print("My dog age is " + str(your_dog.age) + "years old")