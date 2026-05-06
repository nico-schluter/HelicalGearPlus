# RenderEnvironments
Namespace: adsk.fusion
Inherits: Base
Since: May 2023

The list of available render environments. This represents the list of environments shown in the "Scene Settings" dialog as being in the "Fusion Library". It does not include a custom environment, if one has been loaded.

**Accessed from:** RenderManager.renderEnvironments

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: integer) -> RenderEnvironment
Method that returns the specified render environment using an index into the collection.
- **index** (integer): The index of the item within the collection. The first item has an index of 0.
- **Returns** (RenderEnvironment): Returns the specified render environment or null if an invalid index was specified.

### itemById(id: string) -> RenderEnvironment
Returns the render environment with the specified ID.
- **id** (string): The ID of the render environment to return.
- **Returns** (RenderEnvironment): Returns the specified render environment or null if the ID does not match a render environment.

### itemByName(name: string) -> RenderEnvironment
Returns the specified render environment using the name as seen in the user interface.
- **name** (string): The name of the render environment to return.
- **Returns** (RenderEnvironment): Returns the specified render environment or null if there's no match on the name.

## Properties

### count : uinteger [read-only]
The number of render environments in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
