from echochamber.crawler import EchoCrawler

try:
    from echochamber.config_private import TEST_KEY
except:
    TEST_KEY=None

def test_sample():
    if TEST_KEY:
        crawler = EchoCrawler(write_key=TEST_KEY)
        name  = 'three_body_x.json'
        delay = 910
        lagged_values = crawler.get_lagged_values(name=name)
        lagged_times  = crawler.get_lagged_times(name=name)
        samples = crawler.sample(lagged_values=lagged_values,lagged_times=lagged_times,name=name,delay=delay)
        assert len(samples)==crawler.num_predictions

