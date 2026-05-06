# Attribute
Namespace: adsk.core
Inherits: Base
Since: May 2016

Represents an attribute associated with a specific entity, Product, or Document. An attribute is a named value.

**Accessed from:** Attributes.add, Attributes.item, Attributes.itemByName, Attributes.itemsByGroup, CAM.findAttributes, Design.findAttributes, Drawing.findAttributes, FlatPatternProduct.findAttributes, Product.findAttributes, WorkingModel.findAttributes

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this attribute.
- **Returns** (boolean): Returns true if the delete was successful.

## Properties

### groupName : string [read-only]
Gets the name of the group this attribute is a part of.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
Gets the name of the attribute.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### otherParents : ObjectCollection [read-only]
In the case where the entity the attribute was originally placed on has been split, this property will return the other entities the attribute is associated with. For example, if an attribute is placed on a face and then a slot is created that cuts the face into two pieces and the attribute is available from both faces. The parent property returns the "primary" entity and this property returns any other entities, if any. If there aren't any other associated entities the ObjectCollection returned will be empty.

### parent : Base [read-only]
Returns the parent entity this attribute is associated with. This can return null in some cases. For example a BRepEdge might have been consumed by a fillet feature but can come back if the model is rolled back or the fillet is deleted.

It's possible that the original parent that an attribute was placed on has been split. For example, if an attribute is placed on a face and then a slot is created that cuts the face into two pieces and the attribute is available from each face. In this case the parent property will return the "primary" face, which in most cases is somewhat arbitrary. You can get the other entities the attribute is associated with by using the otherParents property.

### value : string [read-write]
Gets and sets the value of this attribute.

The size of an attribute value is limited to 2MB (2097152 bytes). If you need to save data that is larger than 2MB you'll need to break the data into pieces and save it in multiple attributes.
