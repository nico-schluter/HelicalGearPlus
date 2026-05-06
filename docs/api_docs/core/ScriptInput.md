# ScriptInput
Namespace: adsk.core
Inherits: Base
Since: October 2023

Used when creating a new script or add-in to specify all of the required and optional settings needed. This is created using the createScriptInput method on the Scripts object.

**Accessed from:** Scripts.createScriptInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### author : string [read-write]
The author of the add-in that is displayed in the "Scripts and Add-Ins" dialog. This defaults to an empty string.

### description : string [read-write]
The description of the add-in that is displayed in the "Scripts and Add-Ins" dialog. This defaults to an empty string.

### isAddIn : boolean [read-write]
Specifies if a script or add-in is to be created. A value of true indicates an add-in will be created.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets and sets the name of the script or add-in to create. This name must be unique with respect to the other scripts and add-ins in the folder specified by the targetFolder property.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### programmingLanguage : ProgrammingLanguages [read-write]
Gets and sets which programming language the new script or add-in will use.

### runOnStartup : boolean [read-write]
If this Script represents an add-in and isAddIn is True, this specifies if the add-in should be automatically started when Fusion starts up.

### targetFolder : string [read-write]
The full path to the folder where the script or add-in will be created. By default, this is an empty string which uses the default folder specified by the "Default Path for Scripts and Add-Ins" preference. Specifying a path overrides the default and will create the script or add-in in the specified location. No "Scripts" or "AddIns" sub-folder is created.

### targetOperatingSystem : OperatingSystems [read-write]
Specifies the operating systems this script or add-in will be displayed in the "Scripts and Add-Ins" dialog and where it will be automatically run on startup, if that option is specified. Defaults to WindowsAndMacOperatingSystem

### version : string [read-write]
The version of the add-in that is displayed in the "Scripts and Add-Ins" dialog. This defaults to an empty string.
