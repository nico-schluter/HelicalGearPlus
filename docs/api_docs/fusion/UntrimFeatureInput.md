# UntrimFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: January 2021

This class defines the methods and properties that pertain to the definition of an Untrim feature.

**Accessed from:** UntrimFeatures.createInputFromFaces, UntrimFeatures.createInputFromLoops

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setLoops(loops: BRepLoop[]) -> boolean
Set the loops to be removed.
- **loops** (BRepLoop[]): Redefines this input to remove loops from the body. If faces were previously defined, that information will be lost. Only loops that do not have a connected face can be removed (the edges in the loop have a single face) The array can only contain loops from surface bodies, (the isSolid property of the BRepBody returns false).
- **Returns** (boolean): Returns whether the operation was successful

### setLoopsFromFaces(faces: BRepFace[], untrimLoopType: UntrimLoopTypes) -> boolean
Set the loops to be removed from a set of faces.
- **faces** (BRepFace[]): An array of BRepFace objects that will have the loops of the specified types removed. Only loops that do not have a connected face can be removed (the edges in the loop have a single face). The array can only contain faces from surface bodies, (the isSolid property of the BRepBody returns false).
- **untrimLoopType** (UntrimLoopTypes): The loop type to be untrimmed (AllLoopUntrimType, InternalLoopUntrimType, or ExternalLoopUntrimType).
- **Returns** (boolean): Returns whether the operation was successful

## Properties

### extensionDistance : ValueInput [read-write]
Gets and sets the ValueInput object that defines the extension distance applied to faces when an external boundary is removed.

### facesToUntrim : array [read-only]
Gets the face objects to untrim. Returns null/None in the case where loops are specified instead of faces.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### loopsToUntrim : array [read-only]
Gets the loop objects to untrim. Returns null/None in the case where faces are specified instead of loops

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### untrimLoopType : UntrimLoopTypes [read-only]
Gets the loop type to be untrimmed. This is only used when faces are being untrimmed and is ignored for loops.

## Samples
- **Untrim Feature API Sample**: Demonstrates creating a new untrim feature.
