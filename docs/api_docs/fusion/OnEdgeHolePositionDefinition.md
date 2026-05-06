# OnEdgeHolePositionDefinition
Namespace: adsk.fusion
Inherits: HolePositionDefinition
Since: August 2014

Provides positioning information for a hole that is positioned on the start, end or center of an edge.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### edge : BRepEdge [read-only]
Returns the edge the hole is positioned on.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### planarEntity : Base [read-only]
Returns the plane that defines the orientation and start of the hole.

### position : HoleEdgePositions [read-only]
Returns the position of the hole on the edge. The hole can be at the start, midpoint, or end of the edge.
