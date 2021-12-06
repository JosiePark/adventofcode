def text_file_to_list(filepath):
    
    with open(filepath) as f:
        data = [int(row) for row in f]
    return data

def two_column_to_list(filepath):
    
    with open(filepath) as f:
        data = [row.strip('\n').split(' ') for row in f]
        
    for row in range(len(data)):
        data[row][1] = int(data[row][1])
        
    return data