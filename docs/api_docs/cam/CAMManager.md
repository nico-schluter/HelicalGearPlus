# CAMManager
Namespace: adsk.cam
Inherits: Base
Since: April 2023

This singleton object provides access to application-level events and properties that relate to the CAM (Manufacture) workspace in Fusion.

**Accessed from:** CAMManager.get

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### get() -> CAMManager
Access to the root CAMManager object.
- **Returns** (CAMManager): Return the root CAMManager object or null if it failed.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### libraryManager : CAMLibraryManager [read-only]
CAMLibraryManager provides access to properties related to various libraries in the Fusion Manufacture workspace, such as the post library and machine library.

### networkMachineIntegrationManager : NetworkMachineIntegrationManager [read-only]
Gets the NetworkMachineIntegrationManager needed to integrate add-ins into the 'Find network machines' dialog.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### postEnginePath : string [read-only]
Gets the absolute path to the post engine (post.exe) installed with Fusion.

## Samples
- **Additive Manufacturing FFF API Sample**: Demonstrates how to automate the creation of an additive FFF manufacturing setup and generate a toolpath.


To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive setup using that manufacturing model as an input.


The setup will select an FFF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically oriented and arranged within the build area of the selected FFF machine. This script will also create support structures, if required, based on the orientation of each component. Finally, the script generates the toolpath for the active setup and lets the user choose if they wish to post process the resulting toolpath or if they want to simulate it.
- **Additive Manufacturing MJF API Sample**: Demonstrates how to automate the creation of an additive MJF manufacturing setup and arrange components within the build volume of a 3D printer.


To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive Arrange using that manufacturing model as an input.


The setup will select an MJF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically arranged within the build volume of the selected MJF machine.
- **Additive Manufacturing SLA API Sample**: Demonstrates how to automate the creation of an additive SLA manufacturing setup.


To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive setup using that manufacturing model as an input.


The setup will select a SLA 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically oriented and arranged within the build area of the selected SLA machine. This script will also create support structures, based on the orientation of each component.


The support and orientation operations are created from a template. The script further demonstrates how to wrap script code into a command such that only one undo entry is created for the entire script instead of one entry per internal action.
- **Hole and Pocket Recognition API Sample**: This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.
The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.
RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.
The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.
This script works only if the Manufacturing Extension is active.
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
- **Turning Workflow API Sample**: Turning Workflow API Sample
This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
