import cv2
class VideoCamera():
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret, frame = self.video.read()


    
        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tostring()
    # def closeWindows(self):
    #     self.video.release()
    #     cv2.destroyAllWindows()
    #     return True
