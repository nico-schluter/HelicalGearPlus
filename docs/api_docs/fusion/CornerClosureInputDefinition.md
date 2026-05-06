# CornerClosureInputDefinition
Namespace: adsk.fusion
Inherits: Base
Since: January 2026

Defines the common input properties shared by both two-bend and three-bend corner closure features. This class provides the fundamental properties required for any corner closure operation, including miter gap, alignment settings, and bend transition behavior.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### bendTransition : CornerBendTransitionTypes [read-write]
Gets and sets the bend transition type for the corner closure. This determines how the bend transitions are handled at the corner intersection. The default value is TrimToBendCornerBendTransitionType.

### isExtendAligned : boolean [read-write]
Gets and sets a value indicating whether the corner closure extends aligned to the edges. When true, the corner closure will extend in alignment with the adjacent edges. When false, the corner closure will use the default extension behavior. The default value is true.

### isUseSheetMetalRuleMiterGap : boolean [read-write]
Gets and sets whether to use the miter gap value from the Sheet Metal Rule. When true, the miter gap value is taken from the active Sheet Metal Rule and any value set in the miterGap property is ignored. When false (default), the behavior depends on the miterGap property: - If miterGap is set: uses the specified value - If miterGap is not set (null): uses the value from the Sheet Metal Rule as a fallback The default value is false.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### miterGap : ValueInput [read-write]
Gets and sets the gap distance for the miter in the corner closure. This value defines the spacing between the sheets at the corner miter joint. If this property is not set (null) and useSheetMetalRuleMiterGap is false, the miter gap value will be taken from the Sheet Metal Rule as a fallback.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
