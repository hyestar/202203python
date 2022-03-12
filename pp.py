class Person :
  def __init__(self, name, age) :
    self.name = name
    self.age = age
  
  def introduce(self) :
    print("안녕하세요 {}살 {}입니다.".format(self.age, self.name))
