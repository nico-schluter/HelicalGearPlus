# ExtendFeatures
Namespace: adsk.fusion
Inherits: Base
Since: June 2015

Collection that provides access to all of the existing Extend features in a component and supports the ability to create new Extend features.

**Accessed from:** Features.extendFeatures

## Methods

### add(input: ExtendFeatureInput) -> ExtendFeature
Creates a new extend feature.
- **input** (ExtendFeatureInput): An ExtendFeatureInput object that defines the desired extend feature. Use the createInput method to create a new ExtendFeatureInput object and then use methods on it (the ExtendFeatureInput object) to define the desired options for the extent feature.
- **Returns** (ExtendFeature): Returns the newly created ExtendFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(edges: ObjectCollection, distance: ValueInput, extendType: SurfaceExtendTypes, isChainingEnabled: boolean) -> ExtendFeatureInput
Creates an ExtendFeatureInput object. Use properties and methods on this object to define the extend feature you want to create and then use the Add method, passing in the ExtendFeatureInput object.
- **edges** (ObjectCollection): The surface edges to extend. Only the outer edges from an open body can be extended. The edges must all be from the same body. Depending on the extend type there can also be some limitations on the edges being input as described below for the extendType argument.
- **distance** (ValueInput): ValueInput object that defines the distance to extend the face/s. Natural and Tangent Extend types require a positive distance value. Perpendicular Extend Type supports either a positive or negative value to control the direction of the extend. A positive number results in the perpendicular extension being in the same direction as the positive normal of the connected faces.
- **extendType** (SurfaceExtendTypes): The extension type to use when extending the face(s). Input edges must be connected at endpoints when Tangent or Perpendicular Extend Types are used. Input edges need not be connected when Natural Extend type is used.
- **isChainingEnabled** (boolean): An optional boolean argument whose default is true. If this argument is true, all edges that are tangent or curvature continuous, and end point connected, will be found automatically and include in the set of edges to extend.

This is an optional argument whose default value is True.
- **Returns** (ExtendFeatureInput): Returns the newly created ExtendFeatureInput object or null if the creation failed.

### item(index: uinteger) -> ExtendFeature
Function that returns the specified extend feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ExtendFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> ExtendFeature
Function that returns the specified extend feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (ExtendFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of Extend features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **extendFeatures.add**: Demonstrates the extendFeatures.add method. To use this sample, have a design open that contains at least one surface body. When you run the sample, you will be prompted to select an open edge of the body.
- **Extend Feature API Sample**: Demonstrates creating a new extend feature.
