x,y,z = 4,4,4
def solution(x, y,z):
    answer = [x-1,x+1]
    # Write your code here
    answer = [x-1,x+1]
    for i in range(0,z-1):
        for j in range(len(answer)):
            answer.append(answer[j]+1)
            answer.append(answer[j]-1)
    return answer

print(solution(x,y,z))
