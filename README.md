# youtubevideolinksextractor
This extracts video links and video names from multiple youtube channel's video page.

# How To:
Install Python.
Copy/Download Code and open the code in Visual Studio Code root directory.
Windows: Copy paste in VSCode Terminal. If prompted to change environment, select yes.
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

```

Change the url in the videos.py file here: Make sure it points to the videos page and not the channel's homepage
```
# Define the URL of the YouTube channel's video page in the code itself under channels. Make sure they point to the videos page.

```
Also increase this number based on your internet speed. 1 should be enough for most people but if you see the page not completely scrolling to the bottom change it to 2.
```
internet_speed = 2
```

You can keep your terminal open on the side to see how much time is remaining for the scroll as the scroll time is dependent on the number of videos on that youtube channel.


A new file will be created when the links are extracted. You can copy paste it directly in database or excel and it will retain it's structure since it has a tab character in between then.
