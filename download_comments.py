import json
import os 
import logging

from youtube_comment_downloader import YoutubeCommentDownloader
from deep_translator import GoogleTranslator
from pydantic import BaseModel

class Race(BaseModel):
    name: str
    youtube: str
    year: int
    
def load_config():
    with open('races.json', 'r') as f:
        races = json.load(f)
    return [Race(**i) for i in races]

def get_comments(url: str) -> list:
    try:
        downloader = YoutubeCommentDownloader()
        comments = downloader.get_comments_from_url(url)
        comments = [{"text": comment["text"]} for comment in comments]
        return comments
    except Exception as e:
        logger.error(f"Error downloading comments from {url}: {e}")
        return []

def translate_comments(comments: list) -> list:
    try:
        texts = [comment["text"] for comment in comments]
        translations = GoogleTranslator(source='auto', target='en').translate_batch(texts)
        return [{"text": translation} for translation in translations]
    except Exception as e:
        logger.error(f"Error translating comments: {e}")
        return [{"text": comment["text"]} for comment in comments]
    
def save_comments(race: Race):
    try:
        filename = f"2024/{race.name.lower().replace(' ', '_')}.json"
        if os.path.exists(filename):
            logger.info(f"Comments already saved")
            return
        comments = get_comments(race.youtube) 
        print("Comments: ", comments)
        with open(filename, 'w') as f:
            json.dump(comments, f, indent=4)
        tranlated_comments = translate_comments(comments)
        filename = f"2024_translated/{race.name.lower().replace(' ', '_')}.json"
        if os.path.exists(filename):
            logger.info(f"Comments already translated")
            return
        with open(filename, 'w') as f:
            json.dump(tranlated_comments, f, indent=4)
    except Exception as e:
        logger.error(f"Error saving comments: {e}")
    
def main():
    races = load_config()
    for race in races:
        save_comments(race)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    main()