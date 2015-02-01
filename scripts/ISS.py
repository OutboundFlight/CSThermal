import ephem, datetime

iss = ephem.readtle("ISS (ZARYA)",
	"1 25544U 98067A   15032.46425904  .00014369  00000-0  22307-3 0  8084",
	"2 25544  51.6471  41.7603 0005800 315.5306 199.7210 15.54220656926915")

now = datetime.datetime.now()

pdx = ephem.Observer()
pdx.lat, pdx.long = "45.5100209", "-122.6802467"  #Latlong have to be passed as strings for some reason
pdx.date = "%s/%s/%s" % (now.year, now.month, now.day)
iss.compute(pdx)

print "%s %s" % (iss.alt, iss.az)
print "%s %s %s" % (iss.rise_time, iss.transit_time, iss.set_time)
