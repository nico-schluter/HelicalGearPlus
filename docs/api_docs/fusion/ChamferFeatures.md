# ChamferFeatures
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

Collection that provides access to all of the existing chamfer features in a component and supports the ability to create new chamfer features.

**Accessed from:** Features.chamferFeatures

## Methods

### add(input: ChamferFeatureInput) -> ChamferFeature
Creates a new chamfer feature.
- **input** (ChamferFeatureInput): A ChamferFeatureInput object that defines the desired chamfer. Use the createInput method to create a new ChamferFeatureInput object and then use methods on it (the ChamferFeatureInput object) to define the chamfer.
- **Returns** (ChamferFeature): Returns the newly created ChamferFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(edges: ObjectCollection, isTangentChain: boolean) -> ChamferFeatureInput
This function is retired. See more information in the 'Remarks' section below.

Creates a ChamferFeatureInput object. Use properties and methods on this object to define the chamfer you want to create and then use the Add method, passing in the ChamferFeatureInput object.
- **edges** (ObjectCollection): The collection of edges that will be chamfered.
- **isTangentChain** (boolean): Boolean indicating if all edges that are tangentially connected to any of the input edges should be included in the chamfer or not.
- **Returns** (ChamferFeatureInput): Returns the newly created ChamferFeatureInput object or null if the creation failed.

### createInput2() -> ChamferFeatureInput
Creates a ChamferFeatureInput object. Use properties and methods on this object to define the chamfer you want to create and then use the Add method, passing in the ChamferFeatureInput object.
- **Returns** (ChamferFeatureInput): Returns the newly created ChamferFeatureInput object or null if the creation failed.

### item(index: uinteger) -> ChamferFeature
Function that returns the specified chamfer feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ChamferFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> ChamferFeature
Function that returns the specified chamfer feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (ChamferFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of chamfer features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Equal Distance Chamfer Feature API Sample**: Creates an equal distance chamfer on the selected edge. If there are tangent contiguous edges that will also be included in the chamfer.
