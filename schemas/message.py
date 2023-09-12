def messageEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        #"id_trans": int(item["id_trans"]),
        #"id_rec": int(item["id_rec"]),
        "text": item["text"],
        "date": item["date"]
    }
    
def messagesEntity(entity) -> list:
    return [messageEntity(item) for item in entity]