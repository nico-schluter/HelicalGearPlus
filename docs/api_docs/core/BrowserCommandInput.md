# BrowserCommandInput
Namespace: adsk.core
Inherits: CommandInput
Since: July 2021

Browser command inputs behave as a browser where you can define HTML to be displayed within the area occupied by the command input.

**Accessed from:** CommandInputs.addBrowserCommandInput, HTMLEventArgs.browserCommandInput, NavigationEventArgs.browserCommandInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this Command input.
- **Returns** (boolean): Returns true if the delete was successful.

### sendInfoToHTML(action: string, data: string) -> boolean
Sends a string to the JavaScript associated with the loaded HTML.
- **action** (string): The "action" string to pass to the JavaScript associated with the HTML. This string can be anything but will typically be JSON formatted information.
- **data** (string): The "data" string to pass to the JavaScript associated with the HTML. This string can be anything but will typically be JSON formatted information.
- **Returns** (boolean): This API call is asynchronous and true is returned if the send was successful. Any response from the JavaScript response will be returned through the incomingFromHTML event using the data field of the provided HTMLEvent object where the action property is "response".

## Properties

### commandInputs : CommandInputs [read-only]
Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

### htmlFileURL : string [read-write]
Gets and sets the URL to the HTML file currently being displayed. This can be local or on the web.

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

### maximumHeight : integer [read-write]
Gets and sets the maximum height of the browser within the command dialog, in pixels. As the user resizes the dialog, the area taken up by the browser will shrink and grow to fit within the defined space. It will never shrink to be less than the minimum height or expand to be larger than the maximum height. If the content displayed within the browser does not fit within the current area, a scroll bar will appear to allow the user to scroll to see the entire browser content. The default value of zero sets no maximum height, so the browser will expand to the maximum extent available.

### minimumHeight : integer [read-write]
Gets and sets the minimum height of the browser within the command dialog in pixels. As the user resizes the dialog, the area taken up by the browser will shrink and grow to fit within the defined space. It will never shrink to be less than the minimum height or expand to be larger than the maximum height. If the dialog can't fit the browser at the minimum size a scroll bar will appear for the dialog to allow the user to scroll to access all the inputs in the dialog.

### name : string [read-only]
Gets the user visible name of this input.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentCommand : Command [read-only]
Gets the parent Command.

### parentCommandInput : CommandInput [read-only]
Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent.

### toolClipFilename : string [read-write]
Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

### tooltip : string [read-write]
Gets or sets the base tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control.

### tooltipDescription : string [read-write]
Gets or sets additional text to display progressively along with the tooltip. The text for the description can contain some basic HTML formatting tags to format the tags. For example the br tag can be used to create multiple paragraphs. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.
