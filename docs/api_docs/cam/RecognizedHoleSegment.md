# RecognizedHoleSegment
Namespace: adsk.cam
Inherits: Base
Since: May 2023

Object that represents a hole segment, i.e. a single geometric shape like a cylinder or cone within the context of a hole. A segment represents a hole face.

**Accessed from:** RecognizedHole.segment

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### axis : Vector3D [read-only]
Returns the unit vector that points straight up out of the segment in the global coordinate system.

### bottomDiameter : double [read-only]
Returns the diameter of the bottom of this segment.

### face : Base [read-only]
This function is retired. See more information in the 'Remarks' section below.

Returns the model face this segment references.

### faces : array [read-only]
Returns the model faces this segment references.

### halfAngle : double [read-only]
For hole segments of type Cone, returns the cone's half angle, i.e. the angle between the axis of the cone and its surface. Returns 0 for other segment types.

### height : double [read-only]
Returns the height of this segment from top to bottom.

### holeSegmentType : HoleSegmentType [read-only]
Returns whether this segment represents a cylinder, cone, flat, or torus geometry type

### isThreaded : boolean [read-only]
Returns true if this segment is threaded, i.e. associated with a thread feature.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### threadFeatures : array [read-only]
Returns the thread features associated with this segment, or null if none exist for this segment.

### topDiameter : double [read-only]
Returns the diameter of the top of this segment.

## Samples
- **Hole and Pocket Recognition API Sample**: This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.
The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.
RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.
The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.
This script works only if the Manufacturing Extension is active.
