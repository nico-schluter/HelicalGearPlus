# DocumentReferences
Namespace: adsk.core
Inherits: Base
Since: June 2017

Provides access to the list of documents referenced from a document.

**Accessed from:** Document.allDocumentReferences, Document.documentReferences, DrawingDocument.allDocumentReferences, DrawingDocument.documentReferences, FusionDocument.allDocumentReferences, FusionDocument.documentReferences

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> DocumentReference
Returns the specified DocumentReference.
- **index** (uinteger): The index of the object to return where the first one in the collection has an index of 0.
- **Returns** (DocumentReference): Returns the specified DocumentReference or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
The number of DocumentReference objects in this collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
