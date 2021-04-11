import cv2
import numpy as np
import matplotlib.pyplot as plt
def plotter(path):
	img = cv2.imread(path)
	#print(path)
	edges=cv2.Canny(img,100,255)
	edges = cv2.rotate(edges, cv2.ROTATE_90_CLOCKWISE)
	#edges = cv2.flip(edges, 0)

	#plt.savefig(r'C:\Users\HP\Downloads\newer.png')
	indices=np.where(edges != [0])
	print(indices[0])
	coordinates=zip(indices[0],indices[1])
	#print(list(coordinates))
	mytext = list(zip(indices[1], indices[0]))
	#np.savetxt('C:/Users/HP/Downloads/file_numped.txt', mytext ,fmt="%i %5.2f")


	scale_percent = 100 # percent of original size
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	edges=cv2.Canny(resized,100,255)
	edges = cv2.rotate(edges, cv2.ROTATE_90_CLOCKWISE)
	indices=np.where(edges != [0])
	coordinates=zip(indices[0],indices[1])

	mytext = list(zip(indices[0], indices[1]))
	#np.savetxt('C:/Users/HP/Downloads/file_numpedsize.txt', mytext ,fmt="%i %5.2f")
	j = len(mytext)
	listed = []
	listedx=[]
	listedy=[]

	for i in range(j):
	    listedx.append(mytext[i][0])
	    listedy.append(mytext[i][1])
	Stringy =  ' '.join(map(str, listedx))
	xcordinates = str(listedx)
	ycordinates = str(listedy)
	plt.scatter(listedx,listedy,s=0.05)
	plotval = plt.scatter(listedx,listedy,s=0.05)
	plt.show()
	print(mytext)
	return [listedx,listedy]

	



