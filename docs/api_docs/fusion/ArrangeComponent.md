# ArrangeComponent
Namespace: adsk.fusion
Inherits: Base
Since: January 2025

Defines a component within an arrangement. This specifies an occurrence along with additional arrangement information. This object is the API equivalent of a single line within the component list shown in the Arrange dialog. This object is used for both the creation of a new Arrange feature and querying and modifying an existing Arrange feature.

**Accessed from:** ArrangeComponents.add, ArrangeComponents.item, ArrangeFeature.unusedComponents, ArrangeOccurrenceResult.arrangeComponent

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this ArrangeComponent from the arrangement.
- **Returns** (boolean): Returns true if the deletion was successful.

### setRotationUsingEdge(edge: BRepEdge) -> boolean
Sets the rotation angle using the specified edge such that the edge is pointing in the zero rotation angle. This is a convenience method to set the rotation angle. The rotation property can be used to accomplish the same result.

This is only valid for 2D True Shape arrangements and will fail for 2D rectangular and 3D arrangements.
- **edge** (BRepEdge): The BRepEdge object being used to define rotation of the component.
- **Returns** (boolean): Returns true if successful.

## Properties

### isDirectionFlipped : boolean [read-write]
Specifies if the direction is flipped from it's default direction.

For a component defined by a face the default direction is defined by the selected face and the isGlobalDirectionFaceUp property of the Arrange2DDefinition associated with the parent ArrangeFeature object.

For a component defined by an occurrence, the default direction orients the occurrence such that the largest face points downward.

For a 3D arrange, this property is ignored and the orientation of the part is the same as it exists in the original assembly.

### isFiller : boolean [read-write]
Specifies if this component will be used to fill any left over empty space in the available envelopes.

This is only valid for 2D True Shape arrangements and is ignored for 2D rectangular and 3D arrangements.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### occurrence : Occurrence [read-only]
Returns the Occurrence associated with this ArrangeComponent. If an Occurrence was used to define this ArrangeComponent, this will return the same thing as the occurrenceOrFace. If a BRepFace was used to define this ArrangeComponent, this will return the Occurrence the face is in. This is a convenience property to make accessing the occurrence simpler.

### occurrenceOrFace : Base [read-only]
The BRepFace or Occurrence that was used to identify this ArrangeComponent.

### parentArrangeFeature : ArrangeFeature [read-only]
Returns the ArrangeFeature this ArrangeComponent is associated with. This property returns null in the case where a feature hasn't been created yet and there is only an ArrangeFeatureInput.

### priority : ArrangePriorities [read-write]
Specifies the nesting priority for this component.

For a 3D arrange, this property is ignored and setting it will fail.

### quantity : integer [read-write]
Specifies the quantity of this component to use in the arrange. This defaults to -1, which indicates that the global quantity is to be used.

For a 3D arrange, this property is ignored and the quantity is always one.

### rotation : double [read-write]
Gets and sets the rotation angle of this ArrangeComponent. The value is defined in Radians, is relative to the zero direction vector returned by the zeroDirectionVector property, and is in a counterclockwise direction.

This is only valid for 2D True Shape arrangements and is ignored for 2D rectangular and 3D arrangements.

### rotationType : ArrangeRotationTypes [read-write]
Gets and sets the rotation type for this ArrangeComponent. This defaults to use the global rotation type defined for the arrangement.

For a 3D arrange, this property is ignored.

### upDirection : Vector3D [read-only]
Returns a vector that is the up direction of this ArrangeComponent.

### zeroDirection : Vector3D [read-only]
Returns a vector that is the zero degree direction of this ArrangeComponent.
