from pytube import YouTube
from colorama import Fore,init
init()
try:
   print(Fore.GREEN+"Downloading"+Fore.WHITE)
   YouTube("https://youtube.com/shorts/8kHfxN92ur4?feature=share").streams.get_lowest_resolution().download()
   print(Fore.GREEN+"Downloaded"+Fore.WHITE)
    
except:
    print(Fore.RED+"Failed"+Fore.WHITE)