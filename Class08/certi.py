import cv2
import matplotlib.pyplot as plt

def generate_certi(img,name) :
    coordinates = (700,750)
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img,name,coordinates,font,4.6,(0,0,0),10)
    return img

def save_img(img,name) :
    path = "Generated_Certi.png"
    print(cv2.imwrite(path,img))

def plot_img(img) :
    plt.imshow(img)
    plt.show()

img = cv2.imread("https://png.pngtree.com/back_origin_pic/04/47/51/867e8d6b2125e82e10e1329277db8bfd.jpg")
name = input("Enter Your Name")
generate_certi(img,name)
save_img(img,name)
plot_img(img)