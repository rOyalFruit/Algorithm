def solution(polynomial):
    answer = []
    x, c = 0, 0
    
    for p in polynomial.split(" + "):
        if 'x' in p:
            temp = p.replace('x', '')
            x += int(temp) if temp else 1
        else:
            c += int(p)
    
    if x:
        answer.append(f"{'' if x == 1 else x}x")
    if c:
        answer.append(str(c))
    
    return " + ".join(answer)
