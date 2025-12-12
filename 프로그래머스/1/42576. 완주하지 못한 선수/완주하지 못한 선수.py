def solution(participant, completion):
    answer = ''
    people = {}
    for p in participant:
        people[p]=people.get(p,0)+1
    for c in completion:
        people[c]-=1
    for name,count in people.items():
        if count !=0:
            answer=name
    return answer