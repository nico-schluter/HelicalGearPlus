# Occurrences
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Provides access to occurrences within a component and provides methods to create new occurrences.

**Accessed from:** BaseComponent.occurrences, Component.occurrences, FlatPatternComponent.occurrences

## Methods

### addByInsert(dataFile: DataFile, transform: Matrix3D, isReferencedComponent: boolean) -> Occurrence
Method that inserts an existing file.
- **dataFile** (DataFile): The dataFile to insert.
- **transform** (Matrix3D): A transform that defines the location for the new occurrence.
- **isReferencedComponent** (boolean): Indicates if the insert is to be an external reference or embedded within this document. This method will fail if the dataFile being inserted is not from the same project as the document it is being inserted into while isReferencedComponent is True.
- **Returns** (Occurrence): Returns the newly created occurrence or null if the insert failed. Insert will fail if the dataFile being inserted is not from the same project as the document it is being inserted into while isReferencedComponent is True.

### addExistingComponent(component: Component, transform: Matrix3D) -> Occurrence
Method that creates a new occurrence using an existing component. This is the equivalent of copying and pasting an occurrence in the user interface.
- **component** (Component): The existing component to create a new occurrence of.
- **transform** (Matrix3D): A transform that defines the location for the new occurrence
- **Returns** (Occurrence): Returns the newly created occurrence or null if the creation failed.

### addFromConfiguration(configurationRow: ConfigurationRow, transform: Matrix3D) -> Occurrence
Method that inserts a configuration from a configured design. The insert will fail if the configured design being used is not from the same project as the file it is being inserted into.
- **configurationRow** (ConfigurationRow): The row that specifies which configuration to use.
- **transform** (Matrix3D): A transform that defines the location for the new occurrence.
- **Returns** (Occurrence): Returns the newly created occurrence or null if the add failed.

### addNewComponent(transform: Matrix3D) -> Occurrence
Method that creates a new component and an occurrence that references it.
- **transform** (Matrix3D): A transform that defines the location for the new occurrence.
- **Returns** (Occurrence): Returns the newly created occurrence or null if the creation failed.

### addNewComponentCopy(component: Component, transform: Matrix3D) -> Occurrence
Method that creates a new occurrence by creating a new component that is a copy of an existing component. This is the equivalent of copying and using the "Paste New" command in the user interface. This is different from the addExistingComponent in that it's not a new instance to the existing component but a new component is created that has it's own definition (sketches, features, etc.) and a new occurrence instance is created to reference this new component.
- **component** (Component): The existing component to create a copy of.
- **transform** (Matrix3D): A transform that defines the location for the new occurrence
- **Returns** (Occurrence): Returns the newly created occurrence or null if the creation failed. The newly created component can be obtained by using the component property of the returned Occurrence.

### addNewExternalComponent(componentName: string, targetFolder: DataFolder, transform: Matrix3D) -> Occurrence
Method that creates a new occurrence by creating a new external component (X-Ref) that is not saved yet. This is similar to the "New Component" command in the UI when creating an external component, where you specify a name and location but the component is created in-memory without being saved immediately. This allows programs to create and populate an external component without needing to save it first, and makes undo possible. The component will be saved automatically when the parent assembly is saved.
- **componentName** (string): The name for the new external component.
- **targetFolder** (DataFolder): The DataFolder where the component will be saved when the parent assembly is saved.
- **transform** (Matrix3D): A transform that defines the location for the new occurrence.
- **Returns** (Occurrence): Returns the newly created occurrence or null if the creation failed. The component referenced by the occurrence can be edited but is not saved until the parent assembly is saved.

### asArray() -> Occurrence
Get the current list of all occurrences. The occurrences are returned in the same order as they appear in the browser.
- **Returns** (Occurrence): Returns the current list of all occurrences.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Occurrence
Function that returns the specified occurrence using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Occurrence): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> Occurrence
Returns the specified occurrence using the name of the occurrence.
- **name** (string): The name of the occurrence to return.
- **Returns** (Occurrence): Returns the occurrence or null if an invalid name was specified

## Properties

### asList : OccurrenceList [read-only]
Returns the contents of this collection as an OccurrencesList object. This is useful when writing a function that traverses an assembly.

### count : uinteger [read-only]
Returns the number of occurrences in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Assembly traversal using recursion API Sample**: Traverses the entire structure of the currently open assemlby using a recursive function and displays the result in a message box. This will match the occurrence structure seen in the browser.
