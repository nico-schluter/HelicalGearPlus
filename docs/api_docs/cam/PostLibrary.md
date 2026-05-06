# PostLibrary
Namespace: adsk.cam
Inherits: CAMLibrary
Since: April 2023

The PostLibrary provides access to post configurations. Using this object you can import post configurations and get existing post configurations using either a URL or query to find specific post configurations.

**Accessed from:** CAMLibraryManager.postLibrary

## Methods

### childAssetURLs(url: URL) -> URL
Get all assets under given URL.
- **url** (URL): The URL to the parent folder.
- **Returns** (URL): Returns list of asset URLs at given location.

### childFolderURLs(url: URL) -> URL
Get all library folders under given URL.
- **url** (URL): The URL to the parent folder.
- **Returns** (URL): Returns list of folder URLs at given location.

### childPostConfigurations(url: URL) -> PostConfiguration
Get all posts by the given parent folder URL. Returns null, if the URL does not exist.
- **url** (URL): The URL of the folder to get post configurations from.
- **Returns** (PostConfiguration): Returns all children posts for a valid URL, returns null otherwise.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createFolder(parentUrl: URL, folderName: string) -> URL
Create a new folder in the library. Create the folder under given parent URL with given folder name. Add counting suffix, in case a folder with given name already exists. Throw an error if given URL does not point to a valid folder or the URL is read-only. Also throws an error if given folder name is empty.
- **parentUrl** (URL): The parent URL for the folder to be created.
- **folderName** (string): Name of the new folder to be created. Must not be empty.
- **Returns** (URL): Returns the URL to the newly created folder

### createQuery(location: LibraryLocations) -> PostConfigurationQuery
Creates a new PostConfigurationQuery that is used to query the library for post configurations matching the query.
- **location** (LibraryLocations): The location specifies the LibraryLocations where to search for in the post library.
- **Returns** (PostConfigurationQuery): Returns a new PostConfigurationQuery. The query is predefined by given parameter.

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

### importPostConfiguration(postConfig: PostConfiguration, destinationUrl: URL, postName: string) -> URL
Import a given post configuration at a specific location. The post configuration will be stored in the library. Throws an error, if the given URL is read-only.
- **postConfig** (PostConfiguration): The post configuration that should be imported.
- **destinationUrl** (URL): The URL to the folder where to save the post configuration.
- **postName** (string): The name of the post configuration that should be created due to the import. The name can be extended if the name already exists at given location to ensure a unique name.
- **Returns** (URL): Returns the URL of the newly imported post configuration, or null if the import failed.

### postConfigurationAtURL(url: URL) -> PostConfiguration
Get a specific post configuration by the given URL. Returns null, if the URL does not exist.
- **url** (URL): The URL to the post configuration to be loaded.
- **Returns** (PostConfiguration): Returns the post configuration for a valid URL, returns null otherwise.

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
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
- **Turning Workflow API Sample**: Turning Workflow API Sample
This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
