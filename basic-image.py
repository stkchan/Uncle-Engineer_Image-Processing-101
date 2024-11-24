import os
import cv2

path = os.getcwd()

img_path = os.path.join(path, 'img', 'cat.jpg') #Find Path of Image files
img_cat = cv2.imread(img_path, cv2.IMREAD_COLOR)
print(img_cat.shape)
# print(img_path)

# resize = cv2.resize(img_cat, (400, 300)) #Resize image
# resize = cv2.resize(img_cat, (0, 0), fx = 0.5, fy = 0.5) #Resize image

#219,42 & 938,499   
cropped = img_cat[44:499, 219:938] #Crop image

save_loc = os.path.join(path, 'img', 'cat-cropped.jpg')
cv2.imwrite(save_loc, cropped) #Save file

# cv2.imshow('image', img_cat)
# cv2.imshow('image', cropped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()