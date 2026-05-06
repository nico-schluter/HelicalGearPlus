# TessellateFeatures
Namespace: adsk.fusion
Inherits: Base
Since: January 2025

Collection that provides access to all of the existing tessellate features in a component and supports the ability to create new tessellate features.

**Accessed from:** Features.tessellateFeatures

## Methods

### add(input: TessellateFeatureInput) -> TessellateFeature
Creates a tessellate feature.
- **input** (TessellateFeatureInput): A TessellateFeatureInput object that defines the desired tessellate feature. Use the createInput method to create a new TessellateFeatureInput object and then use methods on it (the TessellateFeatureInput object) to define the tessellate.
- **Returns** (TessellateFeature): Returns the newly created TessellateFeatureInput object or null if the creation failed. Returns nothing in the case where the feature is non-parametric.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(bodies: BRepBody[]) -> TessellateFeatureInput
Creates a TessellateFeatureInput object. Use properties and methods on this object to define the tessellation you want to create and then use the add method, passing in the TessellateFeatureInput object.
- **bodies** (BRepBody[]): A array with BReb bodies in either a parametric or direct modeling design.
- **Returns** (TessellateFeatureInput): Returns the newly created TessellateFeatureInput object or null if the creation failed.

### item(index: uinteger) -> TessellateFeature
Function that returns the specified tessellate feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (TessellateFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> TessellateFeature
Function that returns the specified Tessellate feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (TessellateFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of tessellate features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
