#CdbPy
An un-sanctioned **CartoDB** Python Wrapper for Geoprocessing with **PostGIS** *SQL* created with the intent of helping ease **ArcPy** users into **CartoDB** and **PostGIS** 

##Importing CdbPy Username and API Key
	
	import cdbpy

	username = '<CartoDB Username>'
	apikey = '<CartoDB API Key>' 

Or use .gitignore and save data in **\_secret_info.py**

	import _secret_info
	import cdbpy
	
	cdbU = _secret_info.cartoDBusername
	cdbK = _secret_info.cartoDBapikey

##List Functions:

####Test
`printTest(inText)`
	
####Create Table	
`createTable(table_name,username,apikey)`


![logo](logo/cartodb-arcpy-wrapper-logo.png)
