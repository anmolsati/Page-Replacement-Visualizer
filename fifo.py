def fifo(reference_string, frame_count):
    frames = []
    page_faults = 0
    table = []
    for page in reference_string:
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1
        table.append(frames.copy())
    return page_faults, table
