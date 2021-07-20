file = open("clean2_dataproduct.txt", "r")

data = file.read().split("\n")

header = data[0]

products = data[1:]

hang = ["Apple", "Huawei", "Lenovo", "MSI", "HP", "Asus", "Acer", "Dell", "Surface", "LG", "Khác"]

count_daban = [0,0,0,0,0,0,0,0,0,0,0]

for x in range(len(products)):
	products[x] = products[x].split(",")
# có những sp chưa bán dc để "" thay bằng 0 sp
for i in range(len(products)):
	for j in range(len(products[i])):
		if products[i][j] == "" :
			products[i][j] = "0"

# đếm sp đã bán theo hãng
for x in products:
	a = 0
	for i in range(len(hang)) :
		if x[2].find(hang[i]) != -1 or x[2].find(hang[i].lower()) != -1 or x[2].find(hang[i].upper()) != -1:
			count_daban[i] += int(x[13])
			a = 1

	if a == 0:
		count_daban[10] += int(x[13])

# tính trung bình của giamr giá
cout_giamgia = [0,0,0,0,0,0,0,0,0,0,0]
sum_giamgia = [0,0,0,0,0,0,0,0,0,0,0]
for x in products :
	a = 0 
	for i in range(len(hang)) :
		if x[2].find(hang[i]) != -1 or x[2].find(hang[i].lower()) != -1 or x[2].find(hang[i].upper()) != -1:
			cout_giamgia[i] += 1
			sum_giamgia[i] += float(round(int(x[5]) / int (x[4]), 2)) * 100
			a = 1
	if a == 0 :
		cout_giamgia[10] += 1
		sum_giamgia[10] += float(round(int(x[5]) / int (x[4]), 2)) * 100


print(sum_giamgia)
ave_giamgia = []
tb = 0
for i in range(len(cout_giamgia)):
	if cout_giamgia != 0:
		tb = round(sum_giamgia[i] / cout_giamgia[i], 2)
		ave_giamgia.append(round(sum_giamgia[i] / cout_giamgia[i] * 200 / 100, 2))
	else :
		ave_giamgia.append(0)


# draw barchart
import matplotlib.pyplot as plt
import numpy as np

age_label = hang
x = np.arange(11)
y = np.arange(11)

fig, axis = plt.subplots()
plt.bar(x, count_daban)
plt.plot(x, ave_giamgia, color='red', marker='o')
# set limit 
axis.set_ylim(0,200)

# label for column x
plt.xticks(x, age_label)

axis.set_ylabel('Số máy')
axis.set_xlabel("Hãng")

# right side ticks
ax2 = axis.twinx()
ax2.tick_params('y', colors='r')
ax2.set_ylabel("giảm giá (%)")
ax2.set_ylim(0,100)

rects = axis.patches
# Label for barchart
# https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart
labels = count_daban
for rect, label in zip(rects, labels):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 2, label,
            ha='center', va='bottom')

plt.title('Có phải giảm giá nhiều sẽ bán được máy không?')

plt.show()