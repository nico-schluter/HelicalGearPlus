# ThreadInfo
Namespace: adsk.fusion
Inherits: Base
Since: January 2015

This class defines the methods and properties that define the type and size of a thread. This object is used to create and query thread and tapped (straight and tapered) hole features. A new ThreadInfo object is created by using the ThreadInfo.create method. If the ThreadInfo object is obtained from an existing thread or hole feature, modifying the ThreadInfo object will modify the feature.

**Accessed from:** HoleFeature.tappedHoleInfo, ThreadFeature.threadInfo, ThreadFeatureInput.threadInfo, ThreadFeatures.createThreadInfo, ThreadInfo.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(isTapered: boolean, isInternal: boolean, threadType: string, threadDesignation: string, threadClass: string, isRightHanded: boolean) -> ThreadInfo
This method creates a new ThreadInfo object that can be used to create a thread or tapped-hole feature. The ThreadInfo object defines the type and size of the thread to create. When creating a thread, the type and size of the thread are defined by specifying the thread type, designation, and class. Fusion uses this information to look up the full details of the thread in tables delivered with Fusion. The ThreadDataQuery object can be used to determine valid input for this information.

The thread type implicitly defines if the thread is standard or tapered. Tapered threads can only be used when creating tapped holes and are not supported for thread features.
- **isTapered** (boolean): Input Boolean that indicates if the thread is straight or tapered.
- **isInternal** (boolean): Input Boolean that indicates if the thread is internal or external. A value of true indicates an internal thread. When the ThreadInfo is used to create a tapped hole, this value is ignored since it is always an internal thread.
- **threadType** (string): Input string that defines the thread type.
- **threadDesignation** (string): Input string that contains the thread designation.
- **threadClass** (string): Input string that defines the thread class. This argument is ignored for tapered threads, so an empty string can be used.
- **isRightHanded** (boolean): Input boolean that defines if the thread is right or left-handed.
- **Returns** (ThreadInfo): Returns the newly created ThreadInfo object or null if the creation failed.

### redefine(isTapered: boolean, isInternal: boolean, threadType: string, threadDesignation: string, threadClass: string, isRightHanded: boolean) -> boolean
Method that redefines an existing ThreadInfo object. This is typically used to change the thread of an existing thread or tapped hole.

The ThreadInfo object defines the type and size of a thread by specifying the thread type, designation, and class. Fusion uses this information to look up the full details of the thread in tables delivered with Fusion. The ThreadDataQuery object can be used to determine valid input for this information.

Tapered threads can only be used when creating or editing tapped holes and are not supported for thread features.
- **isTapered** (boolean): Input Boolean that indicates if the thread is straight or tapered.
- **isInternal** (boolean): Input Boolean that indicates if the thread is internal or external. A value of true indicates an internal thread. This value is ignored when the ThreadInfo is used for a tapped hole since they are always internal.
- **threadType** (string): Input string that defines the thread type.
- **threadDesignation** (string): Input string that defines the thread designation.
- **threadClass** (string): Input string that defines the thread class. This argument is ignored for tapered threads.
- **isRightHanded** (boolean): Input Boolean that specifies if the thread is straight or tapered.
- **Returns** (boolean): Returns true if the redefinition was successful.

## Properties

### isInternal : boolean [read-write]
Returns and sets if the thread is an internal or external thread. A value of true indicates an internal thread. It defaults to true.

### isRightHanded : boolean [read-write]
Gets and sets if the thread is right or left-handed thread. A value of true indicates a right-handed thread. It defaults to true.

### isTapered : boolean [read-only]
Indicates if this ThreadInfo object defines a standard or tapered thread.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### majorDiameter : double [read-only]
Returns the value that defines the major diameter. The units are centimeters.

### minorDiameter : double [read-only]
Returns the value that defines the minor diameter. The units are centimeters.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### pitchDiameter : double [read-only]
Returns the value that defines the pitch diameter. The units are centimeters.

### taperAngle : double [read-only]
Returns the angle of the tapered thread in centimeters.

This is only valid when isTapered is true.

### taperTapDrillDiameter : double [read-only]
Returns the Diameter of the tap drill required to create this tap.

This is only valid when isTapered is true.

### taperThreadHeight : double [read-only]
Returns the height of a tapered thread in centimeters.

This is only valid when isTapered is true.

### taperUsefulThreadLength : double [read-only]
Returns the useful length of threads for a tapered thread in centimeters.

This is only valid when isTapered is true.

### taperWrenchMakeupInternalDiameter : double [read-only]
The wrench makeup internal diameter for a taper pipe thread, also known as the effective thread diameter, is the diameter at the point where the thread engagement occurs when the pipe is tightened with a wrench.

This is only valid when isTapered is true.

### threadAngle : double [read-only]
Returns the value that defines the thread angle. The units are degrees.

### threadClass : string [read-write]
Returns and sets the string that defines the thread class.

### threadDesignation : string [read-write]
Returns and sets the string that defines the thread designation.

### threadPitch : double [read-only]
Returns the value that defines the thread pitch. The units are centimeters.

### threadSize : string [read-only]
Returns the string that defines the thread size.

### threadType : string [read-write]
Returns and sets the string that defines the thread type.

## Samples
- **Thread Feature API Sample**: Demonstrates creating a new thread feature.
