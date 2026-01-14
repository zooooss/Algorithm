def solution(answers):
    answer=[]
    human1=[1,2,3,4,5]*2000
    human2=[2,1,2,3,2,4,2,5]*1250
    human3=[3,3,1,1,2,2,4,4,5,5]*1000
    j,score1,score2,score3=0,0,0,0
    for i in answers:
        if(i==human1[j]):
            score1+=1
        if(i==human2[j]):
            score2+=1
        if(i==human3[j]):
            score3+=1
        j+=1
    total_score=[score1,score2,score3]
    max_score=max(total_score)
    for i in range(3):
        if(max_score==total_score[i]):
            answer.append(i+1)
    return answer