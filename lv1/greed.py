map_size = int(input("mapsize : "))
plans = input("plan : ").split()

dx=[0,1,0,-1]
dy=[1,0,-1,0]
ways=['R','D','L','U']
x,y=1,1

for plan in plans:
  for way in range(len(ways)):
    #일단 이동 좌표를 설정한다.
    if plan==ways[way]:
      nx=x+dx[way]
      ny=y+dy[way]
  #좌표 설정한 곳이 공간을 넘어가면 이동수행을 안한다.
  if nx<1 or ny<1 or nx>map_size or ny>map_size:
    continue
  
  #이동수행
  x,y=nx,ny
 
print(x, y)
    

