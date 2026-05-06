# Palettes
Namespace: adsk.core
Inherits: Base
Since: March 2017

Provides access to a set of palettes, which are docked or floating windows that display HTML.

**Accessed from:** UserInterface.palettes

## Methods

### add(id: string, name: string, htmlFileURL: string, isVisible: boolean, showCloseButton: boolean, isResizable: boolean, width: integer, height: integer, useNewWebBrowser: boolean) -> Palette
Creates a new Palette.
- **id** (string): The unique id for this palette. The id must be unique with respect to all of the palettes.
- **name** (string): The displayed name of this palette. This is the name visible in the user interface.
- **htmlFileURL** (string): Specifies the URL to the HTML file that will be displayed in the palette. This can be a local file or on the web.
- **isVisible** (boolean): Specifies if the palette is initially visible or not. It's useful to create it invisibly, change other desired properties and then use the isVisible property to finally make it visible to the user.
- **showCloseButton** (boolean): Specifies if a "Close" button should be displayed on the palette to allow the user to easily close it.
- **isResizable** (boolean): Specifies if the palette can be resized by the user or not.
- **width** (integer): Specifies the width of the palette in pixels. If no width is specified a default width will be used.

This is an optional argument whose default value is 200.
- **height** (integer): Specifies the height of the palette in pixels. If no height is specified a default height will be used.

This is an optional argument whose default value is 200.
- **useNewWebBrowser** (boolean): Specifies if you want to use the old or new web browser. A palette is essentially a dialog that hosts a web browser. To support this type of functionality, Fusion has used CEF (Chromium Embedded Framework). Fusion is in the process of switching to the Qt Web Browser wherever an embedded browser is needed in the product. As this transition occurs, Fusion is supporting both web browsers. This argument is optional and defaults to False, which means the palette will behave as before and use the CEF browser. Setting the argument to True will cause the palette to use the new QT Web Browser.

When Fusion completes the transition to the QT Web Browser, support for the CEF browser will be removed from Fusion, and you will always get a QT Web Browser regardless of how the argument is set. Because of this, it is highly recommended you set this argument to true to use the new browser because when support for the CEF browser is removed you will automatically be forced to use the QT Web Browser.

This argument is no longer used because the new QT Web Browser is always used regardless of this parameter's value.

This is an optional argument whose default value is True.
- **Returns** (Palette): Returns the newly created palette or null in the case the creation failed.

### add2(id: string, name: string, htmlFileURL: string, isVisible: boolean, showCloseButton: boolean, isResizable: boolean, width: integer, height: integer) -> Palette
Creates a new Palette.
- **id** (string): The unique id for this palette. The id must be unique with respect to all of the palettes.
- **name** (string): The displayed name of this palette. This is the name visible in the user interface.
- **htmlFileURL** (string): Specifies the URL to the HTML file that will be displayed in the palette. This can be a local file or a URL on the web where the HTML will be read. To avoid reading a file, this can also be the full HTML definition as a string.

If you are providing the HTML content as a string, it should begin with the element. Any references made in the HTML should be to URL's and not local files since the local path is ambiguous.
- **isVisible** (boolean): Specifies if the palette is initially visible or not. It's useful to create it invisibly, change other desired properties and then use the isVisible property to finally make it visible to the user.
- **showCloseButton** (boolean): Specifies if a "Close" button should be displayed on the palette to allow the user to easily close it.
- **isResizable** (boolean): Specifies if the palette can be resized by the user or not.
- **width** (integer): Specifies the width of the palette in pixels. If no width is specified a default width will be used.

This is an optional argument whose default value is 200.
- **height** (integer): Specifies the height of the palette in pixels. If no height is specified a default height will be used.

This is an optional argument whose default value is 200.
- **Returns** (Palette): Returns the newly created palette or null in the case the creation failed.

### addTransparent(id: string, name: string, htmlFileURL: string, isVisible: boolean, showCloseButton: boolean, isResizable: boolean, isOpaqueWhenUndocked: boolean, width: integer, height: integer) -> Palette
Creates a new transparent Palette.
- **id** (string): The unique id for this palette. The id must be unique with respect to all of the palettes.
- **name** (string): The displayed name of this palette. This is the name visible in the user interface.
- **htmlFileURL** (string): Specifies the URL to the HTML file that will be displayed in the palette. This can be a local file or on the web.
- **isVisible** (boolean): Specifies if the palette is initially visible or not. It's useful to create it invisibly, change other desired properties and then use the isVisible property to finally make it visible to the user.
- **showCloseButton** (boolean): Specifies if a "Close" button should be displayed on the palette to allow the user to easily close it.
- **isResizable** (boolean): Specifies if the palette can be resized by the user or not.
- **isOpaqueWhenUndocked** (boolean): Specifies if the palette will be transparent when docked and opaque when undocked.

This is an optional argument whose default value is False.
- **width** (integer): Specifies the width of the palette in pixels. If no width is specified a default width will be used.

This is an optional argument whose default value is 200.
- **height** (integer): Specifies the height of the palette in pixels. If no height is specified a default height will be used.

This is an optional argument whose default value is 200.
- **Returns** (Palette): Returns the newly created palette or null in the case the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Palette
Returns the specified palette using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Palette): Returns the specified item or null if an invalid index was specified.

### itemById(id: string) -> Palette
Returns the palette at the specified ID.
- **id** (string): The Id of the palette within the collection to return.
- **Returns** (Palette): Returns the palette of the specified id or null if no palette has the specified id.

## Properties

### count : uinteger [read-only]
Gets the number of Palettes.

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
