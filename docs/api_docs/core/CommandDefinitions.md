# CommandDefinitions
Namespace: adsk.core
Inherits: Base
Since: August 2014

Provides access to all of the available command definitions. This is all those created via the API but also includes the command definitions defined by Fusion for the native commands.

**Accessed from:** UserInterface.commandDefinitions

## Methods

### addButtonDefinition(id: string, name: string, tooltip: string, resourceFolder: string) -> CommandDefinition
Creates a new command definition that can be used to create a button control and handle the response when the button is clicked.
- **id** (string): The unique identifier for this command definition. It must be unique with respect to all other command definitions and is limited to the following set of characters, [A-Z][a-z][0-9] and _.
- **name** (string): The name displayed in the UI for the associated button control.
- **tooltip** (string): The full description of the command as seen in the extended tooltip in the user interface. Using the returned CommandDefinition you can also optionally set the toolClipFilename property to show an image the extended tooltip.

The width of all tooltips is limited to 300 pixels. Word wrapping is enabled, so Fusion will automatically break the line and flow your text to the next line. However, if you include a long word that exceeds 300 pixels, it doesn't wrap and the right portion will be clipped. This is common when displaying paths or URL's. If a single word is longer than 300 pixels there are a couple of options to avoid the clipping.

The first option is to insert one or more zero width space characters within the word to define where the word should be broken. The UNICODE character '\u200b' defines a zero width space. This is not displayed is only used to designate a possible break point.

The second option is to shorten the word by removing a section. For example, if the word is a full path to a file and a portion of the path is common you can remove that portion and replace it with the ellipsis character to indicate there is some missing text. There is a single UNICODE character you can use the ellipsis. It is '\u2026'.
- **resourceFolder** (string): This argument defines the resource folder that contains the images used for the icon. Icons can be defined using either PNG or SVG files. More information about icons can be found in the user manual topic User Interface Customization.

This is an optional argument and if not provided a default icon will be used.

This is an optional argument whose default value is "".
- **Returns** (CommandDefinition): Returns the created CommandDefinition object or null if the creation failed.

### addCheckBoxDefinition(id: string, name: string, tooltip: string, isChecked: boolean) -> CommandDefinition
Creates a new command definition that can be used to create a single check box control and handle the response when the check box is clicked.
- **id** (string): The unique identifier for this command definition. It must be unique with respect to all other command definitions and is limited to the following set of characters, [A-Z][a-z][0-9] and _.
- **name** (string): The name displayed in the UI for the associated check box control.
- **tooltip** (string): The full description of the command as seen in the extended tooltip in the user interface. Using the returned CommandDefinition you can also optionally set the toolClipFilename property to show an image the extended tooltip.

The width of all tooltips is limited to 300 pixels. Word wrapping is enabled, so Fusion will automatically break the line and flow your text to the next line. However, if you include a long word that exceeds 300 pixels, it doesn't wrap and the right portion will be clipped. This is common when displaying paths or URL's. If a single word is longer than 300 pixels there are a couple of options to avoid the clipping.

The first option is to insert one or more zero width space characters within the word to define where the word should be broken. The UNICODE character '\u200b' defines a zero width space. This is not displayed is only used to designate a possible break point.

The second option is to shorten the word by removing a section. For example, if the word is a full path to a file and a portion of the path is common you can remove that portion and replace it with the ellipsis character to indicate there is some missing text. There is a single UNICODE character you can use the ellipsis. It is '\u2026'.
- **isChecked** (boolean): Indicates if the initial state of the check box.
- **Returns** (CommandDefinition): Returns the created CommandDefinition object or null if the creation failed.

### addListDefinition(id: string, name: string, listControlDisplayType: ListControlDisplayTypes, resourceFolder: string) -> CommandDefinition
Creates a new command definition that can be used to create a list of check boxes, radio buttons, or text with an icon within a pop-up.

When the list is of check boxes any combinations of items in the list can be checked. The drop-down also remains displayed allowing the user to check and uncheck multiple items however a CommandCreated event is fired for every change.

When the list is of radio buttons or a list of text items, only one item in the list can be selected at a time. When an item is selected the drop-down is immediately dismissed.

The items in the list and their initial state are defined using functionality on the associated ListControlDefinition, which is accessible through the returned CommandDefinition.
- **id** (string): The unique identifier for this command definition. It must be unique with respect to all other command definitions and is limited to the following set of characters, [A-Z][a-z][0-9] and _.
- **name** (string): The name displayed in the UI for the associated selected check box list control.
- **listControlDisplayType** (ListControlDisplayTypes): Specifies the type of controls to be displayed within the list.
- **resourceFolder** (string): This argument defines the resource folder that contains the images used as the icon for items in the list. Icons can be defined using either PNG or SVG files. More information about icons can be found in the user manual topic User Interface Customization.

This is an optional argument whose default value is "".
- **Returns** (CommandDefinition): Returns the created CommandDefinition object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> CommandDefinition
Returns the CommandDefinition at the specified index.
- **index** (uinteger): The index of the command definition within the collection to return. The first item in the collection has in index of 0.
- **Returns** (CommandDefinition): Returns the CommandDefinition at the specified index or null if an invalid index is specified.

### itemById(id: string) -> CommandDefinition
Returns the CommandDefinition that has the specified ID.
- **id** (string): The ID of the command definition to return.
- **Returns** (CommandDefinition): Returns the CommandDefinition with the specified ID or null if there isn't a command definition with that ID.

## Properties

### count : uinteger [read-only]
Gets the number of command definitions.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.
- **Customizing the UI using the API Sample**: Demonstrates how to work with tabs, panels, and command in the user interface. The full source for C++ and Python samples can be downloaded. This is especially useful for getting the resource files.
