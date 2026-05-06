# DataFile
Namespace: adsk.core
Inherits: Base
Since: January 2015

A data file in a data folder.

**Accessed from:** CloudFileDialog.dataFile, CloudFileDialog.dataFiles, ConfigurationReplaceDesign.dataFile, Data.findFileById, DataEventArgs.file, DataFile.copy, DataFile.latestVersion, DataFileFuture.dataFile, DataFiles.asArray, DataFiles.item, DataFiles.itemById, DesignDataFile.copy, DesignDataFile.latestVersion, Document.dataFile, DocumentReference.dataFile, DrawingDocument.dataFile, FusionDocument.dataFile, Milestone.version, Occurrence.configuredDataFile, PersonalUseLimits.editableFiles

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy(targetFolder: DataFolder) -> DataFile
Copies this DataFile to the specified folder.
- **targetFolder** (DataFolder): The folder to copy this DataFile to.
- **Returns** (DataFile): Returns the copied DataFile if the copy was successful.

### copyWithInput(input: CopyFileInput) -> DataFileFuture
Executes the copy using the information defined by the provided CopyFileInput.
- **input** (CopyFileInput): The input object is of CopyFileInput object type, based on which our copy behavior will be defined. A CopyDesignFileInput object is created using the DataFile.createCopyDesignFileInput.
- **Returns** (DataFileFuture): The copy process is asynchronous which means that this method will return before the copy process has completed. The returned DataFileFuture object can be used to check on the current state of the copy to determine if it is still copying, is complete, or has failed. If it is complete the new DataFile that was created as a result of the copy can be retrieved through the DataFileFuture object.

### createCopyDesignFileInput(folder: DataFolder) -> CopyDesignFileInput
Creates a new CopyDesignFileInput object that is used to create a copy of a DataFile that represents a Fusion design. You set options on the CopyDesignFileInput object to define the behavior of the copy and call the copyWithInput method passing in the input object to create the copy.
- **folder** (DataFolder): The folder where the copied files will be created.
- **Returns** (CopyDesignFileInput): Returns the created CopyDesignFileInput object or null in the case of failure.

### createCopyFileInput(folder: DataFolder) -> CopyFileInput
Creates a new CopyFileInput object that is used to create a copy of any DataFile.
- **folder** (DataFolder): The folder where the copied file will be created.
- **Returns** (CopyFileInput): Returns the created CopyFileInput object or null in the case of failure.

### createDataVersion(versionDescription: string) -> boolean
Creates a version of this DataFile at tip.
- **versionDescription** (string): The versionDescription is visible in the History Panel.
- **Returns** (boolean): Returns true when Create Version Job is triggered.

### createMilestone(milestoneName: string) -> Milestone
Makes the version this DataFile represents a milestone.
- **milestoneName** (string): The name of the milestone as seen in the data panel and Fusion web client. If an empty string is provided, a default name will be used.
- **Returns** (Milestone): Returns the created Milestone object or null in the case of failure. One case of failure is if a milestone already exists for this version.

### deleteMe() -> boolean
Deletes this DataFile. This can fail if this file is referenced by another file or is currently open.
- **Returns** (boolean): Returns true if the deletion was successful.

### download(path: string, handler: DataEventHandler) -> boolean
Performs a synchronous or asynchronous download of this DataFile. Only DataFiles that represent non-Fusion data can be downloaded. For example, this will work for TXT or XLS files but will fail for F3D files.

When using this in its synchronous mode, Fusion is frozen during the download and the call will not return until the download is complete or has failed. When using this in its asynchronous mode, calling this method will start the download process and the call return before the download is complete. The event on the provided handler will be called notifying you when the download is complete.
- **path** (string): The full path and optionally the filename used on the local file system for the file. If the path doesn't exist it will be created. If only a path is specified, the name and file extension associated with the DataFile is used for the filename. You can also specify the full path, including the filename.
- **handler** (DataEventHandler): If you want to do an asynchronous download, provide the handler object to be called when this operation is complete. To call the method synchronously, set this argument to null/None.
- **Returns** (boolean): Returns True in synchronous mode if successful. Returns True in asynchronous mode if the download was successfully started.

### move(targetFolder: DataFolder) -> boolean
Moves this DataFile to the specified folder.
- **targetFolder** (DataFolder): The folder to move this DataFile to.
- **Returns** (boolean): Returns true if the move was successful.

### promote() -> boolean
Promotes this version to be the latest version. If this is the latest version, nothing happens.
- **Returns** (boolean): Returns true if successful.

