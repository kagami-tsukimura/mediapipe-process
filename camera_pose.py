import time

import cv2

import mediapipe as mp

# MediaPipe Handsモジュールのセットアップ
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5
)


# カメラキャプチャの設定
cap = cv2.VideoCapture(0)

# FPS計測用
prev_frame_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    new_frame_time = time.time()

    # BGR画像をRGBに変換
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 画像を反転 (左右反転)
    image = cv2.flip(image, 1)
    # 処理のパフォーマンスを向上させるために、画像を不可変にする
    image.flags.writeable = False
    # 手のランドマークを検出
    results = hands.process(image)

    # 画像を可変にする
    image.flags.writeable = True
    # RGB画像をBGRに戻す
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 手のランドマークを描画
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS
            )

    # FPSを計算
    if prev_frame_time != new_frame_time:
        fps = 1 / (new_frame_time - prev_frame_time)
    else:
        fps = 0
    prev_frame_time = new_frame_time

    # 画像のサイズを取得
    h, w, _ = image.shape

    # FPSを画像に描画
    cv2.putText(
        image,
        f"FPS: {fps:.2f}",
        (w * 3 // 4, h * 14 // 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
        cv2.LINE_AA,
    )

    # 結果を表示
    cv2.imshow("MediaPipe Hands", image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
