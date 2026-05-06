# Application
Namespace: adsk.core
Inherits: Base
Since: August 2014

The top-level object that represents the Fusion application (all of Fusion). This provides access to the modeler and files.

**Accessed from:** Application.get, Document.parent, DrawingDocument.parent, FusionDocument.parent

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### executeTextCommand(command: string) -> string
Executes the input text command.
- **command** (string): The text command to execute.
- **Returns** (string): Returns the result of the input text command.

### fireCustomEvent(eventId: string, additionalInfo: string) -> boolean
Fires a previously registered custom event. This method is used by a worker thread or another add-in to fire an event to the add-in that registered the event and is running in the primary thread.

Firing a custom event does not immediately result in the event handler being called. When a custom event is fired the event is put on the queue and will be handled in the main thread when Fusion is idle.
- **eventId** (string): The ID of the custom event you want to fire.
- **additionalInfo** (string): Any additional information you want to pass through the event to the add-in in the primary thread.

This is an optional argument whose default value is "".
- **Returns** (boolean): Returns true if the event was successfully added to the event queue. A value of true does not indicate that the event was fired and handled but only that it's been put on the primary thread's event queue to be fired when application is idle.

### get() -> Application
Access to the root Application object.
- **Returns** (Application): Return the root Application object or null if it failed.

### getLastError(description: string) -> integer
Returns information about the last error that occurred.
- **description** (string): A description of the last error in English.

This is an optional argument whose default value is "".
- **Returns** (integer): Returns the number of the specific error.

### log(message: string, level: LogLevels, type: LogTypes)
Logs messages to either the TEXT COMMAND window or the Fusion app log file.
- **message** (string): The message to write to the log.
- **level** (LogLevels): The log level. Default value is InfoLogLevel. This is only used when the log type is FileLogType where the log message will include the log level.

This is an optional argument whose default value is LogLevels.InfoLogLevel.
- **type** (LogTypes): The log type. The default value is ConsoleLogType to write the message to the TEXT COMMAND window. When the type is FileLogType, the message is written to Fusion's app log file which is the same file where Fusion writes all of its log messages. You can get the path and filename of the current log file by using the TEXT COMMAND window. In the lower-right corner you can choose "Txt", "Py", or "Js". Choose the "Txt" option and type "paths.get" in the input field and press return. A list of all of the various paths used by Fusion will be displayed in the TEXT COMMAND window. The line for "AppLogFilePath" has the full path to the log file.

This is an optional argument whose default value is LogTypes.ConsoleLogType.

### registerCustomEvent(eventId: string) -> CustomEvent
This registers a new CustomEvent which is intended to be primarily used to send an event from a worker thread you've created back to your add-in running in the primary thread. It's also possible that two add-ins could be cooperating and another add-in can fire the event to your add-in.
- **eventId** (string): This serves as the unique ID for this event and is used by the worker thread or other add-in to identify which custom event to fire using the fireCustomEvent method.
- **Returns** (CustomEvent): Returns the registered CustomEvent or null in the case of failure, which would typically be because the provided eventId is not unique.

### unregisterCustomEvent(eventId: string) -> boolean
Unregisters an existing CustomEvent.
- **eventId** (string): Th unique ID of the custom event you want to unregister.
- **Returns** (boolean): Returns True if the unregister succeeded.

## Properties

### activeDocument : Document [read-only]
Returns the current active document.

### activeEditObject : Base [read-only]
Returns the current edit target as seen in the user interface. This edit target is defined as the container object that will be added to if something is created. For example, a component can be an edit target so that when new bodies are created they are added to that component. A sketch can also be an edit target.

### activeProduct : Product [read-only]
Returns the current active product.

### activeViewport : Viewport [read-only]
Returns the currently active graphics view.

### applicationFolders : ApplicationFolders [read-only]
Returns the ApplicationFolders object which provides access to the paths of various folders associated with Fusion.

### currentUser : User [read-only]
Returns the User that is currently logged in.

### data : Data [read-only]
Returns the Data object which provides access the files.

### documents : Documents [read-only]
Returns the Documents collection object which supports accessing opened documents, opening existing documents, and creating new documents.

### favoriteAppearances : FavoriteAppearances [read-only]
Returns the set of favorite appearances.

### favoriteMaterials : FavoriteMaterials [read-only]
Returns the set of favorite materials.

### fontNames : array [read-only]
Returns the names of all of the fonts that are available in Fusion when creating text.

### hasActiveJobs : boolean [read-only]
Gets whether there are any active jobs.

### importManager : ImportManager [read-only]
Returns the ImportManager. You use the ImportManager to import files (of various neutral formats.) into existing components or new document.

### isComponentColorsDisplayed : boolean [read-write]
Get and sets if component colors are used when displaying the components within a design. This is the API equivalent of the "Display Component Colors" command.

### isOffLine : boolean [read-write]
Gets and sets if Fusion is offline or not.

