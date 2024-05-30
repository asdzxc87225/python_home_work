import cv2
import numpy as np

class ImageProcessor:
    def __init__(self, img_path):
        self.img_original = cv2.imread(img_path)
        self.low = np.array([0, 0, 221])  # HSV lower bound
        self.high = np.array([185, 30, 255])  # HSV upper bound

    def gray_binary(self, img, x):  # 閥值控制+灰階二值化
        ret, mask250 = cv2.threshold(img, x, 255, cv2.THRESH_BINARY)
        return mask250

    def blurred(self, img, y):  # 高斯模糊
        output1 = cv2.GaussianBlur(img, (y, y), 0)
        return output1

    def color_binary(self, img, x, y):  # 全彩影像二值化(目前只能用白底的圖片)
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask_g = cv2.inRange(img_hsv, x, y)
        return mask_g

    def dilation(self, img, x):  # 膨脹操作
        kernel = np.ones((x, x), np.uint8)
        dst = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        return dst

    def get_img_channels(self):
        img_shape = self.img_original.shape
        if len(img_shape) == 2:
            img_bir = self.gray_binary(self.img_original, 200)
        elif len(img_shape) == 3:
            img_bir = self.color_binary(self.img_original, self.low, self.high)
        return img_bir

    def process(self):
        img_binary = self.get_img_channels()
        img_blurred = self.blurred(self.img_original, 25)
        img_dilation = self.dilation(img_binary, 5)
        
        return self.img_original, img_binary, img_blurred, img_dilation

# 使用範例
processor = ImageProcessor('66666666666666666.jpg')
img_original, img_binary, img_blurred, img_dilation = processor.process()

cv2.imshow('img_original', img_original)
cv2.imshow('img_binary', img_binary)
cv2.imshow('img_blurred', img_blurred)
cv2.imshow('img_dilation', img_dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
