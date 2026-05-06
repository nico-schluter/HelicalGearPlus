# ArrangeComponents
Namespace: adsk.fusion
Inherits: Base
Since: January 2025

The collection of ArrangeComponent objects associated with an arrangement. This provides access to existing ArrangeComponent objects and supports adding new components to the the arrangement. An ArrangeComponent object defines an occurrence along with additional arrangement information. This object is used for both the creation of a new Arrange feature and querying and modifying an existing Arrange feature.

**Accessed from:** ArrangeFeature.arrangeComponents, ArrangeFeatureInput.arrangeComponents

## Methods

### add(occurrenceOrFace: Base) -> ArrangeComponent
Adds a new ArrangeComponent object to the collection.
- **occurrenceOrFace** (Base): For a 2D arrange this can be an Occurrence or BRepFace object that defines which component to use. If a BRepFace object is used, the face is used to orient the part in the arrangement and will face up or down depending on the isGlobalDirectionFaceUp property on the ArrangeFeature2DInput object.

For a 2D arrange, if an Occurrence is provided, the Occurrence will be oriented in the arrangement such that the largest face points downward.

For a 3D arrange this can be an Occurrence or BRepFace object but if a BRepFace is provided it does not define the orientation but is only used to get the parent Occurrence. For a 3D arrange the arranged occurrences have the same orientation as the original occurrence but are positioned within the 3D envelope.
- **Returns** (ArrangeComponent): Returns the created ArrangeComponent where you can use properties on it to define the various other settings supported to control how the component is arranged.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ArrangeComponent
Returns an ArrangeComponent object using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ArrangeComponent): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of ArrangeComponent objects in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
