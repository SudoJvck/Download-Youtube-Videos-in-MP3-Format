import pytube
import os

myVideo = pytube.YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))

video = myVideo.streams.filter(only_audio=True).first()

print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(myVideo.title + " has been successfully download in .mp3 format.")
