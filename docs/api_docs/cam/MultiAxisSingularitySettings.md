# MultiAxisSingularitySettings
Namespace: adsk.cam
Inherits: Base
Since: September 2025

Base class for multi-axis singularity settings.

**Accessed from:** MultiAxisMachineElement.createSingularitySettings, MultiAxisMachineElement.singularitySettings

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createLinearizationSettings() -> MultiAxisSingularityLinearizationSettings
Creates a MultiAxisSingularityLinearizationSettings object. Set this object on the linearizationSettings property to apply the changes.
- **Returns** (MultiAxisSingularityLinearizationSettings): The MultiAxisSingularityLinearizationSettings object created.

## Properties

### angle : double [read-write]
The minimum angular delta movement for the rotary axes before the singularity is adjusted. When fluctuations of the rotary axes are insignificant, this limit prevents adjustment of the tool axis vector. Typically set to 10 degrees or more. Value is in radians.

### cone : double [read-write]
The angular distance range between the tool axis vector and the singularity point before the singularity is adjusted. Typically, the angular distance is less than 5 degrees. The further the tool axis is from the singularity, the less visible the fluctuations in the rotary axes are. Value is in radians.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### linearizationSettings : MultiAxisSingularityLinearizationSettings [read-write]
The settings for linearization of moves around the singularity. See MultiAxisSingularityLinearizeMethod for more details. Set this to null to not use linearization. For changes to to this object to take effect, re-assign them to this property.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### tolerance : double [read-write]
The tolerance value for converting simultaneous multi-axis movements to linear movements when the tool axis is near a singularity.
