# OperationStrategy
Namespace: adsk.cam
Inherits: Base
Since: April 2023

The OperationStrategy contains information about a strategy such as its name, title and description.

**Accessed from:** Operations.compatibleStrategies, OperationStrategy.createFromString

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createFromString(name: string) -> OperationStrategy
Create an OperationStrategy for a given name.
- **name** (string): The name of the strategy. Throws an error if the strategy name is unknown.
- **Returns** (OperationStrategy): Returns the OperationStrategy for given strategy name.

## Properties

### description : string [read-only]
Get the localized description of the strategy.

### is2DStrategy : boolean [read-only]
Gets whether given OperationStrategy is a 2D strategy.

### is3DStrategy : boolean [read-only]
Gets whether given OperationStrategy is a 3D strategy.

### isAdditiveStrategy : boolean [read-only]
Gets whether given OperationStrategy is an additive strategy.

### isCuttingStrategy : boolean [read-only]
Gets whether given OperationStrategy is a cutting strategy.

### isDrillingStrategy : boolean [read-only]
Gets whether given OperationStrategy is a drilling strategy.

### isFinishingStrategy : boolean [read-only]
Gets whether given OperationStrategy is a finishing strategy.

### isGenerationAllowed : boolean [read-only]
Returns true if the strategy is allowed to be generated due to licensing and enabled preview features. Some strategies also require Active machining extension to be generated. Returns false otherwise.

### isMillingStrategy : boolean [read-only]
Gets whether given OperationStrategy is a milling strategy.

### isRotaryStrategy : boolean [read-only]
Gets whether given OperationStrategy is a rotary strategy.

### isSupportStrategy : boolean [read-only]
Gets whether given OperationStrategy is an additive support strategy.

### isTurningStrategy : boolean [read-only]
Gets whether given OperationStrategy is a turning strategy.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
Get the name of the strategy. This is equivalent to the Operation's strategy property. Use as strategy parameter when creating a OperationInput.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### title : string [read-only]
Get the localized title of the strategy.

## Samples
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
