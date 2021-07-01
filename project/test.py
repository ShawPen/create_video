import sys

sys.path.append("../lib/")
from pydub import AudioSegment
from moviepy.editor import concatenate_videoclips, CompositeAudioClip, VideoFileClip, AudioFileClip
import cv2
import os


#将图片转换为视频
def video(path):
    back_pics = os.listdir('input/back/') 
    fileNames = os.listdir(path)
    # 读取时序图中的第一张图片
    img = cv2.imread(path + fileNames[0])
    # 设置每秒读取多少张图片
    fps = 0.5
    imgInfo = img.shape

    # 获取图片宽高度信息
    size = (imgInfo[1], imgInfo[0])
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")

    # 定义写入图片的策略
    videoWrite = cv2.VideoWriter('./video/output.mp4', fourcc, fps, size)

    for fileName in fileNames:
        # 读取所有的图片
        img = cv2.imread(path + '/' + fileName)
        img = cv2.resize(img, size)
        # 将图片写入所创建的视频对象
        videoWrite.write(img)
    
    for back_pic in back_pics:#背景图片
        img = cv2.imread('input/back/'+back_pic)
        img = cv2.resize(img,size)
        videoWrite.write(img)
    videoWrite.release()

#添加音频文件
def create_video(videoFile):
    
    video = VideoFileClip(videoFile)  # 读入视频文件
    t = int(video.duration)
    audioFile = os.getcwd()+'/audio/backgrund_music.mp3'#音频目录
    new_audioFile = r'./audio/new_backgrund_music.mp3'#存放剪切的音频文件
   # mp3 = AudioSegment.from_mp3(audioFile)  # 打开mp3文件
   # mp3[3 * 1000:(t + 4) * 1000].export(new_audioFile, format="mp3")  # 切割前t+1秒并覆盖保存
    
    
    audio = AudioFileClip(audioFile)#音频
    audio1 = audio.subclip(3,t+4)
   # audio1.write_audiofile('new.mp4')

    audio = AudioFileClip(new_audioFile)#音频

    video = video.set_audio(audio1)

    video.write_videofile('./video/with_audio.mp4',audio_codec='aac')#第一个参数为保存的位置
    
   
def app_fun():
    videoFile = r'./video/output.mp4'
    path = './input/img/'
    video(path)
    create_video(videoFile)
    
if __name__=='__main__':
    app_fun()
