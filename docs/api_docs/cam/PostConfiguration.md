# PostConfiguration
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Object that represents a post configuration.

**Accessed from:** NCProgram.postConfiguration, PostConfigurationQuery.execute, PostLibrary.childPostConfigurations, PostLibrary.postConfigurationAtURL

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### capability : PostCapabilities [read-only]
Gets the capabilities supported by the post. Capabilities define what types of operations can be post processed using this configuration.

### description : string [read-only]
Gets the description of the post.

### extension : string [read-only]
Gets the extension of the output file created by the post.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### vendor : string [read-only]
Gets the name of the vendor of the machine tool or controller this post configuration supports.

### version : string [read-only]
Gets the version of the post.

## Samples
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
- **Turning Workflow API Sample**: Turning Workflow API Sample
This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
