import cv2
import tensorflow as tf

import mediapipe as mp

# TensorFlowがGPUを認識しているか確認
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices("GPU")))

# MediaPipe Handsモジュールのセットアップ
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5
)

# カメラキャプチャの設定
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

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

    # GPUメモリの使用量を表示
    gpus = tf.config.experimental.list_physical_devices("GPU")
    if gpus:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices("GPU")
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
        for gpu in logical_gpus:
            memory_info = tf.config.experimental.get_memory_info(gpu.name)
            print(f"GPU Memory Usage: {memory_info['current'] / 1024 / 1024} MB")

    # 結果を表示
    cv2.imshow("MediaPipe Hands", image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
