# youtubevideolinksextractor
This extracts video links and video names for a youtube channel's video page

# How To:
Install Python, pip.
Run Virtual environment.
Install requirements.txt.
Change the url in the videos.py file here: Make sure it points to the videos page and not the channel's hoempage
```
# Define the URL of the YouTube channel's video page
channel_url = 'https://www.youtube.com/@makingtechfriendlyindia/videos'
```
Also increase this number based on your internet speed. 1 should be enough for most people but if you see the page not completely scrolling to the bottom change it to 2.
```
internet_speed = 2
```

You can keep your terminal open on the side to see how much time is remaining for the scroll as the scroll time is dependent on the number of videos on that youtube channel.
