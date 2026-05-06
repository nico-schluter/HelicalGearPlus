# ConfigurationReplaceDesigns
Namespace: adsk.fusion
Inherits: Base
Since: September 2025

Collection object that provides access to all the ConfigurationReplaceDesign objects that have been defined for a ConfigurationReplaceDesignColumn. You can also use this collection to define new replace designs that will then be available when specifying which design to use in a cell.

**Accessed from:** ConfigurationInsertStandardDesignColumn.replaceDesigns

## Methods

### add(name: string, dataFile: DataFile) -> ConfigurationReplaceDesign
Adds a new ConfigurationReplaceDesign object to the column. The ConfigurationReplaceDesign objects associated with the column can be used in the cells in the column.
- **name** (string): The name of the new ConfigurationReplaceDesign object. The name must be unique with respect to the other ConfigurationReplaceDesign objects defined for this column. An empty string can be provided, which will cause Fusion to use a default naming scheme to create a name.
- **dataFile** (DataFile): A DataFile object that defines which Design to use. This must be a DataFile object that represents a standard design, not a configured design.
- **Returns** (ConfigurationReplaceDesign): Returns the newly created ConfigurationReplaceDesign.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ConfigurationReplaceDesign
A method that returns the specified ConfigurationReplaceDesign object using an index into the collection.
- **index** (uinteger): The index of the ConfigurationReplaceDesign object to return, where the first row is index 0.
- **Returns** (ConfigurationReplaceDesign): Returns the specified ConfigurationReplaceDesign object or null if an invalid index was specified.

### itemByName(name: string) -> ConfigurationReplaceDesign
A method that returns the ConfigurationReplaceDesign object with the specified name.
- **name** (string): The name of the ConfigurationReplaceDesign object to return.
- **Returns** (ConfigurationReplaceDesign): Returns the specified ConfigurationReplaceDesign object or null if a ConfigurationReplaceDesign object with the specified name does not exist.

## Properties

### count : uinteger [read-only]
Returns the number of ConfigurationReplaceDesign objects defined for the column.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
