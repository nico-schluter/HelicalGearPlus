# ObjectCollection
Namespace: adsk.core
Inherits: Base
Since: August 2014

Generic collection used to handle lists of any object type.

**Accessed from:** Appearance.usedBy, AsymmetricFilletEdgeSet.edges, AsymmetricFilletEdgeSetInput.entities, Attribute.otherParents, BaseComponent.findBRepUsingPoint, BaseComponent.findBRepUsingRay, BoundaryFillFeature.tools, BoundaryFillFeatureInput.tools, BRepCell.sourceTools, BRepEdge.tangentiallyConnectedEdges, CAM.allOperations, CAMAdditiveContainer.allOperations, CAMFolder.allOperations, CAMFolder.createFromTemplate, CAMPattern.allOperations, CAMPattern.createFromTemplate, ChamferFeature.edges, ChamferFeatureInput.edges, ChordLengthFilletEdgeSet.edges, ChordLengthFilletEdgeSetInput.entities, CircularPatternFeature.inputEntities, CircularPatternFeature.resultFeatures, CircularPatternFeatureInput.inputEntities, CombineFeature.toolBodies, CombineFeatureInput.toolBodies, Component.findBRepUsingPoint, Component.findBRepUsingRay, ConstantRadiusFilletEdgeSet.edges, ConstantRadiusFilletEdgeSetInput.entities, CopyPasteBody.sourceBody, CutPasteBody.sourceBody, DistanceAndAngleChamferEdgeSet.edges, DXF2DImportOptions.results, EqualDistanceChamferEdgeSet.edges, ExtendFeature.edges, ExtendFeatureInput.edges, FilletEdgeSetInput.entities, FlatPatternComponent.findBRepUsingPoint, FlatPatternComponent.findBRepUsingRay, ImportManager.importToTarget2, InfiniteLine3D.intersectWithCurve, InfiniteLine3D.intersectWithSurface, InterferenceInput.entities, InterferenceResults.createBodies, Line3D.intersectWithCurve, Line3D.intersectWithSurface, MirrorFeature.inputEntities, MirrorFeature.resultFeatures, MirrorFeatureInput.inputEntities, MoveFeature.inputEntities, MoveFeatureInput.inputEntities, ObjectCollection.create, ObjectCollection.createWithArray, OffsetFeature.entities, OffsetFeatureInput.entities, PatchFeature.interiorRailsAndPoints, PatchFeatureInput.interiorRailsAndPoints, PathPatternFeature.inputEntities, PathPatternFeature.resultFeatures, PathPatternFeatureInput.inputEntities, Plane.intersectWithCurve, Plane.intersectWithSurface, RectangularPatternFeature.inputEntities, RectangularPatternFeature.resultFeatures, RectangularPatternFeatureInput.inputEntities, ReplaceFaceFeatureInput.sourceFaces, ReverseNormalFeature.surfaces, ScaleFeature.inputEntities, ScaleFeatureInput.inputEntities, SelectionEventArgs.additionalEntities, Selections.all, Setup.allOperations, Setup.createFromTemplate, Setup.fixtures, Setup.models, Setup.stockSolids, ShellFeature.inputEntities, ShellFeatureInput.inputEntities, Sketch.copy, Sketch.findConnectedCurves, Sketch.include, Sketch.offset, Sketch.project, Sketch.projectCutEdges, SketchArc.breakCurve, SketchArc.extend, SketchArc.intersections, SketchArc.split, SketchArc.trim, SketchCircle.breakCurve, SketchCircle.extend, SketchCircle.intersections, SketchCircle.split, SketchCircle.trim, SketchConicCurve.breakCurve, SketchConicCurve.extend, SketchConicCurve.intersections, SketchConicCurve.split, SketchConicCurve.trim, SketchControlPointSpline.breakCurve, SketchControlPointSpline.extend, SketchControlPointSpline.intersections, SketchControlPointSpline.split, SketchControlPointSpline.trim, SketchCurve.breakCurve, SketchCurve.extend, SketchCurve.intersections, SketchCurve.split, SketchCurve.trim, SketchEllipse.breakCurve, SketchEllipse.extend, SketchEllipse.intersections, SketchEllipse.split, SketchEllipse.trim, SketchEllipticalArc.breakCurve, SketchEllipticalArc.extend, SketchEllipticalArc.intersections, SketchEllipticalArc.split, SketchEllipticalArc.trim, SketchFittedSpline.breakCurve, SketchFittedSpline.extend, SketchFittedSpline.intersections, SketchFittedSpline.split, SketchFittedSpline.trim, SketchFixedSpline.breakCurve, SketchFixedSpline.extend, SketchFixedSpline.intersections, SketchFixedSpline.split, SketchFixedSpline.trim, SketchLine.breakCurve, SketchLine.extend, SketchLine.intersections, SketchLine.split, SketchLine.trim, SketchPointsBossPositionDefinition.sketchPoints, SketchPointsHolePositionDefinition.sketchPoints, SplitBodyFeature.splitBodies, SplitFaceFeature.facesToSplit, SplitFaceFeature.splittingTool, SplitFaceFeatureInput.facesToSplit, StitchFeature.stitchSurfaces, StitchFeatureInput.stitchSurfaces, SurfaceEvaluator.getIsoCurve, SurfaceEvaluator.getModelCurveFromParametricCurve, ThickenFeature.inputFaces, ThickenFeatureInput.inputFaces, ThreadFeature.inputCylindricalFaces, ThreadFeatureInput.inputCylindricalFaces, ToolbarPanel.relatedWorkspaces, TwoDistancesChamferEdgeSet.edges, UnstitchFeature.inputFaces, VariableRadiusFilletEdgeSet.edges, VariableRadiusFilletEdgeSetInput.entities

