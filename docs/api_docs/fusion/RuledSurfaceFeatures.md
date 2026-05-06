# RuledSurfaceFeatures
Namespace: adsk.fusion
Inherits: Base
Since: September 2020

Collection that provides access to all of the existing Ruled Surface features in a component and supports the ability to create new Ruled Surface features.

**Accessed from:** Features.ruledSurfaceFeatures

## Methods

### add(input: RuledSurfaceFeatureInput) -> RuledSurfaceFeature
Creates a new RuledSurface feature.
- **input** (RuledSurfaceFeatureInput): An RuledSurfaceFeatureInput object that defines the desired RuledSurface feature. Use the createInput method to create a new RuledSurfaceFeatureInput object and then use methods on it (the RuledSurfaceFeatureInput object) to define the desired options for the ruled surface feature.
- **Returns** (RuledSurfaceFeature): Returns the newly created RuledSurfaceFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(profile: Base, distance: ValueInput, angle: ValueInput, ruledSurfaceType: RuledSurfaceTypes, direction: Base) -> RuledSurfaceFeatureInput
Creates a RuledSurfaceFeatureInput object that defines the input needed to create a ruled surface feature. Use the input object to define the input to create the desired feature and then use the Add method, passing in the RuledSurfaceFeatureInput object.
- **profile** (Base): A Profile object that defines the sketch geometry or edges that define the shape of the ruled surface. The Component.createBRepEdgeProfile method is useful to create a profile defined from edges.
- **distance** (ValueInput): ValueInput object that defines the extension distance of the Ruled Surface..
- **angle** (ValueInput): ValueInput object that defines angle to use when creating the Ruled Surface. When the input is a real value, the units are radians.
- **ruledSurfaceType** (RuledSurfaceTypes): The Ruled Surface type (TangentRuledSurfaceType, NormalRuledSurfaceType, or DirectionRuledSurfaceType).
- **direction** (Base): If the ruled surface type is DirectionRuledSurfaceType, you must specify the direction. The direction is specified by providing a linear or planar entity. For example, a linear edge, construction axis, planar face, or construction plane can be used as input.

This is an optional argument whose default value is null.
- **Returns** (RuledSurfaceFeatureInput): Returns the newly created RuledSurfaceFeatureInput object or null if the creation failed.

### item(index: uinteger) -> RuledSurfaceFeature
Function that returns the specified ruled surface feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (RuledSurfaceFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> RuledSurfaceFeature
Function that returns the specified RuledSurface feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (RuledSurfaceFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of RuledSurface features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Ruled Surface Feature API Sample**: Demonstrates creating a new ruled surface feature.
