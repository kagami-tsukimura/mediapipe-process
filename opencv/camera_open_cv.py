import cv2

cap = cv2.VideoCapture(0)

# 動画読み込み失敗時
if not cap.isOpened():
    raise FileNotFoundError("カメラ映像の読み込みに失敗しました。")

while True:
    ret, frame = cap.read()
    # 画像読み込み失敗時
    if not ret:
        break

    # captureしたframeは、画像のため画像処理可能
    holizontal_frame = cv2.flip(frame, 1)

    # FPSを画面右下に表示
    h, w, _ = holizontal_frame.shape
    cv2.putText(
        holizontal_frame,
        f"FPS: {cap.get(cv2.CAP_PROP_FPS):.2f}",
        (w // 3 * 2, h // 15 * 14),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2,
        cv2.LINE_AA,
    )
    cv2.imshow("frame", holizontal_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
