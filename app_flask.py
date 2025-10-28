
from flask import Flask, render_template, Response
import cv2
import torch

app = Flask(__name__)
camera = cv2.VideoCapture(0)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            results = model(frame)
            _, buffer = cv2.imencode('.jpg', results.render()[0])
            frame = buffer.tobytes()
            yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
