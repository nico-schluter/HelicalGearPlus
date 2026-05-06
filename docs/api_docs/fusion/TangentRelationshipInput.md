# TangentRelationshipInput
Namespace: adsk.fusion
Inherits: Base
Since: May 2022

Defines all of the information required to create a new tangent relationship. This object provides equivalent functionality to the Tangent Relationship command dialog in that it gathers the required information to create a tangent relationship.

**Accessed from:** TangentRelationships.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### faceOne : BRepFace [read-write]
Gets and sets the first BRepFace object that will remain tangent to the set of specified tangent faces.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### tangentFaces : Base [read-write]
Gets and sets a single BRepFace object that is part of the body that faceOne will remain tangent to. All of the faces of the body will be used when computing the tangent relationship.
