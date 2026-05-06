# ColorProperty
Namespace: adsk.core
Inherits: Property
Since: August 2014

A property that defines a color.

This is most commonly used for properties associated with materials and appearances.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### connectedTexture : AppearanceTexture [read-only]
Used for appearances and gets the associated texture, if one exists. The HasConnectedTexture property controls if there is an associated texture or not. If the parent is writable you can edit the texture. If no texture exists, this property will return null.

### hasConnectedTexture : boolean [read-write]
Specifies if this color is specified using a simple color or a texture. If this returns true the color is defined using a texture. If the parent is writable, this property can be set to true to change the definition from a simple color to a texture. You can then use the ConnectedTexture property to get the associated texture and modify it.

### hasMultipleValues : boolean [read-only]
Indicates if this property has multiple values or not.

### id : string [read-only]
Returns the unique ID of this property.

### isReadOnly : boolean [read-only]
Indicates if this property is read-only. If True any attempted edits will fail.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
Returns the name of this property as seen in the user interface. This name is localized and can change based on the current language

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Returns the parent of this property.For properties associated with an appearance this will return the parent Appearance. For properties associated with a material, this will return the parent Material. For other types of properties, this will return the PropertyGroup it is in.

### value : Color [read-write]
Gets and sets this property value if there is a color and not a texture defining this color. If a texture is used, this property returns null. Setting this property when a texture is used removes the texture and changes the color definition to a simple color.

### values : array [read-write]
Gets and sets the values associated with this property. The HasMultipleValues property indicates if this property will be returning more than one value.
