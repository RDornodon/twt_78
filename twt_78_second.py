for I in[I:=input]*int(I()):
 R=[];H=int(I().split()[0]);A={(x,y)for y in range(H)for x,v in enumerate(I().split())if v>'0'}
 while A:
  q=1;f={A.pop()}
  while f:q+=len(f:={v for x,y in f for a,b in[(-1,0),(0,-1),(1,0),(0,1)]if(v:=(x+a,y+b))in A});A-=f
  R+=[q]
 print(*sorted(R))
