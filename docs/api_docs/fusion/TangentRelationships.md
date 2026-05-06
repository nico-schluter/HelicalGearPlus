# TangentRelationships
Namespace: adsk.fusion
Inherits: Base
Since: May 2022

The collection of Tangent Relationships in this component. This provides access to all existing tangent relationships and supports the ability to create new tangent relationships.

**Accessed from:** Component.tangentRelationships, FlatPatternComponent.tangentRelationships

## Methods

### add(input: TangentRelationshipInput) -> TangentRelationship
Creates a new tangent relationship between two components.
- **input** (TangentRelationshipInput): The TangentRelationshipInput object that defines the geometry and various inputs that fully define a tangent relationship. A TangentRelationshipInput object is created using the TangentRelationships.createInput method.
- **Returns** (TangentRelationship): Returns the newly created TangentRelationship or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(faceOne: BRepFace, tangentFaces: Base) -> TangentRelationshipInput
Creates a TangentRelationshipInput object, which is the API equivalent to the Tangent Relationship command dialog. You use methods and properties on the returned class to set the desired options, similar to providing input in the Tangent Relationship command dialog. Once the settings are defined you call the TangentRelationships.add method passing in the TangentRelationshipInput object to create the actual TangentRelationship.
- **faceOne** (BRepFace): A BRepFace object that will remain tangent to the set of specified tangent faces.
- **tangentFaces** (Base): A single BRepFace object that is part of the body that faceOne will remain tangent to. All of the faces of the body will be used when computing the tangent relationship.
- **Returns** (TangentRelationshipInput): Returns the TangentRelationshipInput object or null if the creation failed.

### item(index: uinteger) -> TangentRelationship
Function that returns the specified tangent relationship using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (TangentRelationship): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> TangentRelationship
Function that returns the specified tangent relationship using a name.
- **name** (string): The name of the item within the collection to return.
- **Returns** (TangentRelationship): Returns the specified item or null if an invalid name was specified.

## Properties

### count : uinteger [read-only]
Returns number of TangentRelationship objects in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
