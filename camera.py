import cv2
import numpy




def get_frame():
    cam=cv2.VideoCapture(0)
    while True:
        sucess, frame = cam.read()
        ret,buffer=cv2.imencode('.jpg', frame)
        frame=buffer.tobytes()

        yield(b'--frame\r\n'
                b'content-Type: image/jpeg\r\n\r\n'+ frame + b'\r\n')
    cam.release()
    cv2.destroyAllWindows()













