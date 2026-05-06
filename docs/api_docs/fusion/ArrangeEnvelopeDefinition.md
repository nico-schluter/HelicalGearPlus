# ArrangeEnvelopeDefinition
Namespace: adsk.fusion
Inherits: Base
Since: January 2025

The ArrangeEnvelope object is the base class for the different types of arrangement envelopes and provides access to the information that defines the envelope(s). This defines the settings of the envelope and the EnvelopeResult provides access to the resulting envelope and its contents.

**Accessed from:** Arrange3DResultEnvelope.envelopeDefinition, ArrangeFeature.envelopeDefinition, ArrangePlaneResultEnvelope.envelopeDefinition, ArrangeProfileOrFaceResultEnvelope.envelopeDefinition, ArrangeResultEnvelope.envelopeDefinition

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### frameWidth : ModelParameter [read-only]
Returns the parameter that controls the width of the envelope frame. This defines the offset distance of the objects from the edge of the frame. You can modify the value by using the properties on the returned ModelParameter object.

### isPartialArrangeAllowed : boolean [read-write]
Gets and sets if a partial arrange is allowed for this envelope.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectSpacing : ModelParameter [read-only]
Returns the parameter that controls the space between objects in the arrangement. You can modify the value by using the properties on the returned ModelParameter object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentArrange : ArrangeFeature [read-only]
Returns the parent ArrangeFeature this envelope is associated with.

### placementClearance : ModelParameter [read-only]
Returns the parameter that controls the offset of the objects from the base plane of the arrangement (the "up" direction). You can modify the value by using the properties on the returned ModelParameter object.
