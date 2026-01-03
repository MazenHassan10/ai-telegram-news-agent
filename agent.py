import feedparser, requests, os
from db import get_topics
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

feeds = [
    "https://news.google.com/rss",
    "https://hnrss.org/frontpage"
]

def summarize(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    return " ".join(str(s) for s in summarizer(parser.document, 2))

topics = get_topics()
messages = []

for feed in feeds:
    f = feedparser.parse(feed)
    for e in f.entries:
        text = (e.title + e.get("summary", "")).lower()
        if any(t in text for t in topics):
            messages.append(
                f"📰 {e.title}\n🧠 {summarize(e.summary)}\n🔗 {e.link}"
            )

if not messages:
    messages.append("No relevant updates today.")

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": "\n\n".join(messages[:5])}
)
