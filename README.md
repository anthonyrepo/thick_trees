nycopendata.py will act as a spider over the api

data:

tree_id: Number, Unique identification number for each tree point
created_at: Date & Time (Floating Timestamp), Date
tree_dbh: Number, Diameter of the tree, measured at approximately 54" / 137cm above the ground
status: Text, Indicates whether the tree is alive, standing dead, or a stump (Alive, Dead, Stump)
spc_latin: Text, Scientific name for species, e.g. "Acer rubrum"
spc_common: Text, Common name for species, e.g. "red maple"
address: Text, Nearest estimated address to tree
postcode: Number, Five-digit zipcode in which tree is located
zip_city: Text, City as derived from zipcode. This is often (but no always) the same as borough.
borocode: Number, Code for borough in which tree point is located: 1 (Manhattan), 2 (Bronx), 3 (Brooklyn), 4(Queens), 5 (Staten Island)
borough: Text, Name of borough in which tree point is located
nta: Text, This is the NTA Code corresponding to the neighborhood tabulation area from the 2010 US Census that the tree point falls into
nta_name: Text, This is the NTA name corresponding to the neighborhood tabulation area from the 2010 US Census that the tree point falls into
latitude: Number, Latitude of point, in decimal degrees
longitude: Number, Longitude of point, in decimal degrees