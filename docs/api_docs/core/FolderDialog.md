# FolderDialog
Namespace: adsk.core
Inherits: Base
Since: September 2017

Provides access to a folder selection dialog to allow the user to select a folder.

**Accessed from:** UserInterface.createFolderDialog

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### showDialog() -> DialogResults
Displays a modal dialog allowing the user to select a folder. The return value can be used to determine if the dialog was canceled without selecting a folder. the folder property can be used to get the selected folder.
- **Returns** (DialogResults): Returns an enum value indicating which button was clicked on the dialog.

## Properties

### folder : string [read-only]
Gets the folder selected by the user in the dialog. This property is used after the ShowDialog method has been called to retrieve the folder specified by the user.

### initialDirectory : string [read-write]
Gets or sets the initial directory displayed by the file dialog box.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### title : string [read-write]
Gets or sets the title displayed on the dialog.
