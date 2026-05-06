# DeriveFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: January 2026

This class defines the methods and properties that pertain to the definition of a derive feature.

**Accessed from:** DeriveFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### excludedEntities : array [read-write]
The array of entities that will be excluded from the sourceEntities. These can be any entity that is supported by derive. For example, BRepBody, MeshBody, Sketch, ConstructionPlane, Occurrence, Component(rootComponent), FlatPattern, Canvas etc.

### isIncludeComponentParameters : boolean [read-write]
Gets or sets whether all feature parameters from all selected components from the source design are derived or not.

### isIncludeFavoriteParameters : boolean [read-write]
Gets or sets whether favorite parameters in the source design are derived or not.

### isPlaceObjectsAtOrigin : boolean [read-write]
Gets or sets whether to place all derived objects at the origin in the destination design or not.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### sourceDesign : Design [read-only]
The Design that is obtained from the input DataFile. You can use the API to access various elements within the design to add them to the list of elements to be derived.

### sourceEntities : array [read-write]
The array of entities that will be derived. These can be any entity that is supported by derive. For example, BRepBody, MeshBody, Sketch, ConstructionPlane, Occurrence, Component(rootComponent), FlatPattern, Canvas etc.
