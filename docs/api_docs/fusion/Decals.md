# Decals
Namespace: adsk.fusion
Inherits: Base
Since: September 2024

Provides access to the Decals in a component and provides the functionality to add new Decals.

**Accessed from:** BaseComponent.decals, Component.decals, FlatPatternComponent.decals

## Methods

### add(input: DecalInput) -> Decal
Creates a new decal. Use the createInput method to first create an input object and set the available options. Then, pass that input object to the add method to create the decal.
- **input** (DecalInput): The DecalInput object that defines the required information needed to create a new decal.

A DecalInput object is the logical equivalent to the Decal command dialog by providing access to all the decal options. Passing in the DecalInput object to the add method is the equivalent of clicking the OK button on the dialog to create the decal.
- **Returns** (Decal): Returns the newly created Decal object.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(imageFilename: string, faces: BRepFace[], point: Point3D) -> DecalInput
Creates a new DecalInput object. A DecalInput object is the logical equivalent to the Decal command dialog by providing access to all the decal options. Passing in the DecalInput object to the add method is the equivalent of clicking the OK button on the dialog to create the decal.
- **imageFilename** (string): The full filename to the image to use for the decal. PNG, JPEG, and TIFF files are supported.
- **faces** (BRepFace[]): Specifies the faces the decal will be associated with. Typically, this will be an array containing a single face. If the isChainFaces property on the input is true, only a single face is needed, and the rest of the faces in the body will automatically be used. If the isChainFaces property is false, this defines a subset of faces in the body to which the decal will be applied.

If multiple faces are provided, the first face in the array is used to position and orient the decal. The position and orientation are relative to the first face. Any additional faces should connect directly or indirectly through other connected faces to the first face.
- **point** (Point3D): Specifies a point on the first face that defines the center position of the decal.
- **Returns** (DecalInput): Returns a DecalInput object or null in the case of failure.

### item(index: uinteger) -> Decal
Returns the specified Decal object using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Decal): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> Decal
Returns the specified decal using the name of the decal.
- **name** (string): The name of the decal as seen in the browser and timeline.
- **Returns** (Decal): Returns the specified Decal object, if it exists. Otherwise it returns null.

## Properties

### count : uinteger [read-only]
Returns the number of decals in the component.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
