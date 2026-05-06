# PostConfigurationQuery
Namespace: adsk.cam
Inherits: Base
Since: April 2023

A PostConfigurationQuery can be used to search a LibraryLocation for a set of PostConfiguration objects matching the required properties.

**Accessed from:** PostLibrary.createQuery

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### execute() -> PostConfiguration
Query for specific posts. This PostConfiguration query.
- **Returns** (PostConfiguration): Returns a list of posts. Each returned post matches this query.

## Properties

### capability : PostCapabilities [read-write]
Specifies the capability to search for in the post library.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### location : LibraryLocations [read-write]
The location specifies the location to search in the post library. Setting the location clears any previous specified URL.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### url : URL [read-write]
The URL specifies the location and folder to search for in the post library. Setting the URL updates the location.

### vendor : string [read-write]
The case-insensitive vendor specifies the vendor of the post configuration. The default empty vendor applies to all post configurations.

## Samples
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
- **Turning Workflow API Sample**: Turning Workflow API Sample
This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
