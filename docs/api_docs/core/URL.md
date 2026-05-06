# URL
Namespace: adsk.core
Inherits: Base
Since: April 2023

A URL object provides useful and easy-to-use methods for creating, modifying, and analyzing URLs.

**Accessed from:** CAMLibrary.childAssetURLs, CAMLibrary.childFolderURLs, CAMLibrary.createFolder, CAMLibrary.urlByLocation, CAMTemplateLibrary.childAssetURLs, CAMTemplateLibrary.childFolderURLs, CAMTemplateLibrary.createFolder, CAMTemplateLibrary.importTemplate, CAMTemplateLibrary.updateTemplate, CAMTemplateLibrary.urlByLocation, Machine.postURL, MachineFromLibraryInput.url, MachineLibrary.childAssetURLs, MachineLibrary.childFolderURLs, MachineLibrary.createFolder, MachineLibrary.importMachine, MachineLibrary.urlByLocation, MachineQuery.url, PostConfigurationQuery.url, PostLibrary.childAssetURLs, PostLibrary.childFolderURLs, PostLibrary.createFolder, PostLibrary.importPostConfiguration, PostLibrary.urlByLocation, PostProcessingMachineElement.postURL, PrintSettingLibrary.childAssetURLs, PrintSettingLibrary.childFolderURLs, PrintSettingLibrary.createFolder, PrintSettingLibrary.importPrintSetting, PrintSettingLibrary.urlByLocation, PrintSettingQuery.url, StockMaterialLibrary.childAssetURLs, StockMaterialLibrary.childFolderURLs, StockMaterialLibrary.createFolder, StockMaterialLibrary.importStockMaterial, StockMaterialLibrary.urlByLocation, ToolLibraries.childAssetURLs, ToolLibraries.childFolderURLs, ToolLibraries.createFolder, ToolLibraries.importToolLibrary, ToolLibraries.urlByLocation, ToolQuery.url, ToolQueryResult.toolLibraryURL, URL.create, URL.join, URL.parent

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(url: string) -> URL
Create a new URL by given string.
- **url** (string): The string is used to define the URL.
- **Returns** (URL): Returns the new URL object.

### join(path: string) -> URL
Join this URL with the given path and return the resulting URL. The operation does not alter the current URL. Join inserts a slash '/' to properly extend the path, so that "http://foo".join("bar") will return "http://foo/bar", not "http://foobar".
- **path** (string): The path to join to this URL.
- **Returns** (URL): Returns the joined URL.

### toString() -> string
Get the entire URL as string.
- **Returns** (string): Returns the entire URL as string.

## Properties

### isURLValid : boolean [read-only]
Check whether the URL is valid. Ensures that the URL is formatted with a protocol followed by a path which can be empty. The check is independent of the existence of the resource the URL may point to.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### leafName : string [read-only]
Get the leaf name of the URL, which is the section behind the last '/'.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : URL [read-only]
Get the parent URL, represented by the section before the last '/'.

### pathName : string [read-only]
Get the path name of the URL, including the last '/' of the protocol followed by the path of the URL.

### protocol : string [read-only]
Get the protocol scheme of the URL, including the final ':'.

## Samples
- **Hole and Pocket Recognition API Sample**: This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.
The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.
RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.
The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.
This script works only if the Manufacturing Extension is active.
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
- **Turning Workflow API Sample**: Turning Workflow API Sample
This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
