import time
from selenium import webdriver
from bs4 import BeautifulSoup
from tqdm import tqdm

#If your internet speed is best keep it 1, otherwise increase this.
#This actually changes the time till which scroll happens
internet_speed = 1
# Define the URL of the YouTube channels' video page
channels = [
    'https://www.youtube.com/@ni6hantwork/videos',
    'https://www.youtube.com/@ni6hant/videos',
    'https://www.youtube.com/@ni6hantindia/videos',
    'https://www.youtube.com/@makingtechfriendly/videos',
    'https://www.youtube.com/@makingtechfriendlyindia/videos'
]

# Create a list to store video information
video_info = []


#Iterate through the YouTube Channel lists to go over them one by one:
for channel in channels:
    # Initialize Selenium WebDriver without specifying executable_path
    driver = webdriver.Chrome()
    
    # Open the channel URL
    driver.get(channel)

    # Parse the HTML content with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the total number of videos element by searching for its attributes
    total_videos_element = soup.find('span', {'dir': 'auto', 'class': 'style-scope yt-formatted-string'})

    # Extract the total number of videos and calculate the scroll duration
    total_videos_count = int(total_videos_element.text.replace(',', ''))
    # scroll_duration = 3
    scroll_duration = internet_speed *total_videos_count / 5
    print(total_videos_count, " : ", scroll_duration)

    # Execute JavaScript to scroll to the bottom of the page
    driver.execute_script('''
        var scroll = setInterval(function(){
            window.scrollBy(0, 1000);
        }, 1000);
    ''')

    # Initialize the progress bar
    with tqdm(total=scroll_duration, unit="s", desc="Scrolling") as pbar:
        # Wait for the calculated duration to allow content to load
        for _ in range(int(scroll_duration)):
            time.sleep(1)
            pbar.update(1)  # Update the progress bar

    # Get the updated page source
    updated_page_source = driver.page_source

    # Close the web driver
    driver.quit()

    # Parse the updated HTML content with BeautifulSoup
    soup = BeautifulSoup(updated_page_source, 'html.parser')

    # Find all video title and URL elements using the specified id and class attributes
    video_tags = soup.find_all('a', {'id': 'video-title-link', 'class': 'yt-simple-endpoint focus-on-expand style-scope ytd-rich-grid-media'})

    # Iterate through the video elements and extract information
    for video_tag in video_tags:
        video_title = video_tag.get('title', 'N/A')
        video_url = 'https://www.youtube.com' + video_tag.get('href', 'N/A')
        video_info.append(f"{video_title}\t{video_url}")

# Write the video information to a text file
with open('video_info.txt', 'w', encoding='utf-8') as output_file:
    for entry in video_info:
        output_file.write(entry + '\n')

print("Video information has been saved to video_info.txt")
print(f"Total videos found: {len(video_info)}")
