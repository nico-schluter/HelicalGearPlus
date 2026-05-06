# TextCommandPalette
Namespace: adsk.core
Inherits: Palette
Since: August 2017

Represents the palette that is the Text Command window in Fusion.

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
- **Returns** (boolean): Returns true if setting the maximum size was succesful.

### setMinimumSize(width: integer, height: integer) -> boolean
Sets the minimum size of the palette. The user cannot resize it to be smaller than this size. This does not change the current size of the palette unless the palette is already smaller than this size.

Calling this method and setting the width and height to zero, removes the minimum size restriction.
- **width** (integer): Specifies the minimum width of the palette.
- **height** (integer): Specifies the minimum height of the palette.
- **Returns** (boolean): Returns true if setting the minimum size was succesful.

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

### writeText(text: string) -> boolean
Write the specified text to the TEXT COMMAND window.
- **text** (string): The text to write to the Text Command window.
- **Returns** (boolean): Returns true if successful.

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
- **Customizing the UI using the API Sample**: Demonstrates how to work with tabs, panels, and command in the user interface. The full source for C++ and Python samples can be downloaded. This is especially useful for getting the resource files.
