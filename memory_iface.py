import os
import json


class Memory:
    def __init__(self, filename):
        self.filename = filename
        self.max_items_len = 10
        if os.path.exists(filename):
            with open(filename) as f:
                self.memories = json.loads(f.read())
        else:
            self.memories = []
    
    def find(self, tags=[]):
        items = []
        for item in self.memories:
            found = True    # Be optimistic :-)
            for tag in tags:
                if tag not in item["tags"]:
                    found = False
                    break
            if found:
                items.append(item["data"])
                if len(items) == self.max_items_len:
                    return items
        return items
    
    def exact_match_found(self, new_item):
        for item in self.memories:
            found = True 
            for tag in new_item["tags"]:
                if tag not in item["tags"]:
                    found = False
                    break
            if found:
                if item["data"] == new_item["data"]:
                    return True
        return False
    
    def add(self, item):
        if len(item["tags"]) == 0:
            return "Error: At least one tag must be specified"
        if self.exact_match_found(item):
            return "Error: Item already exists in the memory"
        self.memories.append({
            "data": item["data"],
            "tags": item["tags"]
        })
        try:
            with open(self.filename, 'w') as f:
                f.write(json.dumps(self.memories, indent=4))
        except Exception as e:
            return "Error: Memory has been updated, but caould not be written to the file"
        return "Success: New item was added to the memory"