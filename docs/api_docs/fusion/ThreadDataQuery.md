# ThreadDataQuery
Namespace: adsk.fusion
Inherits: Base
Since: January 2015

This object provides methods to query the thread data contained in the XML files in ThreadData folder within the Fusion install folder. You can use the queried values to create a ThreadInfo object that is then used to create a thread feature.

**Accessed from:** ThreadDataQuery.create, ThreadFeatures.threadDataQuery

## Methods

### allClasses(isInternal: boolean, threadType: string, designation: string) -> string[]
Returns and array/list of all the available classes for a thread type of a given thread designation.
- **isInternal** (boolean): Indicates if the thread is an internal or external thread.
- **threadType** (string): The thread type of the thread class you want.
- **designation** (string): The thread designation of the thread class you want.
- **Returns** (string[]): Returns the specified thread classes or empty array/list if an invalid thread type or designation was specified.

### allDesignations(threadType: string, size: string) -> string[]
returns an array/list of all the available thread designations for a thread type of a given size. Valid thread types and sizes and be obtained by using the allThreadTypes and allSizes functions.
- **threadType** (string): The thread type of the designation you want.
- **size** (string): The thread size of the designation you want.
- **Returns** (string[]): Returns the specified thread designations or empty array/list if an invalid thread type or size was specified.

### allSizes(threadType: string) -> string[]
Returns an array/list of all the available thread sizes for a given thread type. You can use the allThreadTypes property to get the available thread types.
- **threadType** (string): Specify the thread type.
- **Returns** (string[]): Returns the specified thread sizes or an empty array/list if an invalid thread type was specified.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(isTapered: boolean) -> ThreadDataQuery
Static method to create a new ThreadDataQuery object. The ThreadDataQuery object is a utility object that provides methods to query for the valid thread definitions defined in Fusion. This object provides similar functionality as the Thread and Hole command dialogs to find valid thread types, designations and classes which can be used to create thread and tapped hole features.
- **isTapered** (boolean): Specifies if you want to query for standard or tapered holes.

This is an optional argument whose default value is False.
- **Returns** (ThreadDataQuery): Returns a ThreadDataQuery object.

### recommendThreadData(modelDiameter: double, isInternal: boolean, threadType: string, designation: string, threadClass: string) -> boolean
Method that gets the recommended thread data for a given cylinder diameter. This method is only valid for straight threads and will fail for tapered threads.
- **modelDiameter** (double): The diameter of the cylinder the thread will be placed on. The units are centimeters.
- **isInternal** (boolean): Indicates if the thread is an internal or external thread.
- **threadType** (string): Specifies the thread type to query the thread data.
- **designation** (string): The output thread designation.
- **threadClass** (string): The output thread class.
- **Returns** (boolean): Returns true if successful.

### threadTypeCustomName(threadType: string) -> string
Method that returns the custom name for a given thread type. The custom name is the localized name of the thread type using the current language specified for Fusion.
- **threadType** (string): The thread type you want to get the custom name for.
- **Returns** (string): Returns the specified custom name or an empty string if an invalid thread type was specified.

### threadTypeUnit(threadType: string) -> string
Method that returns the unit for a given thread type.
- **threadType** (string): The thread type you want to get the thread unit type for.
- **Returns** (string): Returns the specified unit or empty string if an invalid thread type was specified.

## Properties

### allThreadTypes : array [read-only]
This method returns an array of all the available thread types (families). The type names are always English. This English name should be used in the other methods that take the type as an input argument. If you need to display the type name to the user, you can use the threadTypeCustomName method To get the localized name.

### defaultInchThreadType : string [read-only]
Gets the default thread type for inch threads.

### defaultMetricThreadType : string [read-only]
Gets the default thread type for metric threads.

### isTapered : boolean [read-only]
Returns if this ThreadDataQuery was created to query for standard or tapered threads.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Thread Feature API Sample**: Demonstrates creating a new thread feature.
