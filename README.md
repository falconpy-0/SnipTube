🎵 Snip Tube – YouTube Playlist to MP3 Downloader

Snip Tube is a simple and elegant YouTube Playlist Downloader built with Python (Tkinter).
It allows you to download entire YouTube playlists (or single videos) as MP3 files with just one click.

✨ Features

🎨 Dark/Light Theme Toggle – Switch between clean dark and light modes.
📋 Paste Button – Instantly paste URLs from your clipboard.
🎶 Download YouTube Playlists to MP3 – Powered by yt-dlp +ffmpeg.
📊 Progress Box – Shows real-time status (downloading, complete, or cancelled).
⏹ Cancel Button – Stop downloads anytime.
⚡ Multithreaded – Runs downloads in a separate thread so the UI stays responsive.
🖼️ Custom UI Design – Includes custom fonts and image-based buttons for a modern look.

🛠️ Tech Stack
Python 3
Tkinter – UI
yt-dlp – YouTube downloading backend
ffmpeg – Audio conversion to MP3
psutil – Process management for cancelling downloads
Pillow (PIL) – Image handling

🚀 How It Works
Paste or click the Paste button to insert a YouTube playlist link.
Choose a folder to save your files.
Click Download – Snip Tube will fetch and convert everything into MP3.
Cancel anytime with the Cancel button.

📦 Setup Instructions
Clone this repo:
git clone https://github.com/yourusername/snip-tube.git
cd snip-tube


Install dependencies:
pip install -r requirements.txt
Download yt-dlp.exe and ffmpeg, place them in your project folder, and update paths in the script if needed.

Run the app:
python main.py

