# Script
Namespace: adsk.core
Inherits: Base
Since: October 2023

Object that represents a script or add-in.

**Accessed from:** Scripts.addExisting, Scripts.addNew, Scripts.item, Scripts.itemByPath, Scripts.itemsByName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### edit() -> boolean
Invokes the default edit behavior for this script or add-in.
- **Returns** (boolean): Returns true if successful.

### run(waitForFinish: boolean) -> boolean
Runs this script or add-in, if it's not already running.
- **waitForFinish** (boolean): Specifies if call will wait until the script or add-in has finished running. For add-ins, this should always be false, because they typically continue to run for the entire Fusion session.

For scripts, there are cases where you might want to set this to true, where you need to wait for the script to finish because you want to do something with whatever it creates. Typically, this should be false, so it starts the script and immediately returns.

This is an optional argument whose default value is False.
- **Returns** (boolean): Returns true if successful.

### stop() -> boolean
If this script or add-in is running, this method will stop it. The isRunning property can be used to determine if it is running. If the script or add-in is not running and this method is called, there is no effect.
- **Returns** (boolean): Returns true if successful.

### unlink() -> boolean
Unlinks this script or add-in. This removes it from Fusion's list of linked scripts and add-ins, so it is no longer displayed in the dialog, and if it's an add-in, it will no longer run on startup.

This is only valid for a script or add-in that is linked; the sourceLocation property returns LinkedScriptSourceLocation.
- **Returns** (boolean): Returns true if the unlink was successful.

## Properties

### appStoreURL : string [read-only]
For an add-in installed from the Autodesk App Store, this property returns the URL on the store for the page of this app. This property returns an empty string for all scripts and add-ins not installed from the App Store and if there is a problem determining the URL for an App Store app.

### author : string [read-only]
Returns the author information associated with this script or add-in.

### description : string [read-only]
Gets the description of this script or add-in.

### folder : string [read-only]
Gets the full path of the folder that contains this script or add-in.

### helpFilename : string [read-only]
Returns the filename of a local html file that serves as the help file for this script or add-in. This filename is defined in the manifest of the script or add-in using the "helpFilename" setting.

### iconFilename : string [read-only]
Returns the filename of the image file that can be used as the icon for this script or add-in. This filename is defined in the manifest of the script or add-in using the "iconFilename" setting.

### id : string [read-only]
Gets the ID of this script or add-in. This is typically a GUID and is assumed to be unique with respect to all other add-ins.

### isAddIn : boolean [read-only]
Gets if this Script object represents a script or an add-in. Returns true if it is an add-in.

### isEditable : boolean [read-only]
Indicates if this script or add-in is blocked from being edited by the user in the "Scripts and Add-Ins" dialog.

### isFavorite : boolean [read-write]
Gets and sets whether this script or add-in is a favorite of the user.

### isInternal : boolean [read-only]
Indicates if this is an internal script or add-in that is delivered with Fusion. Returns true if it is an internal script or add-in.

### isRunning : boolean [read-only]
Gets if this script or add-in is currently running.

### isRunOnStartup : boolean [read-write]
Gets and sets whether this add-in will automatically run when Fusion is started. This property is only valid when the isAddIn property returns true.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-write]
Gets and sets whether the script or add-in is visible within the “Scripts and Add-Ins” dialog. By default, all scripts and add-ins are visible. Setting this to false will cause it to be hidden and unloaded if it is already running. Also, if it’s an add-in set to load on startup, it will no longer be loaded.

### location : ScriptSourceLocations [read-only]
Gets which standard location this script is located.

### manifestContent : string [read-only]
Gets the full contents of the manifest file associated with this script or add-in. This is particularly useful if you have any custom information defined in the manifest. The manifest file uses JSON to format its content.

### name : string [read-only]
Gets the name of this script or add-in.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### programmingLanguage : ProgrammingLanguages [read-only]
Returns the programming language this script or add-in is written in.

### targetOperatingSystem : OperatingSystems [read-only]
Returns the operating systems this script or add-in is available for.

### version : string [read-only]
Returns the version information associated with this script or add-in.
