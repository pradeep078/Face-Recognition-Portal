import face_recognition
import cv2
import os
import os.path


from tkinter import *

root = Tk()
root.geometry("300x300+1100+0")
from PIL import Image,ImageTk
     

def cap_fn():
     global img_name
     cam = cv2.VideoCapture(0)
     while True:
          ret, frame = cam.read()
          cv2.imshow("camera", frame)
          if not ret:
               break
          k = cv2.waitKey(1)

          if k%256 == 27:
             print("Escape hit, closing...")
             break
          elif k%265==32:
               img_name=input("enter file name:")
               img_name=img_name+".png"
               cv2.imwrite(os.path.join('C:/Users/Lenovo/Desktop/project/image/' , img_name), frame)
               print("{} written!".format(img_name))
     cam.release()
     cv2.destroyAllWindows()
     
def show_fn():
     img=Image.open('C:/Users/Lenovo/Desktop/project/image/'+img_name)
     img = img.resize((100, 100), Image.ANTIALIAS) #The (250, 250) is (height, width)
     img = ImageTk.PhotoImage(img) # convert to PhotoImage
     canvas = Canvas(root,height=100,width=100)
     canvas.image = img  # <--- keep reference of your image
     canvas.create_image(0,0,anchor='nw',image=img)
     canvas.place(x=160,y=50)

global ent1
lab1=Label(root,text="enter the image name:",font=("bold",13)).place(x=40,y=250)
val1=StringVar()
ent1=Entry(root,textvariable=val1,width=15,bg="white",font=("bold",13))
ent1.place(x=40,y=170)

          
def det_fn():
     s=val1.get()
     video_capture=cv2.VideoCapture(0)
     img_name=s
     if(os.path.exists('C:/Users/Lenovo/Desktop/project/image/'+img_name+'.png')):
          my_image=face_recognition.load_image_file('C:/Users/Lenovo/Desktop/project/image/'+img_name+".png")
          my_encoding=face_recognition.face_encodings(my_image)[0]
          known_face_names=[img_name]
          known_face_encodings=[my_encoding]
          def fun_call():
               print("hello "+img_name)
          def fun_go():
               print("not identified")
          while(True):
               ret,frame=video_capture.read()
               rgb_frame=frame[:,:,::-1]
               face_locations=face_recognition.face_locations(rgb_frame)
               face_encodings=face_recognition.face_encodings(rgb_frame,face_locations)
               for (top,right,bottom,left),face_encodings in zip(face_locations,face_encodings):
                     match=face_recognition.compare_faces(known_face_encodings,face_encodings)
                     name="unknown"
                     if True in match:
                           first_match_index = match.index(True)
                           name = known_face_names[first_match_index]
                           fun_call()
                     else:
                         fun_go()
               
                     cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),3)
                     font = cv2.FONT_HERSHEY_DUPLEX
                     cv2.putText(frame,name,(left+6,bottom),font,1.0,(0,0,255),1)
               cv2.imshow("Face Recognition",frame)
               cv2.waitKey(1)
          video_capture.release()
          cv2.destroyAllWindows()
     else:
        print(img_name+" does not exist")


     
     

cam_button= Button(root, text="Capture", fg="red",command=cap_fn).place( x=10,y=10)

show_button= Button(root, text="Show image", fg="red",command=show_fn).place( x=180,y=10)

id_button=Button(root,text="detect",fg="red",command=det_fn).place(x=75,y=200)




root.mainloop()



