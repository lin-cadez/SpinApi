import feedparser

class Spin:
    class SpinDict(dict):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        @property
        def title(self):
            return self['title']

        @property
        def summary(self):
            return self['summary']

        @property
        def location(self):
            return self['location']

        @property
        def published(self):
            return self['published']

    def __init__(self, url="https://spin3.sos112.si/api/javno/ODRSS/true"):
        self.url = url

    def events(self):
        feed = feedparser.parse(self.url)
        events=[]
        if feed.entries != 0:
            for event in feed.entries:
                title=event.title
                summary=event.summary
                location=event.link
                published=event.published
                event_dict= {
                    'title': title,
                    "summary": summary,
                    "location": location,
                    "published": published
                }
                events.append(self.SpinDict(event_dict))
                return events



    @property
    def last(self):
        if self.events()==None:
            return False
            
        else:
            return self.events()[0]
