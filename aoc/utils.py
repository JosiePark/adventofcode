def text_file_to_list(filepath):
    
    with open(filepath) as f:
        data = [int(row) for row in f]
    return data