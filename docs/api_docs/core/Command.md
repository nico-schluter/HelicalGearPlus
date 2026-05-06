# Command
Namespace: adsk.core
Inherits: Base
Since: August 2014

The Command class contains all of the functionality needed by a command to gather various command input from a user, provide previews, and create the final result which is also encapsulated within a transaction so it can be undone.

**Accessed from:** AngleValueCommandInput.parentCommand, BoolValueCommandInput.parentCommand, BrowserCommandInput.parentCommand, ButtonRowCommandInput.parentCommand, CommandCreatedEventArgs.command, CommandEventArgs.command, CommandInput.parentCommand, CommandInputs.command, DirectionCommandInput.parentCommand, DistanceValueCommandInput.parentCommand, DropDownCommandInput.parentCommand, FloatSliderCommandInput.parentCommand, FloatSpinnerCommandInput.parentCommand, GroupCommandInput.parentCommand, ImageCommandInput.parentCommand, IntegerSliderCommandInput.parentCommand, IntegerSpinnerCommandInput.parentCommand, RadioButtonGroupCommandInput.parentCommand, SelectionCommandInput.parentCommand, SeparatorCommandInput.parentCommand, SliderCommandInput.parentCommand, StringValueCommandInput.parentCommand, TabCommandInput.parentCommand, TableCommandInput.parentCommand, TextBoxCommandInput.parentCommand, TriadCommandInput.parentCommand, ValueCommandInput.parentCommand

## Methods

### beginStep(makeExistingStepNonUndoable: boolean) -> boolean
Begin a transacted step within the command's transaction. If the all of the command inputs are valid, this will trigger the execute event for the current step.
- **makeExistingStepNonUndoable** (boolean): If true the current step will not be undo-able.

This is an optional argument whose default value is False.
- **Returns** (boolean): Returns true if beginning the step was successful.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### doExecute(terminate: boolean) -> boolean
Causes the execution of this command which results in the execute event being fired. This is the same effect as the user clicking the "OK" button in the command dialog and is most useful when there is no command dialog (no command inputs where created) and the isAutoExecute property has been set to False. This allows you to execute the command through code.
- **terminate** (boolean): In the case where there isn't a command dialog you can also use the terminate argument to specify if the command should terminate after execution or continue running. This is similar to the sketch line command where each line placement results in the creation of an undo-able line but the command continues to run to allow additional lines to be placed.
- **Returns** (boolean): Returns true if the execution of the command was successful.

### doExecutePreview() -> boolean
Causes the executePreview event of this command to be fired. This is most useful when there is no command dialog (no command inputs where created) and the isAutoExecute property has been set to False. This allows you to force the preview to be generated instead of relying on changing command inputs.
- **Returns** (boolean): Returns true if the execute Preview event was successfully fired..

### getCursor(cursorImage: string, xHotSpot: integer, yHotSpot: integer) -> boolean
Gets the custom cursor information currently being used.
- **cursorImage** (string): The full path to the png image that is being displayed as the cursor.
- **xHotSpot** (integer): Gets the position of the x pixel within the image that is the "hot" spot or the point that is used as the mouse point. A value of zero indicates the left of the image.
- **yHotSpot** (integer): Gets the position of the y pixel within the image that is the "hot" spot or the point that is used as the mouse point. A value of zero indicates the top of the image.
- **Returns** (boolean): Returns true if getting the cursor information was successful.

### setCursor(cursorImage: string, xHotSpot: integer, yHotSpot: integer) -> boolean
Specifies the cursor to display at the mouse.
- **cursorImage** (string): The path to the PNG image to display as the cursor. This can either be a relative path from the py, dll, or dylib file of the full path. Specifying an empty string will set the cursor back to the default cursor.
- **xHotSpot** (integer): Specifies the position of the x pixel within the image that is the "hot" spot or the point that is used as the mouse point. A value of zero indicates the far left of the image. If an empty string is used as the cursorImage, this value is ignored.
- **yHotSpot** (integer): Specifies the position of the y pixel within the image that is the "hot" spot or the point that is used as the mouse point. A value of zero indicates the top of the image. If an empty string is used as the cursorImage, this value is ignored.
- **Returns** (boolean): Returns true if setting the cursor was successful.

### setDialogInitialSize(width: integer, height: integer) -> boolean
Sets the initial size of the dialog when it is first displayed. If this is not set, Fusion will use a default size for the dialog.
- **width** (integer): The width of the dialog in pixels.
- **height** (integer): The height of the dialog in pixels.
- **Returns** (boolean): Returns true if the default size was successfully set.

### setDialogMinimumSize(width: integer, height: integer) -> boolean
Sets the minimum size for the dialog when resized to by the user. If this is not set, a default minimum size is used.
- **width** (integer): The minimum width of the dialog in pixels.
- **height** (integer): The minimum height of the dialog in pixels.
- **Returns** (boolean): Returns true if the minimum size was successfully set.

