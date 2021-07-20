file = open("clean2_dataproduct.txt", "r")

data = file.read().split("\n")

header = data[0]

products = data[1:]

hang = ["Apple", "Huawei", "Lenovo", "MSI", "HP", "Asus", "Acer", "Dell", "Surface", "LG", "Khác"]

count_daban = [0,0,0,0,0,0,0,0,0,0,0]

for x in range(len(products)):
	products[x] = products[x].split(",")

for i in range(len(products)):
	for j in range(len(products[i])):
		if products[i][j] == "" :
			products[i][j] = "0"


for x in products:
	a = 0
	for i in range(len(hang)) :
		if x[2].find(hang[i]) != -1 or x[2].find(hang[i].lower()) != -1 or x[2].find(hang[i].upper()) != -1:
			count_daban[i] += int(x[13])
			a = 1

	if a == 0:
		count_daban[10] += int(x[13])

# draw barchart
import matplotlib.pyplot as plt
import numpy

figure, axis = plt.subplots()



y_pos = numpy.arange(len(hang))

plt.bar(y_pos, count_daban)
plt.xticks(y_pos, hang)

axis.set_ylim(0,200)

plt.ylabel('Số máy ') 
plt.title('Số lượng máy đã bán theo hãng trên tiki')

rects = axis.patches

for rect,labe1 in zip(rects, count_daban):
	height = rect.get_height()
	axis.text(rect.get_x() + rect.get_width() / 2, height + 0, labe1, ha='center', va='bottom')
	

plt.show()


# print(count_daban)
# print(products[0][13])
# print(products[212][13])
# print(len(products[0]))


