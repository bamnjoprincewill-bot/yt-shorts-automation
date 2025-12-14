
from pytrends.request import TrendReq

pytrends = TrendReq()
pytrends.build_payload(
    kw_list=["AI tools", "AI websites", "Tech hacks"],
    timeframe="now 7-d"
)

data = pytrends.related_queries()
topics = []

for k in data:
    if data[k]["rising"] is not None:
        topics += data[k]["rising"]["query"].tolist()

topics = topics[:3]

with open("topics.txt", "w") as f:
    for t in topics:
        f.write(t + "\n")
