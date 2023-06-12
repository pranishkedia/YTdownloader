from pytube import YouTube
from sys import argv

# The first argument is always the program name so not using [0]
# argv[1] is the first command line argument which the user gives
link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("View", yt.views)

# Downloads the highest version of video
downloader = yt.streams.get_highest_resolution()

# Video is downloaded to this folder
downloader.download("/Users/pk/Documents/Youtube Downloads")