# DataObject
Namespace: adsk.core
Inherits: Base
Since: September 2024

The DataObject provides access to the raw data that represents a logical entity. Typically, it is the bytes of a stored file, but it can also be something like the image data that could be stored within another file.

**Accessed from:** Component.createThumbnail, DataObjectFuture.dataObject, FlatPatternComponent.createThumbnail

## Methods

### asString() -> string
Gets the file as a string (UTF-8). This is convenient when the saved file contains string data. For example, if the file contains JSON data. This eliminates the need to convert the Base64 string into a standard string.
- **Returns** (string): Returns the data as a standard (UTF-8) string. Fails with an appropriate error in the case where the data cannot be provided.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getAsBase64String() -> string
Gets the binary data represented by the DataObject as a Base64 encoded string.
- **Returns** (string): Returns the binary data represented by the DataObject as a standard Base64 encoded string. Fails with an appropriate error in the case where the data cannot be provided.

### saveToFile(filename: string) -> boolean
Saves the data represented by the DataObject to a file.
- **filename** (string): The full filename to save the file to. This includes the full path and the filename. The folder must already exist and you are responsible for specifying the correct extension to match the file type.
- **Returns** (boolean): Returns true if the save was successful.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
