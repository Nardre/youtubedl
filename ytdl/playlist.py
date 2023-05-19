#!/bin/python3

import youtube_dl
def download_ytvid_as_mp3(video_url):
    # video_url = input("enter url of youtube video:")
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Download complete... {}".format(filename))

liens = []
with open("lien.txt", "r+") as file:
    for line in file:
        if line.strip() != '':
            liens += [line.strip()]
    file.close()

for i in range(len(liens)):
    print(f"{i+1}/{len(liens)}: ")
    download_ytvid_as_mp3(liens[i])


