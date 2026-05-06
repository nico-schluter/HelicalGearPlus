# User
Namespace: adsk.core
Inherits: Base
Since: January 2016

A class that represents a Fusion User

**Accessed from:** Application.currentUser, DataFile.createdBy, DataFile.inUseBy, DataFile.lastUpdatedBy, DesignDataFile.createdBy, DesignDataFile.inUseBy, DesignDataFile.lastUpdatedBy

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### displayName : string [read-only]
Returns display name of the user. (i.e. the name that shows up in the Fusion UI)

### email : string [read-only]
Get the email associated with this users Fusion account

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### userId : string [read-only]
Returns the user's internal Autodesk account name. This can be used by applications sold through the Autodesk Exchange Store to verify that the user has in fact purchased the product.

### userName : string [read-only]
Returns the user name associated with this user's Autodesk account
