# UserInterface
Namespace: adsk.core
Inherits: Base
Since: August 2014

Provides access to the user-interface related objects and functionality.

**Accessed from:** Application.userInterface, Toolbar.parentUserInterface, ToolbarPanel.parentUserInterface, ToolbarTab.parentUserInterface

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createCloudFileDialog() -> CloudFileDialog
Creates a new CloudFileDialog object which provides the ability to show a file selection dialog to the user that allows them to choose a file from Fusion web client.
- **Returns** (CloudFileDialog): Returns the created CloudFileDialog object that you can use to define the contents of and display a standard file dialog.

### createFileDialog() -> FileDialog
Creates a new FileDialog object which provides the ability to show a standard file selection dialog to the user.
- **Returns** (FileDialog): Returns the created FileDialog object that you can use to define the contents of and display a standard file dialog.

### createFolderDialog() -> FolderDialog
Creates a new FolderDialog object which provides the ability to show a standard folder selection dialog to the user.
- **Returns** (FolderDialog): Returns the created FolderDialog object that you can use to define the contents of and display a standard folder dialog.

### createProgressDialog() -> ProgressDialog
Creates a new ProgressDialog object that you can use to display and control a progress dialog.
- **Returns** (ProgressDialog): Returns the created ProgressDialog object that you can use to define the contents of and display a progress dialog.

### getText(module: string, id: string, defaultValue: string) -> string
Get the localized text for a specific application text string. The strings used by Fusion are stored in localized XML files that are installed with Fusion. On Windows, you can find them here:

%LocalAppData%\Autodesk\webdeploy\production\VERSION_CODE\StringTable

And on Mac, you can find them here:

~/Library/Application Support/Autodesk/webdeploy/production/VERSION_CODE/Autodesk Fusion.app/Contents/Libraries/Neutron/StringTable

There is a folder for each language that Fusion supports, and the strings for that language are defined in files within that folder. Fusion will use the language specified by the user in their preferences.
- **module** (string): The module name. This is the same as the StringTable .xml filename without the .xml extension and without the version number. For example, the file NaFusionUI10.xml contains many of the strings used for Fusion's modeling commands. When specifying the module, this is specified as "NaFusionUI".
- **id** (string): The id of the text. This is the same as the 'commandName' field in the StringTable .xml file.
- **defaultValue** (string): A default string value to return if the module or string id is not found in the current locale.
- **Returns** (string): The localized string or the defaultValue if one is not found.

### inputBox(prompt: string, cancelled: boolean, title: string, defaultValue: string) -> string
Displays a modal dialog to get string input from the user.
- **prompt** (string): The message text to display in the dialog.
- **cancelled** (boolean): Indicates if the dialog was canceled.
- **title** (string): Sets the title for the dialog if specified, otherwise the script or add-in name is used.

This is an optional argument whose default value is "".
- **defaultValue** (string): The default string that's shown when the dialog is initially displayed, otherwise the input box is empty.

This is an optional argument whose default value is "".
- **Returns** (string): Returns the string entered by the user but because the user can click Cancel, the canceled argument should be tested before using the string.

### messageBox(text: string, title: string, buttons: MessageBoxButtonTypes, icon: MessageBoxIconTypes) -> DialogResults
Display a modal message box with the provided text.
- **text** (string): The message text to display in the dialog.
- **title** (string): If the optional title argument is provided, it sets the title for the dialog, otherwise the script or add-in name is used.

This is an optional argument whose default value is "".
- **buttons** (MessageBoxButtonTypes): The optional buttons array can be used to specify which buttons to display on the dialog. The first button provided is the default action. If buttons are not specified, the dialog will default to a single OK button.

This is an optional argument whose default value is MessageBoxButtonTypes.OKButtonType.
- **icon** (MessageBoxIconTypes): The optional icon argument can be used to specify which icon to display, otherwise the default of no icon is used.

This is an optional argument whose default value is MessageBoxIconTypes.NoIconIconType.
- **Returns** (DialogResults): The button pressed to dismiss the dialog is returned.

### selectEntity(prompt: string, filter: string) -> Selection
Supports the selection of a single entity. This provides a simple way to prompt the user for for a selection in a script. If you need more control over the selection a command should be created and a SelectionCommandInput used.
- **prompt** (string): The prompt displayed to the user during the selection.
- **filter** (string): A string defining the types of entities valid for selection. The valid list of selection filters can be found here: Selection Filters. You can combine multiple types by using a comma delimiter. For example, the string "PlanarFaces,ConstructionPlanes" will allow the selection of either a planar face or a construction plane.
- **Returns** (Selection): Returns a Selection object that provides access the selected entity through it's "entity" property along with the location in space where the entity was selected. Asserts if the selection is aborted.

### terminateActiveCommand() -> boolean
Method that causes the currently active (running) command to be terminated
- **Returns** (boolean): Returns true if terminating the active command was successful.

### toolbarPanelsByProductType(productType: string) -> ToolbarPanelList
Gets all of the toolbar panels associated with the specified product.
- **productType** (string): The name of the product that you want the associated workspaces for. The full list of available products can be obtained by using the Application.supportedProductTypes property.
- **Returns** (ToolbarPanelList): Returns a list of the toolbars associated with the specified product.

