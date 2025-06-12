import os
from memory_iface import Memory


def process_request(rq):
    if rq["type"] == "google":
        return google_data(rq["data"])
    elif rq["type"] == "wget":
        return wget(rq["data"])
    elif rq["type"] == "memory_get":
        return memory('get', tags=rq["tags"])
    elif rq["type"] == "memory_add":
        return memory('add', tags=rq["tags"], data=rq["data"])
    elif rq["type"] == "history":
        return history_get(keywords=rq["keywords"], date=rq["date"])



def main():
    pass


if __name__ == "__main__":
    main()
