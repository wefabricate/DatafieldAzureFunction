# DatafieldAzureFunction
Proof of concept [Azure Function](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python?pivots=python-mode-configuration) that responds to an event gate trigger when an SN has been created and populates the UUID datafield of that SN. Can be expanded to perform other operations and populate other datafields.

## General
Datafields are used in production and testing of products. A common use case is to populate a product's datafield at some point during the production or testing process to store specific data about that product. For example, if a product needs to be calibrated during production, this calibration data might be stored in a datafield. 

This repository holds a python web app that sets a UUID (unique 'password') for heat pumps as they are created. An overview of how this works is as follows:
1. This app would be hosted on a server and would subscribe to the event gate.
2. The event gate sends a message out to all subscribers when a new SN is created.
3. Upon receiving this trigger, the app generates a UUID and attempts to set this custom property in the database for the newly created SN.

This can be expanded upon to do more than generate and set the UUID datafield.

## dev_tools
1. `example_trigger.json` contains an example of the JSON object that this app will receive from the event gate when a new SN has been produced and this app should populate one of it's datafields.
2. `temp.py` script used to create and delete datafields for debug / development.

