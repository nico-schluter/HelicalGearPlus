# CustomFeatureDependencies
Namespace: adsk.fusion
Inherits: Base
Since: January 2021

A collection of dependencies associated with a particular custom feature. These are the entities that the custom feature is dependent on. If these entities are modified, it will cause the custom feature to recompute so it can be up to date. These dependencies are saved with the custom feature and can be accessed at a later time, typically during the compute, to access and use the entities.

**Accessed from:** CustomFeature.dependencies

## Methods

### add(id: string, entity: Base) -> CustomFeatureDependency
Adds an entity or parameter that this feature is dependent on. This is used by Fusion to know when to recompute this feature and to control the behavior of the feature's node in the timeline.
- **id** (string): An ID for this dependency. This is used to allow you to identify which dependency is which in the future. The ID must be unique with respect to the other dependencies of this custom feature.
- **entity** (Base): The entity or parameter you want to add as a dependency. This can be a BRepBody, BRepFace, BrepEdge, BRepVertex, a sketch, any sketch entities, a profile, any construction geometry, or any parameter.
- **Returns** (CustomFeatureDependency): Returns the created CustomFeatureDependency object and asserts if it failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteAll() -> boolean
Deletes all of the current dependencies. This method is for convenience and is equivalent to iterating through the collection and deleting them one at a time.
- **Returns** (boolean): Returns true if the operation was successful.

### item(index: uinteger) -> CustomFeatureDependency
Function that returns the specified custom dependency using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (CustomFeatureDependency): Returns the specified item or null if an invalid index was specified.

### itemById(id: string) -> CustomFeatureDependency
Function that returns the specified custom dependency given its ID.
- **id** (string): The ID of the dependency, which was assigned when the dependency was defined.
- **Returns** (CustomFeatureDependency): Returns the specified item or null if the specified ID was not found.

## Properties

### count : uinteger [read-only]
The number of CustomFeatureParameter objects in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
