# PipeFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: October 2023

This class defines the methods and properties that pertain to the definition of a Pipe feature.

**Accessed from:** PipeFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### creationOccurrence : Occurrence [read-write]
In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the Pipe is created based on geometry (e.g. a path) in another component AND (the Pipe) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

### distanceOne : ValueInput [read-write]
Gets and sets the distance for the pipe created while following the path given as input, in the same order. This value defaults to 1.0 if not set.

If the path is open, setting this to a value between 0.0 and 1.0 decides the length of the created Pipe. If the path is closed, setting this value should not be higher than 1.0 - distanceTwo. Ex: Path is made of curves A-B-C-A. The distanceOne returns and sets the length of the pipe going from A-B-C-A.

This property returns null in the case where the feature is non-parametric.

### distanceTwo : ValueInput [read-write]
Gets and sets the distance for the pipe created while following the reversed path given as input. Before setting this value, distanceOne must be set.

If the path is open, getting this value returns null, and setting the value is ignored. If the path is closed, setting this value should not be higher than 1.0 - distanceOne. Ex: Path is made of curves A-B-C-A. The distanceTwo returns and sets the length of the pipe going from A-C-B-A.

This property returns null in the case where the feature is non-parametric.

### isHollow : boolean [read-write]
Specifies if the Pipe is hollow or not.

Setting this to true will default the sectionThickness to 0.1 cm.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### operation : FeatureOperations [read-write]
Gets and sets the type of operation performed by the Pipe.

### participantBodies : array [read-write]
Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.

If this property has not been set, the default behavior is that all bodies that are intersected by the feature will participate.

This property can return null in the case where the feature has not been fully defined so that possible intersecting bodies can be computed.

### path : Path [read-write]
Gets and sets the path to create the Pipe.

### sectionSize : ValueInput [read-write]
Gets and sets the section size of the Pipe.

### sectionThickness : ValueInput [read-write]
Gets and sets the section thickness of the Pipe.

Setting this will also set the isHollow setting to true.

### sectionType : PipeSectionTypes [read-write]
Gets and sets the section type of the Pipe. The type can be: Circular, Square, Triangular.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.
