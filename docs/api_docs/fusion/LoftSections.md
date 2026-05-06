# LoftSections
Namespace: adsk.fusion
Inherits: Base
Since: August 2016

The set of two or more sections used to define the shape of the loft.

**Accessed from:** LoftFeature.loftSections, LoftFeatureInput.loftSections

## Methods

### add(entity: Base) -> LoftSection
Adds a new section to the loft. The initial end condition is "Free". Additional methods on the returned LoftSection can be used to further define the section.

If this LoftSections object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **entity** (Base): Specifies the BRepFace, Profile, Path, SketchPoint, ConstructionPoint, or an ObjectCollection containing a contiguous set of Profile objects that defines the section.
- **Returns** (LoftSection): Returns the newly created LoftSection object.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: integer) -> LoftSection
Function that returns the specified LoftSection using an index into the collection. They are returned in the same order that they are used in the loft. Their order can be modified using the reorder method of the LoftSection object.
- **index** (integer): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (LoftSection): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
The number of LoftSections in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Loft Feature API Sample**: Demonstrates creating a new loft feature.
