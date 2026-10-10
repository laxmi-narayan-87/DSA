# # cook your dish here
# if __name__=="__main__":
#     t=int(input())
#     for _ in range(t):
#         d1,d2,d3=map(int,input().split())
#         s1,s2,s3=map(int,input().split())
#         ds=d1+d2+d3
#         ss=s1+s2+s3
#         if (ds>ss):
#             print("Dragon")
#         elif(ds<ss):
#             print("Sloth")
#         else:
#             if(d1>s1):
#                 print("Dragon")
#             elif(d1<s1):
#                 print("Sloth")
#             else:
#                 if (d2>s2):
#                     print("Dragon")
#                 elif (d2<s2):
#                     print("Sloth")
#                 else:
#                     print("TIE")
                    
                    
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        d1,d2,d3=map(int,input().split())
        s1,s2,s3=map(int,input().split())
        dragon=(d1+d2+d3,d1,d2)
        sloth=(s1+s2+s3,s1,s2)
        if dragon>sloth:
            print("DRAGON")
        elif dragon<sloth:
            print("SLOTH")
        else:
            print("TIE")