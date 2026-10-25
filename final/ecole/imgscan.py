import sys
from PIL import Image
im=Image.open(sys.argv[1]).convert('RGB')
W,H=im.size
px=im.load()
TH=int(sys.argv[2]) if len(sys.argv)>2 else 300
def isdark(x,y):
    r,g,b=px[x,y]; return r+g+b<TH
def rows(x0,y0,x1,y1):
    out=[];start=None
    for y in range(y0,y1):
        v=any(isdark(x,y) for x in range(x0,x1))
        if v and start is None: start=y
        if not v and start is not None: out.append((start,y-1)); start=None
    if start is not None: out.append((start,y1))
    return out
def cols(x0,y0,x1,y1):
    xs=[x for x in range(x0,x1) if any(isdark(x,y) for y in range(y0,y1))]
    return (min(xs),max(xs)) if xs else None
for spec in sys.argv[3:]:
    name,x0,y0,x1,y1=spec.split(',')
    x0,y0,x1,y1=map(int,(x0,y0,x1,y1))
    rs=rows(x0,y0,x1,y1)
    print(name, 'cols',cols(x0,y0,x1,y1), 'rows',rs)
