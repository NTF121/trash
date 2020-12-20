import random
import time
import string

class timecounter(object):
	def __init__(self):
		self.start = time.time()
	def stop(self):
		print("Время " + str(time.time() - self.start))
		return time.time() - self.start
class main_array(object):
	m_array = []
	def create_array(iteration):
		t = timecounter()
		main_array.m_array.clear()
		for i in range(0,iteration):
			main_array.m_array.append(random.randint(0,iteration-1))
		print(main_array.m_array)
		t.stop()
	def create_text_array(letters,iteration):
		t = timecounter()
		main_array.m_array.clear()
		for i in range(0,iteration):
			main_array.m_array.append("".join(random.choice(string.ascii_letters) for j in range(0,letters-1)))
		print(main_array.m_array)
		t.stop()
class sort(object):
	def __init__(self, array_to_sort):
		self.count_array = []
		self.srt_arr = []
		self.srt_arr = array_to_sort
	def sort_count(self):
		self.count_array.clear()
		t = timecounter()
		for i in range(0,len(self.srt_arr)):
			self.count_array.append(0)
		for i in range(0,len(self.srt_arr)):
			self.count_array[self.srt_arr[i]] += 1
		print("Веса " + str(self.count_array) + "\n")
		self.srt_arr.clear()
		for i in range(0,len(self.count_array)):
			for x in range(0,self.count_array[i]):
				self.srt_arr.append(i)
		print("Результат " + str(self.srt_arr))
		t.stop()
		return self.srt_arr
	def sort2(self):
		t = timecounter()
		self.srt_arr.sort()
		print(self.srt_arr)
		t.stop()
		return self.srt_arr
	def sort_text(self):
		timec = timecounter()
		self.bucket_array = [[] for i in range(0,len(string.ascii_letters))]
		for i in range(len(max(self.srt_arr, key=len)),0,-1):
			self.bucket_array.clear()
			self.bucket_array = [[] for x in range(0,len(string.ascii_letters))]
			for x in self.srt_arr:
				self.bucket_array[list(string.ascii_letters).index(x[i-1])].append(x)
			self.srt_arr.clear()
			# print(self.bucket_array)
			for x in range(0,len(self.bucket_array)):
				for y in self.bucket_array[x]:
					self.srt_arr.append(y)
		print()
		print("Результат " + str(self.srt_arr))
		timec.stop()
		return self.srt_arr
class inputt(object):
	def __init__(self):
		inputtt = input("Введите комманду ")
		if inputtt == "создать":
			main_array.create_array(int(input("Число элементов ")))
		elif inputtt == "создать текст":
			main_array.create_text_array(int(input("Сколько букав ")),int(input("Число элементов ")))
		elif inputtt == "сорт":
			s = sort(main_array.m_array)
			s.sort_count()
		elif inputtt == "сорт текст":
			s = sort(main_array.m_array)
			s.sort_text()
		elif inputtt == "сорт2":
			s = sort(main_array.m_array)
			s.sort2()
		else:
			exit()
while True:
	inputt()