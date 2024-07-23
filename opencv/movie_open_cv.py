import cv2

movie_path = "./videos/movie1.mp4"

cap = cv2.VideoCapture(movie_path)
if not cap.isOpened():
    raise FileNotFoundError(f"動画ファイル {movie_path} が見つかりませんでした。")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
