# CornerClosureFeatures
Namespace: adsk.fusion
Inherits: Base
Since: January 2026

Collection that provides access to all of the existing corner closure features in a design and supports the ability to create new corner closure features.

**Accessed from:** Features.cornerClosureFeatures

## Methods

### add(input: CornerClosureFeatureInput) -> CornerClosureFeature
Creates a new Corner Closure feature.
- **input** (CornerClosureFeatureInput): A CornerClosureFeatureInput object that defines the desired corner closure. Use the createCornerClosureFeatureInput method to create a new CornerClosureFeatureInput object and then use methods on it (the CornerClosureFeatureInput object) to define the corner closure.
- **Returns** (CornerClosureFeature): Returns the newly created CornerClosureFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(dominantEdge: BRepEdge, submissiveEdge: BRepEdge) -> CornerClosureFeatureInput
Creates a CornerClosureFeatureInput object. Use methods on this object to define the corner closure you want to create and then use the add method, passing in the CornerClosureFeatureInput object.
- **dominantEdge** (BRepEdge): The BRepEdge that defines the dominant edge of the corner closure.
- **submissiveEdge** (BRepEdge): The BRepEdge that defines the submissive edge of the corner closure.
- **Returns** (CornerClosureFeatureInput): Returns the newly created CornerClosureFeatureInput object or null if the creation failed.

### item(index: uinteger) -> CornerClosureFeature
Function that returns the specified corner closure feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (CornerClosureFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> CornerClosureFeature
Function that returns the specified corner closure feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (CornerClosureFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of corner closure features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
