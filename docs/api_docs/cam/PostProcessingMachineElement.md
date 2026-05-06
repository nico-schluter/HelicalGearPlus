# PostProcessingMachineElement
Namespace: adsk.cam
Inherits: MachineElement
Since: July 2025

Machine element representing the post processor and post properties.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### staticTypeId() -> string
Identifying name for all elements of this type. Pass this to the itemByType or itemById methods of MachineElements to filter to elements of this type.
- **Returns** (string): Returns identifier of this type.

### updatePostParameters(parameters: CAMParameters) -> boolean
Overrides the default post parameters with the given user's input.
- **Returns** (boolean): Returns true if the update was successful. False otherwise.

## Properties

### elementId : string [read-only]
Identifier for this element. Unique within an element type.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### outputFolder : string [read-write]
Gets and sets the path for the output folder where the .nc files will be located.

### postParameters : CAMParameters [read-only]
Gets the machine scope post properties as parameters.

### postURL : URL [read-write]
Gets or sets the URL of the post assigned to the machine.

### typeId : string [read-only]
Identifier for this type of machine element.
