# TriadCommandInput
Namespace: adsk.core
Inherits: CommandInput
Since: May 2022

Represents a command input that displays a triad and allows the user to control translation rotation, and scaling. Using properties on the input you can choose which controls are available to the user. This displays inputs in the command dialog where the user can enter values and also displays a manipulator in the graphics window to allow them to graphically set the values. The input boxes are displayed in the dialog when the isVisible property of the command input is true. The manipulator is displayed in the graphics window when both the isVisible and isEnabled properties are true.

It will often be useful to first create a GroupCommandInput and then create the TriadCommandInput within the group so it's apparent to the user these items are related and they can be collapsed to reduce clutter in the dialog. This also allows you to label the set of displayed inputs by using the name of the GroupCommandInput.

**Accessed from:** CommandInputs.addTriadCommandInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this Command input.
- **Returns** (boolean): Returns true if the delete was successful.

### hideAll() -> boolean
Hides all controls.
- **Returns** (boolean): Returns true if hiding the controls was successful.

### hideAllRotations() -> boolean
Sets all rotation related controls to be invisible. This is useful if you are only using translations or scaling.
- **Returns** (boolean): Returns true if hiding the controls was successful.

### hideAllScaling() -> boolean
Sets all scaling related controls to be invisible. This is useful if you are only using translations or rotations.
- **Returns** (boolean): Returns true if hiding the controls was successful.

### setFlipVisibility(isVisible: boolean) -> boolean
A convenience method to turn on and off the visibility of the horizontal and vertical flip controls.
- **isVisible** (boolean): Defines if the visibility of the controls should be turned on or off. True indicates they will be visible.
- **Returns** (boolean): Returns true if it was successful.

### setFullVisibility(isVisible: boolean) -> boolean
A convenience method to turn on and off the visibility of commonly used controls in a triad. These include the X, Y, and Z axis translations, the X, Y, and Z axis rotations, scaling in the X, Y, and Z directions, scaling on the X-Y, Y-Z and Z-X planes, translation on the X-Y, Y-Z, and Z-X planes, and the origin move.
- **isVisible** (boolean): Defines if the visibility of the controls should be turned on or off. True indicates they will be visible.
- **Returns** (boolean): Returns true if it was successful.

### setPlanarMoveVisibility(isVisible: boolean) -> boolean
A convenience method to turn on and off the visibility of the X-Y, Y-Z, and Z-X planar translation controls.
- **isVisible** (boolean): Defines if the visibility of the controls should be turned on or off. True indicates they will be visible.
- **Returns** (boolean): Returns true if it was successful.

### setRotateVisibility(isVisible: boolean) -> boolean
A convenience method to turn on and off the visibility of the X, Y, and Z axis rotation controls.
- **isVisible** (boolean): Defines if the visibility of the controls should be turned on or off. True indicates they will be visible.
- **Returns** (boolean): Returns true if it was successful.

### setScaleVisibility(isVisible: boolean) -> boolean
A convenience method to turn on and off the visibility of the controls that define scaling in the X, Y, and Z direction and the X-Y, Y-Z, and Z-X planes.
- **isVisible** (boolean): Defines if the visibility of the controls should be turned on or off. True indicates they will be visible.
- **Returns** (boolean): Returns true if it was successful.

### setTranslateVisibility(isVisible: boolean) -> boolean
A convenience method to turn on and off the visibility of the X, Y, and Z translation controls.
- **isVisible** (boolean): Defines if the visibility of the controls should be turned on or off. True indicates they will be visible.
- **Returns** (boolean): Returns true if it was successful.

## Properties

### commandInputs : CommandInputs [read-only]
Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

### id : string [read-only]
Gets the unique identifier for this input in the command's CommandInputs.

### isEnabled : boolean [read-write]
Gets or sets if this input is currently enabled or disabled for user interaction.

Currently, the isEnabled property does not disable SelectionCommandInput objects but instead has the same effect as the SelectionCommandInput.hasFocus property.

### isFlippedHorizontal : boolean [read-write]
Gets and sets if the triad is flipped horizontally (around the around the Y-Z plane of the triad).

### isFlippedVertical : boolean [read-write]
Gets and sets if the triad is flipped vertically (around the around the X-Z plane of the triad).

### isFullWidth : boolean [read-write]
Gets or sets if this input fills the entire width of the dialog. If true, the name is ignored and the input control will fill the entire width of the command dialog. The default value for this property in a new command input if false, or not to fill the width. This property does not apply to GroupCommandInputs or TabCommandInputs.

### isHorizontalFlipVisible : boolean [read-write]
Gets and sets if the control that lets the user flip horizontally (around the Y-Z plane of the triad) is visible in both the graphical manipulator and the dialog.

### isOriginTranslationVisible : boolean [read-write]
Gets and sets if the control that supports translation in the X, Y, and Z directions is visible in both the graphical manipulator and in the dialog. In the manipulator, this is the large dot at the origin or the triad.

