# PrintSettingItem
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Collection that provides access to the print setting parameters.

**Accessed from:** PrintSetting.duplicatePrintSettingItem, PrintSetting.getDefaultPrintSettingItem, PrintSetting.item, PrintSetting.itemByName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### description : string [read-write]
Body Preset get and set description.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Body Preset get and set name.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parameters : CAMParameters [read-only]
Function that returns the parameters for reading and editing values.
