import pandas as pd

def update():
  a=pd.read_json('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
  print('\n'.join([ f"{c['nm']:<20}\t{c['vap']}\t{c['pvap']}%" for c in a['cand']]))
