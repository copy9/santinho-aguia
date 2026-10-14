# Uso: lê os CSVs eleitorado_local_votacao_2026_<UF>.csv (TSE) e grava loc/<UF>.json.
# Ajuste os caminhos /mnt/user-data/uploads e /home/claude/loc para os do seu computador.
import csv,json,sys,glob,statistics,os
UFS="AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO".split()
res={}
for uf in UFS:
    f=f"/mnt/user-data/uploads/eleitorado_local_votacao_2026_{uf}.csv"
    M={};rows=0;fed=0;bad=0;ufs=set()
    with open(f,encoding='latin1',newline='') as fh:
        r=csv.reader(fh,delimiter=';',quotechar='"')
        H=next(r);ix={h:i for i,h in enumerate(H)}
        for x in r:
            if not x or x[ix['NR_TURNO']]!='1':continue
            rows+=1;ufs.add(x[ix['SG_UF']])
            q=int(x[ix['QT_ELEITOR_ELEICAO_FEDERAL']] or 0);fed+=q
            try:
                la=float(x[ix['NR_LATITUDE']].replace(',','.'));lo=float(x[ix['NR_LONGITUDE']].replace(',','.'))
            except: la=lo=-1
            ok=(-34<la<6 and -75<lo<-33)
            key=(x[ix['CD_MUNICIPIO']],x[ix['NR_LOCAL_VOTACAO']],x[ix['NM_LOCAL_VOTACAO']],round(la,6),round(lo,6) if ok else None)
            m=M.get(key)
            if not m:
                m=M[key]=dict(la=la,lo=lo,ok=ok,n=x[ix['NM_LOCAL_VOTACAO']],mu=x[ix['NM_MUNICIPIO']],e=x[ix['DS_ENDERECO']],b=x[ix['NM_BAIRRO']],s=0,q=0,t=x[ix['DS_TIPO_LOCAL']])
            m['s']+=1;m['q']+=q
    good=[m for m in M.values() if m['ok']]
    nog=[m for m in M.values() if not m['ok']]
    # outliers: longe da mediana
    if good:
        mla=statistics.median(m['la'] for m in good);mlo=statistics.median(m['lo'] for m in good)
        far=[m for m in good if abs(m['la']-mla)>14 or abs(m['lo']-mlo)>14]
    else: far=[]
    res[uf]=dict(rows=rows,locais=len(M),com_coord=len(good),sem_coord=len(nog),longe=len(far),fed=fed,ufs=sorted(ufs),tipos=sorted({m['t'] for m in M.values()}))
    json.dump([m for m in good if m not in far],open(f"/home/claude/loc/{uf}.json",'w'),ensure_ascii=False,separators=(',',':'))
for uf,v in res.items(): print(uf,v)
print("TOTAL locais",sum(v['locais'] for v in res.values()),"com coord",sum(v['com_coord'] for v in res.values()),"sem",sum(v['sem_coord'] for v in res.values()),"rows",sum(v['rows'] for v in res.values()))
