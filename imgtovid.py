from cv2 import VideoWriter, imread, destroyAllWindows
import os

videoFps = 5
currentDirr = os.path.dirname(os.path.realpath(__file__))
image_folder = currentDirr
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = VideoWriter(video_name, 0, videoFps, (width,height))

for image in images:
    video.write(imread(os.path.join(image_folder, image)))

destroyAllWindows()
video.release()
