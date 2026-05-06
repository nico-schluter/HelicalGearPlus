# OffsetFacesFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: November 2025

Object that represents an existing Offset Faces feature in a design. Offset Faces features are created in the UI using the "Offset Face" or "Press Pull" command.

**Accessed from:** OffsetFacesFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### distance : ValueInput [read-write]
The distance of the offset. A positive value offsets the faces in the direction of the face normal. A negative value goes in the other direction.

This is a ValueInput object that can be created using either createByReal or createByString. When a real ValueInput is used, the value is centimeters. When a string ValueInput is used, it defines the expression of the parameter that will be created to control the feature and any valid expression that defines a distance can be used.

### faces : array [read-write]
An array of BRepFace objects you want to offset. These faces can exist on multiple bodies and in multiple components. They cannot be in an externally referenced component.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.
