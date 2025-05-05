class person:
  def __init__(self,name,age,number):
    self.name=name
    self.age=age
    self.number=number
  def __str__(self):
    return f"{self.name}({self.age}){self.number}"
p1=person("haya",12,637648)
print(p1)
