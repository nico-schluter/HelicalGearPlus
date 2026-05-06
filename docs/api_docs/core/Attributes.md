# Attributes
Namespace: adsk.core
Inherits: Base
Since: May 2016

Provides access to attributes associated with a specific entity, Product, or Document. Also supports the creation of new attributes.

**Accessed from:** AccessibilityAnalysis.attributes, Analysis.attributes, ArrangeFeature.attributes, AsBuiltJoint.attributes, AssemblyConstraint.attributes, BaseFeature.attributes, BossFeature.attributes, BoundaryFillFeature.attributes, BoxFeature.attributes, BRepBody.attributes, BRepEdge.attributes, BRepFace.attributes, BRepVertex.attributes, CAM.attributes, CAMAdditiveContainer.attributes, CAMFolder.attributes, CAMHoleRecognition.attributes, CAMPattern.attributes, CAMTemplate.attributes, ChamferFeature.attributes, CircularPatternConstraint.attributes, CircularPatternFeature.attributes, CoilFeature.attributes, CoincidentConstraint.attributes, CoincidentToSurfaceConstraint.attributes, CollinearConstraint.attributes, CombineFeature.attributes, Component.attributes, ConcentricConstraint.attributes, ConstructionAxis.attributes, ConstructionPlane.attributes, ConstructionPoint.attributes, CopyPasteBody.attributes, CornerClosureFeature.attributes, CurvatureCombAnalysis.attributes, CurvatureMapAnalysis.attributes, CustomFeature.attributes, CustomFeatureParameter.attributes, CutPasteBody.attributes, CylinderFeature.attributes, DeleteFaceFeature.attributes, DerivedParameter.attributes, DeriveFeature.attributes, Design.attributes, Document.attributes, DraftAnalysis.attributes, DraftFeature.attributes, Drawing.attributes, DrawingDocument.attributes, EmbossFeature.attributes, EqualConstraint.attributes, ExtendFeature.attributes, ExtrudeFeature.attributes, FaceGroup.attributes, Feature.attributes, FilletFeature.attributes, FlangeFeature.attributes, FlatPattern.attributes, FlatPatternComponent.attributes, FlatPatternProduct.attributes, FormFeature.attributes, FusionDocument.attributes, GeometricConstraint.attributes, HemFeature.attributes, HoleFeature.attributes, HorizontalConstraint.attributes, HorizontalPointsConstraint.attributes, IsoCurveAnalysis.attributes, Joint.attributes, JointOrigin.attributes, LineOnPlanarSurfaceConstraint.attributes, LineParallelToPlanarSurfaceConstraint.attributes, LoftFeature.attributes, MeshBody.attributes, MeshCombineFaceGroupsFeature.attributes, MeshCombineFeature.attributes, MeshConvertFeature.attributes, MeshFeature.attributes, MeshGenerateFaceGroupsFeature.attributes, MeshReduceFeature.attributes, MeshRemeshFeature.attributes, MeshRemoveFeature.attributes, MeshRepairFeature.attributes, MeshReverseNormalFeature.attributes, MeshSeparateFeature.attributes, MeshShellFeature.attributes, MeshSmoothFeature.attributes, MidPointConstraint.attributes, MinimumRadiusAnalysis.attributes, MirrorFeature.attributes, ModelParameter.attributes, MotionLink.attributes, MoveFeature.attributes, NCProgram.attributes, Occurrence.attributes, OffsetConstraint.attributes, OffsetFacesFeature.attributes, OffsetFeature.attributes, Operation.attributes, OperationBase.attributes, ParallelConstraint.attributes, Parameter.attributes, PatchFeature.attributes, PathPatternFeature.attributes, PerpendicularConstraint.attributes, PerpendicularToSurfaceConstraint.attributes, PipeFeature.attributes, PolygonConstraint.attributes, Product.attributes, RectangularPatternConstraint.attributes, RectangularPatternFeature.attributes, RefoldFeature.attributes, RemoveFeature.attributes, ReplaceFaceFeature.attributes, ReverseNormalFeature.attributes, RevolveFeature.attributes, RibFeature.attributes, RigidGroup.attributes, RipFeature.attributes, RuledSurfaceFeature.attributes, RuleFilletFeature.attributes, ScaleFeature.attributes, SectionAnalysis.attributes, Setup.attributes, ShellFeature.attributes, SilhouetteSplitFeature.attributes, Sketch.attributes, SketchAngularDimension.attributes, SketchArc.attributes, SketchCircle.attributes, SketchConcentricCircleDimension.attributes, SketchConicCurve.attributes, SketchControlPointSpline.attributes, SketchCurve.attributes, SketchDiameterDimension.attributes, SketchDimension.attributes, SketchDistanceBetweenLineAndPlanarSurfaceDimension.attributes, SketchDistanceBetweenPointAndSurfaceDimension.attributes, SketchEllipse.attributes, SketchEllipseMajorRadiusDimension.attributes, SketchEllipseMinorRadiusDimension.attributes, SketchEllipticalArc.attributes, SketchEntity.attributes, SketchFittedSpline.attributes, SketchFixedSpline.attributes, SketchLine.attributes, SketchLinearDiameterDimension.attributes, SketchLinearDimension.attributes, SketchOffsetCurvesDimension.attributes, SketchOffsetDimension.attributes, SketchPoint.attributes, SketchRadialDimension.attributes, SketchTangentDistanceDimension.attributes, SketchText.attributes, SmoothConstraint.attributes, SphereFeature.attributes, SplitBodyFeature.attributes, SplitFaceFeature.attributes, StitchFeature.attributes, SurfaceDeleteFaceFeature.attributes, SweepFeature.attributes, SymmetryConstraint.attributes, TangentConstraint.attributes, TangentRelationship.attributes, TessellateFeature.attributes, ThickenFeature.attributes, ThreadFeature.attributes, TorusFeature.attributes, TrimFeature.attributes, UnfoldFeature.attributes, UnstitchFeature.attributes, UntrimFeature.attributes, UserParameter.attributes, VerticalConstraint.attributes, VerticalPointsConstraint.attributes, VolumetricCustomFeature.attributes, VolumetricModelToMeshFeature.attributes, WebFeature.attributes, WorkingModel.attributes, ZebraAnalysis.attributes

