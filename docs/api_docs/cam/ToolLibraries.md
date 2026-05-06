# ToolLibraries
Namespace: adsk.cam
Inherits: CAMLibrary
Since: April 2023

The ToolLibraries object provides utilities to access, import and update tool libraries.

**Accessed from:** CAMLibraryManager.toolLibraries

## Methods

### childAssetURLs(url: URL) -> URL
Get all assets under given URL.
- **url** (URL): The URL to the parent folder.
- **Returns** (URL): Returns list of asset URLs at given location.

### childFolderURLs(url: URL) -> URL
Get all library folders under given URL.
- **url** (URL): The URL to the parent folder.
- **Returns** (URL): Returns list of folder URLs at given location.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createFolder(parentUrl: URL, folderName: string) -> URL
Create a new folder in the library. Create the folder under given parent URL with given folder name. Add counting suffix, in case a folder with given name already exists. Throw an error if given URL does not point to a valid folder or the URL is read-only. Also throws an error if given folder name is empty.
- **parentUrl** (URL): The parent URL for the folder to be created.
- **folderName** (string): Name of the new folder to be created. Must not be empty.
- **Returns** (URL): Returns the URL to the newly created folder

### createQuery(location: LibraryLocations) -> ToolQuery
Creates a new ToolQuery that is used to query the library for tools matching the query.
- **location** (LibraryLocations): The location specifies the LibraryLocations where to search.
- **Returns** (ToolQuery): Returns a new ToolQuery. The query is predefined by given parameter.

### deleteAsset(url: URL) -> boolean
Delete asset by URL from the library. Throw an error if given URL does not point to a valid asset or the URL is read-only.
- **url** (URL): The URL to the asset that should be removed.
- **Returns** (boolean): Returns true if asset was deleted successfully, false otherwise

### deleteFolder(url: URL) -> boolean
Delete folder by URL from the library. Any content of the folder will also be deleted. Throw an error if given URL does not point to a valid folder or the URL is read-only.
- **url** (URL): The URL to the folder that should be removed.
- **Returns** (boolean): Returns true if folder was deleted successfully, false otherwise

### displayName(url: URL) -> string
Get the localized display name for a given URL. The URL must point to a folder.
- **url** (URL): The URL that defines the path to a folder.
- **Returns** (string): Returns localized display name for the folder. Returns empty string for invalid URL.

### doesPathExist(url: URL) -> boolean
Checks if the given URL points to an existing folder or asset in the library.
- **url** (URL): The URL to be checked.
- **Returns** (boolean): Returns true if the URL points to an existing folder or asset, false otherwise.

### importToolLibrary(toolLibrary: ToolLibrary, destinationUrl: URL, libraryName: string) -> URL
Import a given ToolLibrary from a specific location. The imported ToolLibrary can be accessed through this ToolLibraries object. Throws an error, if the given URL is read-only.
- **toolLibrary** (ToolLibrary): The ToolLibrary that should be imported.
- **destinationUrl** (URL): The URL to the parent folder where the imported tool library will be saved.
- **libraryName** (string): The name of the library that should be created due to the import. If the specified name already exists, a number will be added to the name to ensure it is unique.
- **Returns** (URL): Returns the URL of the newly imported tool library, or null if the import failed.

### toolLibraryAtURL(url: URL) -> ToolLibrary
Get a specific ToolLibrary by given URL. Returns null, if the URL does not exist.
- **url** (URL): The URL to the ToolLibrary to be loaded.
- **Returns** (ToolLibrary): Returns the ToolLibrary for a valid URL, returns null otherwise.

### updateToolLibrary(url: URL, toolLibrary: ToolLibrary) -> boolean
Update ToolLibrary in ToolLibraries. Overrides the URL by given ToolLibrary. Throws an error if the URL does not already point to an existing ToolLibrary.
- **url** (URL): The URL to the existing asset in the ToolLibraries that should be updated.
- **toolLibrary** (ToolLibrary): The ToolLibrary that should be persisted.
- **Returns** (boolean): Returns true if asset was updated successfully, false otherwise.

### urlByLocation(location: LibraryLocations) -> URL
Get the URL for a given LibraryLocations.
- **location** (LibraryLocations): The LibraryLocations to be converted into an URL.
- **Returns** (URL): Returns the URL for given location.

## Properties

### assetTypeName : string [read-only]
Get the name of the asset type which can be accessed by the library.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Basic Milling Workflow Sample**: Demonstrates the creation of a basic milling workflow from script
Demonstrates creating a setup, searching tool library to retrieve a tool, create a couple of machining operations and a NC program, ready for post processing.
Use the 2D Strategies model from the Fusion CAM Samples folder as your CAD model.
- **Hole and Pocket Recognition API Sample**: This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.
The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.
RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.
The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.
This script works only if the Manufacturing Extension is active.
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
- **Turning Workflow API Sample**: Turning Workflow API Sample
This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
- **Wood Routing Workflow Sample**: This script demonstrates routing wood panels.
When running the sample, it assumes you have an open design containing one or more "panels" oriented flat in the X-Y plane. The script creates a setup and a 2D contour operation with tabs to route the panels from a standard sheet.
