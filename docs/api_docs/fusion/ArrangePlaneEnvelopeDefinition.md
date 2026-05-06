# ArrangePlaneEnvelopeDefinition
Namespace: adsk.fusion
Inherits: ArrangeEnvelopeDefinition
Since: January 2025

The ArrangePlaneEnvelope object represents an arrange envelope defined by a construction plane. This defines the settings of the envelope and the EnvelopeResult provides access to the resulting envelope and its contents.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### envelopeSpacing : ModelParameter [read-only]
Returns the parameter that controls the offset distance between envelopes when there is more than one. You can modify the value by using the properties on the returned ModelParameter object.

### frameWidth : ModelParameter [read-only]
Returns the parameter that controls the width of the envelope frame. This defines the offset distance of the objects from the edge of the frame. You can modify the value by using the properties on the returned ModelParameter object.

### isPartialArrangeAllowed : boolean [read-write]
Gets and sets if a partial arrange is allowed for this envelope.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### length : ModelParameter [read-only]
Returns the parameter that controls the length of the envelope frame. This defines the You can modify the value by using the properties on the returned ModelParameter object.

### objectSpacing : ModelParameter [read-only]
Returns the parameter that controls the space between objects in the arrangement. You can modify the value by using the properties on the returned ModelParameter object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### originXOffset : ModelParameter [read-only]
Returns the parameter that controls the X offset of the frame from the origin of the construction plane. You can modify the value by using the properties on the returned ModelParameter object.

### originYOffset : ModelParameter [read-only]
Returns the parameter that controls the Y offset of the frame from the origin of the construction plane. You can modify the value by using the properties on the returned ModelParameter object.

### parentArrange : ArrangeFeature [read-only]
Returns the parent ArrangeFeature this envelope is associated with.

### placementClearance : ModelParameter [read-only]
Returns the parameter that controls the offset of the objects from the base plane of the arrangement (the "up" direction). You can modify the value by using the properties on the returned ModelParameter object.

### plane : ConstructionPlane [read-write]
Gets and sets the ConstructionPlane the envelope is defined on.

### quantity : ModelParameter [read-only]
Returns the parameter that defines the number of envelopes that can be created. A value of -1 indicates that there is no limit.

### width : ModelParameter [read-only]
Returns the parameter that controls the width of the envelope frame. This defines the You can modify the value by using the properties on the returned ModelParameter object.
