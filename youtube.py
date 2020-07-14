#!/usr/bin/env python
import os
import time

pwd = os.path.dirname(__file__) + '/'
the_pwd = str(os.popen("cd ~ && cd Downloads && pwd").read().replace('\n','') + '/')

def menu():
    print('''
    Download Video (The Best Quality) --default
    f -- Download video or audio specs (Custom)
    p -- Profile edit
    c -- Resoftware check
    w -- Download the subtitle
    exit -- Close the program
    ''')

def check_the_profile_and_command():
    file_status = os.path.exists(pwd + '.youtubedlconfig')
    if file_status == True:
        print("Reading Profile...")
    else:
        os.system("touch " + pwd + ".youtubedlconfig")
        print("Making profile...")
        target = str(pwd) + '.youtubedlconfig'
        target = open(target, 'w')
        target.write(str("{'youtube-dl': 'no', 'ffmpeg': 'no', 'aria2c': 'no', 'ffmpeg_auto': 'no', 'ffmpeg_default': 'mp4', 'aria2_auto': 'no', 'delete_origin': 'no', 'download_subtitle':'no'}"))
        target.close()

    config_dic = eval(open(pwd + '.youtubedlconfig').read())

    ydl_status = os.path.exists("/usr/local/bin/youtube-dl")
    ffmpeg_status = os.path.exists("/usr/local/bin/ffmpeg")
    aria2c_status = os.path.exists("/usr/local/bin/aria2c")

    if ydl_status == False:
        print("There is no YOUTUBEDL Command")
        config_dic['youtube-dl'] = "no"
        input("Press Enter to exit")
        writeconfig(config_dic)
        exit()
    else:
        config_dic['youtube-dl'] = "yes"
        writeconfig(config_dic)

    if ffmpeg_status ==  False:
        config_dic['ffmpeg'] = "no"
        writeconfig(config_dic)
        print("Need FFMPEG SupporT")
        input("Press Enter to EXIT")
        exit()
    else:
        config_dic['ffmpeg'] = "yes"
        writeconfig(config_dic)

    if aria2c_status ==  False:
        config_dic['aria2c'] = "no"
        writeconfig(config_dic)
        print("Install ARIA2C for the best experience~")
    else:
        config_dic['aria2c'] = "yes"
        writeconfig(config_dic)

def writeconfig(txt):
    target = str(pwd) + '.youtubedlconfig'
    target = open(target,'w')
    target.truncate()
    target.write(str(txt))
    target.close()

def status(name):
    config_dic = eval(open(pwd + '.youtubedlconfig').read())
    return config_dic[name]

def video_download(url):
    print("Getting title")
    title = str(os.popen("youtube-dl -e " + url).read().replace("\n","").replace(" ","").replace("/",""))
    print(title)
    if status("aria2c") == "yes":
        if status("aria2_auto") == "yes":
            os.system('cd {downloadpwd} && youtube-dl -o "{title}" "{url}" --external-downloader aria2c --external-downloader-args "-x 16  -k 1M" '.format(downloadpwd=the_pwd, url=url, title=title))
        else:
            os.system('cd {downloadpwd} && youtube-dl -o "{title}" "{url}"'.format(downloadpwd=the_pwd, url=url, title=title))
    else:
        os.system('cd {downloadpwd} && youtube-dl -o "{title}" "{url}"'.format(downloadpwd=the_pwd, url=url, title=title))
    ffmpeg_translate(title)
    if status("download_subtitle") == "yes":
        write_sub_download(url)
    else:
        pass

def custom_video_download():
    url = str(input('Input URL -> '))
    if "http" in url:
        title = str(os.popen("youtube-dl -e " + url).read().replace("\n", "").replace(" ", "").replace("/", ""))
        print(title)
        os.system('youtube-dl -F ' + url)
        print("\033[1;33mPlease select VIDEO and AUDIO \033[0m ")
        print("\033[1;34mThe first format code must contain the video code !!!\033[0m")
        x = input("eg. VideoNumber+AudioNumber -> ") + ' '
        print("Loading...")
        if status("aria2c") == "yes":
            if status("aria2_auto") == "yes":
                if status("ffmpeg_auto") == "yes":
                    os.system('cd {downloadpwd} && youtube-dl -o "{title}" -f "{x}" "{url}" --external-downloader aria2c --external-downloader-args "-x 16  -k 1M" '.format(downloadpwd=the_pwd, x=x, url=url, title=title))
                else:
                    os.system('cd {downloadpwd} && youtube-dl -f "{x}" "{url}"'.format(downloadpwd=the_pwd, x=x, url=url, title=title))
            else:
                os.system('cd {downloadpwd} && youtube-dl -o "{title}" -f "{x}" "{url}"'.format(downloadpwd=the_pwd, x=x, url=url, title=title))
        else:
            os.system('cd {downloadpwd} && youtube-dl -o "{title}" -f "{x}" "{url}"'.format(downloadpwd=the_pwd, x=x, url=url, title=title))
        ffmpeg_translate(title)
        if status("download_subtitle") == "yes":
            write_sub_download(url)
        else:
            pass
    else:
        print("URL error!!!")
        time.sleep(2)

