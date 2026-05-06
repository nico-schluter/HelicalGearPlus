# ToolbarTab
Namespace: adsk.core
Inherits: Base
Since: August 2019

Toolbar tabs are the tabs shown in the command toolbar.

**Accessed from:** ToolbarTabList.item, ToolbarTabList.itemById, ToolbarTabs.add, ToolbarTabs.item, ToolbarTabs.itemById, UserInterface.activeToolbarTab

## Methods

### activate() -> boolean
Activate this toolbar tab.
- **Returns** (boolean): Boolean return that indicates if the activation was successful or not.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this tab. Fusion native tabs cannot be deleted. Use the isNative property to determine if this is a native or API created tab.
- **Returns** (boolean): Returns true if the delete was successful.

### move(positionId: string, isBefore: boolean) -> boolean
Move this tab to a different position in the Toolbar in the user interface.
- **positionId** (string): The ID of another ToolbarTab in the same Toolbar that is used to position this tab. This tab will be positioned either directly before or after it.
- **isBefore** (boolean): If true, then this tab will be positioned directly before the tab indicated by positionID. If false, then this tab will be positioned after it.
- **Returns** (boolean): Returns true if it was successful.

## Properties

### id : string [read-only]
Gets The unique, language independent, ID of this tab.

### index : uinteger [read-only]
Gets the position this tab is in within the toolbar. The first tab is at position 0. This value is with respect to the complete list of tabs so this value could be outside of the expected range if you have a collection of tabs associated with a workspace, which is a subset of the entire list of tabs.

### isActive : boolean [read-only]
Gets if this toolbar tab is currently active - i.e. displayed.

### isNative : boolean [read-only]
Gets if this tab is native to Fusion or was created via the API.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-write]
Gets or sets whether this tab is currently being displayed in the user interface. By default, a tab is made visible if it is associated with the active workspace and hidden otherwise. Setting it here will override that default behavior.

### name : string [read-write]
Gets or sets the name of the tab as seen in the user interface.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentUserInterface : UserInterface [read-only]
Gets the parent UserInterface object.

### productType : string [read-only]
Returns the name of the product this toolbar tab is associated with.

### toolbarPanels : ToolbarPanels [read-only]
Gets the collection containing the panels associated with this tab. It's through this collection that you can add new toolbar panels.

## Samples
- **Customizing the UI using the API Sample**: Demonstrates how to work with tabs, panels, and command in the user interface. The full source for C++ and Python samples can be downloaded. This is especially useful for getting the resource files.
- **Write user interface to a file API Sample**: Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic User-Interface Customization with Fusion's API
