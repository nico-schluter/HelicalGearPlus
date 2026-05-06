# DecalInput
Namespace: adsk.fusion
Inherits: Base
Since: September 2024

The DecalInput object is used to define the various options when creating a new decal. It's created using the Decals.createInput method and is used by the Decals.add method to create a Decal.

**Accessed from:** Decals.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### faces : array [read-write]
Gets and sets the faces the decal will be associated with. Typically, this will be an array containing a single face and the isChainFaces property on the input will be true. The position and orientation of the decal is based on this face and the decal can wrap onto other faces in the body.

If the isChainFace property is false, the decal will only be applied to the provided faces where the first face is used to calculate the position and orientation of the decal.

### imageFilename : string [read-write]
Gets and sets the filename of the image used for the decal.

When setting this property, it is the full filename to the image to use for the decal. PNG, JPG, and TIFF files are supported.

### isChainFaces : boolean [read-write]
Controls if the decal will wrap onto the faces that connect to the face the decal is placed on. When this is true, the list of faces should contain only one face.

Defaults to true when the input is created.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### opacity : double [read-write]
Gets and sets the opacity of the decal where 0 is completely transparent and 1.0 is completely opaque. Setting this property to a value outside the range of 0-1 will result in the value being set to the closest valid value.

Defaults to 1.0 when the input is created.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

### transform : Matrix3D [read-write]
Gets and sets the transform of the decal. This controls the position, rotation, scaling, and flipping. This is done by providing a 3D matrix that defines a 3D coordinate system in model space. The origin of the matrix defines the center of the decal and must lie somewhere on the first face. The Z-axis of the matrix should be the same as the normal of the face at the origin. The X and Y axes define the orientation of the decal and must be both perpendicular to the Z and each other. Reversing the direction of the X or Y axis will flip the decal in that direction. The magnitude of the X and Y axes controls the scale, and the scale can be non-uniform, meaning the length of the X and Y vectors do not need to be the same.
