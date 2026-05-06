# ToolbarPanel
Namespace: adsk.core
Inherits: Base
Since: August 2014

Toolbar panels are the panels shown in the command toolbar.

**Accessed from:** ToolbarPanelList.item, ToolbarPanelList.itemById, ToolbarPanels.add, ToolbarPanels.item, ToolbarPanels.itemById

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this toolbar panel.
- **Returns** (boolean): Returns true if the delete was successful.

### indexWithinTab(tabId: string) -> uinteger
Gets the position this panel is in within the toolbar tab. The first panel in the tab is at position 0.
- **Returns** (uinteger): Returns the index value of the panel within the tab.

## Properties

### controls : ToolbarControls [read-only]
Gets the controls associated with this panel. These are all in the panel's drop-down (assuming their visible property is true) and are selectively shown within the panel.

### id : string [read-only]
Gets The unique, language independent, ID of this panel.

### index : uinteger [read-only]
Gets the position this panel is in within the toolbar. The first panel is at position 0. This value is with respect to the complete list of panels so this value could be outside of the expected range if you have a collection of panels associated with a workspace, which is a subset of the entire list of panels.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-write]
Gets or sets whether this panel is currently being displayed in the user interface. Visibility of a panel is controlled by it being associated with the currently active workspace. Setting it here will override that default behavior.

### name : string [read-write]
Gets or sets the name of the panel as seen in the user interface.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentUserInterface : UserInterface [read-only]
Gets the parent UserInterface object.

### productType : string [read-only]
Returns the name of the product this toolbar panel is associated with.

### promotedControls : ToolbarControlList [read-only]
Gets the controls in the panel that have been promoted. Promoted controls are the controls that are displayed within the panel.

### relatedWorkspaces : ObjectCollection [read-write]
Gets or sets the set of workspaces that this panel is displayed for.

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
- **Customizing the UI using the API Sample**: Demonstrates how to work with tabs, panels, and command in the user interface. The full source for C++ and Python samples can be downloaded. This is especially useful for getting the resource files.
- **Write user interface to a file API Sample**: Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic User-Interface Customization with Fusion's API
