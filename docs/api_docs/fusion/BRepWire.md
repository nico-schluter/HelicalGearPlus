# BRepWire
Namespace: adsk.fusion
Inherits: Base
Since: December 2017

Represents a single B-Rep wire body. A wire body consists of one or more edges and their vertices.

**Accessed from:** BRepShell.wire, BRepWire.createForAssemblyContext, BRepWire.nativeObject, BRepWires.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> BRepWire
Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context for the created proxy.
- **Returns** (BRepWire): Returns the new BRepWire proxy or null if this isn't the NativeObject.

### offsetPlanarWire(planeNormal: Vector3D, distance: double, cornerType: OffsetCornerTypes) -> BRepBody
Method that computes the offset for a planar wire. A BRepBody containing the resulting BRepWire object(s) is returned. It's possible that the offset result of a single wire can result in multiple wires.
- **planeNormal** (Vector3D): Input Vector3D object that defines the positive direction of the plane the plane the wire lies on. This vector must be normal to the plane and is used to determine the side to offset the curves to. A positive offset distance is in the direction of the cross product (wire_tangent x wire_plane_normal). A negative offset is in the opposite direction.
- **distance** (double): The offset distance in centimeters. See the description for the Normal argument to see how a positive or negative value for the distance specifies the direction of the offset.
- **cornerType** (OffsetCornerTypes): Specifies how the corners are connected when offsetting the curves results in gaps in the corners. See the documentation of the enum for a detailed description of each option.
- **Returns** (BRepBody): Returns a new temporary BRepBody that contains one or more wires that represent the offset.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this BRepFace object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object.

### coEdges : BRepCoEdges [read-only]
Returns the co-edges associated with this wire body. The co-edges record the connections between the edges in the wire body.

### edges : BRepEdges [read-only]
Returns the B-Rep edges associated with this wire body.

### isPlanar : boolean [read-only]
Indicates if this entities making up this wire body are planar and all lie on the same plane.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### nativeObject : BRepWire [read-only]
The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : BRepBody [read-only]
Returns the parent BRepBody object that contains this wire.

### vertices : BRepVertices [read-only]
Returns the B-Rep vertices associated with this wire body.
