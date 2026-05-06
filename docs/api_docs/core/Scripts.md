# Scripts
Namespace: adsk.core
Inherits: Base
Since: October 2023

API object that provides equivalent functionality of the "Scripts and Add-Ins" dialog. Provides access to the scripts and add-ins that Fusion is aware of. It also supports loading other unknown scripts and add-ins, and creating new scripts and add-ins.

**Accessed from:** Application.scripts

## Methods

### addExisting(scriptFolderPath: string) -> Script
Fusion looks in specific folders for scripts and add-ins, but you can manually add other scripts and add-ins to the list of known scripts and add-ins so they will be listed in the "Scripts and Add-ins" dialog. This method does that.
- **scriptFolderPath** (string): The full path to the folder that contains the script or add-in.
- **Returns** (Script): Returns the Script object that represents the script or add-in just added. Returns null in the case of failure.

### addNew(input: ScriptInput) -> Script
Creates a new script or add-in. This uses the same internal template that's used when creating a new script or add-in using the "Scripts and Add-Ins" dialog. The provided ScriptInput object defines the information needed to create a new script or add-in.
- **input** (ScriptInput): A ScriptInput object which defines the required information to create a new script or add-in. It is created using the createNewScriptInput method.
- **Returns** (Script): Returns the newly created Script object.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createScriptInput(name: string, programmingLanguage: ProgrammingLanguages, isAddIn: boolean) -> ScriptInput
Creates a new ScriptInput object. Logically, this object is equivalent to the dialog that is shown when you click the "Create" button in the "Scripts and Add-Ins" command dialog. It collects the information needed to create a new script or add-in. To create the script or add-in, call the addNew method, passing in the ScriptInput object.
- **name** (string): The name of the script or add-in to create. By default, it will be created in the folder specified by the "Default Path for Scripts and Add-Ins" preference, but a different path can be specified using the returned ScriptInput object. Regardless of where it is created, the name must be unique with respect to the other scripts and add-ins in that folder. If it's not unique the creation of the script or add-in will fail.
- **programmingLanguage** (ProgrammingLanguages): The programming language to use for the new script or add-in.
- **isAddIn** (boolean): Specifies if a script or add-in is to be created. If true, an add-in is created.
- **Returns** (ScriptInput): Returns a ScriptInput object or null in the case of failure.

### item(index: uinteger) -> Script
Function that returns the specified script or add-in using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Script): Returns the specified item or null if an invalid index was specified.

### itemByPath(folderPath: string) -> Script
Function that returns the script that is located in the specified folder.
- **folderPath** (string): The full path to the folder that contains the script. This does not include the name of the script, but only the path. For example "C:\Scripts\MyScript" is valid where "C:\Scripts\MyScripts\MyScript.py" is not.
- **Returns** (Script): Returns the specified script or null if there isn't a script at the specified path.

### itemsByName(name: string) -> Script
Function that returns an array of scripts that have the specified name. In most cases this will return an array containing a single script, but it's possible to have more than one script with the same name in the case where the scripts are in different folders.
- **name** (string): The script name to search for.
- **Returns** (Script): Returns the scripts with the specified name or an empty array if there aren't any scripts with that name.

## Properties

### count : uinteger [read-only]
Returns the number of scripts and add-ins.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
