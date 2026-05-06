# ConfigurationJointSnaps
Namespace: adsk.fusion
Inherits: Base
Since: September 2024

Collection object that provides access to all the joint snaps that have been defined for a ConfigurationJointSnapColumn. You can also use this collection to define new joint snaps that will then be available when specifying which snap to use in a cell.

**Accessed from:** ConfigurationJointSnapColumn.snaps

## Methods

### add(name: string, jointGeometry: Base) -> ConfigurationJointSnap
Adds a new snap to the column. The snaps associated with the column can be used in the cells in the column.
- **name** (string): The name of the new snap. The name must be unique with respect to the other snaps defined for this column. An empty string can be provided, which will cause Fusion to use a default naming scheme to create a name.
- **jointGeometry** (Base): A JointGeometry object that defines how the snap is defined. When creating the JointGeometry object, it must be limited to geometry in the occurrence associated with the column.
- **Returns** (ConfigurationJointSnap): Returns the newly created ConfigurationJointSnap.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ConfigurationJointSnap
A method that returns the specified snap using an index into the collection.
- **index** (uinteger): The index of the snap to return, where the first row is index 0.
- **Returns** (ConfigurationJointSnap): Returns the specified snap or null if an invalid index was specified.

### itemByName(name: string) -> ConfigurationJointSnap
A method that returns the snap with the specified name.
- **name** (string): The name of the snap to return.
- **Returns** (ConfigurationJointSnap): Returns the specified snap or null if a snap with the specified name does not exist.

## Properties

### count : uinteger [read-only]
Returns the number of snaps for the column.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