### isUnifiedScalingVisible : boolean [read-write]
Gets and sets if the control that defines the scaling in all directions visible in both the graphical manipulator and in the dialog.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isValidExpressions : boolean [read-only]
Returns true if all of the input fields have valid expressions. If this property is false, the triad is incorrectly defined and the current values should not be used.

### isVerticalFlipVisible : boolean [read-write]
Gets and sets if the control that lets the user flip vertical (around the X-Z plane of the triad) is visible in both the graphical manipulator and the dialog.

### isVisible : boolean [read-write]
Gets or sets if this input will be visible to the user.

Setting a SelectionCommandInput to be invisible will clear any selections it currently has.

### isXRotationVisible : boolean [read-write]
Gets and sets if the control that defines the rotation around the X axis is visible in both the graphical manipulator and in the dialog.

### isXScalingInXYVisible : boolean [read-write]
Gets and sets if the control that defines the scaling along the X axis is visible in both the graphical manipulator and in the dialog. This control lies on the X-Y plane of the triad.

### isXScalingInXZVisible : boolean [read-write]
Gets and sets if the control that defines the scaling along the X axis is visible in both the graphical manipulator and in the dialog. This control lies on the X-Z plane of the triad.

### isXTranslationVisible : boolean [read-write]
Gets and sets if the control that supports X Translation is visible in both the graphical manipulator and in the dialog.

### isXYPlaneScalingVisible : boolean [read-write]
Gets and sets if the control that defines the scaling in the X-Y plane is visible in both the graphical manipulator and in the dialog.

### isXYPlaneTranslationVisible : boolean [read-write]
Gets and sets if the control that defines the translation in the X-Y plane is visible in both the graphical manipulator and in the dialog.

### isXZPlaneScalingVisible : boolean [read-write]
Gets and sets if the control that defines the scaling in the X-Z plane is visible in both the graphical manipulator and in the dialog.

### isXZPlaneTranslationVisible : boolean [read-write]
Gets and sets if the control that defines the translation in the X-Z plane is visible in both the graphical manipulator and in the dialog.

### isYRotationVisible : boolean [read-write]
Gets and sets if the control that defines the rotation around the Y axis is visible in both the graphical manipulator and in the dialog.

### isYScalingInXYVisible : boolean [read-write]
Gets and sets if the control that defines the scaling along the Y axis is visible in both the graphical manipulator and in the dialog. This control lies on the X-Y plane of the triad.

### isYScalingInYZVisible : boolean [read-write]
Gets and sets if the control that defines the scaling along the Y axis is visible in both the graphical manipulator and in the dialog. This control lies on the Y-Z plane of the triad.

### isYTranslationVisible : boolean [read-write]
Gets and sets if the control that defines the Y Translation is visible in both the graphical manipulator and in the dialog.

### isYZPlaneScalingVisible : boolean [read-write]
Gets and sets if the control that defines the scaling in the Y-Z plane is visible in both the graphical manipulator and in the dialog.

### isYZPlaneTranslationVisible : boolean [read-write]
Gets and sets if the control that defines the translation in the Y-Z plane is visible in both the graphical manipulator and in the dialog.

### isZRotationVisible : boolean [read-write]
Gets and sets if the control that defines the rotation around the Z axis is visible in both the graphical manipulator and in the dialog.

### isZScalingInXZVisible : boolean [read-write]
Gets and sets if the control that defines the scaling along the Z axis is visible in both the graphical manipulator and in the dialog. This control lies on the X-Z plane of the triad.

### isZScalingInYZVisible : boolean [read-write]
Gets and sets if the control that defines the scaling along the Z axis is visible in both the graphical manipulator and in the dialog. This control lies on the Y-Z plane of the triad.

### isZTranslationVisible : boolean [read-write]
Gets and sets if the control that defines the Z Translation is visible in both the graphical manipulator and in the dialog.

### lastChangeMade : TriadChanges [read-only]
Returns which value was most recently changed. To determine the actual change made you need to compare the transforms returned by the transform and lastTransform properties. Having information about the specific type of change made makes it easier to compare the matrices because you know what to look for.

### lastTransform : Matrix3D [read-only]
Returns the transform of the triad before the latest change. Using the matrices returned by this property and the transform property you can determine what changed. The lastChangeMade property is also useful to help you know the type of change to look for when comparing the matrices.

### name : string [read-only]
Gets the user visible name of this input.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentCommand : Command [read-only]
Gets the parent Command.

### parentCommandInput : CommandInput [read-only]
Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent.

### positionTransform : Matrix3D [read-only]
Gets the current position and orientation of the triad using a transformation matrix. This transform does not include any scaling.

### toolClipFilename : string [read-write]
Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

### tooltip : string [read-write]
Gets or sets the base tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control.

### tooltipDescription : string [read-write]
Gets or sets additional text to display progressively along with the tooltip. The text for the description can contain some basic HTML formatting tags to format the tags. For example the br tag can be used to create multiple paragraphs. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

### transform : Matrix3D [read-write]
Gets or sets the current position, orientation, and scale of the triad using a transformation matrix.

