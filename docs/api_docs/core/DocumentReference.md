# DocumentReference
Namespace: adsk.core
Inherits: Base
Since: June 2017

Represents a reference to a document from another document.

**Accessed from:** DeriveFeature.documentReference, DocumentReferences.item, Occurrence.documentReference

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getLatestVersion() -> boolean
Updates the reference to use the latest version. This is only useful when the isOutOfDate property is true.
- **Returns** (boolean): Returns true if getting the latest version was successful.

## Properties

### dataFile : DataFile [read-only]
The dataFile on A360 that this object references.

### isOutOfDate : boolean [read-only]
Indicates if this reference is out of date, meaning that the reference is not referencing the latest version.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentDocument : Document [read-only]
The document that is doing the referencing and owns this reference.

### referencedDocument : Document [read-only]
The document currently open in Fusion that this object references.

### version : integer [read-write]
Gets and sets the version of the dataFile on A360 that this document currently represents. Setting this property will cause all occurrences referencing this document to update to that version.
