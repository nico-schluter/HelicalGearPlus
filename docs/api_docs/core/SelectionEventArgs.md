# SelectionEventArgs
Namespace: adsk.core
Inherits: EventArgs
Since: August 2014

Provides a set of arguments from a firing SelectionEvent to a SelectionEventHandler's notify callback method.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### activeInput : SelectionCommandInput [read-only]
Returns the SelectionCommandInput that is currently active in the command dialog and that the user is selecting entities for. This can be used to determine which set of rules you want to apply to determine if the current entity is selectable or not.

### additionalEntities : ObjectCollection [read-write]
Gets or sets any additional entities that should be pre-highlighted and selected if the entity the mouse is over is selected. If you add an entity that is already selected, it will be unselected. The result of adding additional entities is the same as if they were selected one at a time by the user and the user can unselect each entity one at a time by picking it while it's selected.

An example of how this might be used is that the user can select a group of tangentially connected edges by picking a single edge. You can use the BrepEdge.tangentiallyConnectedEdges to easily find the tangent edges and add them to the set of additional entities to be selected. These edges are pre-highlighted and then selected.

If you are using this property you need to make sure that the selection limits for the SelectionCommandInput have been set appropriately. For example, a newly created SeletionCommandInput is set to only allow the selection of a single entity. By adding additional entities you'll need more than one entity because the entire set of entities will be added to the selection. Use the setSelectionLimits method of the SelectionCommandInput to change the number of allowed selections.

The additional entities should all be valid based on the current selection filter.

### firingEvent : Event [read-only]
The event that the firing is in response to.

### isSelectable : boolean [read-write]
Gets or sets whether this entity should be made available to be selected. The value is initialized to true, so doing nothing will result in the entity being selectable.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### selection : Selection [read-only]
Gets the entity that is valid for selection.
