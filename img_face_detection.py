import cv2
import torch

import mediapipe as mp

# PyTorchがGPUを認識しているか確認
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("CUDA is available. PyTorch can use the GPU.")
    print(f"Number of GPUs: {torch.cuda.device_count()}")
    print(f"Device name: {torch.cuda.get_device_name(0)}")
    print(f"CUDA version: {torch.version.cuda}")
else:
    device = torch.device("cpu")
    print("CUDA is not available. PyTorch will use the CPU.")

# MediaPipe Poseモジュールのセットアップ
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    enable_segmentation=False,
    min_detection_confidence=0.5,
)

# 動画ファイルのパスを指定
video_path = "your_video_file.mp4"  # ここに動画ファイルのパスを指定
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # BGR画像をRGBに変換
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 処理のパフォーマンスを向上させるために、画像を不可変にする
    image.flags.writeable = False
    # 姿勢を推定
    results = pose.process(image)

    # 画像を可変にする
    image.flags.writeable = True
    # RGB画像をBGRに戻す
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 姿勢のランドマークを描画
    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(
            image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
        )

    # GPUメモリの使用量を表示
    if torch.cuda.is_available():
        memory_allocated = torch.cuda.memory_allocated(device) / 1024 / 1024
        memory_reserved = torch.cuda.memory_reserved(device) / 1024 / 1024
        print(f"GPU Memory Allocated: {memory_allocated:.2f} MB")
        print(f"GPU Memory Reserved: {memory_reserved:.2f} MB")

    # 結果を表示
    cv2.imshow("MediaPipe Pose", image)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
