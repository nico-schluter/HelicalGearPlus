# Color
Namespace: adsk.core
Inherits: Base
Since: August 2014

The Color class wraps all of the information that defines a simple color.

**Accessed from:** Color.create, ColorControlPoint.value, ColorGraphNodeProperty.value, ColorProperty.value, ColorProperty.values, Component.componentColor, CustomGraphicsBasicMaterialColorEffect.ambientColor, CustomGraphicsBasicMaterialColorEffect.diffuseColor, CustomGraphicsBasicMaterialColorEffect.emissiveColor, CustomGraphicsBasicMaterialColorEffect.specularColor, CustomGraphicsCoordinates.getColor, CustomGraphicsShowThroughColorEffect.color, CustomGraphicsSolidColorEffect.color, FlatPatternComponent.componentColor, SceneSettings.backgroundSolidColor, SectionAnalysis.sectionColor, SectionAnalysisInput.sectionColor, VolumetricColorSample.value

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(red: short, green: short, blue: short, opacity: short) -> Color
Creates a new color.
- **red** (short): The red component of the color. The value can be 0 to 255.
- **green** (short): The green component of the color. The value can be 0 to 255.
- **blue** (short): The blue component of the color. The value can be 0 to 255.
- **opacity** (short): The opacity of the color. The value can be 0 to 255.
- **Returns** (Color): Returns the newly created color or null if the creation failed.

### getColor(red: short, green: short, blue: short, opacity: short) -> boolean
Gets all of the information defining this color.
- **red** (short): The red component of the color. The value can be 0 to 255.
- **green** (short): The green component of the color. The value can be 0 to 255.
- **blue** (short): The blue component of the color. The value can be 0 to 255.
- **opacity** (short): The opacity of the color. The value can be 0 to 255. A value of 255 indicates it is completely opaque.
- **Returns** (boolean): Returns true if getting the color information was successful.

### setColor(red: short, green: short, blue: short, opacity: short) -> boolean
Sets all of the color information.
- **red** (short): The red component of the color. The value can be 0 to 255.
- **green** (short): The green component of the color. The value can be 0 to 255.
- **blue** (short): The blue component of the color. The value can be 0 to 255.
- **opacity** (short): The opacity of the color. The value can be 0 to 255. A value of 255 indicates it is completely opaque. Depending on where the color is used, the opacity value may be ignored.
- **Returns** (boolean): Returns true if setting the color information was successful.

## Properties

### blue : short [read-write]
Gets and sets the blue component of the color. The value can be 0 to 255.

### green : short [read-write]
Gets and sets the green component of the color. The value can be 0 to 255.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### opacity : short [read-write]
Gets and sets the opacity of the color. The value can be 0 to 255. A value of 0 is transparent and 255 is opaque.

### red : short [read-write]
Gets and sets the red component of the color. The value can be 0 to 255.
