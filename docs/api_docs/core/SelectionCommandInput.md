# SelectionCommandInput
Namespace: adsk.core
Inherits: CommandInput
Since: August 2014

Provides a command input to get a selection from the user.

**Accessed from:** CommandInputs.addSelectionInput, SelectionEvent.activeInput, SelectionEventArgs.activeInput

## Methods

### addSelection(selection: Base) -> boolean
Adds the selection to the list of selections associated with this input. This method is not valid within the commandCreated event but must be used later in the command lifetime. If you want to pre-populate the selection when the command is starting, you can use this method in the activate method of the Command. It's also valid to use in other events once the command is running, such as the validateInputs event.
- **selection** (Base): The entity to add a selection of to this input. The addition may fail if the entity does not match the selection filter, or adding it would exceed the limits.
- **Returns** (boolean): Returns true if a selection to the entity was added to this input.

### addSelectionFilter(filter: string) -> boolean
Adds an additional filter to the existing filter list.
- **filter** (string): The name of a selection filter to add. The valid list of selection filters can be found here: Selection Filters.
- **Returns** (boolean): Returns true if the filter was added successfully.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### clearSelection() -> boolean
Clears the current selection so no entities are in the selection.
- **Returns** (boolean): Returns true if successful.

### clearSelectionFilter() -> boolean
Clears the list of selection filters.
- **Returns** (boolean): Returns true if successful.

### deleteMe() -> boolean
Deletes this Command input.
- **Returns** (boolean): Returns true if the delete was successful.

### getSelectionLimits(minimum: uinteger, maximum: uinteger) -> boolean
Get the limits currently defined for this input.
- **minimum** (uinteger): The minimum number of selections required. A value of zero means that there is no minimum limit.
- **maximum** (uinteger): The maximum number of selections required. A value of zero means that there is no maximum limit.
- **Returns** (boolean): Returns true if the selection limits were successfully returned.

### selection(index: uinteger) -> Selection
Returns the selection at the specified index.
- **index** (uinteger): The index of the selection to return.
- **Returns** (Selection): Returns the Selection at the specified index, or null on error.

### setSelectionLimits(minimum: uinteger, maximum: uinteger) -> boolean
Defines the limits for the number of selections associated with this input. A maximum value of 0 indicates that there is no maximum.
- **minimum** (uinteger): The minimum number of selections required. A value of zero means that there is no minimum limit.
- **maximum** (uinteger): The maximum number of selections required. A value of zero means that there is no maximum limit. If maximum is equal to minimum, then exactly that number of selections is required.

This is an optional argument whose default value is 0.
- **Returns** (boolean): Returns true if the limits were successfully set.

## Properties

### commandInputs : CommandInputs [read-only]
Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

### commandPrompt : string [read-write]
Gets or sets the tooltip shown next to the cursor.

### hasFocus : boolean [read-write]
Gets and sets if this selection input has focus with respect to other selection inputs on the command dialog. Only one selection input on a dialog can have focus at a time, so setting hasFocus to true will remove the focus from the selection input that previously had focus. When a selection input has focus; any user selections will be added to that selection input, and the selection rules associated with that selection input will apply.

Setting hasFocus to True for a selection input whose isVisible property is false will fail.

### id : string [read-only]
Gets the unique identifier for this input in the command's CommandInputs.

### isEnabled : boolean [read-write]
Gets or sets if this input is currently enabled or disabled for user interaction.

Currently, the isEnabled property does not disable SelectionCommandInput objects but instead has the same effect as the SelectionCommandInput.hasFocus property.

### isFullWidth : boolean [read-write]
Gets or sets if this input fills the entire width of the dialog. If true, the name is ignored and the input control will fill the entire width of the command dialog. The default value for this property in a new command input if false, or not to fill the width. This property does not apply to GroupCommandInputs or TabCommandInputs.

### isUseCurrentSelections : boolean [read-write]
Determines if any selections the user has made before starting the command can be used by the command's selection inputs. The default is true, which means the active selections will be added to the first selection input whose selection filter allows for that entity type. For example, if you have two selection inputs that have filters to select any number of faces and there are four faces selected when the command is started, those four faces will be selected by the selection input. If there's another selection input for the same command that has the filter set to select sketch curves, and there are faces and sketch curves selected when you start the command, the faces will be selected by the selection input filtering for faces, and the sketch curves will be selected by the selection input filtering for sketch curves.

You can programmatically control which selected entities will be added to the selection inputs by using the preSelect event of the command. The preSelect event will fire for each entity that was already selected before it's added to the selection input, and you can use it to control if it will be added to the selection input.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-write]
Gets or sets if this input will be visible to the user.

Setting a SelectionCommandInput to be invisible will clear any selections it currently has.

### name : string [read-only]
Gets the user visible name of this input.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentCommand : Command [read-only]
Gets the parent Command.

### parentCommandInput : CommandInput [read-only]
Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent.

### selectionCount : uinteger [read-only]
Gets the current number of selections the user has made for this input.

### selectionFilters : array [read-write]
Gets or sets the list of selection filters.

### toolClipFilename : string [read-write]
Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

### tooltip : string [read-write]
Gets or sets the base tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control.

### tooltipDescription : string [read-write]
Gets or sets additional text to display progressively along with the tooltip. The text for the description can contain some basic HTML formatting tags to format the tags. For example the br tag can be used to create multiple paragraphs. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.
