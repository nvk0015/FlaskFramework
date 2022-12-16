from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
cam = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = cam.read()
        if not success:
            break
        else:
            # when an image is sent from backend to frontend it should be encoded and sent in this buffer format. 
            ret, buffer = cv2.imencode('.jpg', frame)
            frame=buffer.tobytes()

        #yield keyword is used instead of return to iterate around the frame object and output multiple frames. 
        # to post the image which is in form of byte it is formatted this way, from OpenCV docc.
        yield(b'--fram\r\n'
                b'Content- Type: image/jpeg\r\n\r\n' + frame +b'\r\n')




@app.route('/')
def index():
    return render_template('CamIndex.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace;boundary=frame')



if __name__=='__main__':
    app.run(debug=True)

