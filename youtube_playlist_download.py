from email.mime import audio
import time
from pytube import Playlist
from moviepy.editor import *
import os,sys


def videodownload():
    
    playlistLink = input("Enter the link (Please, make sure it is correct.):")
    if playlistLink.__contains__("https://www.youtube.com/playlist?list="):    
        playlist = Playlist(playlistLink)
        if len(playlist.video_urls) == 0:
            print("Please enter a valid link")
            videodownload()
        CHECK_FOLDER = os.path.isdir("./Videos")
        if not CHECK_FOLDER:
            os.mkdir("./Videos")

        download_folder = "./Videos/"
        konum = input("Enter Folder Link:")
        download_folder += konum
        CHECK_FOLDER = os.path.isdir(download_folder)

        if not CHECK_FOLDER:
            os.mkdir(download_folder)
            print("Videos will be downloaded to  ", download_folder)

        else:
            print(download_folder, " Already exist!")
            print("Try Again")
            time.sleep(1)
            videodownload()

        print("Total Video Count: ", len(playlist.video_urls))    

        print("\n\n Youtube Videos Link \n")

        for url in playlist.video_urls:
            print(url)

        for video in playlist.videos:
            print('Downloading : {} with url : {}'.format(video.title, video.watch_url))
            video.streams.\
                filter(type='video', progressive=True, file_extension='mp4').\
                order_by('resolution').\
                desc().\
                first().\
                download(download_folder)
        print("Process Completed. Videos Downloaded To"+download_folder)
        time.sleep(1)
        menu()
    else:
        print("Please enter a valid link")
        videodownload()

def audiodownload():
    
    playlistLink = input("Enter the link (Please, make sure it is correct.):")
    if playlistLink.__contains__("https://www.youtube.com/playlist?list="):   
        playlist = Playlist(playlistLink)
        if len(playlist.video_urls) == 0:
            print("Please enter a valid link")
            audiodownload()
        CHECK_FOLDER = os.path.isdir("./Songs")
        if not CHECK_FOLDER:
            os.mkdir("./Songs")

        download_folder = "./Songs/"
        konum = input("Enter Folder Link:")
        download_folder += konum
        CHECK_FOLDER = os.path.isdir(download_folder)

        if not CHECK_FOLDER:
            os.mkdir(download_folder)
            print("Videos will be downloaded to ", download_folder)

        else:
            print(download_folder, " Already exist!")
            print("Try Again")
            time.sleep(1)
            audiodownload()

        print("Total Video Count: ", len(playlist.video_urls))    

        print("\n\n Youtube Songs Link\n")

        for url in playlist.video_urls:
            print(url)

        for video in playlist.videos:
            print('Downloading : {} with url : {}'.format(video.title, video.watch_url))
            audio = video.streams.filter(only_audio=True).first()
            audio.download(download_folder)
        for filename in os.listdir(download_folder):
                infilename = os.path.join(download_folder,filename)
                if not os.path.isfile(infilename): continue
                oldbase = os.path.splitext(filename)
                newname = infilename.replace('.mp4', '.mp3')
                output = os.rename(infilename, newname)
        print("Process Completed. Videos Downloaded To"+download_folder)
        time.sleep(1)
        menu()
        
    else:
        print("Please enter a valid link")
        audiodownload()
    
def menu():
    os.system('cls')
    print("************ YouTube Download Manager **************")
    print()

    choice = input("""
            A or 1: YouTube PlayList Download(video)
            B or 2: YouTube PlayList Download(audio)
            Q: Quit
        Please enter your choice: """)

    if choice == "A" or choice == "a" or choice == "1":
        os.system('cls')
        videodownload()

    elif choice == "B" or choice == "b" or choice == "2":
        os.system('cls')
        audiodownload()

    elif choice == "Q" or choice == "q":
        os.system('cls')
        sys.exit

    else:
        os.system('cls')
        print("You must only select either A, B or Q")
        print("Please try again")
        menu()

menu()
