# ChamferFeature
Namespace: adsk.fusion
Inherits: Feature
Since: November 2014

Object that represents an existing chamfer feature in a design.

**Accessed from:** ChamferFeature.createForAssemblyContext, ChamferFeature.nativeObject, ChamferFeatures.add, ChamferFeatures.item, ChamferFeatures.itemByName, ChamferTypeDefinition.parentFeature, DistanceAndAngleChamferTypeDefinition.parentFeature, EqualDistanceChamferTypeDefinition.parentFeature, TwoDistancesChamferTypeDefinition.parentFeature

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> ChamferFeature
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (ChamferFeature): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes the feature. This works for both parametric and non-parametric features.
- **Returns** (boolean): Returns a bool indicating if the delete was successful or not.

### dissolve() -> boolean
Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.
- **Returns** (boolean): Returns a bool indicating if the dissolve was successful or not.

### setDistanceAndAngle(distance: ValueInput, angle: ValueInput) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Changes the type of chamfer to be a distance and angle chamfer.
- **distance** (ValueInput): A ValueInput object that defines the distance of the chamfer. This distance is along the face which is on the right of the selected edge. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in"). If no units are specified it is interpreted using the current default units for length.
- **angle** (ValueInput): A valueInput object that defines the angle. The direction will be towards to the face which is on the left of the selected edge. This can be a string or a value. If it's a string it is interpreted using the current document units and can include equations. For example all of the following are valid as long as they result in angle units; "45", "45 deg", "a1 / 2". If a value is input it is interpreted as radians. It cannot be negative.
- **Returns** (boolean): Returns true if the feature is successfully changed

### setEqualDistance(distance: ValueInput) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Changes the type of chamfer to be an equal distance chamfer.
- **distance** (ValueInput): A ValueInput object that defines the distance of the chamfer. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in"). If no units are specified it is interpreted using the current default units for length.
- **Returns** (boolean): Returns true if the feature is successfully changed

### setTwoDistances(distanceOne: ValueInput, distanceTwo: ValueInput) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Changes the type of chamfer to be a two distances chamfer.
- **distanceOne** (ValueInput): A ValueInput object that defines the distanceOne of the chamfer. This distance is along the face which is on the left of the selected edge. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in"). If no units are specified it is interpreted using the current default units for length.
- **distanceTwo** (ValueInput): A ValueInput object that defines the distanceTwo of the chamfer. This distance is along the face which is on the right of the selected edge. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in"). If no units are specified it is interpreted using the current default units for length.
- **Returns** (boolean): Returns true if the feature is successfully changed

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this face.

### baseFeature : BaseFeature [read-only]
If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null.

### bodies : BRepBodies [read-only]
Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

For a BaseFeature, this property has two different behaviors depending on if the BaseFeature is active for edit or not. When the base feature is active, this property returns the bodies owned by the base feature or the source bodies. When the base feature is not active, this property returns the result bodies.

When a body is added to a base feature, that body is owned by the base feature and is only seen in the UI when the base feature is active. This body is referred to as a "source body". Fusion creates a parametric copy of the body when you exit the base feature. This copy is referred to as the "result body," and it is used for subsequent modeling operations.

You can map between the source and result bodies by using their position within the bodies returned. To get a valid list of result bodies, you should roll the timeline to immediately after the base feature node in the timeline. Otherwise, subsequent operations could have done something to cause one or more bodies to no longer be available.

### chamferType : ChamferTypes [read-only]
This function is retired. See more information in the 'Remarks' section below.

Gets an enum indicating how the chamfer was defined. The valid return values are EqualDistanceType, TwoDistancesType and DistanceAndAngleType. This property returns nothing in the case where the feature is non-parametric.

### chamferTypeDefinition : ChamferTypeDefinition [read-only]
This function is retired. See more information in the 'Remarks' section below.

Gets the definition object that is defining the type of chamfer. Modifying the definition object will cause the chamfer to recompute. Various types of definition objects can be returned depending on how the chamfer is defined. The ChamferType property can be used to determine which type of definition will be returned. This property returns nothing in the case where the feature is non-parametric.

### cornerType : ChamferCornerTypes [read-write]
Gets and sets the type of corner to be modeled when multiple edges connect at a vertex.

### edges : ObjectCollection [read-write]
This function is retired. See more information in the 'Remarks' section below.

Gets and sets the edges being chamfered. Specific edges can be defined using one or more BRepEdge objects or BRepFace objects can be used to chamfer all edges of the face or Feature objects can be used to chamfer all edges associated with the input features. If BRepEdge objects are provided and the isTangentChain argument is true additional edges may also get chamfered if they are tangentially connected to any of the input edges. When getting the property, your code should check for the different types in the returned collection and handle it appropriately.

To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

This property returns nothing in the case where the feature is non-parametric.

### edgeSets : ChamferEdgeSets [read-only]
Returns the edge sets associated with this chamfer.

### entityToken : string [read-only]
Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### errorOrWarningMessage : string [read-only]
Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string.

### faces : BRepFaces [read-only]
Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available.

### healthState : FeatureHealthStates [read-only]
Returns the current health state of the feature.

### isParametric : boolean [read-only]
Indicates if this feature is parametric or not.

### isSuppressed : boolean [read-write]
Gets and sets if this feature is suppressed. This is only valid for parametric features.

### isTangentChain : boolean [read-write]
This function is retired. See more information in the 'Remarks' section below.

Gets and sets whether or not edges that are tangentially connected to the input edges (if any) will also be chamfered.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### linkedFeatures : FeatureList [read-only]
Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface.

### name : string [read-write]
Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric).

### nativeObject : ChamferFeature [read-only]
The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentComponent : Component [read-only]
Returns the parent component that owns this feature.

### timelineObject : TimelineObject [read-only]
Returns the timeline object associated with this feature.
