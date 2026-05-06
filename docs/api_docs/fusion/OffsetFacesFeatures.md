# OffsetFacesFeatures
Namespace: adsk.fusion
Inherits: Base
Since: June 2017

Collection that provides access to all of the existing Offset Faces features in a design. Offset Face features are created in the UI using the "Offset Face" or "Press Pull" command.

**Accessed from:** Features.offsetFacesFeatures

## Methods

### add(input: OffsetFacesFeatureInput) -> OffsetFacesFeature
Creates a new offset feature.
- **input** (OffsetFacesFeatureInput): An OffsetFacesFeatureInput object that defines the desired offset faces feature. Use the createInput method to create a new OffsetFacesFeatureInput object and then use methods on it (the OffsetFacesFeatureInput object) to define the offset feature.
- **Returns** (OffsetFacesFeature): Returns the newly created OffsetFacesFeature object or null if the creation failed. Returns nothing in the case where the feature is non-parametric.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(faces: BRepFace[], distance: ValueInput) -> OffsetFacesFeatureInput
Creates an OffsetFacesFeatureInput object. Use properties and methods on this object to define the offset feature you want to create and then use the add method, passing in the OffsetFacesFeatureInput object to create the feature.
- **faces** (BRepFace[]): An array of BRepFace objects to offset. These faces can exist on multiple bodies and in multiple components. They cannot be in an externally referenced component.
- **distance** (ValueInput): The distance of the offset. A positive value offsets the faces in the direction of the face normal. A negative value goes in the other direction.

This is a ValueInput object that can be created using either createByReal or createByString. When a real ValueInput is used, the value is centimeters. When a string ValueInput is used, it defines the expression of the parameter that will be created to control the feature and any valid expression that defines a distance can be used.
- **Returns** (OffsetFacesFeatureInput): Returns the newly created OffsetFacesFeatureInput object or null if the creation failed.

### item(index: uinteger) -> OffsetFacesFeature
Function that returns the specified Offset Face feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (OffsetFacesFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> OffsetFacesFeature
Function that returns the specified Offset Face feature using the name of the feature. Offset Face features are created in the UI using the "Press Pull" command.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (OffsetFacesFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of Offset Face features in the collection. Offset Face features are created in the UI using the "Press Pull" command.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
