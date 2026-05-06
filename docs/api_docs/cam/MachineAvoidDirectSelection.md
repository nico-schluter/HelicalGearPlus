# MachineAvoidDirectSelection
Namespace: adsk.cam
Inherits: MachineAvoidSelectionBase
Since: September 2024

Machine/avoid direct selection class. Represents a group of direct selections that the users can make (faces, bodies, components and higher level entities). Provides access to the stored selections.

**Accessed from:** MachineAvoidGroups.createNewMachineAvoidDirectSelectionGroup

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### axialOffset : double [read-write]
Axial offset - sets the corresponding axial offset value based on the machine mode

### combinedOffset : double [read-write]
Combined offset - clearance and stock to leave based on the machine mode This only applies to strategies that use a single offset value (Advanced Swarf, Multi-Axis Clearing, Multi-Axis Finishing, Deburr and Geodesic)

### error : string [read-only]
Gets the last warning string encountered after the selection was applied to a parent.

### hasError : boolean [read-only]
Gets if errors were encountered when applying the selection to a a parent.

### hasWarning : boolean [read-only]
Gets if warnings were encountered when applying the selection to a parent.

### inputGeometry : array [read-write]
Get or set the value of the input geometry.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### machineMode : MachiningMode [read-write]
Desired machining mode. The default is Avoid. The current machining mode will determine which value the radial and axial offset functions refer to. When set to Machine, the radial and axial offset methods will read/set the stock to leave parameter. When set to Avoid, the radial and axial offset methods will read/set the clearance value, and the Fixture mode will map to the relative fixture clearance value.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### radialOffset : double [read-write]
Radial offset - sets the corresponding radial offset value based on the machine mode

### value : array [read-only]
Returns the resulting value of the selection. In general, this returns the input selection, but child classes can override the return value if needed. Refer to the child classes comments for further details. The collection may contain duplicates. For OperationInputs, the return value may not be the same as for Operations, as additional geometry selected by child classes is not evaluated for OperationInputs.

### warning : string [read-only]
Gets the last warning string encountered after the selection was applied to a parent.

## Samples
- **Avoid Machine Surface Settings API Sample**: This sample script demonstrates how to use Machine/Avoid/Gouge/Fixture functionality.
The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a curved surface with a through slot, a countersunk hole and a raised, circular and filleted upstand from the surface. The model is supported by two rectangular blocks, themselves mounted on a fixture plate. A setup is included with a single operation running a 3-axis diagonal raster over the model, supports and fixture. The operation machines the fixture, the supporting blocks, the upper surface of the upstand and the area within the slot and hole, something we would like to avoid.
The script duplicates the original operation and then proceeds to create a series of MachineAvoidGroups. These are labelled as either Machine in the case of 2 cap surfaces for the slot and hole, Fixture for the fixture plate, Gouge for the supporting blocks and Avoid for the top face of the upstand. Additionally, both AxialOffset and RadialOffset can be specified for the Machine, Avoid and Fixture passes.
- **Create Engravings Selection Sets API Sample**: This sample script demonstrates how to find and machine engravings in the Z+ direction using pocket recognition.
The script will first open an example model via its URN. Using pocket recognition, it will identify pockets that may be engravings based on their dimensions.
We assume here that an engraving pocket is:Made with a flat bottom face and no fillet.A closed pocket.Have a Z height less than 2 mm
We demonstrate creating selection sets in both design and manufacture workspaces and use one of the selection sets as an operation geometry selection input to generate an engraving operation.
The engraving toolpath can be seen by expanding the setup and selecting the operation.
