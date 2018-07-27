from search import Search
from video import Video
from video_category import VideoCategory
from channel import Channel

key = open("key.txt").read()

s = Search(q="Tatar ramazan",
           part="id, snippet",
           key=key,
           type="video",
           maxResults=1).data()
print(s)

v = Video(id="JuOi7qHjR7o",
          part="id, snippet,contentDetails,statistics",
          key=key,
          type="video",
          regionCode="tr").data()
print(v)

vc = VideoCategory(part="id, snippet",
                   key=key,
                   type="video",
                   regionCode="tr").data()
print(vc)

c = Channel(id="UCBR8-60-B28hp2BmDPdntcQ",
            part="id, snippet,contentDetails,statistics",
            key=key,
            type="video",
            regionCode="tr").data()
print(c)