## Methods

### add(groupName: string, name: string, value: string) -> Attribute
Adds a new attribute to the parent entity. If an attribute already exists on the entity with the same groupName and name already exists, this will update the existing attribute with the new value.
- **groupName** (string): The name of the attribute group to create this attribute within.
- **name** (string): The name of the attribute. This must be unique with respect to other attributes in the group.
- **value** (string): The value of the attribute. The size of an attribute value is limited to 2MB (2097152 bytes). If you need to save data that is larger than 2MB you'll need to break it into pieces and save it in multiple attributes.
- **Returns** (Attribute): Returns the newly created attribute or null if the creation failed. If an attribute with the same groupName and name already exists, it will return the existing attribute.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Attribute
Returns the specified attribute using an index into the collection.
- **index** (uinteger): The index of the attribute within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Attribute): Returns the specified attribute or null if an invalid index was specified.

### itemByName(groupName: string, name: string) -> Attribute
Returns the specified attribute using the name of the attribute.
- **groupName** (string): The name of the attribute group this attribute will belong to.
- **name** (string): The name of the attribute.
- **Returns** (Attribute): Returns the specified attribute or null if no attribute exists with the specified name.

### itemsByGroup(groupName: string) -> Attribute
Returns an array of all of the attributes that belong to the specified group.
- **groupName** (string): The name of the group.
- **Returns** (Attribute): Returns an array of attributes or will fail in the case where an invalid group name is specified.

## Properties

### count : uinteger [read-only]
Returns the number of attributes in the collection.

### groupNames : array [read-only]
Returns an array of strings that are all of the name of attribute groups that exist on this entity. An empty array can be returns if there are no attributes on the entity.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
