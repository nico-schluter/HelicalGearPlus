# ThreadFeature
Namespace: adsk.fusion
Inherits: Feature
Since: January 2015

Object that represents an existing thread feature in a design. The creation of a tapped hole also results in the creation of a thread feature. There are some limitation when the thread feature is associated with a hole, which are described in the documentation for the property or method where the limitation exists.

**Accessed from:** HoleFeature.thread, RecognizedHoleSegment.threadFeatures, ThreadFeature.createForAssemblyContext, ThreadFeature.nativeObject, ThreadFeatures.add, ThreadFeatures.item, ThreadFeatures.itemByName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> ThreadFeature
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (ThreadFeature): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes the feature. This works for both parametric and non-parametric features.
- **Returns** (boolean): Returns a bool indicating if the delete was successful or not.

### dissolve() -> boolean
Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.
- **Returns** (boolean): Returns a bool indicating if the dissolve was successful or not.

### setThreadOffsetLength(threadOffset: ValueInput, threadLength: ValueInput, threadLocation: ThreadLocations) -> boolean
Sets the thread offset, length and location. Calling this method will cause the isFullLength property to be set to false.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **threadOffset** (ValueInput): A ValueInput object that defines the thread offset.
- **threadLength** (ValueInput): A ValueInput object that defines the thread length.
- **threadLocation** (ThreadLocations): Indicates where the thread length is measured from.
- **Returns** (boolean): Returns true if successful.

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

### hole : HoleFeature [read-only]
If this thread feature is was created as the result of creating a tapped hole, this property will return the associated hole feature. If this is a standard thread feature, this property will return null.

### inputCylindricalFace : BRepFace [read-write]
Gets and sets the threaded face. In the case where there are multiple faces, only the first one is returned. Setting this results in a thread being applied to only a single face. It is recommended that you use the inputCylindricalfaces property in order to have full access to the collection of faces to be threaded.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

If the thread feature is associated with a hole (the hole property is not null), this property will always return null and will fail if set.

### inputCylindricalFaces : ObjectCollection [read-write]
Gets and sets the cylindrical input faces.

To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

If the thread feature is associated with a hole (the hole property is not null), this property will always return null and will fail if set.

### isFullLength : boolean [read-write]
Gets and sets if this thread is the full length of the cylinder. It only can be set to true.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### isModeled : boolean [read-write]
Gets and sets if the thread is physical or cosmetic thread. A value of true indicates a physical thread. It defaults to false.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### isParametric : boolean [read-only]
Indicates if this feature is parametric or not.

### isRightHanded : boolean [read-write]
Gets and sets if the thread is right or left-handed thread. A value of true indicates a right-handed thread. It defaults to true.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### isSuppressed : boolean [read-write]
Gets and sets if this feature is suppressed. This is only valid for parametric features.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### linkedFeatures : FeatureList [read-only]
Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface.

### name : string [read-write]
Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric).

### nativeObject : ThreadFeature [read-only]
The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentComponent : Component [read-only]
Returns the parent component that owns this feature.

### threadInfo : ThreadInfo [read-write]
Gets and sets the thread data. Also can edit the thread through the properties and methods on the ThreadInfo object.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### threadLength : ModelParameter [read-only]
Gets the parameter that controls the depth of the thread. Even though the parameter for the thread depth is always created and accessible through this property, it is only used in the case where the isFullLength property is false. Returns nothing in the case where the feature is non-parametric.

### threadLocation : ThreadLocations [read-write]
Gets and sets where the thread length is measured from. This property is only used in the case where the isFullLength property is false.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

If the thread feature is associated with a hole (the hole property is not null), this property will always return null and will always return LowEndThreadLocation and will fail if set.

### threadOffset : ModelParameter [read-only]
Gets the parameter that controls the offset value of the thread. The offset is the distance along the axis of the cylinder from the edge to the start of the thread, it is only used in the case where the isFullLength property is false. Returns nothing in the case where the feature is non-parametric.

### timelineObject : TimelineObject [read-only]
Returns the timeline object associated with this feature.

## Samples
- **Thread Feature API Sample**: Demonstrates creating a new thread feature.
