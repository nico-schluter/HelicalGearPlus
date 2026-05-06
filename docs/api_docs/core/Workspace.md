# Workspace
Namespace: adsk.core
Inherits: Base
Since: August 2014

A Workspace provides access to a set of panels, which contain commands that are relevant for that particular workspace. The user can switch from one workspace to another in a product (e.g. switch from Model to Sculpt in Fusion).

**Accessed from:** UserInterface.activeWorkspace, WorkspaceEventArgs.workspace, WorkspaceList.item, WorkspaceList.itemById, Workspaces.item, Workspaces.itemById

## Methods

### activate() -> boolean
Activate the workspace (assuming it is valid to do so - a SIM workspace can't be activated if Fusion is the active product).
- **Returns** (boolean): Boolean return that indicates if the activation was successful or not.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this workspace. Only a workspace added by the API can be deleted, (IsNative is false).
- **Returns** (boolean): Boolean return that indicates if the deletion was successful or not.

## Properties

### id : string [read-only]
Gets the unique Id of the workspace that can be used programmatically to find a specific workspace. It is not affected by the current language.

### isActive : boolean [read-only]
Gets if the workspace is currently active - i.e. displayed

### isNative : boolean [read-only]
Gets if this workspace is native to Fusion or was created via the API.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
Gets the visible name of the workspace as seen in the user interface. This is the localized name.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### productType : string [read-only]
Returns the name of the product this workspace is associated with.

### resourceFolder : string [read-write]
Gets or sets the resource folder.

### toolbarPanels : ToolbarPanels [read-only]
Gets the collection containing the panels associated with this workspace. It's through this collection that you can add new toolbar panels.

### toolbarTabs : ToolbarTabs [read-only]
Gets the collection containing the tabs associated with this workspace.

### toolClipFilename : string [read-write]
Gets or sets the full filename of the image file (PNG) used for the tool clip. the tool clip is the image shown when the user hovers the mouse over the workspace name in the workspace drop-down.

### tooltip : string [read-write]
Gets or sets the tooltip text displayed for the workspace. This is the first line of text shown when the user hovers over the workspace name in the Fusion toolbar drop-down. This is typically the name of the workspace. This is different from the name in the that the name is a short name shown in the drop-down. The tooltip is only shown when the user hovers over the name and box appears providing more information about the workspace. For example, the name of the model workspace is "Model" and the tooltip is "Model Workspace".

### tooltipDescription : string [read-write]
Gets or sets the tooltip description displayed for the workspace. The tooltip description is a longer description of the workspace and is only displayed when the user hovers over the workspace name in the Fusion toolbar drop-down. The pop-up dialog that appears contains the tooltip, the tooltip description, and the tool clip which is a picture.

## Samples
- **Customizing the UI using the API Sample**: Demonstrates how to work with tabs, panels, and command in the user interface. The full source for C++ and Python samples can be downloaded. This is especially useful for getting the resource files.
- **Write user interface to a file API Sample**: Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic User-Interface Customization with Fusion's API
