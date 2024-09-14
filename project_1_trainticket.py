import random
class train :
  def __init__(self,trainname,fro,to):
    self.trainname=trainname
    self.fro=fro
    self.to=to

  def book(self):
    print(f"\nYour train name is {self.trainname} and it will be running from {self.fro} to {self.to}\n")

  def getstatus(self):
    print(f"It will be on station on {random.randint(1,12)} O\'clock\n")

  def fare(self):
    print(f"The fare of the train is {random.randint(2000,3500)}\n")
  @staticmethod
  def cancel():
    s=input("Do you want to cancel the ticket\"Yes\\No\"?:")
    if("Yes"in s or 'yes'in s):
      print("Your ticket has been cancelled")
    else:
      print("Then be ready")
  @staticmethod
  def review():
    s=input("Do you want to give a review\"Yes\\No\"?:")
    if("Yes"in s or 'yes' in s):
      input("Enter your review : ")
      print("Thank you for your review")
    else:
      print("Okay")


trainnoo=input("Enter the train name:\n ")
froi=input("Enter the Departure Location \n ")
too=input("Enter your destination location:\n")

a=train(trainnoo,froi,too)


a.book()
a.getstatus()
a.fare()
a.cancel()
print(a.review())