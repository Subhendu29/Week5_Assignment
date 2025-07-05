import schedule
import time
import os
from scripts.export_to_formats import df  # reuse if modularized

def job():
    print("Running scheduled task...")

# Schedule every minute
schedule.every(1).minutes.do(job)

# Simulate file-based event trigger
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileTrigger(FileSystemEventHandler):
    def on_created(self, event):
        print(f"File detected: {event.src_path} → running pipeline...")

event_handler = FileTrigger()
observer = Observer()
observer.schedule(event_handler, path="../data/csv", recursive=False)
observer.start()

while True:
    schedule.run_pending()
    time.sleep(1)