### toolbarTabsByProductType(productType: string) -> ToolbarTabList
Gets all of the toolbar tabs associated with the specified product.
- **productType** (string): The name of the product that you want the associated tabs for. The full list of available products can be obtained by using the Application.supportedProductTypes property.
- **Returns** (ToolbarTabList): Returns a list of the tabs associated with the specified product.

### workspacesByProductType(productType: string) -> WorkspaceList
Returns all of the workspaces associated with the specified product.
- **productType** (string): The name of the product that you want the associated workspaces for. The full list of available products can be obtained by using the Application.supportedProductTypes property.
- **Returns** (WorkspaceList): Returns a list of the associated work spaces.

## Properties

### activeCommand : string [read-only]
Gets the id of the command definition from the active command (the one that is currently running)

### activeSelections : Selections [read-only]
Gets the current set of selected objects.

### activeToolbar : Toolbar [read-only]
Retrieve the active Toolbar being displayed in the user interface.

### activeToolbarTab : ToolbarTab [read-only]
Retrieve the active ToolbarTab being displayed in the user interface. This may be null.

### activeWorkspace : Workspace [read-only]
Gets the active workspace. The active workspace is the one currently active in the user interface. This can be null if there is no active product.

### allToolbarPanels : ToolbarPanelList [read-only]
Gets all of the toolbar panels. This returns all of the panels available, regardless of which workspace or product they're associated with.

### allToolbarTabs : ToolbarTabList [read-only]
Gets all of the toolbar tabs. This returns all of the tabs available, regardless of which workspace or product they're associated with.

### commandDefinitions : CommandDefinitions [read-only]
Gets all of the command definitions currently defined. This is all command definitions both internal and those defined through the API.

### isTabbedToolbarUI : boolean [read-only]
Returns true if Tabbed Toolbars are being used.

### isUIEnabled : boolean [read-write]
Gets and sets if the Fusion user interface is enabled or not. By default it is enabled allowing the user to interact with Fusion. When set to false, the UI is disabled which blocks all interaction, including running commands, manipulating the view and interacting with the browser.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### palettes : Palettes [read-only]
Returns the collection object that provides access to all of the existing palettes and provides the functionality to create new custom palettes.

### progressBar : ProgressBar [read-only]
Gets the ProgressBar object that can be used to display a progress bar in the lower-right corner of the Fusion window.

### statusMessage : string [read-write]
Gets and sets the current message displayed in the lower-right corner of the Fusion window. This is useful when displaying progress information to the user for the current process. Set the value to an empty string to remove the message. The lifetime of your message is indeterminant because Fusion uses the same field to display messages.

If your process is running in the main thread of Fusion, you will need to call adsk.doEvents to give control back to Fusion, so it can update the UI.

The ProgressBar can also be used as a way to communicate to the user the current progress of a running process.

### toolbars : Toolbars [read-only]
Gets a collection that provides access to the toolbars. This includes the left and right QAT, and the Navbar.

### workspaces : Workspaces [read-only]
Gets all of the workspaces currently available.

## Events

### activeSelectionChanged
This event fires whenever the contents of the active selection changes. This occurs as the user selects or unselects entities while using the Fusion Select command. The Select command is the default command that is always running if no other command is active. Pressing Escape terminates the currently active command and starts the Select command. If the Select command is running and you press Escape, it terminates the current Select command and starts a new one.

This event is only associated with the selection associated with the Select command and does not fire when any other command is running. The event fires when there is any change to the active selection, including when the selection is cleared when the Select command is terminated. It is also fired when the user clicks in an open area of the canvas to clear the current selection.

### commandCreated
The commandCreated event fires immediately after the command is created.

### commandStarting
The commandStarting event fires when a request for a command to be executed has been received but before the command is executed. Through this event, it's possible to cancel the command from being executed.

### commandTerminated
Gets an event that is fired when a command is terminated.

### markingMenuDisplaying
The markingMenuDisplaying event fires just before the marking menu and context menus are displayed. The marking menu is the round menu displayed when the user right-clicks the mouse within Fusion. The context menu is the vertical menu displayed. The event provides both the marking menu and the context menu so you can examine and edit the contents of either one or both of them before they are displayed. Fusion will then display the marking and context menu that you've customized. If either one is empty it will not be displayed.

### workspaceActivated
The workspaceActivated event fires at the VERY end of a workspace being activated. The client can add or remove WorkspaceEventHandlers from the WorkspaceEvent.

### workspaceDeactivated
The workspaceDeactivated event fires at the VERY end of a workspace being deactivated. The client can add or remove WorkspaceEventHandlers from the WorkspaceEvent.

### workspacePreActivate
The workspacePreActivate event fires at the VERY start of a workspace being activated. The client can add or remove WorkspaceEventHandlers from the WorkspaceEvent.

### workspacePreDeactivate
The workspacePreDeactivate event fires at the VERY start of a workspace being deactivated. The client can add or remove WorkspaceEventHandlers from the WorkspaceEvent.

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
