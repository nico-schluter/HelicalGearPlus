# BRepFaceDefinitions
Namespace: adsk.fusion
Inherits: Base
Since: September 2020

Provides access to the BRepFaceDefinition objects associated with the object the collection was obtained from. It's through this object that you create new BRepFaceDefinition objects.

**Accessed from:** BRepShellDefinition.faceDefinitions

## Methods

### add(surfaceGeometry: Surface, isParamReversed: boolean) -> BRepFaceDefinition
Creates a new BrepFaceDefinition within the parent BRepShellDefinition object.
- **surfaceGeometry** (Surface): Input surface object that defines the geometry of the face. Valid objects for input are NurbsSurface, Cone, Cylinder, EllipticalCone, EllipticalCylinder, Plane, Sphere, and Torus.
- **isParamReversed** (boolean): Input Boolean that indicates if the normal of this face is reversed with respect to the surface geometry associated with this face definition.
- **Returns** (BRepFaceDefinition): Returns the newly created BRepFaceDefinition object or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> BRepFaceDefinition
Function that returns the specified BRepFaceDefinition object using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (BRepFaceDefinition): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
The number of B-Rep face definition objects in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **BRep Body definition Sample**: Demonstrates creating BRep bodies by BRepBodyDefinition.
