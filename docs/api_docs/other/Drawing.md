# Drawing
Namespace: adsk.drawing
Inherits: Product
Since: December 2020

Object that represents the drawing specific data within a drawing document.

**Accessed from:** DrawingDocument.drawing

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteEntities(entities: ObjectCollection) -> boolean
Deletes the specified set of entities that are associated with this product.
- **entities** (ObjectCollection): An ObjectCollection containing the list of entities to delete.
- **Returns** (boolean): Returns True if any of the entities provided in the list were deleted. If entities were specified that can't be deleted or aren't owned by this product, they are ignored.

### findAttributes(groupName: string, attributeName: string) -> Attribute
Find attributes attached to objects in this product that match the group and or attribute name. This does not find attributes attached directly to the Product or Document objects but finds the attributes attached to entities within the product.

The search string for both the groupName and attributeName arguments can be either an absolute name value, or a regular expression. With an absolute name, the search string must match the entire groupName or attributeName, including case. An empty string will match everything. For example if you have an attribute group named "MyStuff" that contains the attribute "Length1", using the search string "MyStuff" as the group name and "Length1" as the attribute name will find the attributes with those names. Searching for "MyStuff" as the group name and "" as the attribute name will find all attributes that have "MyStuff" as the group name.

Regular expressions provide a more flexible way of searching. To use a regular expression, prefix the input string for the groupName or attributeName arguments with "re:". The regular expression much match the entire group or attribute name. For example if you have a group that contains attributes named "Length1", "Length2", "Width1", and "Width2" and want to find any of the length attributes you can use a regular expression using the string "re:Length.*". For more information on attributes see the Attributes topic in the user manual.
- **groupName** (string): The search string for the group name. See above for more details.
- **attributeName** (string): The search string for the attribute name. See above for more details.
- **Returns** (Attribute): An array of Attribute objects that were found. An empty array is returned if no attributes were found.

## Properties

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this product.

### exportManager : DrawingExportManager [read-only]
Returns the DrawingExportManager for this drawing. You use the ExportManager to export the drawing in various formats.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### namedViews : NamedViews [read-only]
Returns the NamedViews object associated with this product. The NamedViews collection provides access to the named views defined in this product and supports the creation of new named views.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentDocument : Document [read-only]
Returns the parent Document object.

### productType : string [read-only]
Returns the product type name of this product. A list of all of the possible product types can be obtained by using the Application.supportedProductTypes property.

### selectionSets : SelectionSets [read-only]
Returns the SelectionSets object associated with this product. If the product does not support selection sets, null is returned. The SelectionSets object is used to create and access existing selection sets.

### unitsManager : UnitsManager [read-only]
Returns the UnitsManager object associated with this product.

### workspaces : WorkspaceList [read-only]
Returns the workspaces associated with this product.