## Methods

### add(item: Base) -> boolean
Adds an object to the end of the collection. Duplicates can be added to the collection.
- **item** (Base): The item to add to the list.
- **Returns** (boolean): Returns false if the item was not added.

### asArray() -> Base
Returns the content of the ObjectCollection as an array.
- **Returns** (Base): Returns an array of the Fusion objects in the ObjectCollection.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### clear() -> boolean
Clears the entire contents of the collection.
- **Returns** (boolean): Returns true if successful.

### contains(item: Base) -> boolean
Returns whether the specified object exists within the collection.
- **item** (Base): The item to look for in the collection.
- **Returns** (boolean): Returns true if the specified item is found in the collection.

### create() -> ObjectCollection
Creates a new ObjectCollection object.
- **Returns** (ObjectCollection): Returns the newly created ObjectCollection.

### createWithArray(array: Base[]) -> ObjectCollection
Creates a new ObjectCollection that is initialized with the content of the provided array.
- **array** (Base[]): An array of Fusion objects that are used to populate the ObjectCollection. For this method to succeed, getting the input type correct is critical. The term "array" is used generically in the API documentation and describes different things depending on the language being used.

When using C++, std::vector is used to input and output a list of items.However, this particular method requires that the content of the vector be of type core.base. If you have a vector of other types, you need to convert it to core.base. The sample below illustrates converting a vector of Occurrence objects into a vector of core.Base objects.

std::vector<Ptr<adsk::fusion::Occurrence>> occArray = rootComp->occurrences()->asArray();

std::vector<Ptr<adsk::core::Base>> occs{ occArray.begin(), occArray.end() };

Ptr<ObjectCollection> objColl = ObjectCollection::createWithArray(occs);

When using Python, a Python List or Tuple is used as input. Something not obvious is that when an array is returned from a method or property it's not returned as a standard Python List but is a special API-specific class called "vector". Typically, you don't notice this isn't a List because it supports Python iteration like a List does. Because the createWithArray method requires a standard Python list as input, you need to convert it to a standard list before using it in the createWithArray method. For example, the Occurrences.asArray method returns an "array" of the occurrences, which really returns a vector object of the occurrences. The code below converts the vector into a standard list so it can be used to create an ObjectCollection.

occList = list(root.Occurrences.asArray())

objColl = adsk.core.ObjectCollection.craeteWithArray(occList)
- **Returns** (ObjectCollection): Returns the newly created ObjectCollection or null in the case of failure.

### find(item: Base, startIndex: uinteger) -> integer
Finds the specified component in the collection.
- **item** (Base): The item to search for within the collection.
- **startIndex** (uinteger): The index to begin the search.

This is an optional argument whose default value is 0.
- **Returns** (integer): Returns the index of the found item. If not found, -1 is returned.

### item(index: uinteger) -> Base
Function that returns the specified object using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Base): Returns the specified item or null if an invalid index was specified.

### removeByIndex(index: uinteger) -> boolean
Function that removes an item from the list. Will fail if the list is read only.
- **index** (uinteger): The index of the item to remove from the collection. The first item has an index of 0.
- **Returns** (boolean): Returns true if the removal was successful.

### removeByItem(item: Base) -> boolean
Function that removes an item from the collection.
- **item** (Base): The object to remove from the collection.
- **Returns** (boolean): Returns true if the removal was successful.

## Properties

### count : uinteger [read-only]
Returns the number of occurrences in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Set Vise Origin As Setup WCS Origin API Sample**: This sample script demonstrates how to define our setup WCS origin relative to our vise origin from either a component, a sketch point or a joint origin.
The Work Coordinate System is a reference point set in our CAM workspace and on our machine. All machine coordinates are drawn from the WCS. This script demonstrates defining the WCS by each of 4 alternative methods:
Setup by default with no origin defined.
Setup using vise origin as WCS origin.
Setup using a sketch point as WCS origin.
Setup using a joint origin as WCS origin.
- **SketchFittedSplines.add**: Demonstrates the SketchFittedSplines.add method.
