# ConstructionAxis
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

ConstructionAxis Object

**Accessed from:** BaseFeature.constructionAxes, Component.xConstructionAxis, Component.yConstructionAxis, Component.zConstructionAxis, ConstructionAxes.add, ConstructionAxes.item, ConstructionAxes.itemByName, ConstructionAxis.createForAssemblyContext, ConstructionAxis.nativeObject, ConstructionAxisByLineDefinition.parentConstructionAxis, ConstructionAxisCircularFaceDefinition.parentConstructionAxis, ConstructionAxisDefinition.parentConstructionAxis, ConstructionAxisEdgeDefinition.parentConstructionAxis, ConstructionAxisNormalToFaceAtPointDefinition.parentConstructionAxis, ConstructionAxisPerpendicularAtPointDefinition.parentConstructionAxis, ConstructionAxisTwoPlaneDefinition.parentConstructionAxis, ConstructionAxisTwoPointDefinition.parentConstructionAxis, FlatPatternComponent.xConstructionAxis, FlatPatternComponent.yConstructionAxis, FlatPatternComponent.zConstructionAxis

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> ConstructionAxis
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (ConstructionAxis): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes the construction axis.
- **Returns** (boolean): Returns a bool indicating if the delete was successful or not.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this construction axis.

### baseFeature : BaseFeature [read-only]
If this construction axis is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null.

### component : Component [read-only]
Returns the component this construction plane belongs to.

### definition : ConstructionAxisDefinition [read-only]
Returns the construction axis definition object which provides access to the information defining the construction axis.

### deriveFeature : DeriveFeature [read-only]
Returns the DeriveFeature if this construction axis is derived from another design. This property returns null if the construction axis is not derived from another design (i.e. isDerived property returns false).

### entityToken : string [read-only]
Returns a token for the ConstructionAxis object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same construction axis.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### errorOrWarningMessage : string [read-only]
Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string.

### geometry : InfiniteLine3D [read-only]
Returns an infinite line that represents the position and orientation of the construction axis. This geometry is defined in the AssemblyContext of this ConstructionAxis.

### healthState : FeatureHealthStates [read-only]
Returns the current health state of this construction axis.

### isDeletable : boolean [read-only]
Indicates if this construction axis can be deleted. Base construction axes can not be deleted.

### isDerived : boolean [read-only]
Returns if this construction axis is derived from another design. If true, the construction axis cannot be deleted. You should not attempt to make any edits to the derived construction axis. Any edits made to this derived construction axis will be lost when the derive updates.

### isLightBulbOn : boolean [read-write]
Indicates if the light bulb (as displayed in the browser) is on. A construction axis will only be visible if it's light bulb, and that of it's containing folder and parent component/s are also on.

### isParametric : boolean [read-only]
Indicates if this construction axis is parametric or not.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-only]
Gets if the construction plane is visible. This property is affected by the AssemblyContext of the construction axis.

### name : string [read-write]
The name of the construction axis as it is shown in the browser.

### nativeObject : ConstructionAxis [read-only]
The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Returns the parent component or base feature. If both the design and the construction axis are parametric, the parent will be a component. If the design is parametric and the construction axis is not, the parent will be a base feature. If the design is not parametric the parent will be a component.

### timelineObject : TimelineObject [read-only]
Returns the timeline object associated with this construction axis.

## Samples
- **Construction Axis API Sample**: Demonstrates creating construction axis in various ways.
- **Create Setups From Hole Recognition API Sample**: This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.
The Fusion Manufacturing Extension is required for Hole Recognition.
The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector.
