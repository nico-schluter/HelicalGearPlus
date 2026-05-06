# AdditivePlatformMachineElement
Namespace: adsk.cam
Inherits: MachineElement
Since: July 2023

Machine element representing the additive platform settings.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### staticTypeId() -> string
Identifying name for all elements of this type. Pass this to the itemByType or itemById methods of MachineElements to filter to elements of this type.
- **Returns** (string): Returns identifier of this type.

## Properties

### ceilingClearance : double [read-write]
Clearance height used for automatically arranging parts which is the distance from the top of the build platform. Units are cm.

### clearance : double [read-write]
Clearance height used for automatically arranging parts and suggested height for positioning part on the build platform. Units are cm.

### cornerRadius : double [read-write]
Radius used to round the corners of the build platform. Units are cm.

### elementId : string [read-only]
Identifier for this element. Unique within an element type.

### frameWidth : double [read-write]
Clearance width used for automatically arranging parts which is the distance from the edges of the build platform. Units are cm.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### origin : Point3D [read-write]
Origin point specifying the platform coordinates that correspond to the origin of the platform mesh. Units are cm.

### size : Point3D [read-write]
Usable platform size. Units are cm.

### typeId : string [read-only]
Identifier for this type of machine element.

## Samples
- **Additive Manufacturing MJF API Sample**: Demonstrates how to automate the creation of an additive MJF manufacturing setup and arrange components within the build volume of a 3D printer.


To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive Arrange using that manufacturing model as an input.


The setup will select an MJF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically arranged within the build volume of the selected MJF machine.
