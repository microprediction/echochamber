
from microprediction import new_key
from echochamber import EchoCrawler

# Create and launch crawler

try:
    from echochamber.config_private import TEST_KEY
except:
    TEST_KEY = new_key(difficulty=10)

if __name__=="__main__":
    crawler = EchoCrawler(write_key=TEST_KEY,n_reservoir=50)
    crawler.run()