### unifiedeScaleFactor : double [read-write]
Gets and sets the current value of the unified scale factor of the triad.

The isValidExpressions property should be checked before using the value within the command.

### unifiedScaleFactorExpression : string [read-write]
Gets or sets the expression displayed in the input field for the unified scale. This can contain equations and references to parameters but must result in a valid unitless expression.

### xRotation : double [read-write]
Gets and sets the current value of the rotation around the X axis of the triad. The value is in radians but will be displayed to the user in degrees.

The isValidExpressions property should be checked before using the value within the command.

### xRotationExpression : string [read-write]
Gets or sets the expression displayed in the input field for the X rotation. This can contain equations and references to parameters but must result in a valid distance expression. If units are not specified as part of the expression degrees are used.

### xScaleFactor : double [read-write]
Gets and sets the current value of the scale factor along the X axis of the triad.

The isValidExpressions property should be checked before using the value within the command.

### xScaleFactorExpression : string [read-write]
Gets or sets the expression displayed in the input field for the X scale. This can contain equations and references to parameters but must result in a valid unitless expression.

### xTranslation : double [read-write]
Gets and sets the current value of the translation along the X axis of the triad. The value is in centimeters but will be displayed to the user in default units for the design.

The isValidExpressions property should be checked before using the returned value.

### xTranslationExpression : string [read-write]
Gets or sets the expression displayed in the input field for the X translation. This can contain equations and references to parameters but must result in a valid distance expression. If units are not specified as part of the expression, the default user units of length are used.

### xYPlaneScaleFactor : double [read-write]
Gets and sets the current value of the scale factor on the X-Y plane of the triad.

The isValidExpressions property should be checked before using the value within the command.

### xYPlaneScaleFactorExpression : string [read-write]
Gets or sets the expression displayed in the input field for the X-Y plane scale. This can contain equations and references to parameters but must result in a valid unitless expression.

### yRotation : double [read-write]
Gets and sets the current value of the rotation around the Y axis of the triad. The value is in radians but will be displayed to the user in degrees.

The isValidExpressions property should be checked before using the value within the command.

### yRotationExpression : string [read-write]
Gets or sets the expression displayed in the input field for the Y rotation. This can contain equations and references to parameters but must result in a valid distance expression. If units are not specified as part of the expression degrees are used.

### yScaleFactor : double [read-write]
Gets and sets the current value of the scale factor along the Y axis of the triad.

The isValidExpressions property should be checked before using the value within the command.

### yScaleFactorExpression : string [read-write]
Gets or sets the expression displayed in the input field for the Y scale. This can contain equations and references to parameters but must result in a valid unitless expression.

### yTranslation : double [read-write]
Gets and sets the current value of the translation along the Y axis of the triad. The value is in centimeters but will be displayed to the user in default units for the design.

The isValidExpressions property should be checked before using the value within the command.

### yTranslationExpression : string [read-write]
Gets or sets the expression displayed in the input field for the Y translation. This can contain equations and references to parameters but must result in a valid distance expression. If units are not specified as part of the expression, the default user units of length are used.

### yZPlaneScaleFactor : double [read-write]
Gets and sets the current value of the scale factor on the Y-Z plane of the triad.

The isValidExpressions property should be checked before using the value within the command.

### yZPlaneScaleFactorExpression : string [read-write]
Gets or sets the expression displayed in the input field for the Y-Z plane scale. This can contain equations and references to parameters but must result in a valid unitless expression.

### zRotation : double [read-write]
Gets and sets the current value of the rotation around the Z axis of the triad. The value is in radians but will be displayed to the user in degrees.

The isValidExpressions property should be checked before using the value within the command.

### zRotationExpression : string [read-write]
Gets or sets the expression displayed in the input field for the Z rotation. This can contain equations and references to parameters but must result in a valid distance expression. If units are not specified as part of the expression degrees are used.

### zScaleFactor : double [read-write]
Gets and sets the current value of the scale factor along the Z axis of the triad.

The isValidExpressions property should be checked before using the value within the command.

### zScaleFactorExpression : string [read-write]
Gets or sets the expression displayed in the input field for the Z scale. This can contain equations and references to parameters but must result in a valid unitless expression.

### zTranslation : double [read-write]
Gets and sets the current value of the translation along the Z axis of the triad. The value is in centimeters but will be displayed to the user in default units for the design.

The isValidExpressions property should be checked before using the value within the command.

### zTranslationExpression : string [read-write]
Gets or sets the expression displayed in the input field for the Z translation. This can contain equations and references to parameters but must result in a valid distance expression. If units are not specified as part of the expression, the default user units of length are used.

### zXPlaneScaleFactor : double [read-write]
Gets and sets the current value of the scale factor on the Z-X plane of the triad.

The isValidExpressions property should be checked before using the value within the command.

### zXPlaneScaleFactorExpression : string [read-write]
Gets or sets the expression displayed in the input field for the Z-X plane scale. This can contain equations and references to parameters but must result in a valid unitless expression.
