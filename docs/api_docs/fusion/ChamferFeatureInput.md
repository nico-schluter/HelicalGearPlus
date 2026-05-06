# ChamferFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

This class defines the methods and properties that pertain to the definition of a chamfer feature.

**Accessed from:** ChamferFeatures.createInput, ChamferFeatures.createInput2

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setToDistanceAndAngle(distance: ValueInput, angle: ValueInput) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Adds a set of edges to this input.
- **distance** (ValueInput): A ValueInput object that defines the distance of the chamfer. This distance is along the face which is on the right of the selected edge. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in"). If no units are specified it is interpreted using the current default units for length.
- **angle** (ValueInput): A valueInput object that defines the angle. The direction will be towards to the face which is on the left of the selected edge. This can be a string or a value. If it's a string it is interpreted using the current document units and can include equations. For example all of the following are valid as long as they result in angle units; "45", "45 deg", "a1 / 2". If a value is input it is interpreted as radians. It cannot be negative.
- **Returns** (boolean): Returns true if successful.

### setToEqualDistance(distance: ValueInput) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Adds a set of edges to this input.
- **distance** (ValueInput): A ValueInput object that defines the size of the chamfer. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in"). If no units are specified it is interpreted using the current default units for length.
- **Returns** (boolean): Returns true if the set of edges was successfully added to the ChamferFeatureInput.

### setToTwoDistances(distanceOne: ValueInput, distanceTwo: ValueInput) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Adds a set of edges to this input.
- **distanceOne** (ValueInput): A ValueInput object that defines the distanceOne of the chamfer. This distance is along the face which is on the left of the selected edge. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in"). If no units are specified it is interpreted using the current default units for length.
- **distanceTwo** (ValueInput): A ValueInput object that defines the distanceTwo of the chamfer. This distance is along the face which is on the right of the selected edge. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in"). If no units are specified it is interpreted using the current default units for length.
- **Returns** (boolean): Returns true if successful.

## Properties

### chamferEdgeSets : ChamferEdgeSets [read-only]
Returns the collection of edge sets for this chamfer feature input.

### cornerType : ChamferCornerTypes [read-write]
Gets and sets the type of corner to be modeled when multiple edges connect at a vertex.

### edges : ObjectCollection [read-write]
This function is retired. See more information in the 'Remarks' section below.

Gets and sets the collection of edges that will be chamfered.

To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### isTangentChain : boolean [read-write]
This function is retired. See more information in the 'Remarks' section below.

Gets and sets if any edges that are tangentially connected to any of chamfered edges will also be included in the chamfer.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

## Samples
- **Equal Distance Chamfer Feature API Sample**: Creates an equal distance chamfer on the selected edge. If there are tangent contiguous edges that will also be included in the chamfer.
