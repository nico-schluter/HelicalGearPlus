# ToolbarControls
Namespace: adsk.core
Inherits: Base
Since: August 2014

ToolbarControls is a collection of ToolbarControl objects displayed in a toolbar or menu.

**Accessed from:** DropDownControl.controls, LinearMarkingMenu.controls, Toolbar.controls, ToolbarPanel.controls

## Methods

### addCommand(commandDefinition: CommandDefinition, positionID: string, isBefore: boolean) -> CommandControl
Adds a button to the controls in the toolbar, panel, or drop-down. The ID of the created command control is inherited from the associated command definition.
- **commandDefinition** (CommandDefinition): The associated CommandDefinition that defines the resources and receives events related to this control.
- **positionID** (string): Specifies the reference id of the control to position this control relative to. Not setting this value indicates that the control will be created at the end of all other controls in toolbar. The isBefore parameter specifies whether to place the control before or after the reference control.

This is an optional argument whose default value is "".
- **isBefore** (boolean): Specifies whether to place the control before or after the reference control specified by the positionID parameter. This argument is ignored is positionID is not specified.

This is an optional argument whose default value is True.
- **Returns** (CommandControl): Returns the newly created CommandControl object or null if the creation fails.

### addDropDown(text: string, resourceFolder: string, id: string, positionID: string, isBefore: boolean) -> DropDownControl
Adds a drop-down to the controls in the toolbar, panel, or drop-down. When the drop-down is initially created it will be empty. you can get the associated ToolbarControls object from the DropDownControl to add additional controls to the drop-down.
- **text** (string): The text displayed for the drop-down in a menu. For a drop-down in a toolbar this argument is ignored because an icon is used.
- **resourceFolder** (string): This argument defines the resource folder that contains the images used for the icon when the drop-down is in a toolbar. Icons can be defined using either PNG or SVG files. More information about icons can be found in the user manual topic User Interface Customization.
- **id** (string): Optional unique ID for the control. It must be unique with respect to other controls in this collection. If the default empty string is provided, Fusion will create a unique ID.

This is an optional argument whose default value is "".
- **positionID** (string): Specifies the reference id of the control to position this control relative to. Not setting this value indicates that the control will be created at the end of all other controls in toolbar. The isBefore parameter specifies whether to place the control before or after the reference control.

This is an optional argument whose default value is "".
- **isBefore** (boolean): Specifies whether to place the control before or after the reference control specified by the positionID parameter. This argument is ignored is positionID is not specified.

This is an optional argument whose default value is True.
- **Returns** (DropDownControl): Returns the newly created DropDownControl object or null if the creation fails.

### addSeparator(id: string, positionID: string, isBefore: boolean) -> SeparatorControl
Adds a separator to the controls in the toolbar, panel, or drop-down.
- **id** (string): Optional unique ID for the control. It must be unique with respect to other controls in this collection. If the default empty string is provided, Fusion will create a unique ID.

This is an optional argument whose default value is "".
- **positionID** (string): Specifies the reference id of the control to position this separator control relative to. Not setting this value indicates that the separator control will be created at the end of all other controls in toolbar. The isBefore parameter specifies whether to place the control before or after the reference control.

This is an optional argument whose default value is "".
- **isBefore** (boolean): Specifies whether to place the separator control before or after the reference control specified by the positionID parameter. This argument is ignored is positionID is not specified.

This is an optional argument whose default value is True.
- **Returns** (SeparatorControl): Returns the newly created separator controls or null if the creation fails.

### addSplitButton(defaultDefinition: CommandDefinition, additionalDefinitions: CommandDefinition[], showLastUsed: boolean, id: string, positionID: string, isBefore: boolean) -> SplitButtonControl
Adds a split button to the controls in a toolbar. A split button has two active areas that the user can click; the main button portion and the drop-down arrow. Clicking the main button, executes the displayed command. Clicking the drop-down displays the drop-down with additional commands.

