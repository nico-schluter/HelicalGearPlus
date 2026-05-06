# LoftSection
Namespace: adsk.fusion
Inherits: Base
Since: August 2016

A single loft section.

**Accessed from:** LoftDirectionEndCondition.parentLoftSection, LoftEndCondition.parentLoftSection, LoftFreeEndCondition.parentLoftSection, LoftPointSharpEndCondition.parentLoftSection, LoftPointTangentEndCondition.parentLoftSection, LoftSections.add, LoftSections.item, LoftSmoothEndCondition.parentLoftSection, LoftTangentEndCondition.parentLoftSection

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this LoftSection.

If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **Returns** (boolean): Returns true if the operation was successful.

### reorder(newIndex: integer) -> boolean
Repositions this section so that it has the new index specified.

If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **newIndex** (integer): The new index value. For example, passing in zero as the new index will make this the first section in the loft and (LoftSections.count - 1) will make it the last section. All other sections will be maintain their existing order but be shifted to allow space for this section.
- **Returns** (boolean): Returns true if the reorder operation was successful.

### setDirectionEndCondition(angle: ValueInput, weight: ValueInput) -> boolean
Sets the end condition to be defined by a direction and weight.

This is valid for sections defined with sketch curves.

If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **angle** (ValueInput): Input ValueInput object that specifies the direction by using an angle. This defaults to an angle of 0.0. If the ValueInput object is a string it must be an valid expression that can be evaluated as an angle. If the ValueInput is a value then it is in radians.

This is an optional argument whose default value is null.
- **weight** (ValueInput): Input ValueInput object that defines the weight or the amount of influence of end condition on the loft. This defaults to a value of 1.0. If the ValueInput object is a string it must be an valid expression that can be evaluated as a unitless value. In any case, the value must be greater than 0.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if the operation was successful.

### setFreeEndCondition() -> boolean
Sets the end condition to be a "Free" end condition. This is the default end condition when a new section is added.

This is valid for sections defined with all curve types.

If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **Returns** (boolean): Returns true if the operation was successful.

### setPointSharpEndCondition() -> boolean
Sets the end condition to be sharp where the section is a point. This is the default condition for a point section.

If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **Returns** (boolean): Returns true if the operation was successful.

### setPointTangentEndCondition(weight: ValueInput) -> boolean
Set the end condition to a tangent condition in the case where the section is a point.

If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **weight** (ValueInput): Input ValueInput object that defines the weight or the amount of influence of end condition on the loft. This defaults to a value of 1.0. If the ValueInput object is a string it must be an valid expression that can be evaluated as a unitless value. In any case, the value must be greater than 0.
- **Returns** (boolean): Returns true if the operation was successful.

### setSmoothEndCondition(weight: ValueInput) -> boolean
Sets the end condition to be smooth to the adjacent face. If the end profile is not defined by a BRepEdge, then this is ignored because there is no face to be smooth to.

This is only valid on the first or last section.

If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **weight** (ValueInput): Input ValueInput object that defines the weight or the amount of influence of end condition on the loft. This defaults to a value of 1.0. If the ValueInput object is a string it must be an valid expression that can be evaluated as a unitless value. In any case, the value must be greater than 0.
- **Returns** (boolean): Returns true if the operation was successful.

### setTangentEndCondition(weight: ValueInput) -> boolean
Sets the end condition to be tangent to the adjacent face. If the section is not defined by a BRepEdge, then this is ignored because there is no face to be tangent to.

This is only valid on the first or last profile.

If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **weight** (ValueInput): Input ValueInput object that defines the weight or the amount of influence of end condition on the loft. This defaults to a value of 1.0. If the ValueInput object is a string it must be an valid expression that can be evaluated as a unitless value. In any case, the value must be greater than 0.
- **Returns** (boolean): Returns true if the operation was successful.

## Properties

### endCondition : LoftEndCondition [read-only]
Returns the current end condition. This is only valid for the first and last section and when the result is not closed. In other cases this will return null. This returns one of the several objects derived from LoftEndCondition and represents the current end condition. You can edit the existing condition using properties on the returned object. You can change the end condition using one of the set methods on the LoftSection object.

If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### entity : Base [read-write]
Get and sets the entity that defines the section of the loft. This can be a BRepFace, Profile, Path, SketchPoint, ConstructionPoint, or an ObjectCollection of contiguous profiles.

If this LoftSection object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### index : integer [read-only]
The position of this LoftSection within the collection. The first section has an index of 0. This is also the order of how the section will be used in the loft. The order can be modified by using the reorder method.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
