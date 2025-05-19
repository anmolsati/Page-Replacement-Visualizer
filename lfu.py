def lfu(reference_string, frame_count):
    frames = []
    freq = {}
    page_faults = 0
    table = []

    for page in reference_string:
        if page in frames:
            freq[page] += 1
        else:
            if len(frames) < frame_count:
                frames.append(page)
                freq[page] = 1
            else:
                min_freq = min(freq[p] for p in frames)
                lfu_candidates = [p for p in frames if freq[p] == min_freq]
                page_to_remove = lfu_candidates[0]
                frames[frames.index(page_to_remove)] = page
                del freq[page_to_remove]
                freq[page] = 1
            page_faults += 1
        table.append(frames.copy())
    return page_faults, table
