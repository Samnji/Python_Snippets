#The pizza shop like and dislikes

n = int(input())
likes = []
dislikes = []

for i in range(n):
    like = input().split(' ')
    like.pop(0)
    
    for l  in like:
        if l not in likes:
            likes.append(l)

    dislike = input().split(' ')
    dislike.pop(0)
    
    for dl  in dislike:
        if dl not in dislikes:
            dislikes.append(dl)
    
    
totsLike = []

for name in likes:
    if name not in dislikes:
        totsLike.append(name)
        
str_totsLike = ' '.join(totsLike)
print(f'{len(totsLike)} {str_totsLike}')



