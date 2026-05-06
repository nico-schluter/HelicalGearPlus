# VariableRadiusFilletEdgeSet
Namespace: adsk.fusion
Inherits: FilletEdgeSet
Since: November 2014

Provides access to the edges and the parameters associated with a variable radius fillet.

**Accessed from:** FilletEdgeSets.addVariableRadiusEdgeSet

## Methods

### addMidPosition(position: ValueInput, radius: ValueInput) -> boolean
Creates a new mid position radius on the variable radius edge set.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **position** (ValueInput): The position where the new radius is to be created. This is a value between 0 and 1 where 0 is at the start of the edge and 1 is at the end. If the ValueInput uses a real then it is interpreted as a unitless value. If it is a string then it must resolve to a unitless value.
- **radius** (ValueInput): A ValueInput object that defines the radius at the defined position. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in"). If no units are specified it will be interpreted using the current default units for length.
- **Returns** (boolean): Returns true if successful.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes the fillet edge set from the fillet.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **Returns** (boolean): Returns true if the operation was successful.

### deleteMidPosition(positionIndex: uinteger) -> boolean
Deletes the specified mid position from the variable radius fillet.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **positionIndex** (uinteger): The index of the mid position to delete. The points are in the order they appear along the edge where the first point has an index of 0. The number of mid positions and their locations can be obtained by getting the list of mid positions using the midPositions property.
- **Returns** (boolean): Returns true if successful.

## Properties

### continuity : SurfaceContinuityTypes [read-write]
Gets and sets the continuity of the fillet edge set. Valid values are TangentSurfaceContinuityType and CurvatureSurfaceContinuityType.

### edges : ObjectCollection [read-write]
Gets and sets an ObjectCollection containing the edges that are filleted.

To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### endRadius : ModelParameter [read-only]
Returns the model parameter that controls the end radius of the fillet. You can edit the end radius by using the properties on the returned ModelParameter object.

### isTangentChain : boolean [read-write]
Gets and sets the Tangent chain for fillet. This enables tangent chain option for fillet.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### midPositions : ParameterList [read-only]
Returns a list of model parameters that control the location of each mid point radius. These positions are defined from 0 to 1 where 0 is at the start of the edge and 1 is at the end. You can edit any of these positions by using the properties on its returned ModelParameter object.

### midRadii : ParameterList [read-only]
Returns a list of model parameters that control radius of the fillet at each position defined along the edge set. You can edit any of these radii by using the properties on its returned ModelParameter object. This list does not include the parameters for the start and end radii. Use the startRadius and endRadius properties to get those.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### startRadius : ModelParameter [read-only]
Returns the model parameter that controls the start radius of the fillet. You can edit the start radius by using the properties on the returned ModelParameter object.

### tangencyWeight : ModelParameter [read-only]
Returns the model parameter that controls the G1 or G2 tangency weight of the fillet. It must be a real value between 0.1 and 2.0 inclusive. You can edit the tangency weight by using the properties on the returned ModelParameter object.

## Samples
- **Fillet Feature Edit API Sample**: Demonstrates editing a fillet feature.
To successfully run this sample you can use this
