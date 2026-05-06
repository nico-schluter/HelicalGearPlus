# BRepFaceDefinition
Namespace: adsk.fusion
Inherits: Base
Since: September 2020

Represents the definition of a B-Rep face that can be used as input to create a BRepBody that includes this face.

**Accessed from:** BRepFaceDefinitions.add, BRepFaceDefinitions.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### associativeID : integer [read-write]
Gets and sets the associate ID of this face definition. This ID will be copied to the corresponding face when the BRepBodyDefinition is used to create a BrepBody. It is used by Fusion as the identifier for the face and is used for tracking this geometry for parametric recomputes.

### isParamReversed : boolean [read-write]
Gets and sets if the normal of this face is reversed with respect to the surface geometry associated with this face definition.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### loopDefinitions : BRepLoopDefinitions [read-only]
Provides access to the BRepLoopDefinitions object associated with this BRepFaceDefinition. It's through the returned collection that you can create new BRepLoopDefinition objects.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### surfaceGeometry : Surface [read-write]
Gets and sets the surface geometry associated with this face definition.

## Samples
- **BRep Body definition Sample**: Demonstrates creating BRep bodies by BRepBodyDefinition.
