from random import choices
from csv import reader
import datetime as dt



class Worker():
	def __init__(self, ID_prac=None, name=None, lastname=None, ID_zesp=None, date=None):
		self.ID_prac = ID_prac
		self.name = name
		self.lastname = lastname
		self.ID_zesp = ID_zesp
		self.date = date
		self.sex = None

	def __repr__(self):
		self.data = [self.ID_prac, self.name, self.lastname, self.ID_zesp, self.date]
		return f"{self.data}"

	def draw_sex(self):
		self.sex = choices(["male", "female"], weights=[0.4, 0.6], k=1)[0]

	def draw_person(self):
		if self.sex == None:
			self.draw_sex()
		if self.sex == "male":
			name_file = "male_names.csv"
			lastname_file = "male_lastname.csv"
		else:
			name_file = "female_names.csv"
			lastname_file = "female_lastname.csv"
		with open(name_file, encoding="utf8") as f:
			csv_reader = reader(f)
			next(csv_reader) # to skip headers
			data = [row for row in csv_reader]
			names = [name[0] for name in data]
			weights = [float(weight[2]) for weight in data]
			self.name = choices(names, weights=weights, k=1)[0]
		with open(lastname_file, encoding="utf8") as f:
			csv_reader = reader(f)
			next(csv_reader) # to skip headers
			data = [row for row in csv_reader]
			lastnames = [lastname[0] for lastname in data]
			weights = [float(weight[1]) for weight in data]
			self.lastname = choices(lastnames, weights=weights, k=1)[0]
			
	def edit_name(self,name):
		self.name = name
		
	def edit_lastname(self,lastname):
		self.lastname = lastname

	def edit_ID_prac(self,ID_prac):
		self.ID_prac = ID_prac

	def edit_ID_zesp(self,ID_zesp):
		self.ID_zesp = ID_zesp

class Workers():
	def __init__(self, workers=[]):
		self.workers = workers

	def amount(self):
		return len(self.workers)

	def __repr__(self):
		return f"The table represents a data of {self.amount()} workers"

	def add_worker(self, name, lastname, ID_zesp=None):
		ID_prac = self.amount()+1
		date = dt.date.today()
		worker = Worker(ID_prac,name,lastname,ID_zesp,date)
		self.workers.append(worker)
		

	def add_random_worker(self):
		ID_prac = self.amount()+1
		date = dt.date.today()
		ID_zesp = choices([1,2,3,4,5], k=1)[0]
		worker = Worker(ID_prac,None,None,ID_zesp,date)
		worker.draw_person()
		self.workers.append(worker)
		

	def add_random_workers(self, amount):
		for i in range(amount):
			self.add_random_worker()
			



pracownicy = Workers()
pracownicy.add_worker("Piotr","Kuc",5)
pracownicy.add_worker("Kamil","Zdun",3)
print(pracownicy.workers)
pracownicy.add_random_worker() 
print(pracownicy.workers)

pracownicy.add_random_workers(5) 
print(pracownicy.amount())
print(pracownicy.workers)


# worker_first = Worker()
# print(worker_first)
# worker_first.draw_person()
# print(worker_first)
# worker_first.edit_name("Bill")
# print(worker_first)
