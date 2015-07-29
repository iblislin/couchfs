def is_db(doc: dict) -> bool:
    if doc.get('db_name') and doc.get('update_seq'):
        return True
    return False


def is_doc(doc: dict) -> bool:
    if doc.get('_id') and doc.get('_rev'):
        return True
    return False
