from microprediction import new_key
from echochamber import EchoCrawler

# Example of creating, modify and launch crawler

class MyEchoCrawler(EchoCrawler):

    def candidate_streams(self):
        sponsors = self.get_sponsors()
        bobcats_streams   = [name for name, sponsor in sponsors.items() if 'cellose bobcat' in sponsor.lower()]
        return [s for s in bobcats_streams if not '~' in s ]

    def candidate_delays(self, name=None):
        return [d for d in self.delays if d>100 ]

if __name__=="__main__":
    write_key = new_key(difficulty=10)      # <--- This will take a while
    crawler = MyEchoCrawler(n_reservoir=50)
    crawler.run()