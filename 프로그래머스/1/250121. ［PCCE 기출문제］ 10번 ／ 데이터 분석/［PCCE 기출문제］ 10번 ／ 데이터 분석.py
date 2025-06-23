def solution(data, ext, val_ext, sort_by):
    col = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    row = [row for row in data if row[col[ext]] < val_ext]
    
    return sorted(row, key=lambda x: x[col[sort_by]])