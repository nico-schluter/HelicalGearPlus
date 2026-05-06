# DataFolder
Namespace: adsk.core
Inherits: Base
Since: January 2015

A data folder that contains a collection of data items.

**Accessed from:** CloudFileDialog.dataFolder, CopyDesignFileInput.targetFolder, CopyFileInput.targetFolder, Data.activeFolder, Data.findFolderById, DataFile.parentFolder, DataFolder.parentFolder, DataFolders.add, DataFolders.asArray, DataFolders.item, DataFolders.itemById, DataFolders.itemByName, DataProject.rootFolder, DesignDataFile.parentFolder, NCProgram.fusionHubFolder

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this folder item.
- **Returns** (boolean): Returns true if the deletion was successful.

### uploadAssembly(filenames: string[]) -> DataFileFuture
Uploads a set of files that represent an assembly There should only be a single top-level assembly file but there can be any number of other files that represent sub-assemblies.
- **filenames** (string[]): An array of strings that contains the list of all of the files that are part of the assembly. The name of the top-level assembly file must be the first file in the array.
- **Returns** (DataFileFuture): The upload process is asynchronous which means that this method will return before the upload process had completed. The returned DataFileFuture object can be used to check on the current state of the upload to determine if it is still uploading, is complete, or has failed. If it is complete the final DataFinal can be retrieved through the DataFileFuture object.

### uploadFile(filename: string) -> DataFileFuture
Uploads a single file to this directory.
- **filename** (string): The full filename of the file to upload.
- **Returns** (DataFileFuture): The upload process is asynchronous which means that this method will return before the upload process had completed. The returned DataFileFuture object can be used to check on the current state of the upload to determine if it is still uploading, is complete, or has failed. If it is complete the final DataFinal can be retrieved through the DataFileFuture object.

## Properties

### dataFiles : DataFiles [read-only]
Returns a collection containing all of the items within this folder, excluding folders. Use the dataFolders property to get the folders.

### dataFolders : DataFolders [read-only]
Returns a collection containing all of the folders within this folder.

### id : string [read-only]
Returns the unique ID for this folder. This is the same id used in the APS Data Management API.

### isRoot : boolean [read-only]
Indicates if this folder is the root folder within the parent project.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets and sets the displayed name of this folder.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentFolder : DataFolder [read-only]
Returns the parent folder this folder is contained within. Returns null if this is the project's root folder.

### parentProject : DataProject [read-only]
Returns the parent project that owns this folder.
