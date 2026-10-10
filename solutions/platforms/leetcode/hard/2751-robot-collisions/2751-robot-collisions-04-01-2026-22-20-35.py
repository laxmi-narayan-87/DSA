class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots=[]
        for i in range(len(positions)):
            robots.append((positions[i],healths[i],directions[i],i))
        robots.sort(key=lambda x:x[0])
        robots=[list(r) for r in robots]
        stack=[]
        for i in range(len(robots)):
            if robots[i][2]=='R':
                stack.append(i)
            else:
                while stack and robots[i][1]>0:
                    j=stack[-1]
                    if robots[j][1]<robots[i][1]:
                        stack.pop()
                        robots[i][1]-=1
                        robots[j][1]=0
                    elif robots[j][1]>robots[i][1]:
                        robots[j][1]-=1
                        robots[i][1]=0
                        break
                    else:
                        robots[j][1]=0
                        robots[i][1]=0
                        stack.pop()
                        break
        survivors=[]
        for r in robots:
            if r[1]>0:
                survivors.append((r[3],r[1]))
        survivors.sort(key=lambda x:x[0])
        result=[]
        for _,h in survivors:
            result.append(h)
        return result