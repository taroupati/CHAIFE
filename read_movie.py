import cv2

video = cv2.VideoCapture("movie/test.mp4")

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (width, height)

frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

for i in range(frame_count):
    ret, frame = video.read()
    # 類似度を計算する関数呼び出し
    # 該当するフレームならリストに保存