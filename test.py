import _secret_info
import cdbpy

print 'The test begins now'

cdbU = _secret_info.cartoDBusername
cdbK = _secret_info.cartoDBapikey

cdbpy.printTest("Let's try the")

cdbpy.createTable("NEWTABLE20151119",cdbU,cdbK)