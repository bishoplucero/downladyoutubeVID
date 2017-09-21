# Hello, Bishop. This is David speaking.
# From whatever means necessary,
# I want you to code a program that downloads a video
# from youtube.
# HINTS:
# Stackoverflow and StackExchange
# youtube-dl
# pip3 install <program>
#
# Good luck my dude.
# Code the code underneath here and upload it to your
# GitHub page when you complete and just tell me!

import youtube_dl #library

def downloadyoutubeVID():
        user = input("youtube video url: ")


        ydl = youtube_dl.YoutubeDL({'outtmpl': input("Title of video: ")})
        with ydl:
            result = ydl.extract_info(user ,download=True )

            #code

downloadyoutubeVID()
