# CAMTemplateLibrary
Namespace: adsk.cam
Inherits: CAMLibrary
Since: April 2023

The CAMTemplateLibrary provides access to templates. Using this object you can import templates and get existing templates using a URL.

**Accessed from:** CAMLibraryManager.templateLibrary

## Methods

### childAssetURLs(url: URL) -> URL
Get all assets under given URL.
- **url** (URL): The URL to the parent folder.
- **Returns** (URL): Returns list of asset URLs at given location.

### childFolderURLs(url: URL) -> URL
Get all library folders under given URL.
- **url** (URL): The URL to the parent folder.
- **Returns** (URL): Returns list of folder URLs at given location.

### childTemplates(url: URL) -> CAMTemplate
Get all templates by the given parent folder URL. Returns null if there is no folder at the URL.
- **url** (URL): The URL of the folder to get the templates from.
- **Returns** (CAMTemplate): Returns an array of templates contained within the specified folder URL. Returns null if the URL is not valid.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createFolder(parentUrl: URL, folderName: string) -> URL
Create a new folder in the library. Create the folder under given parent URL with given folder name. Add counting suffix, in case a folder with given name already exists. Throw an error if given URL does not point to a valid folder or the URL is read-only. Also throws an error if given folder name is empty.
- **parentUrl** (URL): The parent URL for the folder to be created.
- **folderName** (string): Name of the new folder to be created. Must not be empty.
- **Returns** (URL): Returns the URL to the newly created folder

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

### importTemplate(camTemplate: CAMTemplate, destinationUrl: URL) -> URL
Import a given template at a specific location. The template will be stored in the library. Throws an error if the given URL is read-only.
- **camTemplate** (CAMTemplate): The template that should be imported.
- **destinationUrl** (URL): The URL to the folder where to save the template.
- **Returns** (URL): Returns the URL of the newly imported template, or null if the import failed.

### templateAtURL(url: URL) -> CAMTemplate
Gets a specific template specified by the given URL. Returns null if the specified template does not exist.
- **url** (URL): The URL to the template to be fetched.
- **Returns** (CAMTemplate): Returns the template for a valid URL, returns null otherwise.

### updateTemplate(camTemplate: CAMTemplate, url: URL) -> URL
Update a template in the library. The library substitutes the existing template at the URL by given template. Throws an error if the URL does not already point to an existing template. If the name member of the CAMTemplate doesn't match the name portion of the URL then this will include a rename operation and the returned URL will reflect the new name.
- **camTemplate** (CAMTemplate): The template that should be persisted.
- **url** (URL): The URL to the existing template in the library that should be updated.
- **Returns** (URL): Returns the URL of the updated template, or null if the update failed.

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
- **Additive Manufacturing SLA API Sample**: Demonstrates how to automate the creation of an additive SLA manufacturing setup.


To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive setup using that manufacturing model as an input.


The setup will select a SLA 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically oriented and arranged within the build area of the selected SLA machine. This script will also create support structures, based on the orientation of each component.


The support and orientation operations are created from a template. The script further demonstrates how to wrap script code into a command such that only one undo entry is created for the entire script instead of one entry per internal action.
