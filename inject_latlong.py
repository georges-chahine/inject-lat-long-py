from shapely.geometry import Point
import utm

def inject_lat_long (pt, dx):

   u = utm.from_latlon(p.x, p.y);
   u=list(u);
   u[0]=u[0]+dx;
   u[1]=u[1]+dx;

   u=tuple(u)
	
   v=utm.to_latlon(*u)
   v=list(v);
   v[0]=float('%.6f'%(v[0]))
   v[1]=float('%.6f'%(v[1]))
   v=tuple(v)
   pt=Point(v[0],v[1]);
   
   return pt;






p=Point(49.041955, 3.957195)
dx=10
print ("old point is: ",p)   
new_p=inject_lat_long (p, dx)
print ("new point is: ",new_p)

