# DataHub
Namespace: adsk.core
Inherits: Base
Since: September 2016

Represents a hub within the data.

**Accessed from:** Data.activeHub, DataHubs.asArray, DataHubs.item, DataHubs.itemById, DataProject.parentHub

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### dataProjects : DataProjects [read-only]
Returns the projects within this hub.

### fusionWebURL : string [read-only]
Returns a URL that can be used to access the Fusion Web interface for this hub within a browser. The person using the URL must have an Autodesk account and have authority to access the hub.

### hubType : HubTypes [read-only]
Gets if this hub is a Personal (PersonalHubType) or Team (TeamHubType) type hub.

### id : string [read-only]
Returns the unique ID for this hub. This is the same id used in the APS Data Management API in an unencoded form and will look something like this: "a.45637".

### isCollaborativeEditingEnabled : boolean [read-only]
Returns true if Concurrent Editing is enabled.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### mfgdmId : string [read-only]
Get the MFGDM ID for this hub.

### name : string [read-only]
Returns the name of the hub.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### version : string [read-only]
Returns the version of the hub.
