# AssemblyConstraint
Namespace: adsk.fusion
Inherits: Base
Since: July 2025

Represents an assembly constraint.

**Accessed from:** AssemblyConstraint.createForAssemblyContext, AssemblyConstraint.nativeObject, AssemblyConstraints.add, AssemblyConstraints.item, AssemblyConstraints.itemByName, Component.allAssemblyConstraints, FlatPatternComponent.allAssemblyConstraints

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> AssemblyConstraint
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (AssemblyConstraint): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes this assembly constraint.
- **Returns** (boolean): Returns true if the delete is successful.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this assembly constraint.

### entityToken : string [read-only]
Returns a token for the assembly constraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same assembly constraint.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### errorOrWarningMessage : string [read-only]
Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string.

### geometricRelationships : GeometricRelationships [read-only]
Returns the set of geometric relationships used for this assembly constraint.

### healthState : FeatureHealthStates [read-only]
Returns the current health state of the assembly constraint.

### isLightBulbOn : boolean [read-write]
Gets and sets if the light bulb of this assembly constraint, as displayed in the browser, is on or off. An assembly constraint will only be visible if the light bulb is switched on. However, the light bulb can be on and the assembly constraint still invisible if a higher level occurrence in the assembly context is not visible because its light bulb is off or the light bulb of the parent Joints folder is off.

### isSuppressed : boolean [read-write]
Gets and sets if this assembly constraint is suppressed. If suppressed, all of the assembly constraints within the will be suppressed.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-only]
Gets whether the assembly constraint is visible. To change the visibility see the isLightBulbOn property. This property is affected by the assembly context.

### name : string [read-write]
Gets and sets the name of the assembly constraint. This is the name seen in the browser and timeline.

### nativeObject : AssemblyConstraint [read-only]
The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentComponent : Component [read-only]
Returns the parent component that owns this assembly constraint.

### timelineObject : TimelineObject [read-only]
Returns the timeline object associated with this assembly constraint.
