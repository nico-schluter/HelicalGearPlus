# Palette
Namespace: adsk.core
Inherits: Base
Since: March 2017

A Palette is a floating or docked dialog in Fusion. The browser is an example of a built-in palette. The contents of a custom palette are created by displaying an HTML file.

**Accessed from:** Palettes.add, Palettes.add2, Palettes.addTransparent, Palettes.item, Palettes.itemById

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this palette. Fusion native palettes cannot be deleted. Use the isNative property to determine if this is a native or API created palette.
- **Returns** (boolean): Returns true if the delete was successful.

### sendInfoToHTML(action: string, data: string) -> string
Sends the string to the JavaScript associated with the loaded HTML.
- **action** (string): The "action" string to pass to the JavaScript associated with the HTML. This string can be anything but will typically be JSON formatted information.
- **data** (string): The "data" string to pass to the JavaScript associated with the HTML. This string can be anything but will typically be JSON formatted information.
- **Returns** (string): Returns a string that can be anything that your JavaScript code generates. The JavaScript should always return some content because an empty string is used to indicate a failure.

If useNewWebBrowser flag is set to true while creating the palette control this API call will be asynchronous and an empty string is returned. Response will come in data field of HTMLEvent with action equal to 'response'.

### setMaximumSize(width: integer, height: integer) -> boolean
Sets the maximum size of the palette. The user cannot resize it to be larger than this size. This does not change the current size of the palette unless the palette is already larger than this size.

Calling this method and setting the width and height to zero, removes the maximum size restriction.
- **width** (integer): Specifies the maximum width of the palette.
- **height** (integer): Specifies the maximum height of the palette.
- **Returns** (boolean): Returns true if setting the maximum size was successful.

### setMinimumSize(width: integer, height: integer) -> boolean
Sets the minimum size of the palette. The user cannot resize it to be smaller than this size. This does not change the current size of the palette unless the palette is already smaller than this size.

Calling this method and setting the width and height to zero, removes the minimum size restriction.
- **width** (integer): Specifies the minimum width of the palette.
- **height** (integer): Specifies the minimum height of the palette.
- **Returns** (boolean): Returns true if setting the minimum size was successful.

### setPosition(left: integer, top: integer) -> boolean
Sets the position of the palette. If the palette is docked or snapped, this will result in changing it to be floating.
- **left** (integer): The position of the left side of the palette relative to screen space and in pixels. Because palettes can be positioned outside of the Fusion window, a value of zero indicates the left side of the screen and not the Fusion window.
- **top** (integer): The position of the top of the palette relative to screen space and in pixels. Because palettes can be positioned outside of the Fusion window, a value of zero indicates the top of the screen and not the Fusion window.
- **Returns** (boolean): Returns true if setting the position was successful.

### setSize(width: integer, height: integer) -> boolean
Sets the size of the palette. This is best used for a floating palette because either the width or height can be locked when a palette is docked.
- **width** (integer): Specifies the width of the palette. Depending on how the palette is docked or snapped, the width may not be editable.
- **height** (integer): Specifies the height of the palette. Depending on how the palette is docked or snapped, the height may not be editable.
- **Returns** (boolean): Returns true if the sizing was succesful. It is still considered a success even if the width or height could not be changed because of how the palette is docked or snapped.

### snapTo(palette: Palette, snapOption: PaletteSnapOptions) -> boolean
Snaps this palette to another palette.
- **palette** (Palette): Specifies the palette to snap to.
- **snapOption** (PaletteSnapOptions): Specifies how this palette should be snapped to the other palette.
- **Returns** (boolean): Returns true if the palette was successfully snapped to the other palette.

## Properties

### dockingOption : PaletteDockingOptions [read-write]
Defines the docking behavior for this palette. This controls how the user is allowed to dock the palette.

### dockingState : PaletteDockingStates [read-write]
Gets and sets how the palette is currently docked.

### height : integer [read-write]
Gets and sets the height of the palette. Setting this property may not always set the height. Depending on how the palette is docked or snapped, the height may not be editable.

### htmlFileURL : string [read-write]
Gets and sets the URL to the HTML file that will be displayed in the palette. This can be a local file or a URL on the web where the HTML will be read. To avoid reading a file, this can also be the full HTML definition as a string.

If you are providing the HTML content as a string, it should begin with the element. Any references made in the HTML should be to URL's and not local files since the local path is ambiguous.

### id : string [read-only]
Gets The unique, language independent, ID of this palette.

### isNative : boolean [read-only]
Indicates if this is one of the standard Fusion palettes or a custom palette created through the API. If true, it is a standard Fusion palette and will have some restrictions on changing its properties and cannot be deleted.

### isTransparent : boolean [read-only]
Returns if this palette was created as a transparent palette.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-write]
Gets and sets whether this palette is currently being displayed in the user interface.

### left : integer [read-write]
Gets and sets the left side of the palette relative to screen space and in pixels. Because palettes can be positioned outside of the Fusion window, a value of zero indicates the left side of the screen and not the Fusion window.

### name : string [read-write]
Gets and set the name of the palette as seen in the user interface. The name of native palettes cannot be set.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### top : integer [read-write]
Gets and sets the top of the palette relative to screen space and in pixels. Because palettes can be positioned outside of the Fusion window, a value of zero indicates the top of the screen and not the Fusion window.

### width : integer [read-write]
Gets and sets the width of the palette. Setting this property may not always set the width. Depending on how the palette is docked or snapped, the width may not be editable.

## Events

### closed
This event is fired when the user clicks the "Close" button on the palette. You can choose if the "Close" button is available or not when you initially create the palette. When a palette is closed, it still exists but is change to invisible so you can still interact with it and retrieve any needed information and can make it visible again. Use the deleteMe method to delete the palette.

### incomingFromHTML
This event is fired when the JavaScript associated with the HTML calls the adsk.fusionSendData function. This allows the HTML to communicate with the add-in by passing information to the add-in.

### navigatingURL
This event is fired when a navigation event occurs on the page. This allows the add-in to determine how this navigation should be handled by the browser.

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
