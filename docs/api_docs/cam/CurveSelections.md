# CurveSelections
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Collection for all curve selections to be passed to a CadContours2DParameterValue object. This is a read-only container. It returns the curve selections associated with the parent parameter value object, but does not write to it. To apply changes done to the collection and the selections it contains, CadContours2DParameterValue.applyCurveSelections() needs to be called.

**Accessed from:** CadContours2dParameterValue.getCurveSelections

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### clear()
Clears all entries.

### createNewChainSelection() -> ChainSelection
Creates a new chain selection and adds it to the end of the collection.
- **Returns** (ChainSelection): Returns newly created ChainSelection.

### createNewFaceContourSelection() -> FaceContourSelection
Creates a new face contour selection and adds it to the end of the collection.
- **Returns** (FaceContourSelection): Returns newly created FaceContourSelection.

### createNewPocketRecognitionSelection()
Creates a new pocket recognition selection and adds it to the end of the collection.

### createNewPocketSelection() -> PocketSelection
Creates a new pocket selection and adds it to the end of the collection.
- **Returns** (PocketSelection): Returns newly created PocketSelection.

### createNewSilhouetteSelection() -> SilhouetteSelection
Creates a new silhouette selection and adds it to the end of the collection.
- **Returns** (SilhouetteSelection): Returns newly created SilhouetteSelection.

### createNewSketchSelection()
Creates a new sketch selection and adds it to the end of the collection.

### item(index: uinteger) -> CurveSelection
Function that returns the specified curve selection object using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (CurveSelection): Returns the specified item or null if an invalid index was specified.

### remove(index: uinteger)
Function that removes the specified curve selection object using an index in the collection.
- **index** (uinteger): The index of the item within the collection to remove. The first item in the collection has an index of 0.

### removeByObject(selection: CurveSelection)
Function that removes the specified curve selection object from the collection.
- **selection** (CurveSelection): The item within the collection to remove. Throws an exception if the curve selection is not part of the given selection.

## Properties

### count : uinteger [read-only]
The number of items in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Hole and Pocket Recognition API Sample**: This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.
The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.
RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.
The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.
This script works only if the Manufacturing Extension is active.
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
