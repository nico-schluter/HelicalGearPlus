# SectionAnalyses
Namespace: adsk.fusion
Inherits: Base
Since: January 2023

Provides access to any section analyses results in the design and supports the ability to create new sections.

**Accessed from:** Analyses.sectionAnalyses

## Methods

### add(input: SectionAnalysisInput) -> SectionAnalysis
Creates a new Section Analysis.
- **input** (SectionAnalysisInput): A SectionAnalysisInput object that defines how the section analysis should be created. Use the createInput method to create a new SectionAnalysisInput object.
- **Returns** (SectionAnalysis): Returns the new SectionAnalysis object if successful.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(cutPlaneEntity: Base, distance: double) -> SectionAnalysisInput
Creates a new SectionAnalysisInput object to use when creating a new Section Analysis. A SectionAnalysisInput object is the API equivalent of the command dialog that contains the inputs to create a section analysis. Use this object to define the settings you need and then pass this into the add method to create the section analysis.
- **cutPlaneEntity** (Base): The planar entity used to define the cut plane and can be either a planar BRepFace or a ConstructionPlane object.
- **distance** (double): The offset distance of the section from the cut plane. A positive value will offset in the positive normal direction of the cut plane entity. The value is in centimeters. This value is used to create a transformation matrix that defines the specified offset.
- **Returns** (SectionAnalysisInput): Returns a SectionAnalysisInput object if successful.

### item(index: uinteger) -> SectionAnalysis
A method that returns the specified SectionAnalysis object using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SectionAnalysis): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> SectionAnalysis
A method that returns the specified SectionAnalysis object using the name of the analysis as displayed in the browser.
- **name** (string): The name of the SectionAnalysis object as displayed in the browser.
- **Returns** (SectionAnalysis): Returns the specified item or null if an invalid name was specified.

## Properties

### count : uinteger [read-only]
Returns the number of SectionAnalysis objects in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
