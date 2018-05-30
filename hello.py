# def createGtr():
# 	mylist = range(5)
# 	for i in mylist:
# 		yield i**3

# mygtr = createGtr()
# print(mygtr)

# for i in mygtr:
# 	print(i)

# squares = []

# for i in range(1,101):
# 	squares.append(i**2)



# print(squares)

# squares = [i ** 2 for i in range(1,101)]

# print(squares)


# remainders5 = [x ** 2  % 10 for x in range(1,101)] 

# print(remainders5)

# import math

# def area(r):
# 	return math.pi * (r**2)

# radii = [2,5,7.1,0.3,10]

# areas = []

# for r in radii:
# 	a = area(r)
# 	areas.append(a)

# print(areas)


# print(list(map(area,radii)))

# temps = [("berlin",29),("cairo",36),("buenos aires",19),("los angeles",26),("beijing",32)]


# c_to_f = lambda data: (data[0],(9/5)*data[1] +32)
# print(list(map(c_to_f,temps)))


# import statistics

# data = [1,3,4,5,6,4,5,2.1,4.3,-2.3]
# avg = statistics.mean(data)
# # print(avg)

# filter(lambda x: x > avg,data)
# print(list(filter(lambda x: x > avg,data)))

# def f(x):
# 	return x**2 

# r = map(f,[1,2,3,4,5,6,8])
# print(list(r))

# import sys

# __author__ = "secondtown"

# def test():
# 	args = sys.argv

# 	if len(args) == 1:
# 		print("hello this fucking world")
# 	elif len(args) == 2:
# 		print("thanks %s!" %args[1])

# 	else:
# 		print("you have finished ")

# if __name__ == "__main__":
# 	test()

# from PIL import Image
# im = Image.open("test.jpg")
# print(im.format,im.size,im.mode)

# JPEG (400,300) RGB
# im.thumbnail((200,100))
# im.save("thumb.jpg",'JPEG')


# import sys
# print(sys.path)

# pip install --upgrade pip



# class Student(object):

# 	def __init__(self,name,score):
# 		self.__name = name
# 		self.__score = score

# 	def print_score(self):
# 		print("%s : %s" %(self.__name,self.__score))

# 	def get_grade(self):
# 		if self.__score >= 90 :
# 			return 'A'
# 		elif self.__score >=60 :
# 			return 'B'
# 		else :
# 			return 'C'

# 	def get_name(self):
# 		return self.__name

# 	def get_score(self):
# 		return self.__score




# bart = Student("Bart Simpson",59)
# Lisa = Student("Lisa Simpson",87)
# bart.print_score()
# Lisa.print_score()

# print(bart)
# print(Lisa)
# print(bart.get_grade())
# print("-"*20)

# print(bart._Student__name)

# class Animal(object):
# 	def run(self):
# 		print("animal is running")

# class Dog(Animal):
# 	def run(self):
# 		print("the dog is running")
# 	def eat(self):
# 		print("the dog is eatting meat right now")

# class Cat(Animal):
# 	pass


# dog = Dog()
# dog.run()	

# class Myobject(object):
# 	def __init__(self):
# 		self.x = 9

# 	def power(self):
# 		return self.x **2

# class Student(object):

# 	def __init__(self,name):
# 		self.name = name

# s = Student("Bob")
# s.score = 90

# class Student(object):
# 	name = "student"

# s = Student()
# print(s.name)

# print(Student.name)

# print("--"*10)

# s.name = "secondtown"
# print(s.name)
# print(Student.name)

# class Student(object):
# 	__slots__ = ("name","age")
# 	pass

# class Student(object):


# 	def get_score(self):
# 		return self._score

# 	def set_score(self,value):
# 		if not isinstance(value,int):
# 			raise ValueError("score must be an integer")

# 		if value < 0 or value>100:
# 			raise ValueError("score must be between 0 and 100 ")

# 		self._score = value
		


# class Animal(object):
# 	pass

# class Bird(Animal):
# 	pass

# class Mammal(Animal):
# 	pass


# class Runnable(object):
# 	def run(self):
# 		print("is running...")

# class Flyable(object):
# 	def fly(self):
# 		print("is flying...")




# class Dog(Mammal,Runnable):
# 	pass

# class Bat(Mammal,Flyable):
# 	pass

# class Parrot(Bird,Flyable):
# 	pass

# class Ostrich(Bird,Runnable):
# 	pass


# class Student(object):
# 	def __init__(self,name):
# 		self.name = name

# 	def __str__(self):
# 		return "Studnet object (name: %s) " %self.name


# try:
# 	print("try....")
# 	r = 10/3
# 	print("result is : ",r)
# except ZeroDivisionError as e:
# 	print("except:",e)
# except ValueError as e:
# 	print("valueError is: ",e)
# else:
# 	print("there is no error at all")
# finally:
# 	print("finally......")


# print("END")


# import logging

# def foo(s):
# 	return 10/int(s)

# def bar(s):
# 	return foo(s) * 2

# def main():
# 	try:
# 		bar("0")
# 	except Exception as e:
# 		logging.exception(e)

# main()
# print("END")


# class FooError(ValueError):
# 	pass

# def foo(s):
# 	n = int(s)
# 	if n == 0 :
# 		raise FooError("invalid value:%s" %s)
# 	return 10 / n

# foo("0")
 
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re

# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html)
# images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})

# for image in images:
# 	print(image["src"])

# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# # html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# html = urlopen("https://i-voce.jp/feed/7204/")
# bsObj = BeautifulSoup(html)

# for link in bsObj.findAll("img"):
# 	if 'src' in link.attrs:
# 		print(link.attrs['src'])


# import socket
# import sys

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = socket.gethostname()

# port = 9999

# s.connect((host,port))

# msg = s.recv(1024)

# s.close()

# print(msg.decode('utf-8'))


from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_STREAM)

while True:
	data = input("fuck")
	if not data:
		break

	udpCliSock.sendto(data,ADDR)
	data,ADDR = udpCliSock.recvfrom(BUFSIZ)

	if not data:
		break

	print(data)

udpCliSock.close()




















































