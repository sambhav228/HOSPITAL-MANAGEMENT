class CircularQueue(): 
def __init__(self, size): # initializing the class 
		self.size = size 
		self.queue = [None for i in range(size)] 
		self.front = self.rear = -1
def enqueue(self, data):  
		if ((self.rear + 1) % self.size == self.front): 
			print(" FILE IS FULL\n")  
		elif (self.front == -1): 
			self.front = 0
			self.rear = 0
			self.queue[self.rear] = data 
		else: 
	 		self.rear = (self.rear + 1) % self.size 
			self.queue[self.rear] = data 
	def dequeue(self): 
		if (self.front == -1): # codition for empty queue 
			print ("FILE is Empty\n")  
		elif (self.front == self.rear): 
			temp=self.queue[self.front] 
			self.front = -1
			self.rear = -1
			return temp 
		else: 
temp = self.queue[self.front] 
			self.front = (self.front + 1) % self.size 
			return temp 
def display(self): 
		print("AFTER ENTERING NEW PATIENT ID. NO: ")
		if(self.front == -1): 
			print ("FILE is Empty") 
elif (self.rear >= self.front):
			print("ID.NUMBER in the FILE are:", end = " ") 
			for i in range(self.front, self.rear + 1): 
				print(self.queue[i], end = " ") 
			print () 
else: 
			print ("ID.NUMBER in FILE are:", end = " ") 
			for i in range(self.front, self.size): 
				print(self.queue[i], end = " ") 
			for i in range(0, self.rear + 1): 
				print(self.queue[i], end = " ") 
			print () 
if ((self.rear + 1) % self.size == self.front): 
			print("FILE is Full")
print("***********************************************")
print("             HOSPITAL MANAGEMENT               ")
print("***********************************************")
print("PATIENT'S DETAILS: ")
name =input("Enter patient name :")
print(name)
dis=input("Enter patient  disease name :")
print(dis)
date=input("Enter Date of Registration :")
print(date)
ID=input("Enter patient ID number :")
print(ID)
city = input("Enter patient city name :")
print(city)
state= input("Enter patient state name: ")
print(state)
ob = CircularQueue(5) 
ob.enqueue(748712) 
ob.enqueue(2398654) 
ob.enqueue(812495) 
ob.enqueue(ID) 
ob.display() 
print ("Deleted Patient ID = ", ob.dequeue()) 
print ("Deleted Patient ID = ", ob.dequeue()) 
ob.display() 
ob.enqueue(735236) 
ob.enqueue(226573) 
ob.enqueue(880980) 
ob.display()
