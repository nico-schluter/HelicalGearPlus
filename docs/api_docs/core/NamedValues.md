# NamedValues
Namespace: adsk.core
Inherits: Base
Since: August 2014

Wraps a list of named values.

**Accessed from:** NamedValues.create, PostProcessInput.postProperties, ToolQuery.criteria

## Methods

### add(name: string, value: ValueInput) -> boolean
Adds a name value pair to the NamedValues object
- **name** (string): A name for the name value pair
- **value** (ValueInput): A ValueInput object that defines the value of the name value pair
- **Returns** (boolean): Returns true if the name value pair is added successfully.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create() -> NamedValues
Creates a transient NamedValues object.
- **Returns** (NamedValues): Returns the created NamedValue object.

### getByIndex(index: integer, name: string, value: ValueInput) -> boolean
Function that returns the name and ValueInput object of a name value pair by specifying an index number
- **index** (integer): The index of the name value pair to return. The first pair in the collection has an index of 0.
- **name** (string): The name
- **value** (ValueInput): The ValueInput object
- **Returns** (boolean): Returns true if successful

### getValueByName(name: string, value: ValueInput) -> boolean
Function that returns the ValueInput object of a name value pair by specifying its name
- **name** (string): The name of the name value pair to return the ValueInput object from
- **value** (ValueInput): The ValueInput object
- **Returns** (boolean): Returns true if successful

## Properties

### count : uinteger [read-only]
Returns the number of name value pairs in this object.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
