import cv2

src = cv2.imread("roh.jpg",cv2.IMREAD_UNCHANGED)

scalepercent = 50

newheight = int(src.shape[1]*scalepercent/100)
newwidth = int(src.shape[0]*scalepercent/100)

out = cv2.resize(src,(newheight,newwidth))

cv2.imwrite('resizedimg.jpg',out)
cv2.waitKey(0)