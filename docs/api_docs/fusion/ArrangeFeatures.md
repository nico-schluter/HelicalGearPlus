# ArrangeFeatures
Namespace: adsk.fusion
Inherits: Base
Since: January 2025

Provides access to the Arrange features in a component and provides the functionality to create new Arrange features

**Accessed from:** Features.arrangeFeatures

## Methods

### add(input: ArrangeFeatureInput) -> ArrangeFeature
Creates a new Arrange feature. Use the create2DInput or create3DInput method to first create an input object and fully define the required input. Then, pass that input object to the add method to create the Arrange feature.
- **input** (ArrangeFeatureInput): The ArrangeFeature2DInput or ArrangeFeature3DInput object that defines the required information needed to create a new Arrange feature. An ArrangeFeatureInput object is the logical equivalent to the command dialog when creating an Arrange feature. It provides access to the various options and collects all of the required input when creating an Arrange feature and call the add method is the API equivalent to clicking the OK button on the command dialog to create the Arrange feature.
- **Returns** (ArrangeFeature): Returns the newly created ArrangeFeature object.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(solverType: ArrangeSolverTypes) -> ArrangeFeatureInput
Creates a new ArrangeFeatureInput object. An ArrangeFeatureInput object is the logical equivalent to the command dialog when creating an Arrange feature. It provides access to the various options and collects all the required input when creating an Arrange feature. Once fully defined, you pass this into the add method to create the Arrange feature.
- **solverType** (ArrangeSolverTypes): Specify if the input will be used to define a "2D True Shape", "2D Rectangular", or "3D" type of arrange feature.
- **Returns** (ArrangeFeatureInput): Returns an ArrangeFeatureInput object or null in the case of failure.

### item(index: uinteger) -> ArrangeFeature
Returns the specified Arrange feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ArrangeFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> ArrangeFeature
Returns the specified Arrange feature using the name of the feature.
- **name** (string): The name of the Arrange feature as seen in the timeline.
- **Returns** (ArrangeFeature): Returns the specified Arrange feature, if it exists. Otherwise it returns null.

## Properties

### count : uinteger [read-only]
Returns the number of Arrange features in the component.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
