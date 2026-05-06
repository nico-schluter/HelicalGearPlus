# EmbossFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: September 2025

This class defines the methods and properties that pertain to the definition of an emboss feature.

**Accessed from:** EmbossFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### creationOccurrence : Occurrence [read-write]
In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the emboss feature is created based on geometry (e.g. a profile and/or face(s)) in another component AND (the emboss feature) is not in the root component. The creationOccurrence is analogous to the active occurrence in the UI

### depth : ValueInput [read-write]
Gets and sets the ValueInput object that defines the depth of the emboss. A positive value results in the emboss protruding out of the body and the negative value results in the emboss going into the body.

### horizontalDistance : ValueInput [read-write]
Gets and sets the horizontal offset distance. This defaults to zero.

### inputFaces : array [read-write]
Gets and sets an array of BRepFace objects that define the faces the emboss will be performed on. By default, faces that are tangent to any of the input faces are also used. Use the isTangentChain property of the EmbossFeatureInput object to disable the use of tangent faces. If multiple inputFaces are provided, they must all be on the same body.

### isTangentChain : boolean [read-write]
Gets and sets whether any faces that are tangentially connected to any of the input faces will also be used. By default this property is true.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### profiles : array [read-write]
Gets and sets an array of Profile objects that define the shape of the emboss. The profile argument can be Profile and SketchText objects. When multiple objects are used, all profiles and sketch texts must be co-planar.

### rotationAngle : ValueInput [read-write]
Gets and sets the rotation angle. This defaults to zero.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

### verticalDistance : ValueInput [read-write]
Gets and sets the vertical offset distance. This defaults to zero.
