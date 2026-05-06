# PrintSettingQuery
Namespace: adsk.cam
Inherits: Base
Since: April 2023

A PrintSettingQuery can be used to search a LibraryLocation for a set of PrintSetting objects matching the required properties.

**Accessed from:** PrintSettingLibrary.createQuery

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### execute() -> PrintSetting
Query for specific PrintSettings. This PrintSettingQuery query.
- **Returns** (PrintSetting): Returns a list of PrintSetting. Each returned PrintSetting matches this query.

## Properties

### filamentDiameter : double [read-write]
This function is retired. See more information in the 'Remarks' section below.

The filament diameter specifies filament diameter for FFF Printer. This should match the FFF PrintSetting filament diameter in cm.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### layerHeight : double [read-write]
The layer height specifies layer height of the PrintSetting. This should match the PrintSetting layer height in cm.

### location : LibraryLocations [read-write]
The location specifies the location to search in the PrintSetting library. Setting the location clears any previous specified URL.

### machine : Machine [read-write]
The machine specifies which machine the found print setting are compatible with.

### material : string [read-write]
The case-insensitive material specifies material of the MPBF PrintSetting.

### name : string [read-write]
The case-insensitive name specifies the name of the PrintSetting.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### technology : string [read-write]
The case-insensitive technology specifies technology of the PrintSetting.

### url : URL [read-write]
The URL specifies the location and folder to search for in the PrintSetting library. Setting the URL updates the location.

### vendor : string [read-write]
The case-insensitive vendor specifies vendor of the PrintSetting. Generic FFF PrintSetting doesnt have a vendor.
