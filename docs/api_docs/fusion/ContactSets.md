# ContactSets
Namespace: adsk.fusion
Inherits: Base
Since: September 2016

Provides access to the existing contact sets in a design and supports creating new contact sets.

**Accessed from:** Design.contactSets, FlatPatternProduct.contactSets, WorkingModel.contactSets

## Methods

### add(occurrencesAndBodies: Base[]) -> ContactSet
Creates a new contact set for the provided occurrences and/or bodies.
- **occurrencesAndBodies** (Base[]): An array of Occurrence or BRepBody objects that will be included in the contact set. All occurrences and bodies must be in the context of the root component.
- **Returns** (ContactSet): Returns the newly created ContactSet or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ContactSet
Returns the specified contact set using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ContactSet): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> ContactSet
Returns the specified contact set.
- **name** (string): The name of the contact set to return.
- **Returns** (ContactSet): Returns the specified contact set or null there isn't a contact set with that name.

## Properties

### count : uinteger [read-only]
Returns the number of contacts sets in the design.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **SliderJointMotion API Sample**: Demonstrates creating a joint with slider joint motion.
