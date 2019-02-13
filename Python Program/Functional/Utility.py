import math
from array import *
import numpy as np
import random
import datetime


def stringReplace():
	str = "Hello <<UserName>>, How are you?"
	name = input("Enter your name : ")
	str = str.replace("<<UserName>>",name)
	print(str)

def leapYear(n):
	if n%100==0:
		if n%400==0:
			print("Year is leap")
		else:
			print("Year is not leap year")
	elif n%4==0:
		print("Year is leap Year")
	else:
		print("Year is not leap year")

def powerOfTwo(power):
	for i in range(power+1):
		if power<=31:
			print(i," is power of 2 is ",int(math.pow(2,i)))
		else:
			print("Range exceeded")

def harmonicValue(n):
	value = 0;
	for i in range(1,n+1):
		value = value+1/n;
	return value;

def isPrime(n):
	for i in range(2,n):
		if(n%i==0):
			return False
	return True

def primeFactor(n):
	print("Prime factor is : ")
	for i in range(2,n):
		print(i)
		if isPrime(i):
			if n%i==0:
				print(i," ")

def sumOfThree(n):
	for i in range(len(n)):
		for j in range(i+1,len(n)):
			for k in range(j+1,len(n)):
				if(n[i]+n[j]+n[k]==0):
					print(n[i]," + ",n[j]," + ",n[k]," = 0")

def euclideanDistance(x,y):
	return (math.sqrt(math.pow(x,x)+math.pow(y,y)))

def rootOfX(a,b,c):
	delta = b*b-4*a*c
	x1 = (b+math.sqrt(abs(delta)))/(2*a)
	x2 = (-b-math.sqrt(abs(delta)))/(2*a)
	# x1 = (5+math.sqrt(delta))/(2*a)
	# x2 = (­-5-math.sqrt(delta))/(2*a)
	return x1,x2

def weather(t,v):
	w = 35.74 + 0.6215*t + (0.4275*t-35.75)*math.pow(v,0.16)
	return w

def getTwoDArr(r,c):
	print("Enter a list : ")
	arr=np.zeros((r,c))
	for i in range(r):
		for j in range(c):
			arr[i][j]=chr(input())
	return arr

def displayTwoDArr(arr):
	print(arr)


def ticTacToe(self):
	arr = np.zeros((3,3))
	player = int(input("If you want to play first then enter 1 else 2. "))
	cnt = 0;
	while cnt<9:
		if player==1:
			print(arr)
			self.player(arr)
			cnt+=1
			player=2
			if self.winCheck(arr,'X')==-1: player = -1
		elif player==2:
			self.computer(arr)
			cnt+=1
			player=1
			if self.winCheck(arr,'O')==-1: player = -1
		else:
				print(arr)
				break;

def player(self,arr):
	print("Enter position with x and y co-ordinate")
	posX, posY = int(input()),int(input())
	while True:
		if arr[posX][posY]==0:
			arr[posX][posY]=ord('X')
			break;
		else:
			print("This position already marked.")
			print(arr)
			self.player()

def computer(self,arr):
	while True:
		posX = random.randrange(0,3,1)
		posY = random.randrange(0,3,1)
		if arr[posX][posY]==0:
			arr[posX][posY]=ord('O')
			break;

def winCheck(self,arr,ch):
	c = ord(ch)
	if (arr[0][0]==c and arr[0][1]==c and arr[0][2]==c) \
		or (arr[1][0]==c and arr[1][1]==c and arr[1][2]==c) \
		or (arr[2][0]==c and arr[2][1]==c and arr[2][2]==c) \
		or (arr[0][0]==c and arr[1][0]==c and arr[2][0]==c) \
		or (arr[0][1]==c and arr[1][1]==c and arr[2][1]==c) \
		or (arr[0][2]==c and arr[1][2]==c and arr[2][2]==c) \
		or (arr[0][0]==c and arr[1][1]==c and arr[2][2]==c) \
		or (arr[0][2]==c and arr[1][1]==c and arr[2][0]==c):
			if ch=='X':
				print("Player won")
				return -1;
			else:
				print("Computer won")
				return -1

def startWatch():
	start = datetime.datetime.now().microsecond
	return start

def stopWatch(start):
	stop = datetime.datetime.now().microsecond
	return stop-start

def swap(str,l,r):
	str = list(str)
	str [l], str[r]=str[r], str[l]
	return ''.join(str)

def permutation(str,l,r):
	if l==r:
		print(str)
	else:
		for i in range(l,r):
			str = swap(str,l,i)
			permutation(str,l+1,r)
			str = swap(str,l,i)

def couponGenerator(n):
	li = [None]*n
	c = random.randrange(100,500,5)
	li[0] = int(c)
	j=0;
	while j<n:
		c = random.randrange(100,500,5)
		for i in range(j):
			if li[i]==c:
					c = random.randrange(100,500,5)
					i=0
		li[j] = int(c)
		j+=1
	return li

def gambler(goal):
	doller=1
	win, loss = 0, 0
	while True:
		n = int(input("You guess some number between 1 to 3"))
		g = random.randrange(1,4,1)
		if n==g:
			doller+=1;
			win+=1
			print("You won this bet.")
		else:
			print("You loss this bet.")
			doller-=1
			loss+=1
		if doller==0:
			print("You loss your all doller.")
			break;
		elif doller==goal:
			print("You achived your goal.")
			break
	# print("Percentage of win : ",((win*100)/win+loss))
	# print("Percentage of loss : ",((loss*100)/win+loss))

def flipCoin(n):
	for i in range(n):
		rand = random.random()
	if rand<0.5:
		print("Percentage of Head : ",int(rand*100))
	else:
		print("Percentage of Tail : ",int(rand*100))		
# 
# Algorithm
# 
def isAnagram(str1,str2):
	if len(str1)==len(str2):
			arr=np.full((len(str2)),False)
			cnt=0
			for i in range(len(str1)):
				for j in range(len(str2)):
					if str1[i]==str2[j] and arr[j]==False:
						arr[j]=True
						cnt+=1
						break
	else:
		return False
	if cnt==len(str1):
		return True

def isPrime(n):
	for i in range(2,n):
		if n%i==0:
			return False
	return True

def isPalindrome(n):
	new = n
	reverse = 0
	while new != 0:
		temp = int(new%10)
		new = int(new/10)
		reverse = (reverse*10)+temp
	if n==reverse:
		return True
	else:
		return False

def getPrimeNumber(rng):
	arr = []
	for i in range(2,rng+1):
		if isPrime(i):
			arr.append(i)
	return arr

def getPalindrome(arr):
	newArr = []
	for i in arr:
		if isPalindrome(i):
			newArr.append(i)
	return newArr

def getAnagram(arr):
	newArr = []
	for i in range(len(arr)-1):
		for j in range(1+i,len(arr)):
			if isAnagram(str(arr[i]),str(arr[j])):
				newArr.append(arr[i])
				newArr.append(arr[j])
	return newArr

def insertionSort(arr):
	for i in range(1,len(arr)):
		j=i-1
		while j>-1:
			if arr[i]<arr[j]:
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp
			j-=1
	return arr

def bubbleSort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-1):
			if(arr[j]>arr[j+1]):
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
	return arr

	