# 🎵 Spotify Time Machine

## 🌟 Overview

The **Spotify Time Machine** is a Python application that generates a personalized Spotify playlist based on the Billboard Hot 100 chart from a specific date in history. Users can input a date, and the app will scrape the Billboard Hot 100 songs for that date, search for those tracks on Spotify, and create a private playlist.

## 🛠 Features
* **Billboard Hot 100 Scraping:** Fetches the top 100 songs from Billboard for a user-specified date.
* **Spotify Playlist Creation:** Creates a private Spotify playlist using the scraped songs.
* **Seamless Integration:** Automatically adds available tracks to the playlist.
* **Dynamic User Input:** Supports any date in the past to explore musical trends.

## 📂 Project Structure

    .
    ├── main.py                 # Main Python script for the application
    ├── requirements.txt        # Project dependencies
    ├── README.md               # Project documentation

## 🔧 Setup Guide

**Prerequisites**

* Python 3.x installed.
* Spotify developer account with a created application.
* Spotify API credentials (Client ID and Client Secret).

**Installation**

1. Clone this repository:



        git clone https://github.com/matanohana433/spotify-time-machine.git
        cd spotify-time-machine


2. Create and activate a virtual environment (optional but recommended):

**Windows:**


    python -m venv venv
    venv\Scripts\activate


**macOS/Linux:**


    python3 -m venv venv
    source venv/bin/activate


3. Install dependencies:

  
        pip install -r requirements.txt


4. Set environment variables:

   * Create a `.env` file or set the variables manually:



            SPOTIFY_CLIENT_ID=your_spotify_client_id
            SPOTIFY_CLIENT_SECRET=your_spotify_client_secret


## 🚀 Usage

1. **Run the Application:**


        python main.py


2. **Input a Date:**

* When prompted, enter a date in the format `YYYY-MM-DD`:



      Which year do you want to travel to? Type the date in this format YYYY-MM-DD:


* Example: `1990-08-01`

3. **Playlist Creation:**

* The app will scrape Billboard's Hot 100 for the given date and attempt to find matching tracks on Spotify.
* Once the playlist is created, you'll receive a link:

    
      Here is your link: https://open.spotify.com/playlist/... Enjoy :)


## 🌟 Key Features

1. **Billboard Integration:**
   * Scrapes top 100 songs from Billboard's website for the specified date.
2. **Spotify Playlist:**
   * Automatically creates a private playlist with the matched songs.
3. **Dynamic Date Support:**
   * Users can explore music from any date in Billboard's history.

## 🚀 Future Enhancements

1. Add error handling for failed scrapes or missing songs on Spotify.
2. Implement a feature to allow public playlists.
3. Extend functionality to include more charts (e.g., genres or albums).

## 📬 Contact

For questions or collaboration:

* **Email:** matanohana433@gmail.com
* **GitHub:** [matanohana433](https://github.com/matanohana433)
