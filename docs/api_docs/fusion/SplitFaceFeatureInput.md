# SplitFaceFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: June 2015

This class defines the methods and properties that pertain to the definition of a split face feature.

**Accessed from:** SplitFaceFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setAlongVectorSplitType(directionEntity: Base) -> boolean
Sets the split type to project the splitting tool along the direction defined by the specified entity.
- **directionEntity** (Base): An entity that defines the direction of projection of the splitting tool. This can be a linear BRepEdge, SketchLine, ConstructionLine, or a planar face where the face normal is used.
- **Returns** (boolean): Returns true is setting the split type was successful.

### setClosestPointSplitType() -> boolean
Sets the split type to be a curve that defined by projecting the splitting curve to the closest point on the surface.
- **Returns** (boolean): Returns true is setting the split type was successful.

### setSurfaceIntersectionSplitType(isSplittingToolExtended: boolean) -> boolean
Set the split type to be a surface to surface intersection. If the split tool is a curve it will be extruded into a surface to use in the split. If it's a surface, the surface will be used and optionally extended to fully intersect the faces to be split.
- **isSplittingToolExtended** (boolean): Specifies if the splitting tool should be extended so that is fully intersects the faces to be split.
- **Returns** (boolean): Returns true is setting the split type was successful.

## Properties

### facesToSplit : ObjectCollection [read-write]
Gets and sets the faces to be split. The collection can contain one or more faces selected from solid and/or open bodies.

### isSplittingToolExtended : boolean [read-write]
Gets and sets whether or not the splittingTool is to be automatically extended (if possible) so as to completely intersect the facesToSplit.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### splittingTool : Base [read-write]
Gets and sets the entity(s) that define the splitting tool(s). The splitting tool can be a single entity or an ObjectCollection containing solid and/or open bodies, construction planes, faces, or sketch curves that partially or fully intersect the faces that are being split.

### splitType : SplitFaceSplitTypes [read-only]
Returns the type of split type currently defined.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

## Samples
- **Split Face Feature API Sample**: Demonstrates creating a new split face feature.
