# Analyses
Namespace: adsk.fusion
Inherits: Base
Since: January 2023

Provides access to the existing analysis results within a design.

**Accessed from:** Design.analyses, FlatPatternProduct.analyses, WorkingModel.analyses

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Analysis
A method that returns the specified Analysis using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Analysis): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> Analysis
A method that returns the specified Analysis using the name of the analysis as it is displayed in the browser.
- **name** (string): The name of the Analysis as it is displayed in the browser.
- **Returns** (Analysis): Returns the specified item or null if an invalid name was specified.

## Properties

### accessibilityAnalyses : AccessibilityAnalyses [read-only]
Returns the AccessibilityAnalyses object, which provides access to any existing AccessibilityAnalysis objects in the design.

### count : uinteger [read-only]
Returns the number of Analysis objects in the collection.

### curvatureCombAnalyses : CurvatureCombAnalyses [read-only]
Returns the CurvatureCombAnalyses object, which provides access to any existing CurvatureCombAnalysis objects in the design.

### curvatureMapAnalyses : CurvatureMapAnalyses [read-only]
Returns the CurvatureMapAnalyses object, which provides access to any existing CurvatureMapAnalysis objects in the design.

### draftAnalyses : DraftAnalyses [read-only]
Returns the DraftAnalyses object, which provides access to any existing DraftAnalysis objects in the design.

### isLightBulbOn : boolean [read-write]
A property that gets and sets if the display is enabled for all Analysis objects in the design. If this is false, all Analysis results will be hidden. If this is true, the Analysis objects whose isLightBulbOn property is also true will be visible.

### isoCurveAnalyses : IsoCurveAnalyses [read-only]
Returns the IsoCurveAnalyses object, which provides access to any existing IsoCurveAnalysis objects in the design.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### minimumRadiusAnalyses : MinimumRadiusAnalyses [read-only]
Returns the MinimumRadiusAnalyses object, which provides access to any existing MinimumRadiusAnalysis objects in the design.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### sectionAnalyses : SectionAnalyses [read-only]
Returns the SectionAnalyses object, which provides access to any existing SectionAnalysis objects in the design.

### zebraAnalyses : ZebraAnalyses [read-only]
Returns the ZebraAnalyses object, which provides access to any existing ZebraAnalysis objects in the design.
