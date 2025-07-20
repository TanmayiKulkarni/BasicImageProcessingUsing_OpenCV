import cv2

# 1. Read an image
image = cv2.imread("C:\\Users\\hp\\Downloads\\demo1.jpg")
#2 display image
cv2.imshow('original image',image)
cv2.waitKey(0)


#3 save image
cv2.imwrite('saved_image.jpg', image)

# 4. Resize the image
resized_image = cv2.resize(image, (700, 500))
cv2.imshow('4. Resized Image (700x500)', resized_image)
cv2.waitKey(0)

flipped_image = cv2.flip(image, -1)
cv2.imshow('5. Flipped Image (Horizontal)', flipped_image)
cv2.waitKey(0)

# 6. Crop the image (e.g., top-left 100x100)
cropped_image = image[0:300,0:300]
cv2.imshow('6. Cropped Image (Top-left 100x100)', cropped_image)
cv2.waitKey(0)
# 7. Convert to Gray
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('7. Gray Image', gray_image)
cv2.waitKey(0)
hsv_img=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV image ',hsv_img)
cv2.waitKey(0)

# 8. Enhance contrast
enhanced_image = cv2.convertScaleAbs(image, alpha=1.5)
cv2.imshow('8. Contrast Enhanced Image', enhanced_image)
cv2.waitKey(0)

cv2.destroyAllWindows()