# JointOriginInput
Namespace: adsk.fusion
Inherits: Base
Since: September 2015

Defines all of the information required to create a new joint origin. This object provides equivalent functionality to the Joint Origin command dialog in that it gathers the required information to create a joint origin.

**Accessed from:** JointOrigins.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### angle : ValueInput [read-write]
Gets and sets the value that defines the angle for the joint origin. This defaults to zero if it's not specified. The value defines an angle and if the ValueInput is defined using the createByReal method the value is assumed to be radians.

### geometry : JointGeometry [read-write]
Gets and sets the joint geometry for this joint origin input. This defines the location of the joint origin.

### globalOrientParamOne : ValueInput [read-write]
Gets and sets the value that defines the first global orient parameter for the joint origin. This defaults to zero if it's not specified. For Cylineder or cone, it represents the angle around the center axis. For Sphere and Torus, it represents the angle around the center axis. For Spline, it represents the U parameter.

### globalOrientParamTwo : ValueInput [read-write]
Gets and sets the value that defines the second global orient parameter for the joint origin. This defaults to zero if it's not specified. For Cylinder or cone, it is not used. For Sphere, it represents the polar angle, which is the angle between the radius line and the equator plane. For Torus, it represents the angle around the center of the section circle. For Spline, it represents the V parameter.

### isFlipped : boolean [read-write]
Gets and sets if the joint origin direction is flipped or not.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### offsetX : ValueInput [read-write]
Gets and sets the value that defines the X offset direction. This defaults to zero if it's not specified. The value defines a distance and if the ValueInput is defined using the createByReal method the value is assumed to be centimeters.

### offsetY : ValueInput [read-write]
Gets and sets the value that defines the Y offset direction. This defaults to zero if it's not specified. The value defines a distance and if the ValueInput is defined using the createByReal method the value is assumed to be centimeters.

### offsetZ : ValueInput [read-write]
Gets and sets the value that defines the Z offset direction. This defaults to zero if it's not specified. The value defines a distance and if the ValueInput is defined using the createByReal method the value is assumed to be centimeters.

### primaryAxisVector : Vector3D [read-only]
Returns the direction of the primary axis that's been calculated for this joint origin. This is conceptually the Z axis as shown by the triad representing the joint origin.

### secondaryAxisVector : Vector3D [read-only]
Returns the direction of the secondary axis that's been calculated for this joint origin. This is conceptually the X axis as shown by the triad representing the joint origin.

### thirdAxisVector : Vector3D [read-only]
Returns the direction of the third axis that's been calculated for this joint origin. This is conceptually the Y axis as shown by the triad representing the joint origin.

### xAxisEntity : Base [read-write]
Gets and sets the entity that defines the X axis direction. This defaults to null meaning the X axis is inferred from the input geometry.

### zAxisEntity : Base [read-write]
Gets and sets the entity that defines the Z axis direction. This defaults to null meaning the Z axis is inferred from the input geometry.

## Samples
- **Joint Origin Between Two Faces Sample**: Demonstrates creating a new Joint Origin between two planes.
- **Joint Origin Sample**: Demonstrates creating a new Joint Origin.
