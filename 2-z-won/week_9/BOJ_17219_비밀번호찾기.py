m, n = map(int, input().split())
idpasdi = {}
for i in range(m):
  site, psswd = map(str, input().split())
  idpasdi.update({site: psswd})
for i in range(n):
  site = input()
  if site in idpasdi:
    print(idpasdi[site])
