# SelectionSets
Namespace: adsk.core
Inherits: Base
Since: May 2022

The SelectionSets object is used to create and access existing selection sets.

In the user interface, selection sets are created by selecting geometry and then running the "Create Selection Set" command from the context menu. All existing selection sets are shown in a "Selection Sets" folder in the browser.

**Accessed from:** CAM.selectionSets, Design.selectionSets, Drawing.selectionSets, FlatPatternProduct.selectionSets, Product.selectionSets, WorkingModel.selectionSets

## Methods

### add(entities: Base[], name: string) -> SelectionSet
Adds a new SelectionSet to the parent product.
- **entities** (Base[]): An array of entities that will be in the created selection set. All entities must be in the context of the root component. This means if the entity isn't directly owned by the root component, it must be a proxy.
- **name** (string): The name of the selection set. This is an optional argument is if not specified, or an empty string is provided, Fusion will create a name for the selection set. If provided, the name should be unique with respect to other selection sets in the product. If a name is provided that is the same as an existing selection set, Fusion will append a counter to the name to make the name unique.

This is an optional argument whose default value is "".
- **Returns** (SelectionSet): Returns the created selection set or null in the case the selection set couldn't be created. This method can fail in the case where no entities are provided or if any of the provided entities are not selectable.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SelectionSet
Returns the specified SelectionSet object using an index into the collection.
- **index** (uinteger): The index of the SelectionSet within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SelectionSet): Returns the specified SelectionSet or null if an invalid index was specified.

### itemByName(name: string) -> SelectionSet
Returns the specified SelectionSet object using the name of the selection set.
- **name** (string): The name of the SelectionSet object to return.
- **Returns** (SelectionSet): Returns the specified SelectionSet object or null if no SelectionSet object exists with the specified name.

## Properties

### count : uinteger [read-only]
Returns the number of SelectionSet objects in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
