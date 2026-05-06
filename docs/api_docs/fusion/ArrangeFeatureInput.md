# ArrangeFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: January 2025

The ArrangeFeatureInput object is the base class for the different types of input objects used to create an arrange feature.

**Accessed from:** ArrangeFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### set3DEnvelope(plane: ConstructionPlane, length: ValueInput, width: ValueInput, height: ValueInput) -> Arrange3DEnvelopeInput
Defines a 3D envelope input. Only a single envelope input can exist at time. Calling this method will cause any existing envelope input object to be invalid.
- **plane** (ConstructionPlane): The Construction plane the envelope will be on.
- **length** (ValueInput): The length of the envelope. This is the size of the envelope as measured along the X axis of the specified construction plane.

This value will become a parameter when the arrangement is created. If the ValueInput is created using a real number it is in centimeters. If you use a string, it is evaluated the same as a value would be in the command dialog and uses the current document units. For example, if the document units are inch and you specific "0.25" it will result in 1/4 inch clearance. Using a string, you can also specify the units as part of the expression, such as "0.25 in + 2 mm". And you can define equations like "PartSize + 2 mm" where "PartSize" is an existing parameter.
- **width** (ValueInput): The width of the envelope. This is the size of the envelope as measured along the Y axis of the specified construction plane.

This value will become a parameter when the arrangement is created. If the ValueInput is created using a real number it is in centimeters. If you use a string, it is evaluated the same as a value would be in the command dialog and uses the current document units. For example, if the document units are inch and you specific "0.25" it will result in 1/4 inch clearance. Using a string, you can also specify the units as part of the expression, such as "0.25 in + 2 mm". And you can define equations like "PartSize + 2 mm" where "PartSize" is an existing parameter.
- **height** (ValueInput): The height of the envelope. This is the size of the envelope as measured along the Z axis of the specified construction plane.

This value will become a parameter when the arrangement is created. If the ValueInput is created using a real number it is in centimeters. If you use a string, it is evaluated the same as a value would be in the command dialog and uses the current document units. For example, if the document units are inch and you specific "0.25" it will result in 1/4 inch clearance. Using a string, you can also specify the units as part of the expression, such as "0.25 in + 2 mm". And you can define equations like "PartSize + 2 mm" where "PartSize" is an existing parameter.
- **Returns** (Arrange3DEnvelopeInput): Returns the created Arrange3DEnvelopeInput object or null if the creation fails.

### setPlaneEnvelope(plane: ConstructionPlane, length: ValueInput, width: ValueInput) -> Arrange2DPlaneEnvelopeInput
Defines an envelope input defined by a plane for the arrange feature. Only a single envelope input can exist at a time. Calling this method will cause any existing envelope object input that has been created for this input to be invalid.
- **plane** (ConstructionPlane): The Construction plane the envelope will be on.
- **length** (ValueInput): The length of the envelope. This is the size of the envelope as measured along the X axis of the specified construction plane.

This value will become a parameter when the arrangement is created. If the ValueInput is created using a real number it is in centimeters. If you use a string, it is evaluated the same as a value would be in the command dialog and uses the current document units. For example, if the document units are inch and you specific "0.25" it will result in 1/4 inch clearance. Using a string, you can also specify the units as part of the expression, such as "0.25 in + 2 mm". And you can define equations like "PartSize + 2 mm" where "PartSize" is an existing parameter.
- **width** (ValueInput): The width of the envelope. This is the size of the envelope as measured along the Y axis of the specified construction plane.

This value will become a parameter when the arrangement is created. If the ValueInput is created using a real number it is in centimeters. If you use a string, it is evaluated the same as a value would be in the command dialog and uses the current document units. For example, if the document units are inch and you specific "0.25" it will result in 1/4 inch clearance. Using a string, you can also specify the units as part of the expression, such as "0.25 in + 2 mm". And you can define equations like "PartSize + 2 mm" where "PartSize" is an existing parameter.
- **Returns** (Arrange2DPlaneEnvelopeInput): Returns the created Arrange2DPlaneEnvelopeInput object or null if the creation fails.

### setProfileOrFaceEnvelope(profilesOrFaces: Base[]) -> Arrange2DProfileOrFaceEnvelopeInput
Defines an envelope defined by one or more profiles or planar faces. Only a single envelope input can exist at time. Calling this method will cause any existing envelope input object to be invalid.
- **profilesOrFaces** (Base[]): An array of Profile and planar BRepFace objects that define the shape of the available envelopes.
- **Returns** (Arrange2DProfileOrFaceEnvelopeInput): Returns the created Arrange2DProfileOrFaceEnvelopeInput object or null if the creation fails.

## Properties

### arrangeComponents : ArrangeComponents [read-only]
Returns the ArrangeComponents object associated with this input. Use this to add and define the components that will be arranged.

### definition : ArrangeDefinitionInput [read-only]
Returns a definition input object that provides access to the information to define an arrange feature. This will return different types of definition inputs depending on the solver type specified when creating the input.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### solverType : ArrangeSolverTypes [read-only]
Returns the arrange feature solver type defined by this input.
