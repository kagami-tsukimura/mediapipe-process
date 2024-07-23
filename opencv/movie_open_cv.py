import cv2

movie_path = "./videos/movie1.mp4"

cap = cv2.VideoCapture(movie_path)

# 動画読み込み失敗時
if not cap.isOpened():
    raise FileNotFoundError(f"動画ファイル {movie_path} が見つかりませんでした。")

while True:
    ret, frame = cap.read()
    # 画像読み込み失敗時
    if not ret:
        break

    # captureしたframeは、画像のため画像処理可能
    resize_frame = cv2.resize(frame, dsize=None, fx=0.5, fy=0.5)

    cv2.imshow("frame", resize_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
