# ControllerConfigurationMachineElement
Namespace: adsk.cam
Inherits: MachineElement
Since: April 2023

Machine element representing controller settings for kinematics.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### staticTypeId() -> string
Identifying name for all elements of this type. Pass this to the itemByType or itemById methods of MachineElements to filter to elements of this type.
- **Returns** (string): Returns identifier of this type.

## Properties

### axisConfigurations : MachineAxisConfigurations [read-only]
Gets the collection of axis configuration objects.

### elementId : string [read-only]
Identifier for this element. Unique within an element type.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maxBlockProcessingSpeed : uinteger [read-write]
Maximum block processing rate for the controller.

### maxNormalSpeed : double [read-write]
Global maximum non-rapid linear motion speed. Units are cm/s.

### nonTcpRapidInterpolationMode : MachineNonTCPInterpolationMode [read-write]
Specifies how the CNC machine axes behave during rapid moves when TCP (Tool Center Point) is inactive, as defined in the machine's controller. Independent Axes moves the axes independently at maximum speed, potentially resulting in different completion times for each axis. Synchronized Axes moves the axes together, completing the motion simultaneously, although the tool's tip may deviate from the direct line between the start and finish points.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### tcpRapidInterpolationMode : MachineTCPInterpolationMode [read-write]
Specifies how the CNC machine axes behave during rapid moves when TCP (Tool Center Point) is active, as defined in the machine's controller. Independent Axes moves the axes independently at maximum speed, potentially resulting in different completion times for each axis. Synchronized Axes moves the axes together, completing the motion simultaneously, although the tool's tip may deviate from the direct line between the start and finish points. Tool Tip adjusts the linear axes to keep the tool's tip positioned along the direct line between the start and finish points.

### typeId : string [read-only]
Identifier for this type of machine element.