### isStartupComplete : boolean [read-only]
Boolean property indicating whether Fusion has completed its initialization. This includes initialization of all the Add-ins loaded at startup.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### lightingEnvironment : LightingEnvironments [read-write]
Gets and sets the current lighting environment to use when rendering the graphics.

### materialLibraries : MaterialLibraries [read-only]
Returns the collection of material libraries currently available.

### measureManager : MeasureManager [read-only]
Get the MeasureManager object which can be used to perform measurements of geometry.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### pointTolerance : double [read-only]
The modeling tolerance used internally when comparing two points. The value is in centimeters.

### preferences : Preferences [read-only]
Provides access to all of the application preferences.

### scripts : Scripts [read-only]
Returns the Scripts object which provides the ability to manage scripts and add-ins.

### supportedProductTypes : array [read-only]
Returns an array containing the names of the products types currently supported by Fusion. For example, the name returned for Fusion is "DesignProductType". These product type names are used to identify specific products in some other API functions such as the productType property on the Workspace and ToolbarPanel objects.

### userId : string [read-only]
Returns the internal name of the Autodesk account currently logged in. This can be used by applications sold through the Autodesk Exchange Store to verify that the user has in fact purchased the product.

### userInterface : UserInterface [read-only]
Provides access to functionality specific to the user interface.

### userName : string [read-only]
Returns the user name of the Autodesk account currently logged in.

### vectorAngleTolerance : double [read-only]
The modeling tolerance used when comparing vector angles. The value is in radians.

### version : string [read-only]
Returns the current version of the Fusion application.

## Events

### cameraChanged
The cameraChanged event fires immediately after a change in the camera has been made. Camera changes happen when user changes the view by rotating, zooming in or out, panning, changing from parallel to perspective, or when the extents of the viewport changes.

You can add or remove event handlers from the CameraEvent.

### dataFileComplete
The dataFileComplete event fires when a data file upload has completed including any cloud side translations.

### dataFileCopyComplete
The dataFileCopyComplete event fires when a data file copy has completed including any PIM Data copy.

### documentActivated
The DocumentActivated event fires at the VERY end of a document being activated.

### documentActivating
The DocumentActivating event fires at the VERY start of a document being activated.

### documentClosed
The DocumentClosed event fires at the VERY end of a document being closed. The Document object is not longer available because it has been closed.

### documentClosing
The DocumentClosing event fires at the VERY start of a document being closed. User can set the isSaveCanceled property of DocumentEventArgs to true to cancel the document close.

### documentCreated
The DocumentCreated event fires when a new document is created.

### documentDeactivated
The DocumentDeactivated event fires at the VERY end of a document being deactivated.

### documentDeactivating
The DocumentDeactivating event fires at the VERY start of a document being deactivated.

### documentOpened
The DocumentOpened event fires at the VERY end of a document being opened so the Document object is available to be used.

When a document is opened that references other documents, only the top-level document will cause the documentOpened event to be fired. You can access the referenced documents by using the documentReferences property of the Document object.

### documentOpening
The DocumentOpening event fires at the VERY start of a document being opened. There is no promise that the document will be opened, hence a documentOpened event may not follow.

When a document is being opened that references other documents, only the top-level document will cause a documentOpening event to be fired.

### documentSaved
The DocumentSaved event fires after the save operation has been completed.

### documentSaving
The DocumentSaving event fires at the VERY start of a document being saved. You can set the isSaveCanceled property of DocumentEventArgs to true to cancel the document save.

### insertedFromURL
The insertedFromURL event fires after the user has clicked a link in a web page that uses the Fusion protocol handler to insert a file as new component and that operation has completed.

### insertingFromURL
The insertingFromURL event fires when the user has clicked a link in a web page that uses the Fusion protocol handler to insert a file as new component. This event is fired at the beginning of the request but before Fusion has take any action so that it's still possible to cancel the operation.

### mfgdmDataReady
The mfgdmDataReady event fires when the MFGDM data structure for a document has been updated and properties to IDs and structure from the data model is ready.

### onlineStatusChanged
The onlineStatusChanged event fires immediately after Fusion goes online or offline. This event fires whether or not the online status was changed deliberately by the user by using the Fusion 'Work Offline' command or because of inadvertent network/Internet connectivity issues. You can get the isOffline property of ApplicationEventArgs to determine whether Fusion has gone Offline or has come back online. The client can add or remove ApplicationEventHandlers from the ApplicationEvent.

### openedFromURL
The openedFromURL event fires after the user has clicked a link in a web page that uses the Fusion protocol handler to create a new using an existing file as the initial contents and that operation has completed.

### openingFromURL
The openingFromURL event fires when the user has clicked a link in a web page that uses the Fusion protocol handler to create a new file using an existing file as the initial contents. This event is fired at the beginning of the request but before Fusion has take any action so that it's still possible to cancel the operation.

### startupCompleted
The startupCompleted event fires after Fusion has completed its initialization. This includes initialization of all the Add-ins loaded at startup. The client can add or remove ApplicationEventHandlers from the ApplicationEvent.
