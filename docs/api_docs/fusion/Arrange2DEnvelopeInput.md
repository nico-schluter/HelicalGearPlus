# Arrange2DEnvelopeInput
Namespace: adsk.fusion
Inherits: ArrangeEnvelopeInput
Since: January 2025

The Arrange2DEnvelopeInput is a base class used to define the various settings common to the envelopes defined by a plane or by profiles and planar faces.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### frameWidth : ValueInput [read-write]
Specifies the minimum distance between the components in the arrangement and the envelope frame.

This value will become a parameter when the arrangement is created. If the ValueInput is created using a real number it is in centimeters. If you use a string, it is evaluated the same as a value would be in the command dialog and uses the current document units. For example, if the document units are inch and you specific "0.25" it will result in 1/4 inch clearance. You can also specify the units as part of the expression, such as "0.25 in + 2 mm". And you can define equations like "ToolDia + 2 mm" where "ToolDia" is an existing parameter.

### isFlipped : boolean [read-write]
Specifies if the arrangement of objects is so they are above or X-Y plane of the envelope. Defaults to false so the objects are above the construction plane, profile or face.

### isPartialArrangeAllowed : boolean [read-write]
Gets and sets if a partial arrange is allowed. If true, it will still create a result when there is not enough space on the envelope to fit all of the components. Components are arranged until all the available space is used up. The components that were not included in the partial arrangement are highlighted in the components list. If the envelope size increases, the arrangement recalculates to include the components that did not previously fit in the arrangement.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectSpacing : ValueInput [read-write]
Specifies the minimum clearance between components in the arrangement. for a 3D layout this also specified the distance between the components in the Z direction.

This value will become a parameter when the arrangement is created. If the ValueInput is created using a real number it is in centimeters. If you use a string, it is evaluated the same as a value would be in the command dialog and uses the current document units. For example, if the document units are inch and you specific "0.25" it will result in 1/4 inch clearance. You can also specify the units as part of the expression, such as "0.25 in + 2 mm". And you can define equations like "ToolDia + 2 mm" where "ToolDia" is an existing parameter.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### placementClearance : ValueInput [read-write]
Specifies the distance of the components and the bottom of the envelope. This raises the components above the X-Y plane of the specified construction plane.

This value will become a parameter when the arrangement is created. If the ValueInput is created using a real number it is in centimeters. If you use a string, it is evaluated the same as a value would be in the command dialog and uses the current document units. For example, if the document units are inch and you specific "0.25" it will result in 1/4 inch clearance. You can also specify the units as part of the expression, such as "0.25 in + 2 mm". And you can define equations like "ToolDia + 2 mm" where "ToolDia" is an existing parameter.
