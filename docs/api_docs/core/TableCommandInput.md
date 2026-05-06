# TableCommandInput
Namespace: adsk.core
Inherits: CommandInput
Since: September 2016

Represents a table within a command dialog. The table consists of rows and columns where each cell can contain another command input. The selection and button row command inputs cannot be used within a table. In addition to the rows and columns, each table can optionally have a toolbar of separate command inputs that is shown at the bottom of the table.

A table command input can conceptually be compared to an Excel table where you have an infinite number of rows and columns available but use a small portion. As you add inputs to the table, the table will adjust so all used columns are visible. The visible number of rows is controlled by you and if you create more rows than can be displayed a scroll bar becomes available.

For an example of this command input, see the loft command which uses it to show the selected profiles and rails.

**Accessed from:** CommandInputs.addTableCommandInput

## Methods

### addCommandInput(input: CommandInput, row: integer, column: integer, rowSpan: integer, columnSpan: integer) -> boolean
Adds a command input to a particular cell in the table. Rows are automatically added to the table to able to contain the command input. The command input can span multiple columns within a row and spanning across multiple rows is not currently supported.

The command input is created in the standard way but when it's added to the table using this method it will be displayed in the table instead of the main area of the dialog.
- **input** (CommandInput): The command input to associate to a cell. The command input is created in the standard way but when it's added to the table using this method it will be displayed in the table instead of the main area of the dialog.
- **row** (integer): The row index of the cell where 0 is the first row.
- **column** (integer): The column index of the cell where 0 is the first column.
- **rowSpan** (integer): The number of additional rows that this input uses. The default value of 0 indicates that no additional rows are used. Row spanning is not currently supported so this value must always be 0.

This is an optional argument whose default value is 0.
- **columnSpan** (integer): The number of additional columns that this input uses. The default value of 0 indicates that no additional columns are used.

This is an optional argument whose default value is 0.
- **Returns** (boolean): Returns true if the association of the command input to the cell was successful.

### addToolbarCommandInput(input: CommandInput) -> boolean
Adds a new command input to the toolbar at the bottom of the table.
- **input** (CommandInput): Adds a command input to the toolbar at the bottom of the table. The inputs are displayed in the same order that they're added.

The command input is created in the standard way but when it's added to the table using this method it will be displayed in the table instead of the main area of the dialog.
- **Returns** (boolean): Returns true if the command input was successfully added.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### clear() -> boolean
Removes all rows in the table and the toolbar.
- **Returns** (boolean): Returns true if successful.

### deleteMe() -> boolean
Deletes this Command input.
- **Returns** (boolean): Returns true if the delete was successful.

### deleteRow(row: integer) -> boolean
Deletes the specified row. The following rows will be shifted up. The row and the command inputs it contains are deleted. To temporarily hide a row you can set the visibility of all of the command inputs it contains to be invisible. If all inputs are invisible the row will automatically be hidden.
- **row** (integer): The row to delete where valid values are 0 to the number of rows minus 1. A value of 0 will delete the first row. A value greater than the number of rows will delete the last row.
- **Returns** (boolean): Returns true if the delete was successful.

### getInputAtPosition(row: integer, column: integer) -> CommandInput
Returns the command input that is in the specified row and column. In the case where a command input spans multiple columns, the same input can be returned from multiple positions.
- **row** (integer): The row index to return the command input from where the first row is 0.
- **column** (integer): The row index to return the command input from where the first row is 0.
- **Returns** (CommandInput): Returns the command input that is in the specified row and column. If there isn't a command input in the specified location, null is returned.

### getPosition(input: CommandInput, row: integer, column: integer, rowSpan: integer, columnSpan: integer) -> boolean
Gets the position of the specified command input within the table.
- **input** (CommandInput): The existing command input you want to find the associated cell for.
- **row** (integer): The returned row index of the cell.
- **column** (integer): The returned column index of the cell.
- **rowSpan** (integer): The returned number of additional rows used by the input. A value of 0 indicates that no additional rows are used.
- **columnSpan** (integer): The returned number of additional columns used by the input. A value of 0 indicates that no additional columns are used.
- **Returns** (boolean): Returns true if the position was successfully returned.

