# ExtrudeFeatures
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Collection that provides access to all of the existing extrude features in a design and supports the ability to create new extrude features.

**Accessed from:** Features.extrudeFeatures

## Methods

### add(input: ExtrudeFeatureInput) -> ExtrudeFeature
Creates a new extrude feature based on the information defined by the provided ExtrudeFeatureInput object. To create a new extrusion use the createInput function to create a new input object and use the methods and properties on that object to define the required input for an extrusion. Once the information is defined on the input object you can pass it to the Add method to create the extrusion.
- **input** (ExtrudeFeatureInput): The ExtrudeFeatureInput object that specifies the input needed to create a new extrude feature.
- **Returns** (ExtrudeFeature): Returns the newly created ExtrudeFeature or null if the creation failed.

### addSimple(profile: Base, distance: ValueInput, operation: FeatureOperations) -> ExtrudeFeature
Creates a basic extrusion that goes from the profile plane the specified distance.
- **profile** (Base): The profile argument can be a single Profile, a single planar face, a single SketchText object, or an ObjectCollection consisting of multiple profiles, planar faces, and sketch texts. When an ObjectCollection is used all of the profiles, faces, and sketch texts must be co-planar.

This method can only be used to create solid extrusions. To create a surface extrusion you need to use the add method.
- **distance** (ValueInput): ValueInput object that defines the extrude distance. A positive value extrudes in the positive direction of the sketch plane and negative value is in the opposite direction.
- **operation** (FeatureOperations): The feature operation to perform.
- **Returns** (ExtrudeFeature): Returns the newly created ExtrudeFeature or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(profile: Base, operation: FeatureOperations) -> ExtrudeFeatureInput
Creates a new ExtrudeFeatureInput object that is used to specify the input needed to create a new extrude feature.
- **profile** (Base): The profile argument can be a single Profile, a single planar face, a single SketchText object, or an ObjectCollection consisting of multiple profiles, planar faces, and sketch texts. When an ObjectCollection is used all of the profiles, faces, and sketch texts must be co-planar.

To create a surface (non-solid) extrusion, you can use the createOpenProfile and createBRepEdgeProfile methods of the Component object to create an open profile. You also need to set the isSolid property of the returned ExtrudeFeatureInput property to False.
- **operation** (FeatureOperations): The feature operation to perform.
- **Returns** (ExtrudeFeatureInput): Returns the newly created ExtrudeFeatureInput object or null if the creation failed.

### item(index: uinteger) -> ExtrudeFeature
Function that returns the specified extrude feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ExtrudeFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> ExtrudeFeature
Function that returns the specified extrude feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (ExtrudeFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of extrude features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Extrude Feature API Sample**: Demonstrates creating a new extrude feature.
- **Move Feature API Sample**: Demonstrates creating a new move feature.
- **Manage Participant Bodies API Sample**: Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also.
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
- **ReplaceFace Feature**: Demonstrates creating a new replaceface feature.
- **Shell Feature API Sample**: Demonstrates creating a new shell feature.
- **Simple Extrusion Sample**: Creates a new extrusion feature, resulting in a new component.
