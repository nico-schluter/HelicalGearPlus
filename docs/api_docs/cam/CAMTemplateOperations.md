# CAMTemplateOperations
Namespace: adsk.cam
Inherits: Base
Since: March 2025

A list of CAMTemplateOperationInput.

These are stored 'by value' -- get() returns a copy of the element at the given index, and set() will overwrite the element at the given index with a copy of the given element.

**Accessed from:** CAMTemplate.operations

## Methods

### add(input: CAMTemplateOperationInput)
Add an item to the list.
- **input** (CAMTemplateOperationInput): This element will be copied to the end of the list. Must come from get() or makeInput().

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### get(operationIndex: integer)
Return a copy of an element.
- **operationIndex** (integer): Index of the element to copy.

### makeInput(strategyType: string)
Make a CAMTemplateOperationInput of the given strategy type which is compatible with add() and set().

### set(operationIndex: integer, input: CAMTemplateOperationInput)
Set the element at the given index.
- **operationIndex** (integer): Index of the element to overwrite
- **input** (CAMTemplateOperationInput): The element will be overwritten with a copy of this element. Must come from get() or makeInput().

## Properties

### count : integer [read-only]
The number of items in the list.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
