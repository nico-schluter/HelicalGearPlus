# HoleFeatures
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Collection that provides access to all of the existing hole features in a component and supports the ability to create new hole features.

**Accessed from:** Features.holeFeatures

## Methods

### add(input: HoleFeatureInput) -> HoleFeature
Creates a new hole feature based on the information provided by a HoleFeatureInput object. To create a new hole, use one of the createInput functions to define a new input object for the type of hole you want to create. Use the methods and properties on the input object to define any additional input. Once the information is defined on the input object, you can pass it to the Add method to create the hole.
- **input** (HoleFeatureInput): The HoleFeatureInput object that defines the hole you want to create.
- **Returns** (HoleFeature): Returns the newly created HoleFeature or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createCounterboreInput(holeDiameter: ValueInput, counterboreDiameter: ValueInput, counterboreDepth: ValueInput) -> HoleFeatureInput
Creates a HoleFeatureInput object that defines a counterbore hole. This is not a hole feature but an object used to create a hole feature. Functionality on the returned HoleFeatureInput object is used to define the position and extent of the hole.
- **holeDiameter** (ValueInput): A ValueInput object that defines the diameter of the hole. If the ValueInput uses a real, it is interpreted as centimeters. If it is a string, the units can be defined as part of the string (i.e. "3 in") If no units are specified, it is interpreted using the current default units for length.

If tap information is added to the hole using the returned HoleFeatureInput, it will override this diameter, and the hole will be the correct size for the specified tap.
- **counterboreDiameter** (ValueInput): A ValueInput object that defines the counterbore diameter of the hole. If the ValueInput uses a real, it is interpreted as centimeters. If it is a string, the units can be defined as part of the string (i.e. "3 in") If no units are specified, it is interpreted using the current default units for length.
- **counterboreDepth** (ValueInput): A ValueInput object that defines the counterbore depth of the hole. If the ValueInput uses a real, it is interpreted as centimeters. If it is a string, the units can be defined as part of the string (i.e. "3 in") If no units are specified, it is interpreted using the current default units for length.
- **Returns** (HoleFeatureInput): Returns the newly created HoleFeatureInput object or null if the creation failed.

### createCountersinkInput(holeDiameter: ValueInput, countersinkDiameter: ValueInput, countersinkAngle: ValueInput) -> HoleFeatureInput
Creates a HoleFeatureInput object that defines a countersink hole. This is not a hole feature but an object used to create a hole feature. Functionality on the returned HoleFeatureInput object is used to define the position and extent of the hole.
- **holeDiameter** (ValueInput): A ValueInput object that defines the diameter of the hole. If the ValueInput uses a real, it is interpreted as centimeters. If it is a string, the units can be defined as part of the string (i.e. "3 in") If no units are specified, it is interpreted using the current default units for length.

If tap information is added to the hole using the returned HoleFeatureInput, it will override this diameter, and the hole will be the correct size for the specified tap.
- **countersinkDiameter** (ValueInput): A ValueInput object that defines the diameter of the countersink. If the ValueInput uses a real, it is interpreted as centimeters. If it is a string, the units can be defined as part of the string (i.e. "3 in") If no units are specified, it is interpreted using the current default units for length.
- **countersinkAngle** (ValueInput): A ValueInput object that defines the angle of the countersink. If the ValueInput uses a real then it is interpreted as radians. If it is a string then the units can be defined as part of the string (i.e. "120 deg"). If no units are specified it is interpreted using the current default units for angles.
- **Returns** (HoleFeatureInput): Returns the newly created HoleFeatureInput object or null if the creation failed.

### createSimpleInput(holeDiameter: ValueInput) -> HoleFeatureInput
Creates a HoleFeatureInput object that defines a simple hole (a single diameter). This is not a hole feature, but an object used to create a hole feature. Functionality on the returned HoleFeatureInput object is used to define the position and extent of the hole.
- **holeDiameter** (ValueInput): A ValueInput object that defines the diameter of the hole. If the ValueInput uses a real, it is interpreted as centimeters. If it is a string, the units can be defined as part of the string (i.e. "3 in") If no units are specified, it is interpreted using the current default units for length.

If tap information is added to the hole using the returned HoleFeatureInput, it will override this diameter, and the hole will be the correct size for the specified tap.
- **Returns** (HoleFeatureInput): Returns the newly created HoleFeatureInput object or null if the creation failed.

### item(index: uinteger) -> HoleFeature
Function that returns the specified hole feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (HoleFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> HoleFeature
Function that returns the specified hole feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (HoleFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of hole features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Hole Feature API Sample**: Demonstrates creating a new hole feature.
