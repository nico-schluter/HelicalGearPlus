# ScaleFeatures
Namespace: adsk.fusion
Inherits: Base
Since: January 2015

Collection that provides access to all of the existing scale features in a component and supports the ability to create new scale features.

**Accessed from:** Features.scaleFeatures

## Methods

### add(input: ScaleFeatureInput) -> ScaleFeature
Creates a new scale feature.
- **input** (ScaleFeatureInput): A ScaleFeatureInput object that defines the desired scale. Use the createInput method to create a new ScaleFeatureInput object and then use methods on it (the ScaleFeatureInput object) to define the scale.
- **Returns** (ScaleFeature): Returns the newly created ScaleFeature object or null if the creation failed. Returns nothing in the case where the feature is non-parametric.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(inputEntities: ObjectCollection, point: Base, scaleFactor: ValueInput) -> ScaleFeatureInput
Creates a ScaleFeatureInput object. Use properties and methods on this object to define the scale you want to create and then use the Add method, passing in the ScaleFeatureInput object.
- **inputEntities** (ObjectCollection): This collection can contain sketches, BRep bodies and T-Spline bodies in parametric modeling. It can contain sketches, BRep bodies, T-Spline bodies, mesh bodies, root component and occurrences in non-parametric modeling.
- **point** (Base): Input a point as reference to scale. This can be a BRepVertex, a SketchPoint or a ConstructionPoint.
- **scaleFactor** (ValueInput): The ValueInput object that defines the scale factor for uniform scale.
- **Returns** (ScaleFeatureInput): Returns the newly created ScaleFeatureInput object or null if the creation failed.

### item(index: uinteger) -> ScaleFeature
Function that returns the specified scale feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ScaleFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> ScaleFeature
Function that returns the specified scale feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (ScaleFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of scale features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Scale Feature API Sample**: Demonstrates creating a new scale feature.