### refresh(handler: DataEventHandler) -> boolean
Refreshes the data associated with a DataFile object to be up to date with the associated cloud data. The DataFile returned by the API reflects the local representation of the DataFile as used by the Data Panel. This is method is only useful in very limited cases and should rarely be used. In most cases the local representation will match the actual data on the cloud. In rare occasions where Fusion was off-line while the cloud processing of DataFile is completed or the DataFile is not in the folder shown in the Data Panel. Getting a DataFileFolder contents forces an update of the local data for all of the data files it contains so they will all be up to date.
- **handler** (DataEventHandler): If you want to do an asynchronous refresh, provide the handler object to be called when this operation is complete. To call the method synchronously, set this argument to null/None.
- **Returns** (boolean): Returns True in synchronous mode if successful. Returns True in asynchronous mode if the refresh was successfully started.

## Properties

### childReferences : DataFiles [read-only]
Returns a collection of DataFiles that are the children (referenced designs) this datafile references.

### configurationRowId : string [read-only]
Returns the ID of the row that defines this configuration. Use the isCongiguration property to determine if this Design is a configuration or not. If this is not a configuration, this property returns an empty string.

### configurationTable : Base [read-only]
If this file is a configured design or a configuration, this property returns the associated ConfigTable object. If this is not a configured design or configuration, this property returns null.

This property is typed as core.Base because the adsk.core library does not reference the fusion library where the ConfigurationTable object is defined. At runtime, this property will return a ConfigurationTable object.

### createdBy : User [read-only]
Returns the User that created this data file.

### dataObject : DataObjectFuture [read-only]
Starts the process to get the raw binary data associated with this DataFile. Because the data exists on the cloud, a DataObjectFuture is returned that you can use to monitor the state of downloading the data and then getting the raw data once it is available.

Only DataFiles that represent non-Fusion data can accessed. For example, this will work for TXT or XLS files but will fail for F3D files.

### dateCreated : uinteger [read-only]
Returns the date when this data file was created as UNIX epoch time. UNIX epoch time is the number of seconds since January 1, 1970 (midnight UTC/GMT).

In Python you can import the standard time module to work with UNIX epoch time.

In C++ you can use functions in time.h and std::chrono to work with UNIX epoch time.

### dateModified : uinteger [read-only]
Returns the date when this data file was modified. Most changes to a file result in a new version which means a new DataFile is created and will have a new creation date. There are a few changes, like rename, that modify a DataFile without creating a new version and the date of that change is returned by this property.

The date is returned as UNIX epoch time, which is the number of seconds since January 1, 1970 (midnight UTC/GMT). In Python you can import the standard time module to work with UNIX epoch time. In C++ you can use functions in time.h and std::chrono to work with UNIX epoch time.

### description : string [read-only]
Gets and sets the description information associated with this item.

### fileExtension : string [read-only]
Gets the file extension for this data file. The file type can be inferred from this.

### fusionWebURL : string [read-only]
Returns a URL that can be used to access the Fusion Web interface for this file within a browser. The person using the URL must have an Autodesk account and have authority to access the hub this file is owned by.

You can also use this URL to directly open the file in Fusion using the Fusion protocol handler as discussed in the Opening Files from a Web Page topic in the API user manual.

### hasChildReferences : boolean [read-only]
Gets if this datafile has children, (i.e. a Fusion Design containing referenced components).

### hasOutofDateChildReferences : boolean [read-only]
Gets if this datafile has Children (referenced components) that are out of date (not the latest version).

### hasParentReferences : boolean [read-only]
Gets if this datafile has parents, (i.e. this is a child being referenced in another Fusion design).

### id : string [read-only]
Returns the unique ID for this DataFile. This is the same id used in the APS Data Management API for an Item and is in the unencoded form and will look similar to this: "urn:adsk.wipprod:dm.lineage:hC6k4hndRWaeIVhIjvHu8w"

### inUseBy : array [read-only]
Returns the array of users that are currently using (have open for edit) this data file.

### isComplete : boolean [read-only]
Returns if the DataFile is fully processed. This is especially useful when a new file is being saved or uploaded. The initial call to save or upload the file returns when the process has started but processing continues on the cloud. This property will return true when all of the processing has been completed and all information related to the Datafile is now available.

### isConfiguration : boolean [read-only]
Gets if this file is a configuration of a configuration table. If this returns true, the configurationRowId can be used to get the row used to define this configuration. Also, when this is true, the design is essentially read-only and edits are either blocked from taking place or cannot be saved.

### isConfiguredDesign : boolean [read-only]
Gets if this file represents a configured design. This is a design where a configuration table is defined. Use the configurationTable property to get the associated table.

