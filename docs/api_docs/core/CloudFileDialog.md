# CloudFileDialog
Namespace: adsk.core
Inherits: Base
Since: October 2022

Provides access to a cloud file dialog. A cloud file dialog can be used to prompt the user to select a location and file on Fusion web client.

**Accessed from:** UserInterface.createCloudFileDialog

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### showOpen() -> DialogResults
Displays a modal open dialog, allowing the user to select one or more files. The return value can be used to determine if the dialog was canceled without selecting a file. The dataFile and dataFiles properties can be used to get the selected files.
- **Returns** (DialogResults): Returns an enum value indicating which button was clicked on the dialog.

### showSave() -> DialogResults
Displays a modal save dialog, allowing the user to specify a file. The return value can be used to determine if the dialog was canceled without giving a filename. The filename property can be used to get that file.
- **Returns** (DialogResults): Returns an enum value indicating which button was clicked on the dialog.

## Properties

### dataFile : DataFile [read-only]
Gets the DataFile selected by the user in the dialog. This property is used after the ShowOpen method has been called to retrieve the filename specified by the user.

If ShowOpen was used and isMultiSelectEnabled is true, then this property will only display the first DataFile selected and the dataFiles property should be used instead to retrieved the full list. If ShowSave was used, then only a single DataFile is ever returned.

### dataFiles : array [read-only]
Gets the DataFiles specified by the user in the dialog. This property is used after the ShowOpen method has been called to retrieve the DataFiles specified by the user.

If ShowOpen is used and isMultiSelectEnabled is true, the user is able to select more than one file. This property returns all of the files that were selected.

### dataFolder : DataFolder [read-write]
Gets or sets the initial DataFolder displayed in the dialog. The DataFolder should be in current project. If null, this defaults to the DataFolder that is currently active in the Data Panel.

When using the showSave method, use this property to get the DataFolder that the user specified.

### filename : string [read-write]
Gets and sets the filename when using the showSave method. If you set this value before using the showSave method, this will display the filename as the default in the dialog, but the user can change it. The default is an empty string, which indicates there is not an initial filename.

After calling the showSave method, use this property to get the filename the user specified. You can use this in combination with the dataFolder property to know where the user has specified to save the file.

### filter : string [read-write]
Gets or sets the current file type filter. This controls the types of files displayed in the dialog. The filter consists of file extensions separated by a semi-colon. The string below is an example of the filter used by Fusion for the Open command.

"f3d;f2d;f2t;fbrd;fsch;flbr;fprj;prt;par;sldprt;sldasm;ipt;iam;stp;ste;step"

An empty string indicates that no filter should be used and all files in the current DataFolder should be displayed.

### isMultiSelectEnabled : boolean [read-write]
Gets or sets a value indicating whether the dialog allows multiple files to be selected. This defaults to False when a new CloudFileDialog is created. It is only used when using the showOpen method.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### title : string [read-write]
Gets or sets the title displayed on the dialog.
