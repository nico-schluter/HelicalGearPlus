# FullRoundFilletFaceSets
Namespace: adsk.fusion
Inherits: Base
Since: September 2025

Collection that provides access to all existing full round fillet face sets associated with a full round fillet feature or a FullRoundFilletFeatureInput object, and allows adding new full round fillet face sets.

**Accessed from:** FilletFeature.fullRoundFilletFaceSets, FullRoundFilletFeatureInput.faceSets

## Methods

### add(centerFace: BRepFace, sideOneFaces: BRepFace[], sideTwoFaces: BRepFace[], areAutomaticSideFaces: boolean) -> FullRoundFilletFaceSet
Adds a set of faces to be filleted to the full round fillet feature.

When this face set is associated with an existing fillet feature, to use this method you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True).
- **centerFace** (BRepFace): Input a BRepFace object that specifies the center face to be filleted.

When specifying a center face which has tangentially connected faces then all the tangentially connected faces will be filleted automatically.
- **sideOneFaces** (BRepFace[]): Input array of BRepFace objects to specify the side one faces. Only one BRepFace object which is adjacent to the center face can be provided if you set areAutomaticSideFaces to true.
- **sideTwoFaces** (BRepFace[]): Input array of BRepFace objects to specify the side two faces. Only one BRepFace object which is adjacent to the center face can be provided if you set areAutomaticSideFaces to true.
- **areAutomaticSideFaces** (boolean): Optional input boolean that specifies whether the input side faces are used as automatically inferred side faces. It defaults to true, which results in the side faces not being shown in the dialog when the user edits the feature. The same as when the user infers the side faces from the center face selection. When this is set to false, the side faces will be shown in the dialog as if the user had used the side face selection inputs when creating the feature. For the default to apply the input must meet the requirements that one side one face and one side two face is input and those faces are connected to the center face.

This is an optional argument whose default value is True.
- **Returns** (FullRoundFilletFaceSet): Returns the newly created FullRoundFilletFaceSet or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> FullRoundFilletFaceSet
Function that returns the specified full round fillet face set using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (FullRoundFilletFaceSet): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
The number of full round fillet face sets in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