def config_define():
    while True:
        ffmpeg_auto = status("ffmpeg_auto")
        ffmpeg_default = status("ffmpeg_default")
        aria2_auto = status("aria2_auto")
        delete_origin = status("delete_origin")
        download_subtitle = status("download_subtitle")

        f = status("ffmpeg")
        y = status("youtube-dl")
        ari = status("aria2c")

        ffssy = ffssn = aria2y = aria2n = delete_originy = delete_originn = subtitley = subtitlen = " "

        if ffmpeg_auto == "yes":
            ffssy = "*"
        else:
            ffssn = "*"
        if aria2_auto == "yes":
            aria2y = "*"
        else:
            aria2n = "*"
        if delete_origin == "yes":
            delete_originy = "*"
        else:
            delete_originn = "*"
        if download_subtitle == "yes":
            subtitley = "*"
        else:
            subtitlen = "*"

        if f == "yes":
            ffmpeginstall = "\033[1;32m Installed \033[0m"
        else:
            ffmpeginstall = "\033[1;31m UNINSTALL \033[0m"
        if y == "yes":
            youtubedlinstall = "\033[1;32m Installed \033[0m"
        else:
            youtubedlinstall = "\033[1;31m UNINSTALL \033[0m"
        if ari == "yes":
            aria2cinstall = "\033[1;32m Installed \033[0m"
        else:
            aria2cinstall = "\033[1;31m UNINSTALL \033[0m"

        os.system("clear")
        print('''
        Youtube profile config:
        
        ffmpeg_status = [{ffmpeginstall}] youtube-dl_status = [{youtubedlinstall}]  aria2c_status = [{aria2cinstall}]
        
        ffmpeg_auto:    (1)YES[{ffssy}]    (2)NO[{ffssn}]  (Automatic transcoding)
        
        ffmpeg_default: (3){ffmpeg_default}                 (Automatic transcoding FORMAT)
        
        aria2_auto:     (4)YES[{aria2y}]    (5)NO[{aria2n}]  (Start aria2 acceleration)
        
        delete_origin:  (6)YES[{delete_originy}]    (7)NO[{delete_originn}]  (Delete original file AFTER ffmpeg_auto)
        
        download_subtitle   (8)YES[{subtitley}]     (9)NO[{subtitlen}]  (Download the video subtitle)
        
        back -- Go back to the previous level
        '''.format(ffssy=ffssy, ffssn=ffssn, ffmpeg_default=ffmpeg_default, aria2y=aria2y, aria2n=aria2n, delete_originy=delete_originy, delete_originn=delete_originn, ffmpeginstall=ffmpeginstall, youtubedlinstall=youtubedlinstall, aria2cinstall=aria2cinstall, subtitley=subtitley, subtitlen=subtitlen))

        option = str(input("-> "))
        config_dic = eval(open(pwd + '.youtubedlconfig').read())
        if option == "1":
            config_dic['ffmpeg_auto'] = "yes"
            writeconfig(config_dic)
        elif option == "2":
            config_dic['ffmpeg_auto'] = "no"
            writeconfig(config_dic)
        elif option == "3":
            the_input = str(input("Default format eg.mp4 -> "))
            config_dic['ffmpeg_default'] = the_input
            writeconfig(config_dic)
        elif option == "4":
            config_dic['aria2_auto'] = "yes"
            writeconfig(config_dic)
        elif option == "5":
            config_dic['aria2_auto'] = "no"
            writeconfig(config_dic)
        elif option == "6":
            config_dic['delete_origin'] = "yes"
            writeconfig(config_dic)
        elif option == "7":
            config_dic['delete_origin'] = "no"
            writeconfig(config_dic)
        elif option == "8":
            config_dic['download_subtitle'] = "yes"
            writeconfig(config_dic)
        elif option == "9":
            config_dic['download_subtitle'] = "no"
            writeconfig(config_dic)
        elif option == "back":
            break
        else:
            print("Incorrect input character...")
            time.sleep(2)

def ffmpeg_translate(video_title):
    ffmpeg_auto_status = status("ffmpeg_auto")
    delete_origin = status("delete_origin")
    flist = os.listdir(the_pwd)
    finaltitle = ''
    for titles in flist:
        if video_title in titles:
            finaltitle = titles

    if ffmpeg_auto_status == "yes":
        print("AUTO Video transcoding...")
        video_format = status("ffmpeg_default")
        os.system('cd {downloadpwd} && ffmpeg -i "{video_title}" "{video_title}.{ffmpeg_default}"'.format(video_title=finaltitle, ffmpeg_default=video_format, downloadpwd=the_pwd))
        if delete_origin == "yes":
            os.system('cd {downloadpwd} && rm -rf "{titles}"'.format(downloadpwd=the_pwd, titles=finaltitle))
        else:
            pass
    else:
        pass

def write_sub_download(url):
    os.system("cd {downloadpwd} && ".format(downloadpwd=the_pwd) + "youtube-dl --write-sub --skip-download " + url)


if __name__ == '__main__':
    check_the_profile_and_command()
    while True:
        os.system("clear")
        menu()
        choice = str(input('->'))
        if "https" in choice:
            video_download(choice)
            print("\033[1;36mProcess Completed!!\033[0m")
            print("\033[1;36mProcess Completed!!\033[0m")
            input("\033[1;36mPress Enter to continue...\033[0m")
        elif choice == "f":
            custom_video_download()
            print("\033[1;36mProcess Completed!!\033[0m")
            print("\033[1;36mProcess Completed!!\033[0m")
            input("\033[1;36mPress Enter to continue...\033[0m")
        elif choice == "p":
            config_define()
        elif choice == "c":
            check_the_profile_and_command()
            print("\033[1;36mSoftware was already rechecked!!!\033[0m")
            input("\033[1;36mPress Enter to continue...\033[0m")
        elif choice == "w":
            x = input("URL -> ")
            write_sub_download(x)
        elif choice == "exit":
            exit()
        else:
            print("\033[1;31mIncorrect input character...\033[0m")
            time.sleep(2)
