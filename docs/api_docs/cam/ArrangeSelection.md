# ArrangeSelection
Namespace: adsk.cam
Inherits: GeometrySelection
Since: March 2024

Class for arrange selections. Provides access to the selected geometry and its properties.

**Accessed from:** ArrangeSelections.createNewArrangeSelection, ArrangeSelections.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### customQuantity : uinteger [read-write]
Gets and sets the custom quantity. This function is not available in Fusion for Personal Use. Throws an exception when calling this function in Fusion for Personal Use. The default value for this property is 1. Note: If customQuantity is called, isUsingCustomQuantity will be set to true automatically.

### customRotationX : double [read-write]
Gets and sets the rotation increments (in degrees) for the x-axis. This function is not available in Fusion for Personal Use. Throws an exception when calling this function in Fusion for Personal Use. To enable any rotation the parameter "arrange_rotation_group" of the operation must be set to true. To disable x-axis rotation for this selection, customRotationX must be set to 0. The default value for this property is 45 degrees. Note: If customRotationX is called, isUsingCustomRotationX will be set to true automatically.

### customRotationY : double [read-write]
Gets and sets the rotation increments (in degrees) for the y-axis. This function is not available in Fusion for Personal Use. Throws an exception when calling this function in Fusion for Personal Use. To enable any rotation the parameter "arrange_rotation_group" of the operation must be set to true. To disable y-axis rotation for this selection, customRotationY must be set to 0. The default value for this property is 45 degrees. Note: If customRotationY is called, isUsingCustomRotationY will be set to true automatically.

### customRotationZ : double [read-write]
Gets and sets the rotation increments (in degrees) for the z-axis. This function is not available in Fusion for Personal Use. Throws an exception when calling this function in Fusion for Personal Use. To enable any rotation the parameter "arrange_rotation_group" of the operation must be set to true. To disable z-axis rotation for this selection, customRotationZ must be set to 0. The default value for this property is 45 degrees. Note: If customRotationZ is called, isUsingCustomRotationZ will be set to true automatically.

### error : string [read-only]
Gets the last warning string encountered after the selection was applied to a parent.

### hasError : boolean [read-only]
Gets if errors were encountered when applying the selection to a a parent.

### hasWarning : boolean [read-only]
Gets if warnings were encountered when applying the selection to a parent.

### inputGeometry : Base [read-write]
Gets and sets the value of the input geometry. If the value originates from a component instead of an occurrence, or an occurrence outside of the CAM environment, then the subpath is checked against the CAM model tree. For some child classes, this may be the same as the value property, but might also consist of fewer elements. Valid elements depend on the capabilities of the derived class. An exception is thrown if the matching fails or the given entity does not match the expected type.

### isUsingCustomQuantity : boolean [read-write]
Gets and sets if custom quantity is used for this element. This function is not available in Fusion for Personal Use. Throws an exception when calling this function in Fusion for Personal Use. If isUsingCustomQuantity is false, the global quantity of the operation's parameter "arrange_global_quantity" is used. The default value for this property false.

### isUsingCustomRotationX : boolean [read-write]
Gets and sets if custom rotation is used for the x-axis. This function is not available in Fusion for Personal Use. Throws an exception when calling this function in Fusion for Personal Use. To enable any rotation the parameter "arrange_rotation_group" of the operation must be set to true. If isUsingCustomRotationX is false, the rotation of the operation's parameter "arrange_rotation_x" is used. The default value for this property false.

### isUsingCustomRotationY : boolean [read-write]
Gets and sets if custom rotation is used for the y-axis. This function is not available in Fusion for Personal Use. Throws an exception when calling this function in Fusion for Personal Use. To enable any rotation the parameter "arrange_rotation_group" of the operation must be set to true. If isUsingCustomRotationY is false, the rotation of the operation's parameter "arrange_rotation_y" is used. The default value for this property false.

### isUsingCustomRotationZ : boolean [read-write]
Gets and sets if custom rotation is used for the z-axis. This function is not available in Fusion for Personal Use. Throws an exception when calling this function in Fusion for Personal Use. To enable any rotation the parameter "arrange_rotation_group" of the operation must be set to true. If isUsingCustomRotationZ is false, the rotation of the operation's parameter "arrange_rotation_z" is used. The default value for this property true.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### priorityType : ArrangePriorityTypes [read-write]
Gets and sets the priority value for each element in the selection list. This function is not available in Fusion for Personal Use. Throws an exception when calling this function in Fusion for Personal Use. The default value for this property is MediumArrangePriorityType.

### value : array [read-only]
Returns the resulting value of the selection. In general, this returns the input selection, but child classes can override the return value if needed. Refer to the child classes comments for further details. The collection may contain duplicates. For OperationInputs, the return value may not be the same as for Operations, as additional geometry selected by child classes is not evaluated for OperationInputs.

### warning : string [read-only]
Gets the last warning string encountered after the selection was applied to a parent.
