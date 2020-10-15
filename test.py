
class Person():
  def __init__(self,name,age):
    self.name = name
    self.age = 0
  def ageup(self):
    self.age = self.age + 2

shugo = Person('shugo',13)
sasaki = Person('sasaki',14)
shugo.ageup()
sasaki.ageup()

print(shugo.age)




  







