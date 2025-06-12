import os
import json
import time


class Memory:
    def __init__(self, filename):
        self.filename = filename
        self.max_items_len = 10
        if os.path.exists(filename):
            with open(filename) as f:
                self.history = json.loads(f.read())
        else:
            self.history = []
    
    def add(self, author, text):
        timestamp = int(time.time())
        self.history.append({
            "timestamp": timestamp,
            "author": author,
            "text": text
        })
    
    def get_recent(self):
        items = []
        for item in self.history[-1*self.max_items_len:]:
            items.append(f"[{item['author']}] >>> {item['text']}")
        return "\n".join(items)
