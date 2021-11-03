for I in[I:=input]*int(I()):
 R,Q=[],[];H,W=*map(int, I().split()),;A=[I().split()for _ in'*'*H]
 for h in range(H):
  for w in range(W):
   if int(A[h][w]):
    F=*filter(lambda l:(w-1,h)in l or(w,h-1)in l,R),
    if len(F)>1:F[0].extend(((w,h),*F[1]));R.remove(F[1])
    elif F:F[0].append((w,h))
    else:R.append([(w,h)])
  q=*filter(lambda l:all(y<h for x,y in l),R),
  for r in q:Q.append(r);R.remove(r)
 R.extend(Q);print(*sorted(map(len,R)))

