def optimal(reference_string, frame_count):
    frames = []
    page_faults = 0
    table = []
    for i in range(len(reference_string)):
        page = reference_string[i]
        if page not in frames:
            if len(frames) < frame_count:
                frames.append(page)
            else:
                future_uses = []
                for frame in frames:
                    if frame in reference_string[i+1:]:
                        future_uses.append(reference_string[i+1:].index(frame))
                    else:
                        future_uses.append(float('inf'))
                to_replace = future_uses.index(max(future_uses))
                frames[to_replace] = page
            page_faults += 1
        table.append(frames.copy())
    return page_faults, table
