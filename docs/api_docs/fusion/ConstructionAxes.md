# ConstructionAxes
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Provides access to the construction axes within a component and provides methods to create new construction axes.

**Accessed from:** BaseComponent.constructionAxes, Component.constructionAxes, FlatPatternComponent.constructionAxes

## Methods

### add(input: ConstructionAxisInput) -> ConstructionAxis
Creates and adds a new ConstructionAxis using the creation parameters in the ConstructionAxisInput.

If the ConstructionAxisInput was defined using the setByLine method then the add will only work in the direct modeling mode and will fail in the parametric modeling mode.
- **input** (ConstructionAxisInput): A ConstructionAxisInput object
- **Returns** (ConstructionAxis): Returns the newly created construction axis or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(occurrenceForCreation: Occurrence) -> ConstructionAxisInput
Create a ConstructionAxisInput object that is in turn used to create a ConstructionAxis.
- **occurrenceForCreation** (Occurrence): A creation occurrence is needed if the input is in another component AND the construction axis is not in the root component. The occurrenceForCreation is analogous to the active occurrence in the UI.

This is an optional argument whose default value is null.
- **Returns** (ConstructionAxisInput): Returns a ConstructionAxisInput object

### item(index: uinteger) -> ConstructionAxis
Function that returns the specified construction axis using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ConstructionAxis): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> ConstructionAxis
Returns the specified construction axis using the name of the construction axis as it is displayed in the browser.
- **name** (string): The name of the axis as it is displayed in the browser
- **Returns** (ConstructionAxis): Returns the specified item or null if an invalid name was specified.

## Properties

### component : Component [read-only]
The component that owns this collection.

### count : uinteger [read-only]
The number of construction axes in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Construction Axis API Sample**: Demonstrates creating construction axis in various ways.