### setDialogSize(width: integer, height: integer) -> boolean
Sets the size of the dialog and overrides any size. This can be used when the command is created or anytime while the command is running. If the height is zero, the dialog will be sized to fit the command inputs currently displayed.
- **width** (integer): The width of the dialog in pixels.
- **height** (integer): The height of the dialog in pixels. If zero, the dialog will be sized to fit the command inputs currently displayed.
- **Returns** (boolean): Returns true if size was successfully set.

## Properties

### cancelButtonText : string [read-write]
Gets and sets the text displayed on the Cancel button. The value of this property is ignored if the isCancelButtonVisible property is false.

### commandInputs : CommandInputs [read-only]
Gets the associated CommandInputs object which provides the ability to create new command inputs and provides access to any existing inputs that have already been created for this command.

### editingFeature : Base [read-write]
Sets the editing feature for this command. The timeline will be rolled to the editing feature on activate and will the current position will be restored on deactivate.

### hasDistinctSelectionSets : boolean [read-write]
Determines if this selection input shares a common selection set with the other selection inputs of this command or its own unique selection set. The default is False, which means each selection input will have its own selection set. This means that the items in this selection set are only shown as selected when this selection input is active. As a result, other selection inputs associated with this command can select those same entities.

If this is True, then all selection inputs share a selection set, which means that when entities are selected by any of the selection inputs of this command, they will remain selected regardless of which command input is active. This has the side effect that once an entity is selected, it cannot be selected again by another selection input.

### helpFile : string [read-write]
Gets and sets the associated HTML help file for this command.

### isAutoExecute : boolean [read-write]
Gets and sets whether this command will automatically execute if no command inputs have been defined. If any command inputs have been created, the value of this property is ignored and the command dialog will be displayed and the command will execute when the user clicks 'OK'. if no command inputs have been defined and this is set to False, then the command will not execute but will remain running.

The default value for this property is true so that the command will execute if no command inputs have been defined.

### isExecutedWhenPreEmpted : boolean [read-write]
Specifies what the behavior will be when a command is preempted by the user executing another command. If true (the default), and all of the current inputs are valid, the command will be executed just the same as if the user clicked the OK button. If false, the command is terminated.

### isOKButtonVisible : boolean [read-write]
Specifies if the OK button is visible or not. If set to false then the OK button is removed and the "CANCEL" button text changes to "CLOSE". You can override the default button text using the cancelButtonText property.

### isPositionDependent : boolean [read-write]
When working in a parametric design in Fusion and you move any occurrences, those move operations are pending and aren't captured until you use the "Capture Position" command from the POSITION panel or use the "Revert" command from the same panel to move them all back to their original positions. If the design is in a pending situation and you run a command like "Create Sketch", a dialog appears asking if you want to capture the current position or not before continuing. This is because the creation of a sketch can be dependent on the current positions of occurrences in the design. Other commands, like "Fillet", depend directly on model geometry and do not rely on occurrence positions so running the Fillet command does not display the dialog and does not affect the pending state of the occurrences.

This property allows you to specify if your command is dependent on the current position of occurrences or not. One good way to know if your command is dependent or not is to run the commands in the UI that are equivalent to the API functions you're using and see if the dialog that prompts to save or abort appears. If it does, then you know your command is dependent on occurrence positions.

If this property is true, then the dialog will appear if there are any pending moved occurrences. The user can choose whether to capture the current changes or abort them, and then your command will continue.

If you set this property to false, (which is the default), then even if there are pending changes, the occurrences are left in their current positions and your command will run.

### isRepeatable : boolean [read-write]
Gets and Sets if this command is repeatable using the 'Repeat Last Command' option from the Fusion marking menu.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### okButtonText : string [read-write]
Gets and sets the text displayed on the OK button. When the OK and Cancel buttons are displayed, this text defaults to "OK". If the Cancel button is not displayed the text defaults to "CLOSE".

### parentCommandDefinition : CommandDefinition [read-only]
Gets the parent CommandDefinition object.

## Events

### activate
Gets an event that is fired when the command is first activated or re-activated after being suspended.

### deactivate
Gets an event that is fired when the command is deactivated. The command still exists and could still be activated again.

### destroy
Gets an event that is fired when the command is destroyed. The command is destroyed and can be cleaned up.

### execute
Gets an event that is fired when the command has completed gathering the required input and now needs to perform whatever action the command does.

### executePreview
Gets an event that is fired when the command has completed gathering the required input and now needs to perform a preview.

### incomingFromHTML
This event is fired when the JavaScript associated with the HTML displayed in a BrowserCommandInput calls the adsk.fusionSendData function and when the JavaScript responds to the sendInfoToHTML call. The HTMLEventArgs provided by the event indicates which BrowserCommandInput triggered the event.

### inputChanged
Gets an event that is fired whenever an input value is changed.

### keyDown
Gets an event that is fired when a key on the keyboard is pressed down.

### keyUp
Gets an event that is fired when a key on the keyboard goes up.

### mouseClick
Gets an event that is fired when the mouse is clicked, (a button is pressed and released).

