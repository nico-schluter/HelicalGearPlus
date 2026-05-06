# CustomFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: January 2021

This class defines the methods and properties that pertain to the definition of a Ruled Surface feature.

**Accessed from:** CustomFeatures.createInput

## Methods

### addCustomParameter(id: string, label: string, value: ValueInput, units: string, isVisible: boolean) -> boolean
Defines the information needed to create a new custom parameter that will be associated with this feature. A custom parameter appears as a model parameter and will be listed as a child of the custom feature in the parameter dialog. The custom feature will automatically have a dependency on this parameter.
- **id** (string): An id for this parameter. This is used to allow you to identify the parameter in the future. This must be unique with respect to all other parameters associated with this custom feature. It's needed because the label does not need to be unique and the Fusion auto-generated name can be edited by the user.
- **label** (string): The label for this parameter as seen in the parameters dialog. This identifies to the user the purpose of this parameter. For example, when you create an extrusion with a specific distance, there are two parameters displayed in the parameters dialog with the labels "AlongDistance" and "TaperAngle". This does not have to be unique because in the case of a fillet feature there can be multiple parameters all labeled "Radius".
- **value** (ValueInput): ValueInput object that specifies the value of the parameter. If the ValueInput was created using a real, the value will be interpreted using the internal unit for the unit type specified by the "units" argument. For example, if the ValueInput was created using the real value 5 and the input to the "units" argument is any valid length unit, the value will be interpreted as 5 centimeters since centimeters is the internal unit for lengths. If the "units" argument is a valid angle unit the value will be interpreted as 5 radians.

If the ValueInput was created using a string, the string is used as-is for the expression of the parameter. This means if there are units as part of the string it must evaluate to the same unit type as that specified by the "units" argument and if no units are specified it will use the current default units specified for the current document. For example, if the ValueInput was created with the string "5 in", then the "units" argument must define any valid length so it is compatible. If the ValueInput was created with the string "5", any unit type can be used and the result will be 5 of that unit.

When using a ValueInput created using a string, it's the same as creating a parameter in the user-interface. You can specify any valid expression, i.e. "5", "5 in", "5 in / 2", "5 + Length", etc. and you can choose from many different types of units. The only requirement is that the units must match in type. For example, they must both be lengths, or they must both be angles.
- **units** (string): The units to use for the value of the parameter. Units specified must match the units specified (if any) in the ValueInput object.

To create a parameter with no units (unitless) you can specify either an empty string.
- **isVisible** (boolean): Optional argument that specifies if the parameter will be visible in the parameters dialog or not. By default the parameter will be visible.

This can be useful in cases where the feature can be edited to be in different states where a parameter is only valid in a certain state. You can change the visibility based on the current state of the feature and if that parameter should be available for edit. This implies that you create all the parameters that might be needed and then change their visibility based on the current state of the feature. The parameters that are not visible will not be returned by the ModelParameters collection and are only available through the custom feature they're associated with.

This is an optional argument whose default value is True.
- **Returns** (boolean): Returns true if the definition of the model parameter was successfully added.

### addDependency(id: string, entity: Base) -> boolean
Adds an entity or parameter this feature is dependent on. This is used by Fusion to know when to recompute this feature and to control the behavior of the feature's node in the timeline.
- **id** (string): An ID for this dependency. This is used to allow you to identify which dependency is which in the future. The ID must be unique with respect to the other dependencies of this custom feature.
- **entity** (Base): The entity or parameter you want to add as a dependency. This can be a BRepBody, BRepFace, BrepEdge, BRepVertex, a sketch, any sketch entities, a profile, any construction geometry, or any parameter.
- **Returns** (boolean): Returns true if the dependency was successfully added.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setStartAndEndFeatures(startFeature: Base, endFeature: Base) -> boolean
Sets the start and end features that the custom feature will group. A "feature" in this case is an object that is visible in the timeline, such as modeling features, sketches, and construction geometry. The custom feature will group the input start and end features and all features between them in the timeline.

You can determine the current start and end features using the features property and use the first and last features returned. If the custom feature contains a single feature, you can use the same feature for both the start and end feature arguments. You can also use null for both arguments to remove all features from a custom feature. The custom feature still exists but will be empty, and the features will be displayed individually within the timeline.
- **startFeature** (Base): The first feature in the timeline that the custom feature will group.
- **endFeature** (Base): The last feature in the timeline that the custom feature will group. When creating a custom feature that contains a single feature, this can be the same feature as the startFeature argument.
- **Returns** (boolean): Returns true if setting the start and end features was successful.

## Properties

### features : array [read-only]
Returns the features that are grouped by this custom feature. The start and end features and all of the features between them in the timeline are returned. This includes all entities represented in the timeline including modeling features, construction geometry, sketches, etc.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
