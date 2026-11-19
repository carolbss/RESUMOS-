# injeta/atualiza a busca carolzita em todos os resumos e no index (idempotente)
import sys,re,glob,os
d=sys.argv[1];base=os.path.dirname(os.path.abspath(__file__))
js=open(os.path.join(base,'carolzita-busca.js'),encoding='utf-8').read()
gi=open(os.path.join(base,'index-busca.html'),encoding='utf-8').read()
blk='<!-- czb:start -->\n<script>\n'+js+'</script>\n<!-- czb:end -->\n'
def put(s,b,tag):
  s=re.sub(r'<!-- '+tag+r':start -->.*?<!-- '+tag+r':end -->\n?','',s,flags=re.S)
  i=s.lower().rfind('</body>');return s[:i]+b+s[i:] if i>-1 else s+b
n=0
for f in glob.glob(os.path.join(d,'*.html')):
  s=open(f,encoding='utf-8').read()
  t=put(s,gi,'czb-global') if os.path.basename(f)=='index.html' else put(s,blk,'czb')
  if t!=s: open(f,'w',encoding='utf-8').write(t);n+=1
print(n,'arquivos atualizados')