### mouseDoubleClick
Gets an event that is fired when the mouse is double-clicked, (clicked twice within the time specified by a system setting.)

### mouseDown
Gets an event that is fired when a mouse button is pressed.

### mouseDrag
Gets an event that is fired when the mouse is in drag mode, (being moved while a button is pressed).

### mouseDragBegin
Gets an event that is fired when a mouse drag starts, (the mouse is pressed and moved).

### mouseDragEnd
Gets an event that is fired when the mouse button is released after a drag.

### mouseMove
Gets an event that is fired when the mouse is moved.

### mouseUp
Gets an event that is fired when a mouse button is released.

### mouseWheel
Gets an event that is fired when the mouse wheel is rotated.

### navigatingURL
This event is fired when a navigation event occurs on the page displayed within a BrowserCommandInput. This allows the add-in to determine how this navigation should be handled by the browser. The NavigationEventArgs provided by the event indicates which BrowserCommandInput triggered the event.

### preSelect
This event is used to be able to participate in the selection process in a dynamic way. When a user is selecting geometry, they move the mouse over the model and if the entity the mouse is currently over is valid for selection it will highlight indicating that it can be selected. This process of determining what is available for selection and highlighting it is referred to as the "preselect" behavior.

You use functions on the SelectionCommandInput object to define what types of entities are selectable and in many cases this coarse level of specification is all that's needed, but in other cases you may need more control over the selection. For example, you might want to allow the user to selection construction planes and planar faces, which can easily be controlled by defining those as valid entities for selection in the SelectionCommandInput object. But if you only want to allow the user to select planes that are parallel then you need some dynamic control over the selection, which can be done using the preSelect event.

In the example of selecting parallel planes, you would still set the valid selection types for the SelectionCommandInput to allow selection of construction planes and planar faces. This will limit the selection to only planes but any plane can still be selected. You'll also need to connect to the preSelect event for the command. As the user moves the mouse over any construction plane or planar face, the preSelect event will fire for the plane the mouse is current over. If no planes have yet been selected, then you allow the user to select this plane. If one or more planes have already selected, then in the preSelect event you'll check to see if the plane the mouse is over is parallel to the first plane already selected. If it is then you allow it to be selected. If it isn't parallel then you set the isSelectable property of the provided SelectEventArgs object to False so that it won't pre-highlight and won't be selectable.

The entity and mouse position on the entity can be obtained through the Selection object returned through the selection property of the SelectionEventArgs object provided through the event.

### preSelectEnd
This event fires when the moused is moved away from an entity that was in a pre-select state. If your add-in has done something in reaction to the preSelect event, like draw some custom graphics, this event provides the notification to clean up whatever you've done that's associated with the current pre-select.

The entity and mouse position on the entity can be obtained through the Selection object returned through the selection property of the SelectionEventArgs object provided through the event.

### preSelectMouseMove
This event fires continually while the mouse is moved over an entity that is valid for selected.

The entity and mouse position on the entity can be obtained through the Selection object returned through the selection property of the SelectionEventArgs object provided through the event.

### preSelectStart
As the mouse moves over entities in the graphics window, entities valid for selection are highlighted. Before an entity is highlighted, Fusion determines if it is a valid selectable entity using the selection filter defined on the SelectionCommandInput and the preSelect event of the command. The preSelectStart event fires when the mouse first moves over an entity valid for selection. You can obtain the entity and mouse position from the Selection object returned by the selection property of the SelectionEventArgs object provided through the event.

Some related events are the preSelectMouseMove event, which fires as the mouse moves across the entity, and the preSelectEnd event, which fires when the mouse moves off the entity.

### select
This even fires when the user selects an entity. This is different from the preselect where an entity is shown as being available for selection as the mouse passes over the entity. This is the actual selection where the user has clicked the mouse on the entity.

The entity and mouse position on the entity can be obtained through the Selection object returned through the selection property of the SelectionEventArgs object provided through the event.

### selectionEvent
This function is retired. See more information in the 'Remarks' section below.

Provides a notification when the mouse passes over an entity allowing you to determine if the entity should be available for selection or not.

### unselect
This even fires when the user unselects an entity by clicking the mouse again on selected entity or canceling previous selection.

The entity and mouse position on the entity can be obtained through the Selection object returned through the selection property of the SelectionEventArgs object provided through the event.

### validateInputs
Gets an event that is fired to allow you to check if the current state of the inputs are valid for execution.

The timing of this event is indeterminate and not always tied to the editing of an input. There are cases where this isn't fired when an input is edited. This happens when an input is able to validate its content on its own. For example, if you enter an invalid value for a ValueCommandInput, it can evaluate this on its own, and as a result, the validate inputs event is not fired. Fusion will sometimes fire this event at other random times that are not tied to the edit of an input.

If you want to be notified when an input changes, you should use the input changed event instead.

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.
- **Customizing the UI using the API Sample**: Demonstrates how to work with tabs, panels, and command in the user interface. The full source for C++ and Python samples can be downloaded. This is especially useful for getting the resource files.
