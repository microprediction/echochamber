
from microprediction import new_key
from echochamber import EchoCrawler

# Create and launch crawler

if __name__=="__main__":
    write_key = new_key(difficulty=10)      # <--- This will take a while
    crawler = EchoCrawler(n_reservoir=50)
    crawler.run()