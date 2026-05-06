# CornerClosureFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: January 2026

This class defines the methods and properties that pertain to the definition of a corner closure feature.

**Accessed from:** CornerClosureFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setThreeBendCornerClosure(parameters: ThreeBendCornerClosureInputDefinition) -> boolean
Sets the corner closure input with the values to be used to create a three-bend corner closure feature. Before using this method, the definitionType property should be examined to determine whether the corner is two-bend or three-bend, as this method is only applicable for three-bend corner closures.
- **parameters** (ThreeBendCornerClosureInputDefinition): A ThreeBendCornerClosureParameters object that encapsulates all the required parameters for creating a three-bend corner closure feature. This includes miter gap, alignment settings, bend transition type, relief shape, and relief radius options.
- **Returns** (boolean): Returns true if defining the corner closure is successful.

### setTwoBendCornerClosure(parameters: TwoBendCornerClosureInputDefinition) -> boolean
Sets the corner closure input with the values to be used to create a two-bend corner closure feature. Before using this method, the definitionType property should be examined to determine whether the corner is two-bend or three-bend, as this method is only applicable for two-bend corner closures.
- **parameters** (TwoBendCornerClosureInputDefinition): A TwoBendCornerClosureParameters object that encapsulates all the required parameters for creating a two-bend corner closure feature. This includes miter gap, alignment settings, bend transition type, relief shape, relief size, and relief placement options.
- **Returns** (boolean): Returns true if defining the corner closure is successful.

## Properties

### definitionType : CornerClosureFeatureDefinitionTypes [read-only]
Gets the type of corner closure defined.

### dominantEdge : BRepEdge [read-write]
Gets and sets the dominant edge for the corner closure

After setting the edge, the definitionType property should be examined to determine whether the corner is two-bend or three-bend, as after the setting another edge the type of corner might be altered.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### submissiveEdge : BRepEdge [read-write]
Gets and sets the submissive edge for the corner closure

After setting the edge, the definitionType property should be examined to determine whether the corner is two-bend or three-bend, as after the setting another edge the type of corner might be altered.
