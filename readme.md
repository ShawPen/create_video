只能在linux系统上运行
audio:音频文件夹

​		backgrund_music.mp3（原始音频）

​		new_backgrund_music.mp3（剪切后的音频）

video:视频文件夹（通过图片生成视频的文件夹和合并音频的文件夹）

​		output.mp4(图片生成的视频)

​		with_audio.mp4(视频加上音频)			

input:读入图片文件

​		img:人脸图片存放的位置

​		back：最后三张图存放位置

两个可执行文件为工具文件，想放在一个文件夹下的，但是出错了

create_video.py为python文件，首先删除<code>if __name__=='__main_':</code>，调用app_fun函数即可。
