
import youtube_dl #library

def downloadyoutubeVID():
        user = input("youtube video url: ")


        ydl = youtube_dl.YoutubeDL({'outtmpl': input("Title of video: ")})
        with ydl:
            result = ydl.extract_info(user ,download=True )

            #code

downloadyoutubeVID()
