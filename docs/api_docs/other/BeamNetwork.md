# BeamNetwork
Namespace: adsk.volume
Inherits: Base
Since: July 2025

A geometry reference property that defines a BeamNetwork object which is commonly used in discrete lattice structures.

**Accessed from:** BeamNetwork.create, GeometryGraphNodeProperty.beamNetwork

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create()
The creator function of the BeamNetwork object.

## Properties

### beams : array [read-write]
The beams of the beam network. Each beam is a pair of vertex indices. The size of the array should be a multiple of 2, and equal to the length of the radii array.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### radii : array [read-write]
The radii of the beams. Each radius is a double value. The radii define the radius of one end of the beam that corresponds to the same index in the beams array. The size of the array should be a multiple of 2, and equal to the length of the beams array.

### vertices : array [read-write]
The vertices of the beam network. Each vertex is a Point3D.
