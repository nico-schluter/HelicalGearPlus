# ParameterList
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Transient object used to pass a set of parameters.

**Accessed from:** CustomFeatureParameter.dependencyParameters, CustomFeatureParameter.dependentParameters, DerivedParameter.dependencyParameters, DerivedParameter.dependentParameters, Design.allParameters, FlatPatternProduct.allParameters, ModelParameter.dependencyParameters, ModelParameter.dependentParameters, Parameter.dependencyParameters, Parameter.dependentParameters, ParameterList.create, UserParameter.dependencyParameters, UserParameter.dependentParameters, VariableRadiusFilletEdgeSet.midPositions, VariableRadiusFilletEdgeSet.midRadii, WorkingModel.allParameters

## Methods

### add(parameter: Parameter) -> boolean
Adds a parameter to the list. This does not create a new parameter, it adds an existing parameter to the list. Note that duplicates can exist in the list.
- **parameter** (Parameter): The existing parameter to add to the list
- **Returns** (boolean): Returns true if successful. This method will fail if the list is read-only

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### contains(parameter: Parameter) -> boolean
Indicates whether or not ParameterList collection contains a specified parameter
- **parameter** (Parameter): The parameter to look for in the list
- **Returns** (boolean): Returns true if list contains the specified parameter

### create() -> ParameterList
Creates a parameter list that the client can use for various purposes. Use ParameterList.Add to add parameters to the list after creating it.
- **Returns** (ParameterList): Returns a ParameterList

### find(parameter: Parameter, startIndex: uinteger) -> integer
Finds the specified parameter in the list. The search can be started at a specified index rather than from the beginning of the list. If not found, -1 is returned.
- **parameter** (Parameter): The parameter to find
- **startIndex** (uinteger): the index in the list to start the search from

This is an optional argument whose default value is 0.
- **Returns** (integer): Returns the index of the parameter found in the list.

### item(index: uinteger) -> Parameter
Function that returns the specified parameter using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Parameter): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> Parameter
Returns the specified parameter using the name of the parameter as it is displayed in the parameters dialog
- **name** (string): The name of the parameter as it is displayed in the parameters dialog
- **Returns** (Parameter): Returns the specified item or null if an invalid name was specified.

### removeByIndex(index: uinteger) -> boolean
Method that removes a parameter from the list using the index of the item in the list Will fail if the list is read only.
- **index** (uinteger): The index of the parameter to be removed from the list
- **Returns** (boolean): Returns true if successful. This method will fail if the list is read-only

### removeByItem(item: Parameter) -> boolean
Method that removes a parameter from the list by specifying the parameter (item) to remove
- **item** (Parameter): The parameter item to remove from the list
- **Returns** (boolean): Returns true if successful. This method will fail if the list is read-only

## Properties

### count : uinteger [read-only]
Returns the number of parameters in the collection.

### isReadOnly : boolean [read-only]
Indicates if the list is read-only Some lists returned by API calls (instead of lists created by the user) are read only. Items cannot be added or remove from such a list.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Create Animation API Sample**: Creates a series of images of a design where a parameter is being changed. The series of images can be used to create an animation using other software. To run this sample, have a part open that contains a parameter named "Length". The parameter should be able to be successfully modified from 10 to 15 centimeters. Run the sample and choose or create a directory for the output. After running you should have a folder full of images that are snapshots of each parameter value.
