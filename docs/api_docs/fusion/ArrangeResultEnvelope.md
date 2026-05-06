# ArrangeResultEnvelope
Namespace: adsk.fusion
Inherits: Base
Since: January 2025

The ArrangeResult object represents the results of an arrangement for a single envelope.

**Accessed from:** ArrangeOccurrenceResult.parentEnvelope, ArrangeResultEnvelopes.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### envelopeDefinition : ArrangeEnvelopeDefinition [read-only]
Returns the envelope definition that provides the settings for this envelope.

To use this property, you need to position the timeline marker immediately before the Arrange feature. This can be accomplished using the following code: arrangeFeature.timelineObject.rollTo(True)

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets and sets the name of the envelope as seen in the browser.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### occurrences : ArrangeOccurrenceResults [read-only]
Returns a collection object of the occurrences in this envelope.

### parentFeature : ArrangeFeature [read-only]
Returns the ArrangeFeature object this result is for.
