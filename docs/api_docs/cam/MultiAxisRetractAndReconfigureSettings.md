# MultiAxisRetractAndReconfigureSettings
Namespace: adsk.cam
Inherits: Base
Since: September 2025

Settings for multi-axis retract and reconfigure.

**Accessed from:** MultiAxisMachineElement.createRetractAndReconfigureSettings, MultiAxisMachineElement.retractAndReconfigureSettings

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### retractPreference : MultiAxisRetractPreference [read-write]
The retract preference. See MultiAxisRetractPreference values for more details.

### rewindPreference : MultiAxisRewindPreference [read-write]
The rewind preferece. See MultiAxisRewindPreference values for more details.

### safePlungeFeedrate : double [read-write]
The safe plunge feedrate for plunge moves. A plunge rate is the speed at which the tool is driven down into the material when starting a cut. It varies depending on the tool and material. Plunging too fast may damage the tip of the cutter. (cm/min)

### safeRetractDistance : double [read-write]
The length of the retract moves along the tool axis, to perform a rewind.

### safeRetractFeedrate : double [read-write]
The safe retract feedrate for retract moves. (cm/min)

### stockExpansion : Vector3D [read-write]
Defines the stock expansion for computing retract moves in rewinds.
