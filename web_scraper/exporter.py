from web_scraper import scraper
import json


def main(station):
    train_times = scraper.get_train_times(station)

    filename = "exported_times.json"
    with open(filename, "w") as f:
        json.dump(train_times, f)

    print("Done")

    # with open(filename) as f:
    #     imported_times = json.load(f)
