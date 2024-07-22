import time

import cv2
import torch
from ultralytics import YOLO

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
video_path = "../../Downloads/test.mp4"  # ここに動画ファイルのパスを指定
cap = cv2.VideoCapture(video_path)

# YOLOv8モデルの読み込み
model = YOLO("yolov8s.pt")

# FPS計測用
prev_frame_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    new_frame_time = time.time()

    # YOLOv8でトラッキング
    results = model.track(frame, persist=True)
    result = results[0]

    # 推論結果からbboxの座標取得
    boxes = result.boxes.xyxy.cpu().numpy().astype(int)

    # BGR画像をRGBに変換
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 各bboxごとに姿勢推定を行い、結果を描画
    for bbox in boxes:
        x1, y1, x2, y2 = bbox
        # バウンディングボックスで切り出し
        person_roi = image[y1:y2, x1:x2].copy()

        # 姿勢を推定
        person_roi_rgb = cv2.cvtColor(person_roi, cv2.COLOR_RGB2BGR)
        person_roi_rgb.flags.writeable = False
        pose_results = pose.process(person_roi_rgb)
        person_roi_rgb.flags.writeable = True

        # 姿勢のランドマークを描画
        if pose_results.pose_landmarks:
            # 描画用に変換
            person_roi_bgr = cv2.cvtColor(person_roi_rgb, cv2.COLOR_RGB2BGR)
            mp.solutions.drawing_utils.draw_landmarks(
                person_roi_bgr, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS
            )
            # 切り出した領域を元の画像に戻す
            image[y1:y2, x1:x2] = person_roi_bgr

    # RGB画像をBGRに戻す
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

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
        image_bgr,
        f"FPS: {fps:.2f}",
        (w * 4 // 5, h * 14 // 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
        cv2.LINE_AA,
    )

    # # GPUメモリの使用量を表示
    # if torch.cuda.is_available():
    #     memory_allocated = torch.cuda.memory_allocated(device) / 1024 / 1024
    #     memory_reserved = torch.cuda.memory_reserved(device) / 1024 / 1024
    #     print(f"GPU Memory Allocated: {memory_allocated:.2f} MB")
    #     print(f"GPU Memory Reserved: {memory_reserved:.2f} MB")

    # 結果を表示
    cv2.imshow("MediaPipe Pose", image_bgr)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
