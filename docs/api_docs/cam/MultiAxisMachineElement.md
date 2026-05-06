# MultiAxisMachineElement
Namespace: adsk.cam
Inherits: MachineElement
Since: September 2025

Machine element representing multi-axis machine settings.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createFeedrateSettings(input: MultiAxisFeedrateSettingsInput) -> MultiAxisFeedrateSettings
Creates a MultiAxisFeedrateSettings specialized object from the given input.
- **input** (MultiAxisFeedrateSettingsInput): The input object containing the settings to create the MultiAxisFeedrateSettings object. Set this object on the feedrateSettings property to apply the changes.
- **Returns** (MultiAxisFeedrateSettings): The specialized MultiAxisFeedrateSettings object created from the input.

### createFeedrateSettingsInput() -> MultiAxisFeedrateSettingsInput
Creates a MultiAxisFeedrateSettingsInput object to be used as input for creating MultiAxisFeedrateSettings objects.
- **Returns** (MultiAxisFeedrateSettingsInput): The MultiAxisFeedrateSettingsInput object

### createRetractAndReconfigureSettings() -> MultiAxisRetractAndReconfigureSettings
Creates a MultiAxisRetractAndReconfigureSettings object. Set this object on the retractAndReconfigureSettings property to apply the changes.
- **Returns** (MultiAxisRetractAndReconfigureSettings): The MultiAxisRetractAndReconfigureSettings object created.

### createSingularitySettings() -> MultiAxisSingularitySettings
Creates a MultiAxisSingularitySettings object. Set this object on the singularitySettings property to apply the changes.
- **Returns** (MultiAxisSingularitySettings): The MultiAxisSingularitySettings object created.

### deleteMe()
Delete this multi-axis machine element from the machine.

### staticTypeId() -> string
Identifying name for all elements of this type. Pass this to the itemByType or itemById methods of MachineElements to filter to elements of this type.
- **Returns** (string): Returns identifier of this type.

## Properties

### elementId : string [read-only]
Identifier for this element. Unique within an element type.

### feedrateSettings : MultiAxisFeedrateSettings [read-write]
The multi-axis feedrate settings for this machine. For changes to to this object to take effect, re-assign them to this property. Cannot be set to null.

### isUsingVirtualTooltip : boolean [read-write]
Specifies if the position of the virtual tool tip (tool end) should be output. Only relevant for rotary head axes.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### retractAndReconfigureSettings : MultiAxisRetractAndReconfigureSettings [read-write]
The multi-axis retract and reconfigure settings for this machine. For changes to to this object to take effect, re-assign them to this property. To not use multi-axis retract and reconfigure, set this to null.

### singularitySettings : MultiAxisSingularitySettings [read-write]
The multi-axis kinematics settings for this machine. For changes to to this object to take effect, re-assign them to this property. To not use multi-axis kinematics, set this to null.

### typeId : string [read-only]
Identifier for this type of machine element.
