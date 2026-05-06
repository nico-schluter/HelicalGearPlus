# ConstructionPlane
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

ConstructionPlane Object

**Accessed from:** Arrange2DPlaneEnvelopeInput.plane, Arrange3DEnvelopeDefinition.plane, Arrange3DEnvelopeInput.plane, ArrangePlaneEnvelopeDefinition.plane, BaseFeature.constructionPlanes, Component.xYConstructionPlane, Component.xZConstructionPlane, Component.yZConstructionPlane, ConstructionPlane.createForAssemblyContext, ConstructionPlane.nativeObject, ConstructionPlaneAtAngleDefinition.parentConstructionPlane, ConstructionPlaneByPlaneDefinition.parentConstructionPlane, ConstructionPlaneDefinition.parentConstructionPlane, ConstructionPlaneDistanceOnPathDefinition.parentConstructionPlane, ConstructionPlaneMidplaneDefinition.parentConstructionPlane, ConstructionPlaneOffsetDefinition.parentConstructionPlane, ConstructionPlaneOffsetThroughPointDefinition.parentConstructionPlane, ConstructionPlanes.add, ConstructionPlanes.item, ConstructionPlanes.itemByName, ConstructionPlaneTangentAtPointDefinition.parentConstructionPlane, ConstructionPlaneTangentDefinition.parentConstructionPlane, ConstructionPlaneThreePointsDefinition.parentConstructionPlane, ConstructionPlaneTwoEdgesDefinition.parentConstructionPlane, FlatPatternComponent.xYConstructionPlane, FlatPatternComponent.xZConstructionPlane, FlatPatternComponent.yZConstructionPlane

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> ConstructionPlane
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (ConstructionPlane): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes the construction plane.
- **Returns** (boolean): Returns a bool indicating if the delete was successful or not.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this construction plane.

### baseFeature : BaseFeature [read-only]
If this construction plane is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null.

### component : Component [read-only]
Returns the component this construction plane belongs to.

### definition : ConstructionPlaneDefinition [read-only]
Returns the ConstructionPlaneDefinition object which provides access to the information defining this ConstructionPlane.

### deriveFeature : DeriveFeature [read-only]
Returns the DeriveFeature if this construction plane is derived from another design. This property returns null if the construction plane is not derived from another design (i.e. isDerived property returns false).

### displayBounds : BoundingBox2D [read-write]
Gets and sets the display size of the construction plane. The bounding box defines the min and max corners of the plane as defined in the 2D space of the construction plane.

### entityToken : string [read-only]
Returns a token for the ConstructionPlane object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same construction plane.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### errorOrWarningMessage : string [read-only]
Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string.

### geometry : Plane [read-only]
Returns a plane that represents the position and orientation of the construction plane. This geometry is defined in the AssemblyContext of this ConstructionPlane.

### healthState : FeatureHealthStates [read-only]
Returns the current health state of this construction plane.

### isDeletable : boolean [read-only]
Indicates if this construction plane can be deleted. Base construction planes can not be deleted.

### isDerived : boolean [read-only]
Returns if this construction plane is derived from another design. If true, the construction plane cannot be deleted. You should not attempt to make any edits to the derived construction plane. Any edits made to this derived construction plane will be lost when the derive updates.

### isLightBulbOn : boolean [read-write]
Indicates if the light bulb (as displayed in the browser) is on. A construction plane will only be visible if it's light bulb, and that of it's containing folder and parent component/s are also on.

### isParametric : boolean [read-only]
Indicates if this construction plane is parametric or not.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-only]
Indicates if the construction plane is visible. This property is affected by the AssemblyContext of the construction plane.

### name : string [read-write]
Returns the name of the construction plane as it is shown in the browser.

### nativeObject : ConstructionPlane [read-only]
The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Returns the parent component or base feature. If both the design and the construction plane are parametric, the parent will be a component. If the design is parametric and the construction plane is not, the parent will be a base feature. If the design is not parametric the parent will be a component.

### timelineObject : TimelineObject [read-only]
Returns the timeline object associated with this construction plane.

### transform : Matrix3D [read-write]
Returns the current position and orientation of the construction plane as a matrix. For a parametric construction plane, this property is read-only. For a construction plane in a direct modeling model or in a base feature, this is read-write and can be used to reposition the constructions plane.

## Samples
- **Construction Plane API Sample**: Demonstrates creating construction plane by different ways.
- **Loft Feature API Sample**: Demonstrates creating a new loft feature.
