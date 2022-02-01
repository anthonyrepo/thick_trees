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