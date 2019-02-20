from youtube_dl import YoutubeDL

# example 1: Download a single youtube video:
# dl = YoutubeDL()
# dl.download(["https://www.youtube.com/watch?v=WHK5p7JL7g4"])

# Example 2: Download multiple youtube videos
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])

# Example 3: Download audio
# options = {
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL()
# dl.download(["https://www.youtube.com/watch?v=c3jHlYsnEe0"])

# Example 4: Search and then download the first video:
# options = {
#     "default_search": "ytsearch",
#     "max_downloads": 1
# }
# dl = YoutubeDL(options)
# dl.download(["con điên TAMKA PKL"])

# Exampl 5: Search and then download the first audit:
options = {
    "default_search": "ytsearch",
    "max_downloads": 1,
    "format": "bestaudio/audio"
}
dl = YoutubeDL(options)
dl.download(["Nhớ mưa sài gòn lam trường"])

