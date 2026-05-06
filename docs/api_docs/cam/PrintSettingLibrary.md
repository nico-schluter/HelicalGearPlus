# PrintSettingLibrary
Namespace: adsk.cam
Inherits: CAMLibrary
Since: April 2023

The PrintSettingLibrary provides access to PrintSettings. Using this object you can import PrintSettings and get existing PrintSettings using either URL or query to find specific PrintSetting.

**Accessed from:** CAMLibraryManager.printSettingLibrary

## Methods

### childAssetURLs(url: URL) -> URL
Get all assets under given URL.
- **url** (URL): The URL to the parent folder.
- **Returns** (URL): Returns list of asset URLs at given location.

### childFolderURLs(url: URL) -> URL
Get all library folders under given URL.
- **url** (URL): The URL to the parent folder.
- **Returns** (URL): Returns list of folder URLs at given location.

### childPrintSettings(url: URL) -> PrintSetting
Get all PrintSettings by the given parent folder URL. Returns null, if the URL does not exist.
- **url** (URL): The URL of the folder to get PrintSettings from.
- **Returns** (PrintSetting): Returns the PrintSetting for a valid URL, returns null otherwise.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createFolder(parentUrl: URL, folderName: string) -> URL
Create a new folder in the library. Create the folder under given parent URL with given folder name. Add counting suffix, in case a folder with given name already exists. Throw an error if given URL does not point to a valid folder or the URL is read-only. Also throws an error if given folder name is empty.
- **parentUrl** (URL): The parent URL for the folder to be created.
- **folderName** (string): Name of the new folder to be created. Must not be empty.
- **Returns** (URL): Returns the URL to the newly created folder

### createQuery(location: LibraryLocations) -> PrintSettingQuery
Creates a new PrintSettingQuery that is used to query the library for PrintSettings matching the query.
- **location** (LibraryLocations): The location specifies the LibraryLocations where to search for in the PrintSetting library.
- **Returns** (PrintSettingQuery): Returns a new PrintSettingQuery. The query is predefined by given parameter.

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

### importPrintSetting(printSetting: PrintSetting, destinationUrl: URL, printSettingName: string) -> URL
Import a given PrintSetting at a specific location. The PrintSetting will be stored in the library. Throws an error if the given URL is read-only.
- **printSetting** (PrintSetting): The PrintSetting that should be imported.
- **destinationUrl** (URL): The URL to the folder where to save the PrintSetting.
- **printSettingName** (string): The name that should be assigned to imported PrintSetting. The name can be extended if there already exists a PrintSetting at given location to ensure a unique name.
- **Returns** (URL): Returns the URL of the newly imported PrintSetting, or null if the import failed.

### printSettingAtURL(url: URL) -> PrintSetting
Get a specific PrintSetting by the given URL. Returns null if the URL does not exist.
- **url** (URL): The URL to the PrintSetting to be loaded.
- **Returns** (PrintSetting): Returns the PrintSetting for a valid URL, returns null otherwise.

### updatePrintSetting(url: URL, printSetting: PrintSetting) -> boolean
Update a PrintSetting in the library. The library overrides the URL by given PrintSetting. Throws an error if the URL does not already point to an existing printSetting.
- **url** (URL): The URL to the existing asset in the library that should be updated.
- **printSetting** (PrintSetting): The PrintSetting that should be persisted.
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
