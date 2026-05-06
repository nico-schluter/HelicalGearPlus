# ConfigurationReplaceDesign
Namespace: adsk.fusion
Inherits: Base
Since: September 2025

This object represents an individual ConfigurationReplaceDesign object that has been defined for a ConfigurationReplaceDesignColumn. Multiple ConfigurationReplaceDesign objects can be defined for a column and then one of those ConfigurationReplaceDesign objects is specified in each cell of the column.

**Accessed from:** ConfigurationInsertStandardDesignCell.replaceDesign, ConfigurationReplaceDesigns.add, ConfigurationReplaceDesigns.item, ConfigurationReplaceDesigns.itemByName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this ConfigurationReplaceDesign.
- **Returns** (boolean): Returns true if the deletion was successful.

## Properties

### dataFile : DataFile [read-only]
Gets the Design object associated with this ConfigurationReplaceDesign object. This must be a DataFile object that represents a standard design, not a configured design.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
Gets the name of the ConfigurationReplaceDesign object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
