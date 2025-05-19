def lru(reference_string, frame_count):
    frames = []
    recent = []
    page_faults = 0
    table = []
    for page in reference_string:
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                lru_page = recent.pop(0)
                frames.remove(lru_page)
                frames.append(page)
            page_faults += 1
        else:
            recent.remove(page)
        recent.append(page)
        table.append(frames.copy())
    return page_faults, table
