# ApplicationFolders
Namespace: adsk.core
Inherits: Base
Since: September 2024

The ApplicationFolders object provides access to the paths of various folders associated with Fusion.

**Accessed from:** Application.applicationFolders

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### appLogFilePath : string [read-only]
Returns the full filename for the current application log file.

### appStoreInstallPath : string [read-only]
Returns the path where apps from the Autodesk App Store are installed.

### defaultPathForScriptsAndAddIns : string [read-write]
Gets and sets the default path for scripts and add-ins. This is the same as the defaultPathForScriptsAndAddIns property on the APIPreferences object.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### materialsPath : string [read-only]
Returns the path where user-created material and appearance libraries are saved.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### optionsPath : string [read-only]
Returns the path to the user-specific folder where Fusion saves various options.

### rootPath : string [read-only]
Returns the path to the version-specific folder where Fusion is installed.

### userDataPath : string [read-only]
Returns the path where some user-specific data is stored.