The split button itself does not fire any events, but the buttons within it will fire events to their associated command definitions.
- **defaultDefinition** (CommandDefinition): A command definition that will be used to create the main button. A button will also be created in the drop-down for this definition.
- **additionalDefinitions** (CommandDefinition[]): An array of command definitions that will be used to create the buttons on the drop-down.
- **showLastUsed** (boolean): Specifies if the split button should have the behavior where the command shown on the main button changes to the last executed command.
- **id** (string): Optional unique ID for the control. It must be unique with respect to other controls in this collection. If the default empty string is provided, Fusion will create a unique ID.

This is an optional argument whose default value is "".
- **positionID** (string): Specifies the reference id of the control to position this control relative to. Not setting this value indicates that the control will be created at the end of all other controls in toolbar. The isBefore parameter specifies whether to place the control before or after the reference control.

This is an optional argument whose default value is "".
- **isBefore** (boolean): Specifies whether to place the control before or after the reference control specified by the positionID parameter. This argument is ignored is positionID is not specified

This is an optional argument whose default value is True.
- **Returns** (SplitButtonControl): Returns the newly created SplitButtonControl object or null if the creation fails.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ToolbarControl
Returns the ToolbarControl at the specified index. When iterating by index, the controls are returned in the same order as they are shown in the user interface.
- **index** (uinteger): The index of the control within the collection to return. The first item in the collection has in index of 0.
- **Returns** (ToolbarControl): Returns the ToolbarControl at the specified index or null if an invalid index was specified.

### itemById(id: string) -> ToolbarControl
Returns the ToolbarControl at the specified ID.
- **id** (string): The ID of the control within the collection to return.
- **Returns** (ToolbarControl): Returns the ToolbarControl with the specified ID or null if no control has this ID.

## Properties

### count : uinteger [read-only]
Gets the number of controls in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Palette Sample**: Demonstrates how to create a palette, how to dock and snap palettes and how Fusion communicates with the palette HTML. The sample is an add-in. To use it, create a new Python add-in and replace the code with the code below. You also need to create an html file using the name and code below. The html file needs to be in the same folder as the py file.

When you load the add-in, you'll see two new commands under the ADD-INS panel of the TOOLS tab. The "Show Custom Palette" command will cause the custom palette to be displayed. It will remain displayed until you click its Close button. Clicking the "Click to send info to Fusion" button on the palette, will send information to your add-in, which uses the API to display that information in a message box. Running the "Send Info to HTML" command to send data to the javascript running in the palette, which uses it to update the content of a paragraph.

palette.html

<!DOCTYPE html>
<html>
<head>
</head>
<body>
<p>Click the button below to send data to Fusion.</p>
<button type='button' onclick='sendInfoToFusion()'>Click to send info to Fusion</button>
<p id='p1'>Run the "Send Info to HTML" command in the ADD-INS panel to update this text.</p>
<br /><br />

</body>
<script>
function sendInfoToFusion(){
var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0');
var yyyy = today.getFullYear();

var hours = String(today.getHours()).padStart(2, '0');
var minutes = String(today.getMinutes()).padStart(2, '0');
var seconds = String(today.getSeconds()).padStart(2, '0');

var date = dd + '/' + mm + '/' + yyyy;
var time = hours + ':' + minutes + ':' + seconds;
var args = {
arg1 : "Sample argument 1",
arg2 : "Sample argument 2"
};
adsk.fusionSendData('send', JSON.stringify(args));
}

window.fusionJavaScriptHandler = {handle: function(action, data){
try {
if (action == 'send') {
// Update a paragraph with the data passed in.
document.getElementById('p1').innerHTML = data;
}
else if (action == 'debugger') {
debugger;
}
else {
return 'Unexpected command type: ' + action;
}
} catch (e) {
console.log(e);
console.log('exception caught with command: ' + action + ', data: ' + data);
}
return 'OK';
}};
</script>
</html>
- **Write user interface to a file API Sample**: Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic User-Interface Customization with Fusion's API