### isInUse : boolean [read-only]
Gets if this DataFile is currently in use (opened for edit) by any other user.

### isMilestone : boolean [read-only]
Returns if the version this Datafile represents is a milestone. Returns true if it is a milestone.

### isReadOnly : boolean [read-only]
Gets if this file is currently read-only or not. A file can be read-only for various reasons. For example, if you are running with a "Fusion for Personal Use license" and have not designate the file to be editable or if someone else is editing the file.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### lastUpdatedBy : User [read-only]
Returns the User that last updated this data file

### latestVersion : DataFile [read-only]
Returns the latest version of the DataFile. It can return a reference to the same DataFile is this DataFile is the latest version.

### latestVersionNumber : integer [read-only]
Gets the latest version number for this DataFile.

### milestone : Milestone [read-only]
If the version this DataFile represents is a milestone, a Milestone object will be returned. If it's not a milestone, null is returned.

### milestones : Milestones [read-only]
Returns a collection of Milestones associated with all versions of this DataFile.

### name : string [read-write]
Gets and sets the displayed name of this item.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentFolder : DataFolder [read-only]
Returns the parent folder this item is contained within.

### parentProject : DataProject [read-only]
Returns the parent project that this item is in.

### parentReferences : DataFiles [read-only]
Returns a collection DataFiles collection that are the parents (designs that reference) this datafile.

### publicLink : string [read-only]
This function is retired. See more information in the 'Remarks' section below.

Returns a short URL of this data file which can be shared with others.

### sharedLink : SharedLink [read-only]
Returns the SharedLink object associated with this DataFile. You can use the SharedLink object to enable a shared link and set its behavior and to get the shared link URL.

### thumbnail : DataObjectFuture [read-only]
Starts the process to get the thumbnail image data associated with this DataFile. Because the data exists on the cloud, a DataObjectFuture is returned that you can use to monitor the state of downloading the thumbnail and then getting the image once it is available.

The data returned is a 256x256 PNG image. For cases where the DataFile does not have an associated thumbnail, the dataObject property of the returned DataObjectFuture will return null and the state property will return 'FailedFutureState'.

### versionId : string [read-only]
Returns the version ID for this DataFile. This is the same id used in the APS Data Management API for an Item and is in the unencoded form and will look similar to this: "urn:adsk.wipqa:fs.file:vf.W3syIw1lQAW-5vWObMdYnA?version=2"

### versionNumber : integer [read-only]
Gets the version number of this DataFile.

### versions : DataFiles [read-only]
Gets the other version of this item.

## Samples
- **Avoid Machine Surface Settings API Sample**: This sample script demonstrates how to use Machine/Avoid/Gouge/Fixture functionality.
The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a curved surface with a through slot, a countersunk hole and a raised, circular and filleted upstand from the surface. The model is supported by two rectangular blocks, themselves mounted on a fixture plate. A setup is included with a single operation running a 3-axis diagonal raster over the model, supports and fixture. The operation machines the fixture, the supporting blocks, the upper surface of the upstand and the area within the slot and hole, something we would like to avoid.
The script duplicates the original operation and then proceeds to create a series of MachineAvoidGroups. These are labelled as either Machine in the case of 2 cap surfaces for the slot and hole, Fixture for the fixture plate, Gouge for the supporting blocks and Avoid for the top face of the upstand. Additionally, both AxialOffset and RadialOffset can be specified for the Machine, Avoid and Fixture passes.
- **Create Engravings Selection Sets API Sample**: This sample script demonstrates how to find and machine engravings in the Z+ direction using pocket recognition.
The script will first open an example model via its URN. Using pocket recognition, it will identify pockets that may be engravings based on their dimensions.
We assume here that an engraving pocket is:Made with a flat bottom face and no fillet.A closed pocket.Have a Z height less than 2 mm
We demonstrate creating selection sets in both design and manufacture workspaces and use one of the selection sets as an operation geometry selection input to generate an engraving operation.
The engraving toolpath can be seen by expanding the setup and selecting the operation.
- **Create Setups From Hole Recognition API Sample**: This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.
The Fusion Manufacturing Extension is required for Hole Recognition.
The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector.
- **Set Vise Origin As Setup WCS Origin API Sample**: This sample script demonstrates how to define our setup WCS origin relative to our vise origin from either a component, a sketch point or a joint origin.
The Work Coordinate System is a reference point set in our CAM workspace and on our machine. All machine coordinates are drawn from the WCS. This script demonstrates defining the WCS by each of 4 alternative methods:
Setup by default with no origin defined.
Setup using vise origin as WCS origin.
Setup using a sketch point as WCS origin.
Setup using a joint origin as WCS origin.
