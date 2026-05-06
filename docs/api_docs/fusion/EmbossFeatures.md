# EmbossFeatures
Namespace: adsk.fusion
Inherits: Base
Since: September 2025

Collection that provides access to all of the existing emboss features in a component and supports the ability to create new emboss features.

**Accessed from:** Features.embossFeatures

## Methods

### add(input: EmbossFeatureInput) -> EmbossFeature
Creates a new emboss feature.
- **input** (EmbossFeatureInput): An EmbossFeatureInput object that defines the desired emboss feature. Use the createInput method to create a new EmbossFeatureInput object and then use methods on the EmbossFeatureInput object to define the emboss feature.
- **Returns** (EmbossFeature): Returns the newly created EmbossFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(profiles: Base[], faces: BRepFace[], depth: ValueInput) -> EmbossFeatureInput
Creates an EmbossFeatureInput object. Use properties and methods on this object to define the emboss feature you want to create and then use the Add method, passing in the EmbossFeatureInput object to create the feature.
- **profiles** (Base[]): An array of Profile objects that define the shape of the emboss. The profile argument can be Profile and SketchText objects. When multiple objects are used, all profiles and sketch texts must be co-planar.
- **faces** (BRepFace[]): An array of BRepFace objects that define the faces the emboss will be performed on. By default, faces that are tangent to any of the input faces are also used. Use the isTangentChain property on the input object to disable the use of tangent faces.
- **depth** (ValueInput): A ValueInput object that defines the depth of the emboss. A positive value results in the emboss protruding out of the body and a negative value results in the emboss going into the body.
- **Returns** (EmbossFeatureInput): Returns the newly created EmbossFeatureInput object or null if the creation failed.

### item(index: uinteger) -> EmbossFeature
Function that returns the specified emboss feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (EmbossFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> EmbossFeature
Function that returns the specified emboss feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (EmbossFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of emboss features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
