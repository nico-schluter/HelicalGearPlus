# PostProcessInput
Namespace: adsk.cam
Inherits: Base
Since: January 2016

This object is retired. See more information in the 'Remarks' section below.

This class defines the properties that pertain to the settings and options required for posting a toolpath to generate a CNC file. A PostProcessInput object is a required parameter for the postProcessAll() and postProcess() methods on the CAM class.

**Accessed from:** PostProcessInput.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(programName: string, postConfiguration: string, outputFolder: string, outputUnits: PostOutputUnitOptions) -> PostProcessInput
Creates a new PostProcessInput object to be used as an input argument by the postProcess() and postProcessAll() methods on the CAM class for posting toolpaths and generating CNC files.
- **programName** (string): The program name or number. If the post configuration specifies the parameter programNameIsInteger = true, then the program name must be a number.
- **postConfiguration** (string): The full filename (including the path) to the post configuration file (.cps) The post config file can be stored in any path but for convenience you can use the genericPostFolder or the personalPostFolder property on the CAM class to specify the path if your .cps file is stored in either of those locations. You must add a forward slash (this works for Mac or Windows) to the path defined by these folder properties before the filename (e.g. postConfiguration = cam.genericPostFolder + '/' + 'fanuc.cps')
- **outputFolder** (string): The path for the existing output folder where the .cnc files will be located. This method will create the specified output folder if it does not already exist. It is not necessary to add a slash to the end of the outputFolder path. You should use forward slashes in your path definition if you want your script to run on both Mac and Windows.
- **outputUnits** (PostOutputUnitOptions): The units option for the CNC output. Valid options are DocumentUnitsOutput, InchesOutput or MillimetersOutput
- **Returns** (PostProcessInput): Returns the newly created PostProcessInput object or null if the creation failed.

## Properties

### areToolChangesMinimized : boolean [read-write]
Gets and sets that operations may be reordered between setups to minimize the number of tool changes. Operations within each setup will still be executed in the programmed order. This is commonly used for tombstone machining where you have multiple setups. The default value for this property is false.

### isOpenInEditor : boolean [read-write]
Gets and sets the option if opening the CNC file with the editor after it is created. The default value for this property is true.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### outputFolder : string [read-write]
Gets and sets the path for the output folder where the .cnc files will be located.

### outputUnits : PostOutputUnitOptions [read-write]
Gets and sets the units option for the CNC output. Valid options are DocumentUnitsOutput, InchesOutput or MillimetersOutput

### postConfiguration : string [read-write]
Gets and sets the full filename (including the path) for the post configuration file (.cps)

### postProperties : NamedValues [read-write]
Gets and sets the list of post properties. Each property has a string name and a ValueInput object. The default value for this is an empty NamedValues.

### programComment : string [read-write]
Gets and sets the program comment. The default value for this property is an empty string ("").

### programName : string [read-write]
Gets and sets the program name or number. If the post configuration specifies the parameter programNameIsInteger = true, then the program name must be a number.

## Samples
- **Post Toolpaths API Sample**: Demonstrates posting toolpaths in the active document.
