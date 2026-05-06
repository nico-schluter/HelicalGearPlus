# ThreadFeatures
Namespace: adsk.fusion
Inherits: Base
Since: January 2015

Collection that provides access to all of the existing thread features in a component and supports the ability to create new thread features.

The creation of a tapped hole also results in the creation of a thread feature. These thread features are also returned by this collection, even though they aren't present in the timeline and are represented by the hole feature.

**Accessed from:** Features.threadFeatures

## Methods

### add(input: ThreadFeatureInput) -> ThreadFeature
Creates a new thread feature.
- **input** (ThreadFeatureInput): A ThreadFeatureInput object that defines the desired thread. Use the createInput method to create a new ThreadFeatureInput object and then use methods on it (the ThreadFeatureInput object) to define the thread.
- **Returns** (ThreadFeature): Returns the newly created ThreadFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(inputCylindricalFaces: Base, threadInfo: ThreadInfo) -> ThreadFeatureInput
Creates a ThreadFeatureInput object. This object is the API equivalent of the Thread feature dialog. It collects the required input and once fully defined you can pass this object to the ThreadFeatures.add method to create the thread feature.
- **inputCylindricalFaces** (Base): A single cylindrical BRep face or a collection of cylindrical BRep faces to thread. A collection of faces must all be from either holes (for internal threading) or all from cylinders (for external threading). Both internal and external threads cannot be created in the same feature. The faces in a collection can come from different bodies or components.
- **threadInfo** (ThreadInfo): The ThreadInfo object that defines the type and size of the thread to create. When creating a thread, the type and size of the thread is specified by referencing thread information defined in one of the XML files in the ThreadData folder within the Fusion install folder. You can use the ThreadDataQuery object to query these XML files to find the specific thread you want to create. The ThreadDataQuery object can be obtained by using the ThreadFeatures.threadDataQuery property. You then use this information to create a ThreadInfo object using the ThreadFeatures.createThreadInfo method.
- **Returns** (ThreadFeatureInput): Returns the newly created ThreadFeatureInput object or null/None if the creation failed.

### createThreadInfo(isInternal: boolean, threadType: string, threadDesignation: string, threadClass: string) -> ThreadInfo
This function is retired. See more information in the 'Remarks' section below.

Method that creates a new ThreadInfo object that can be used in creating thread features. The ThreadInfo object that defines the type and size of the thread to create. When creating a thread, the type and size of the thread is specified by referencing thread information defined in one of the XML files in the ThreadData folder within the Fusion install folder. You can use the ThreadDataQuery object to query these XML files to find the specific thread you want to create. The ThreadDataQuery object can be obtained by using the ThreadFeatures.threadDataQuery property.
- **isInternal** (boolean): Input Boolean that indicates if the thread is an internal or external thread. A value of true indicates an internal thread.
- **threadType** (string): Input string that defines the thread type.
- **threadDesignation** (string): Input string that contains the thread designation. This is input as the full thread designation that will be used in a drawing for the thread call-out. The nominal size and pitch information are extracted from the designation.
- **threadClass** (string): Input string that defines the thread class.
- **Returns** (ThreadInfo): Returns the newly created ThreadInfo object or null if the creation failed.

### item(index: uinteger) -> ThreadFeature
Function that returns the specified thread feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ThreadFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> ThreadFeature
Function that returns the specified thread feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (ThreadFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of thread features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### threadDataQuery : ThreadDataQuery [read-only]
This function is retired. See more information in the 'Remarks' section below.

Property that returns the ThreadDataQuery object. When creating a thread, the type and size of the thread is specified by referencing thread information defined in one of the XML files in the ThreadData folder. The ThreadDataQuery is an object that supports methods to query the existing threads defined in these files.

## Samples
- **Thread Feature API Sample**: Demonstrates creating a new thread feature.
