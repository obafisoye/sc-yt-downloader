import yt_dlp


def download(url):
    dl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '0',
            },
            {'key': 'EmbedThumbnail'},
            {'key': 'FFmpegMetadata'},
        ],
        'writethumbnail': True,
        'addmetadata': True,
        'prefer_ffmeg': True,
    }

    if 'youtube.com' in url or 'youtu.be' in url:
        dl_opts['format'] = 'bestvideo+bestaudio/best'
        dl_opts['postprocessors'] = [
            {'key': 'FFmpegMetadata'},
            {'key': 'EmbedThumbnail'},
        ]

    with yt_dlp.YoutubeDL(dl_opts) as ydl:
        ydl.download([url])


if __name__ == '__main__':
    url = input("enter a link: ")
    download(url)
