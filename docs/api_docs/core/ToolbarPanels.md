# ToolbarPanels
Namespace: adsk.core
Inherits: Base
Since: August 2014

Provides access to a set of toolbar panels. Many toolbar panels exist and their visibility is determined by the active workspace. A panel can be associated with one or more workspaces and when the associated workspace is active, the panel is made visible.

This collection is associated with a workspace and possibly a tab in the toolbar for that workspace. If this collection is from a toolbar tab, the collection order is the left-to-right order of panels in the toolbar tab.

**Accessed from:** ToolbarTab.toolbarPanels, Workspace.toolbarPanels

## Methods

### add(id: string, name: string, positionID: string, isBefore: boolean) -> ToolbarPanel
Creates a new ToolbarPanel. The panel is initially empty. Use the associated ToolbarControls collection to add buttons.

If this collection is associated with a tab, the new panel will be added to that tab. If this collection is not associated with a tab, the new panel will be added to the end of the "Tools" Tab. A "Tools" tab will be created for you if it does not currently exist for this collection's workspace.
- **id** (string): The unique id for this panel. The id must be unique with respect to all of the panels.
- **name** (string): The displayed name of this panel. This is the name visible in the user interface.
- **positionID** (string): Specifies the id of the panel to position this panel relative to. Not setting this value indicates that the panel will be created at the end of all other panels. The isBefore parameter specifies whether to place the panel before or after this panel.

This is an optional argument whose default value is "".
- **isBefore** (boolean): Specifies whether to place the panel before or after the panel specified by the positionID argument. This argument is ignored is positionID is not specified

This is an optional argument whose default value is True.
- **Returns** (ToolbarPanel): Returns the newly created panel or null in the case the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ToolbarPanel
Returns the specified toolbar panel using an index into the collection. When iterating by index, the panels are returned in the same order as they are shown in the user interface.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ToolbarPanel): Returns the specified item or null if an invalid index was specified.

### itemById(id: string) -> ToolbarPanel
Returns the ToolbarPanel at the specified ID.
- **id** (string): The Id of the panel within the collection to return.
- **Returns** (ToolbarPanel): Returns the ToolbarPanel of the specified id or null no panel has the specified id.

## Properties

### count : uinteger [read-only]
Gets the number of ToolbarPanels.

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
- **Customizing the UI using the API Sample**: Demonstrates how to work with tabs, panels, and command in the user interface. The full source for C++ and Python samples can be downloaded. This is especially useful for getting the resource files.
- **Write user interface to a file API Sample**: Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic User-Interface Customization with Fusion's API
