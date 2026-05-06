# MachineQuery
Namespace: adsk.cam
Inherits: Base
Since: April 2023

MachineQuery defines the query to access Machines.

**Accessed from:** MachineLibrary.createQuery

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### execute() -> Machine
Executes the query for specific machines based on the query's properties.
- **Returns** (Machine): Returns a list of `Machine`. Each returned machine matches this query.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### location : LibraryLocations [read-write]
The location specifies the location to search in the machine library. Setting the location clears any previous specified URL.

### model : string [read-write]
The case-insensitive model specifies the model of the machine. The default empty model applies to all machines.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### url : URL [read-write]
The URL specifies the location and folder to search for in the machine library. Setting the URL updates the location.

### vendor : string [read-write]
The case-insensitive vendor specifies the vendor of the machine. The default empty vendor applies to all machines.
