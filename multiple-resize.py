import os
import cv2

path = os.getcwd()
list_image = os.listdir(os.path.join(path, 'multi-resize')) #Check file
print(list_image)

for img in list_image:
    image_path   = os.path.join(path, 'multi-resize', img)
    image_resize = cv2.imread(image_path, cv2.IMREAD_COLOR)
    resize       = cv2.resize(image_resize, (0, 0), fx = 0.5, fy = 0.5)
    newfile      = 'resized_' + img   #Naming new files
    save_loc     = os.path.join(path, 'multi-resize', newfile)
    cv2.imwrite(save_loc, resize)