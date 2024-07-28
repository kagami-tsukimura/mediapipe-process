import cv2

import openpifpaf

# 動画ファイルのパスを指定
video_path = "path/to/your/video.mp4"  # ここに動画ファイルのパスを指定
cap = cv2.VideoCapture(video_path)

# OpenPifPafの推論器をセットアップ
predictor = openpifpaf.Predictor(checkpoint="shufflenetv2k16")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # フレームをRGBに変換
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # OpenPifPafで姿勢推定
    predictions, gt_anns, meta = predictor.numpy_image(rgb_frame)

    # 結果を描画
    for ann in predictions:
        keypoints = ann.data
        for i in range(0, len(keypoints), 3):
            x, y, confidence = keypoints[i : i + 3]
            if confidence > 0.5:
                cv2.circle(frame, (int(x), int(y)), 3, (0, 255, 0), -1)

    # フレームを表示
    cv2.imshow("OpenPifPaf Pose Estimation", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESCキーで終了
        break

cap.release()
cv2.destroyAllWindows()
