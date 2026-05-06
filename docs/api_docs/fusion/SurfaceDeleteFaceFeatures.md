# SurfaceDeleteFaceFeatures
Namespace: adsk.fusion
Inherits: Base
Since: August 2016

Collection that provides access to all of the existing SurfaceDeleteFaceFeature features in a component and supports the ability to create new SurfaceDeleteFaceFeature features.

The SurfaceDeleteFaceFeature and DeleteFaceFeature differ in that the SurfaceDeleteFaceFeature can delete any face without any restrictions. If the body is a solid, it will become a surface when the first face is deleted. The specified face is deleted without any other changes being made to the body. The DeleteFaceFeature deletes the specified face and also modifies the other faces in the body to heal or fill in the area of the deleted face. This means that a solid body will remain solid.

**Accessed from:** Features.surfaceDeleteFaceFeatures

## Methods

### add(facesToDelete: Base) -> SurfaceDeleteFaceFeature
Creates a new SurfaceDeleteFaceFeature feature. This deletes the specified faces from their bodies without any attempt to heal the openings. This is equivalent to selecting and deleting faces when in the Patch workspace.
- **facesToDelete** (Base): A single BRepFace or an ObjectCollection containing multiple BRepFace objects.
- **Returns** (SurfaceDeleteFaceFeature): Returns the newly created SurfaceDeleteFaceFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SurfaceDeleteFaceFeature
Function that returns the specified SurfaceDeleteFaceFeature object using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SurfaceDeleteFaceFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> SurfaceDeleteFaceFeature
Function that returns the specified SurfaceDeleteFaceFeature object using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (SurfaceDeleteFaceFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of SurfaceDeleteFaceFeature objects in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **DeleteFace Feature API Sample**: Demonstrates creating a new deleteFace feature.
