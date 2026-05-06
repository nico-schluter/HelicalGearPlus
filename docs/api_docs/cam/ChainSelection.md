# ChainSelection
Namespace: adsk.cam
Inherits: CurveSelection
Since: April 2023

Represents a chain type of curve selection. Allows B-Rep edges and sketch geometry for the inputGeometry property. The automatic tool side detection is currently disabled when using the API, thus the side is determined based on the direction of the first edge and the z-axis of the tool orientation.

This class overrides the value property of its GeometrySelection parent to return the result edge selection. The result may contain more edges than the input if gaps between the desired start and end edge were automatically filled.

**Accessed from:** CurveSelections.createNewChainSelection

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### endExtensionLength : double [read-write]
Property that gets and sets the length of the extension of an open curve at the end of the chain. The value is specified in centimeters. This is only applicable to open contours and when DistanceCap is chosen as the extension cap.

### error : string [read-only]
Gets the last warning string encountered after the selection was applied to a parent.

### extensionMethod : ExtensionMethods [read-write]
Property that gets and sets extension method to use. The default is TangentExtension. Only applicable to open contours.

### extensionType : ExtensionTypes [read-write]
Property that gets and sets the desired extension type method. The default is DistanceCap. This is only applicable to open contours.

### hasError : boolean [read-only]
Gets if errors were encountered when applying the selection to a a parent.

### hasWarning : boolean [read-only]
Gets if warnings were encountered when applying the selection to a parent.

### inputGeometry : array [read-write]
Get or set the value of the input geometry. If the value originates from a component instead of an occurrence, or an occurrence outside of the CAM environment, then the subpath is checked against the CAM model tree. For some child classes, this may be the same as the value property, but might also consist of fewer elements. Valid elements depend on the capabilities of the derived class. An exception is thrown if the matching fails or the given entity does not match the expected type.

### isOpen : boolean [read-write]
Property to get or set if an open contour should be closed or not. If true and the input does not specify a closed contour, additional curve segments will be generated to close the contour.

### isOpenAllowed : boolean [read-only]
Property to specify if the underlying CadContours2DParameterValue allows open contours. Some examples of some open contours are adaptive clearing 3d and swarf. And, some examples of closed contours are face and machining boundary.

### isReverted : boolean [read-write]
Property to control if the curve is reverted or not. The curve needs to be reverted, if Fusion's guess does not match the user's expectation.

The initial tool placement depends on the first input edge or sketch line and the height of the bordering faces or sketch boundaries, with the tool being placed outside of the higher face or sketch boundary.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### startExtensionLength : double [read-write]
Property that gets and sets the length of the extension of an open curve at the start of the chain. This is only applicable to open contours and when DistanceCap is chosen as the extension cap.

### value : array [read-only]
Returns the resulting value of the selection. In general, this returns the input selection, but child classes can override the return value if needed. Refer to the child classes comments for further details. The collection may contain duplicates. For OperationInputs, the return value may not be the same as for Operations, as additional geometry selected by child classes is not evaluated for OperationInputs.

### warning : string [read-only]
Gets the last warning string encountered after the selection was applied to a parent.

## Samples
- **Hole and Pocket Recognition API Sample**: This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.
The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.
RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.
The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.
This script works only if the Manufacturing Extension is active.
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
