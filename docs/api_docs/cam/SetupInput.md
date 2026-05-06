# SetupInput
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Object that represents an setup creation parameters. The input-object can be used from the Setups.add method to instantiate a new setup

**Accessed from:** Setups.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### fixtureEnabled : boolean [read-write]
Set this value to enable the use of fixtures for this setup. To then set the fixture models themselves use the `fixtures` property.

### fixtures : array [read-write]
An array of models that represent fixtures, where a model can be an Occurrence, BRepBody, or MeshBody.

The returned array is connected to the SetupInput and can be added to directly without needing to create a new array, populate it, and assign using this property, although, that is supported too.

### isUsingPreviousSetupData : boolean [read-write]
Get and set if data from the previous setup should be used when creating another setup. The data applied from the previous setup is machine information and the stock from the preceeding setup. By default this value is false.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### machine : Machine [read-write]
Gets and sets the Machine associated with the setup.

### models : array [read-write]
A list of models, where a model can be an Occurrence, BRepBody, or MeshBody. The returned array is connected to the SetupInput and can be added to directly without needing to create a new array, populate it, and assign it using this property, although, that is supported too.

### name : string [read-write]
Name of the new setup. This is displayed in the browser tree and can be used to access the setup from Setups.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### operationType : OperationTypes [read-only]
Operation Type for the setup

### parameters : CAMParameters [read-only]
Get all parameters for the setup to be created. Parameters are initialized by user defaults. Configure operation parameters before creation for a better performance.

### printSetting : PrintSetting [read-write]
Gets and sets the PrintSetting associated with the setup.

### stockMode : SetupStockModes [read-write]
StockMode for the setup.

### stockSolids : array [read-write]
An array of models, where a model can be an Occurrence, ManufacturingModel, BRepBody, or MeshBody. Setting this property, or adding the first object to the returned array will automatically set the stockMode to "SolidStock".

The returned array is connected to the SetupInput and can be added to directly without needing to create a new array, populate it, and assign it using this property, although, that is supported too.

## Samples
- **Additive Manufacturing MJF API Sample**: Demonstrates how to automate the creation of an additive MJF manufacturing setup and arrange components within the build volume of a 3D printer.


To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive Arrange using that manufacturing model as an input.


The setup will select an MJF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically arranged within the build volume of the selected MJF machine.
- **Create Setups From Hole Recognition API Sample**: This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.
The Fusion Manufacturing Extension is required for Hole Recognition.
The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector.
- **Hole and Pocket Recognition API Sample**: This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.
The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.
RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.
The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.
This script works only if the Manufacturing Extension is active.
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
- **Set Vise Origin As Setup WCS Origin API Sample**: This sample script demonstrates how to define our setup WCS origin relative to our vise origin from either a component, a sketch point or a joint origin.
The Work Coordinate System is a reference point set in our CAM workspace and on our machine. All machine coordinates are drawn from the WCS. This script demonstrates defining the WCS by each of 4 alternative methods:
Setup by default with no origin defined.
Setup using vise origin as WCS origin.
Setup using a sketch point as WCS origin.
Setup using a joint origin as WCS origin.
- **Turning Workflow API Sample**: Turning Workflow API Sample
This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
