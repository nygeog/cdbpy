 ##   ###   ###    ###  #   #
#     #  #  #  #   #  #  # #
#     #  #  ###    ###    #
#     #  #  #  #   #      #
 ##   ###   ###    #      #
import urllib
import urllib2
import time

def printTest(inText):
	print inText + ' cdbpy.py - printTest'

def createTable(table_name,username,apikey): #add a field for a dictionary of fields and field types you want to add
	url = "https://%s.cartodb.com/api/v1/sql" % username
	insertList = ["CREATE TABLE "+table_name+" (uid int);",
	"SELECT cdb_cartodbfytable('"+table_name+"');"]
	for pauser, insert in enumerate(insertList): 
		params = {'api_key' : apikey,'q' : insert}  
	    	print insert
	    	req = urllib2.Request(url, urllib.urlencode(params))
	    	response = urllib2.urlopen(req)
	    	print '-' * (pauser + 1)
	    	time.sleep(2)
 
#def addPoints(table_name):

def buffer(in_buffer,buffer_dist,ou_buffer,username,apikey):  	
	url = "https://%s.cartodb.com/api/v1/sql" % username
	print url
	insertList = ["CREATE TABLE "+ou_buffer+" AS SELECT ST_Buffer(the_geom_webmercator, "+buffer_dist+") FROM "+in_buffer, """SELECT cdb_cartodbfytable('"""+ou_buffer+"""');"""]
	for pauser, insert in enumerate(insertList): 
		params = {'api_key' : apikey,'q' : insert}  
	    	print insert
	    	req = urllib2.Request(url, urllib.urlencode(params))
	    	response = urllib2.urlopen(req)
	    	print '-' * (pauser + 1)
	    	time.sleep(5)


def intersect(in_tables,ou_table,in_fields,username,apikey):
	url = "https://%s.cartodb.com/api/v1/sql" % username
	insertList = ["CREATE TABLE "+ou_table+" AS SELECT ST_Intersection("+in_tables[0]+".the_geom, "+in_tables[1]+".the_geom) AS * FROM "+in_buffer, #the_geom_webmercator, cartodb_id, cdbawcensusuid FROM latlngtable_"+fd+"",
    "SELECT cdb_cartodbfytable('"+ou_buffer+"');"]
	for pauser, insert in enumerate(insertList): 
		params = {'api_key' : apikey,'q' : insert}  
	    	print insert
	    	req = urllib2.Request(url, urllib.urlencode(params))
	    	response = urllib2.urlopen(req)
	    	print '-' * (pauser + 1)
	    	time.sleep(2)

