# FileDialog
Namespace: adsk.core
Inherits: Base
Since: August 2014

Provides access to a file dialog. A file dialog can be used to prompt the user for file names to open or save to.

**Accessed from:** UserInterface.createFileDialog

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### showOpen() -> DialogResults
Displays a modal open dialog, allowing the user to select one or more files. The return value can be used to determine if the dialog was canceled without selecting a file. The Filename and Filenames properties can be used to get the selected files.
- **Returns** (DialogResults): Returns an enum value indicating which button was clicked on the dialog.

### showSave() -> DialogResults
Displays a modal save dialog, allowing the user to specify a file. The return value can be used to determine if the dialog was canceled without selecting a file. The Filename and Filenames properties can be used to get the selected files.
- **Returns** (DialogResults): Returns an enum value indicating which button was clicked on the dialog.

## Properties

### filename : string [read-only]
Gets the filename specified by the user in the dialog. This property is used after the ShowOpen or ShowSave methods have been called to retrieve the filename specified by the user. The file name includes both the file path and the extension.

If ShowOpen was used and IsMultiSelectEnabled is true, then this property will only display the first filename selected and the Filenames property should be used instead to retrieved the full list. Is ShowSave was used, then only a single file name is ever returned.

### filenames : array [read-only]
Gets the filenames specified by the user in the dialog. This property is used after the ShowOpen or ShowSave methods have been called to retrieve the filenames specified by the user. Each file name includes both the file path and the extension.

If ShowOpen is used and IsMultiSelectEnabled is true, the user is able to select more than one file. This property returns all of the files that were selected. If ShowSave is used or IsMultiSelectEnabled is false then this array will contain the single file name.

### filter : string [read-write]
Gets or sets the current file name filter string, which determines the choices that appear in the "Save as file type" or "Files of type" box in the dialog box.

For each filtering option, the filter string contains a description of the filter and the filter pattern as specified in parentheses and separated by semi-colons. Multiple filters are separated by a double semi-colon. These are illustrated below.

The following is an example of a filter string:

Text files (*.txt);;All files (*.*)

You can add several filter patterns to a filter by separating the file types with semicolons, for example:

Image Files (*.BMP;*.JPG;*.GIF);;All files (*.*)

### filterIndex : integer [read-write]
Gets or sets the index of the filter currently selected in the file dialog box. Use the FilterIndex property to set which filtering option is shown first to the user. You can also use the value of FilterIndex after showing the file dialog to perform special file operations depending upon the filter chosen. The first item in the filter list is index 0.

### initialDirectory : string [read-write]
Gets or sets the initial directory displayed by the file dialog box.

### initialFilename : string [read-write]
Gets or sets the initial filename displayed when the dialog is first displayed. When a new FileDialog object is created this defaults to an empty string so no initial filename is specified.

If the showOpen option is used, the file must already exist in the directory specified by the initialDirectory property. If it doesn't exist, the initial filename will not be used.

### isMultiSelectEnabled : boolean [read-write]
Gets or sets a value indicating whether the dialog box allows multiple files to be selected.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### title : string [read-write]
Gets or sets the title displayed on the dialog.

## Samples
- **Write user interface to a file API Sample**: Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic User-Interface Customization with Fusion's API
