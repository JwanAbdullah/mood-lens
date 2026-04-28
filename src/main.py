import cv2
import os
from detector import detect_emotions

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMOJI_DIR = os.path.join(BASE_DIR, "assets", "emojis")

EMOJI_MAP = {
    "angry": "angry.png",
    "happy": "happy.png",
    "sad": "sad.png",
    "surprise": "surprise.png",
    "winked": "wink.png",
    "fear": "surprise.png",
    "disgust": "angry.png",
}

def load_emoji(emotion):
    filename = EMOJI_MAP.get(emotion, "wink.png")
    path = os.path.join(EMOJI_DIR, filename)
    return cv2.imread(path, cv2.IMREAD_UNCHANGED)

def overlay_image(background, overlay, x, y, width, height):
    if overlay is None:
        return background

    overlay = cv2.resize(overlay, (width, height))

    if overlay.shape[2] == 4:
        alpha = overlay[:, :, 3] / 255.0
        overlay_rgb = overlay[:, :, :3]
    else:
        alpha = 1
        overlay_rgb = overlay

    h, w = overlay_rgb.shape[:2]

    if x < 0 or y < 0 or x + w > background.shape[1] or y + h > background.shape[0]:
        return background

    for c in range(3):
        background[y:y+h, x:x+w, c] = (
            alpha * overlay_rgb[:, :, c]
            + (1 - alpha) * background[y:y+h, x:x+w, c]
        )

    return background

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    print("Camera could not be opened.")
    exit()

while True:
    success, frame = camera.read()

    if not success:
        break

    results = detect_emotions(frame)

    for result in results:
        x, y, w, h = result["box"]
        emotions = result["emotions"]

        top_emotion = max(emotions, key=emotions.get)
        confidence = emotions[top_emotion]

        emoji = load_emoji(top_emotion)

        emoji_size = w
        emoji_x = x
        emoji_y = y - emoji_size - 10

        if emoji_y < 0:
            emoji_y = y + h + 10

        frame = overlay_image(frame, emoji, emoji_x, emoji_y, emoji_size, emoji_size)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.putText(
            frame,
            f"{top_emotion} {confidence:.2f}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Mood Lens", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

frame_count = 0
last_results = []

while True:
    success, frame = camera.read()
    if not success:
        break

    frame_count += 1

    if frame_count % 10 == 0:
        small_frame = cv2.resize(frame, (320, 240))
        last_results = detect_emotions(small_frame)

        # scale boxes back up
        for result in last_results:
            x, y, w, h = result["box"]
            result["box"] = [x * 2, y * 2, w * 2, h * 2]

    results = last_results