### removeInput(row: integer, column: integer) -> boolean
Removes the command input that is at the specified row and column. This doesn't delete the command input from the collection of inputs associated with the command but just removes it from being displayed in the table.
- **row** (integer): The row where the command input to be removed is located.
- **column** (integer): The row where the command input to be removed is located.
- **Returns** (boolean): Returns true if the removal was successful.

## Properties

### columnRatio : string [read-write]
Gets and sets the width ratio of the columns. This is defined using a string such as "1:1:1" where this defines that the first three columns are all the same width. A value of "2:1" defines that the first column is twice the width of the second.

If the table has more columns than are defined by this property, they will automatically default to a value of 1. If this property defines the width of more columns than are displayed, the extra definitions are ignored.

You can also specify 0 as a column width and this will have the effect of hiding that column. Setting a column width to 0 does not delete the column or the command inputs but only hides them so they can be turned back on at a later time by resetting the column ratio.

### columnSpacing : integer [read-write]
Gets and sets the spacing between columns. This is defined in pixels. For a newly created table, this property defaults to 1.

### commandInputs : CommandInputs [read-only]
Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

### hasGrid : boolean [read-write]
Gets and sets whether a grid is displayed for the table. For a newly created table, this property defaults to false.

### id : string [read-only]
Gets the unique identifier for this input in the command's CommandInputs.

### isEnabled : boolean [read-write]
Gets or sets if this input is currently enabled or disabled for user interaction.

Currently, the isEnabled property does not disable SelectionCommandInput objects but instead has the same effect as the SelectionCommandInput.hasFocus property.

### isFullWidth : boolean [read-write]
Gets or sets if this input fills the entire width of the dialog. If true, the name is ignored and the input control will fill the entire width of the command dialog. The default value for this property in a new command input if false, or not to fill the width. This property does not apply to GroupCommandInputs or TabCommandInputs.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-write]
Gets or sets if this input will be visible to the user.

Setting a SelectionCommandInput to be invisible will clear any selections it currently has.

### maximumVisibleRows : integer [read-write]
Gets and sets the maximum number of rows that can be displayed. As rows are added the visible size of the table will grow to show all rows until this maximum number of rows is reached and then a scroll bar will be displayed to allow the user to access all rows. For a new created table, this property defaults to 4.

### minimumVisibleRows : integer [read-write]
Gets and sets the minimum number of rows displayed. This is the minimum amount of space taken up on the command dialog, even if the table doesn't yet contain any rows. For a newly created table, this property defaults to 2.

### name : string [read-only]
Gets the user visible name of this input.

### numberOfColumns : integer [read-write]
Returns the current number of visible columns displayed. Setting this property has no effect because the number of columns is automatically inferred by the command inputs that have been added to the table. The table automatically adjusts the number of rows displayed so all inputs can be seen.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentCommand : Command [read-only]
Gets the parent Command.

### parentCommandInput : CommandInput [read-only]
Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent.

### rowCount : integer [read-only]
Returns the number of rows in the table. The actual number of rows in the table is defined by the number of rows that contain command inputs.

### rowSpacing : integer [read-write]
Gets and sets the spacing between rows. This is defined in pixels. For a newly created table, this property defaults to 1.

### selectedRow : integer [read-write]
Gets and sets which row is selected in the user-interface. A value of 0 indicates that the first row is selected. A value of -1 indicates that no row is selected.

### tablePresentationStyle : TablePresentationStyles [read-write]
Gets and sets the presentation style the table is currently using for its display.

### toolClipFilename : string [read-write]
Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

### tooltip : string [read-write]
Gets or sets the base tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control.

### tooltipDescription : string [read-write]
Gets or sets additional text to display progressively along with the tooltip. The text for the description can contain some basic HTML formatting tags to format the tags. For example the br tag can be used to create multiple paragraphs. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.
- **Custom Event for Command Dialog**: Demonstrates using a custom event to process getting information in the background to display in a command dialog. This is an add-in and should be copied and pasted into an add-in project.
