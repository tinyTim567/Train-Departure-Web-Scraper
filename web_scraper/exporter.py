import scraper
import json

train_times = scraper.get_train_times("HUL")

filename = "exported_times.json"
with open(filename, "w") as f:
    json.dump(train_times, f)

print("Done")

# with open(filename) as f:
#     imported_times = json.load(f)
