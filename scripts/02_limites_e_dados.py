# Uso: cruza os limites do IBGE (BR, BR__1_, municipios.json) com loc/<UF>.json e gera data2.js,
# que vai embutido no index.html. Ajuste os caminhos para os do seu computador.
import json,re,gzip,base64,numpy as np
from matplotlib.path import Path
from scipy.spatial import cKDTree
U='/mnt/user-data/uploads/'
UFS="AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO".split()
def ufof(m):
    for k in ('microrregiao','regiao-imediata'):
        v=m.get(k)
        if v:
            return (v['mesorregiao']['UF'] if k=='microrregiao' else v['regiao-intermediaria']['UF'])['sigla']
names={}
for m in json.load(open(U+'municipios.json')): names[m['id']]=(m['nome'],ufof(m))
code2uf={}
for i,(n,u) in names.items(): code2uf[i//100000]=u
def rings(g):
    P=[g['coordinates']] if g['type']=='Polygon' else g['coordinates']
    return [r for p in P for r in p]
M={int(f['properties']['codarea']):rings(f['geometry']) for f in json.load(open(U+'BR'))['features']}
S={code2uf[int(f['properties']['codarea'])]:rings(f['geometry']) for f in json.load(open(U+'BR__1_'))['features']}
print('estados',len(S),'faltam',set(UFS)-set(S))
print('municipios malha',len(M),'nomes',len(names),'sem malha',[ (i,names[i]) for i in names if i not in M][:5],'sem nome',[i for i in M if i not in names][:5])
def enc(r):
    a=[];px=py=0
    for lon,lat in r:
        x=round(lon*1e4);y=round(lat*1e4);a+=[x-px,y-py];px,py=x,y
    return a
def area_cen(r):
    r=np.array(r);x,y=r[:,0],r[:,1];x1,y1=np.roll(x,-1),np.roll(y,-1);c=x*y1-x1*y;A=c.sum()/2
    if abs(A)<1e-12:return 0,x.mean(),y.mean()
    return A,((x+x1)*c).sum()/(6*A),((y+y1)*c).sum()/(6*A)
def gz(o): return base64.b64encode(gzip.compress(json.dumps(o,ensure_ascii=False,separators=(',',':')).encode(),9)).decode()
oldLM=json.loads(re.search(r'const LM=(\{.*?\});',open('data.js').read(),re.S).group(1))
LD={};LM={};MG={};BS={}
tot_drop=0
for uf in UFS:
    ids=sorted(i for i in M if code2uf[i//100000]==uf)
    pts=json.load(open(f'loc/{uf}.json'))
    P=np.array([[m['lo'],m['la']] for m in pts])
    asg=-np.ones(len(P),int)
    bbs=[]
    for k,i in enumerate(ids):
        R=M[i];allp=np.vstack([np.array(r) for r in R]);bb=(allp[:,0].min(),allp[:,1].min(),allp[:,0].max(),allp[:,1].max());bbs.append(bb)
        sel=np.where((asg<0)&(P[:,0]>=bb[0])&(P[:,0]<=bb[2])&(P[:,1]>=bb[1])&(P[:,1]<=bb[3]))[0]
        if not len(sel):continue
        ins=np.zeros(len(sel),bool)
        for r in R: ins^=Path(np.array(r)).contains_points(P[sel])
        asg[sel[ins]]=k
    out=asg<0
    V=[];L=[]
    for k,i in enumerate(ids):
        for r in M[i]:
            for v in r:V.append(v);L.append(k)
    V=np.array(V);L=np.array(L);tree=cKDTree(V)
    d,j=tree.query(P[out]) if out.any() else (np.array([]),np.array([],int))
    near=d<=0.1
    idx=np.where(out)[0]
    asg[idx[near]]=L[j[near]]
    keep=asg>=0;dropped=int((~keep).sum());tot_drop+=dropped
    arr=[]
    for n,m in enumerate(pts):
        if not keep[n]:continue
        arr.append([round(m['la'],5),round(m['lo'],5),m['n'],m['mu'],m['e'],m['b'],m['s'],m['q'],m['t'],int(asg[n])])
    arr.sort(key=lambda a:(a[9],a[2]))
    LD[uf]=gz(arr)
    old=oldLM[uf];longe=(old[0]-old[1])-len(pts)
    LM[uf]=[old[0],old[1],longe+dropped]
    md=[]
    for k,i in enumerate(ids):
        A,cx,cy=area_cen(max(M[i],key=lambda r:abs(area_cen(r)[0])))
        md.append([i,names[i][0],round(cx*1e4),round(cy*1e4),[enc(r) for r in M[i]]])
    MG[uf]=gz(md)
    BS[uf]=[enc(r) for r in S[uf]]
    print(uf,'municipios',len(ids),'pontos',len(pts),'dentro',int(keep.sum()),'borda',int(near.sum()),'descartados',dropped)
js="const LD="+json.dumps(LD)+";\nconst LM="+json.dumps(LM)+";\nconst MG="+json.dumps(MG)+";\nconst BS="+json.dumps(BS,separators=(',',':'))+";\n"
open('data2.js','w').write(js);print('tamanho data2.js',len(js),'descartados total',tot_drop)
