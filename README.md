# McAfee WebGateway API Overview: 

This is an open source project to help developers working on the McAfee Web Gateway REST API interface, 
Since McAFee lacks a pre-developed code package. 
Package is written in reference of MWG Version 8.2. 



# Usage:  

~~~~

pip install mcafee-mwgapi

from webgatewayapi.authenticate import authenticate

MWG_SERVER = input("Enter MWG Server")
PORT = input("Enter API Port")

authServer = authenticate(hostname=MWG_SERVER, port=PORT)
auth = authServer.createSession(username="something", password="something")
print(auth.session) 

from webgatewayapi.appliances import appliances
appliance = appliances(auth=auth.session, hostname=MWG_SERVER, port=PORT)
listappliance = appliance.listAppliances()
print(listappliance)

from webgatewayapi.listdata import listdata
list = listdata(auth.auth.session, hostname=MWG_SERVER, port=PORT)
getalllists = listdata.listdata()
print(getalllists)

trustedsoruce:
publichostvalidation = trustedsource()
print(publichostvalidation.lookup(data=test.setup()))

~~~~

# Contribution:
This is an Open Source Project, Contributions are welcome. 

# License: 
MIT License


# Credits:

This application uses Open Source components. You can find the source code of their open source projects along with license information below. We acknowledge and are grateful to these developers for their contributions to open source.

Project: https://github.com/KateLibC/McAfeeWebGateway
Copyright (c) 2017 Cariad Keigher (KateLibC) 
License (GPL-2.0)(GNU General Public License v2.0) https://github.com/KateLibC/McAfeeWebGateway/blob/master/LICENCE.md
__
