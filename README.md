# echochamber


This tiny project is an example of creating a time series crawler at www.microprediction.org  Using some code adapted
from pyESN written originally by Clemens Korndofer we create a "Crawler" which looks for univariate time 
series and supplies predictions for them.  


## Install

   pip install echochamber
   pip install microprediction 

## Usage

See /examples

    from microprediction import new_key
    from echochamber import EchoCrawler
    
    # Create and launch crawler
    
    if __name__=="__main__":
        write_key = new_key(difficulty=10)    # Patience is a virtue
        print(write_key)
        crawler = EchoCrawler(n_reservoir=50)
        crawler.run()

To check its position on the leaderboards just plug in the write_key at https://www.microprediction.com/dashboard.html


## Write_key

Generating may take half an hour or so. See www.muid.org for more information. We suggest you alter the code to hardwire your write_key. 