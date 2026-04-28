from fer import FER

emotion_detector = FER(mtcnn=False)

def detect_emotions(frame):
    return emotion_detector.detect_emotions(frame)