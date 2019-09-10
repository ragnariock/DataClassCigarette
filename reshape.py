import re
import os
import cv2

num = 1

width = 800
height = 800
dim = (width, height)


for root, dirs, files in os.walk(".", topdown=False):
	for name in files:
		print(os.path.join(root, name))
		nameImage = os.path.join(root,name)
		nameImage = str(nameImage)
		name_root = str(root)
		if re.search(r'all',name_root):
			if re.search(r'jpg',nameImage) or re.search(r'png',nameImage):
				img = cv2.imread(nameImage)

				cv2.imwrite('vape/'+str(num) + '.jpg', img )
				num +=1

print(num)
