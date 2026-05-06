# FlatPatternProduct
Namespace: adsk.fusion
Inherits: Design
Since: October 2022

Product that contains all of the information associated with a flat pattern.

A FlatPatternProduct object exists for each flat pattern created.

## Methods

### activateRootComponent() -> boolean
Makes the root component the active component in the user interface. This is the same as enabling the radio button next to the root component in the browser.
- **Returns** (boolean): Returns true if the activation was successful.

### analyzeInterference(input: InterferenceInput) -> InterferenceResults
Calculates the interference between the input bodies and/or occurrences.
- **input** (InterferenceInput): An InterferenceInput that defines all of the necessary input needed to calculate the interference. An InterferenceInput object is created using the createInterferenceInput method.
- **Returns** (InterferenceResults): Returns an InterferenceResults object that can be used to examine the interference results.

### areaProperties(inputs: ObjectCollection, accuracy: CalculationAccuracy) -> AreaProperties
Returns the AreaProperties object that has properties for getting the area, perimeter, centroid, etc for a collection of 2D sketch profiles and/or planar surfaces that all lie on the same plane.
- **inputs** (ObjectCollection): A collection of one or more 2D sketch profile and/or planar surface input objects to perform the calculations on. Supported input object types are 2D closed sketch profiles and planar surfaces. Object must all lie on the same plane. Calculation results reflect the sums of the input objects (i.e. total area of multiple sketch profiles)
- **accuracy** (CalculationAccuracy): Specifies the desired level of computational accuracy of the property calculations. The default value of 'LowCalculationAccuracy' returns results within a +/- 1% error margin.

This is an optional argument whose default value is CalculationAccuracy.LowCalculationAccuracy.
- **Returns** (AreaProperties): Returns an AreaProperties object that can be used to examine the area results.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### computeAll() -> boolean
Forces a recompute of the entire design. This is the equivalent of the "Compute All" command.
- **Returns** (boolean): Returns true if the compute completed. This doesn't indicate if all the items in the timeline successfully computed or not. You need to check the health state of each item in the timeline to determine if everything successfully computed or not.

### createConfiguredDesign() -> ConfigurationTopTable
Converts this design into a configured design. The returned ConfigurationTable has a single row and no columns. You can use it to add columns and rows to define the configuration.
- **Returns** (ConfigurationTopTable): Returns the ConfigurationTable that defines the configurations for this design.

### createInterferenceInput(entities: ObjectCollection) -> InterferenceInput
Creates an InterferenceInput object. This object collects the entities and options that are used when calculating interference. To analyze interference you first create an InterferenceInput supplying the entities and set any other settings and then provide this object as input to the analyzeInterference method.
- **entities** (ObjectCollection): An ObjectCollection containing the BRepBody and/or Occurrence entities that will be used in the interference calculation. All entities must be in the context of the root component of the top-level design.
- **Returns** (InterferenceInput): Returns an InterferenceInput object which you can use to set any other interference settings and then use as input to the analyzeInterference method to calculate the interference. Returns null if the creation failed.

### deleteEntities(entities: ObjectCollection) -> boolean
Deletes the specified set of entities that are associated with this product.
- **entities** (ObjectCollection): An ObjectCollection containing the list of entities to delete.
- **Returns** (boolean): Returns True if any of the entities provided in the list were deleted. If entities were specified that can't be deleted or aren't owned by this product, they are ignored.

### deleteMe() -> boolean
Deletes this FlatPatternProduct and the flat pattern it contains.
- **Returns** (boolean): Returns true if the delete was successful.

### findAttributes(groupName: string, attributeName: string) -> Attribute
Find attributes attached to objects in this product that match the group and or attribute name. This does not find attributes attached directly to the Product or Document objects but finds the attributes attached to entities within the product.

The search string for both the groupName and attributeName arguments can be either an absolute name value, or a regular expression. With an absolute name, the search string must match the entire groupName or attributeName, including case. An empty string will match everything. For example if you have an attribute group named "MyStuff" that contains the attribute "Length1", using the search string "MyStuff" as the group name and "Length1" as the attribute name will find the attributes with those names. Searching for "MyStuff" as the group name and "" as the attribute name will find all attributes that have "MyStuff" as the group name.

Regular expressions provide a more flexible way of searching. To use a regular expression, prefix the input string for the groupName or attributeName arguments with "re:". The regular expression much match the entire group or attribute name. For example if you have a group that contains attributes named "Length1", "Length2", "Width1", and "Width2" and want to find any of the length attributes you can use a regular expression using the string "re:Length.*". For more information on attributes see the Attributes topic in the user manual.
- **groupName** (string): The search string for the group name. See above for more details.
- **attributeName** (string): The search string for the attribute name. See above for more details.
- **Returns** (Attribute): An array of Attribute objects that were found. An empty array is returned if no attributes were found.

### findEntityByToken(entityToken: string) -> Base
Returns the entities associated with the provided token. The return is an array of entities. In most cases an array containing a single entity will be returned but there are cases where more than one entity can be returned. An example of this is where a token is obtained from a face and subsequent modeling operations cause the face to be split into two or more pieces. All of the faces that represent the original face will be returned with the first face being the most logical match to the original face.
- **entityToken** (string): The input entity token you want to find the matching entity for.
- **Returns** (Base): Returns an array of entities associated with the provided token, or an empty array in the case where there are no matches.

### modifyParameters(parameters: Parameter[], values: ValueInput[]) -> boolean
Modifies the values of many parameters all at once. Changing them all at once is more efficient than modifying them one at a time.
- **parameters** (Parameter[]): An array of UserParameter and ModelParameter objects that you want to change the value. The parameters must all exist within the Design object you're calling this method from. They can be in any component but must be local components owned by the Design.
- **values** (ValueInput[]): An array of ValueInput objects that defines the new value for each parameter defined by the "parameters" argument. This array must be the same size as the array used for the "parameters" argument, and the items in the arrays are used in the order they exist within the arrays. For example, the parameter at index 0 will use the value at index 0.

If you use the createByString method to create the ValueInput, the expression of the parameter will be edited, and the effect is the same as interactively editing the expression.When you set the expression, you can include units, references to other parameters, and math operators and functions.For example, "(Length / 3) * cos(Angle)" is a valid expression for a distance parameter if the parameters "Length" and "Angle" already exist.

If you use the createByReal method, the value is assigned directly and is always in the internal units for the unit type associated with the parameter.For example, if the parameter is a length, the value will ALWAYS be used as centimeters. If the parameter is an angle, the value will ALWAYS be used as radians.This is because the default design unit types for length are ignored, and internal units are ALWAYS used.
- **Returns** (boolean): Returns true if setting all of the parameters was successful. Setting multiple parameters is either all or none. If it fails to set any parameters, none of them are updated, and the method will return false.

### physicalProperties(inputs: ObjectCollection, accuracy: CalculationAccuracy)
Returns the PhysicalProperties object that has properties for getting the area, density, mass, volume, moments, etc for a collection of 3D solid objects.
- **inputs** (ObjectCollection): A collection of one or more 3D solid input objects to perform the calculations on. Supported input object types are Components, Occurrences and BRepBodies. Calculation results reflect the sums of the input objects (i.e. total volume of multiple bodies)
- **accuracy** (CalculationAccuracy): Specifies the desired level of computational accuracy of the property calculations. The default value of 'LowCalculationAccuracy' returns results within a +/- 1% error margin.

This is an optional argument whose default value is CalculationAccuracy.LowCalculationAccuracy.

### setGroundPlaneOffset(offset: double) -> boolean
Sets the offset of the ground plane. If the isAdpativeGroundPlane property is true, setting the offset will change isAdaptiveGroundPlane to false. The offset value is an offset relative to the current position of the ground plane.

One example of how this method can be used is to set the isAdaptiveGroundPlane property to true, which will position the ground plane at the bottom of the part. By doing this, you know the current position of the ground plane. Then calling this method with a value of -2.0 will reposition the ground plane 2 cm below the part. If you called this method again with a value of -1.0 the ground plane will be moved an additional 1 cm away from the geometry, since this is defining an offset relative to the current position.
- **offset** (double): Defines the relative offset based on the current position of the ground plane. The offset is in centimeters, and a positive value will move it towards the design geometry and a negative value away from the geometry.
- **Returns** (boolean): Returns true if setting the offset was successful.

## Properties

### activeComponent : Component [read-only]
Returns the component that is current being edited. This can return the root component or another component within the design.

### activeEditObject : Base [read-only]
Returns the current edit target as seen in the user interface. This edit target is defined as the container object that will be added to if something is created. For example, a component can be an edit target so that when new bodies are created they are added to that component. A sketch can also be an edit target.

### activeOccurrence : Occurrence [read-only]
Returns the occurrence that is currently activated, if any. This can return null in the case where no occurrence is activated and the root component is active.

### allComponents : Components [read-only]
Returns the Components collection that provides access to existing components in a design.

### allParameters : ParameterList [read-only]
Returns a read only list of all parameters in the design. This includes the user parameters and model parameters from all components in this design. The parameters from Externally Referenced components are NOT included because they are in actuality, separate designs.

### analyses : Analyses [read-only]
Gets the collection of design analyses associated with this design.

### appearances : Appearances [read-only]
Returns the appearances contained in this document.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this product.

### configurationRowId : string [read-only]
Returns the ID of the row that defines this configuration. Use the isConfiguration property to determine if this Design is a configuration or not. If this is not a configuration, this property returns an empty string.

### configurationTopTable : ConfigurationTopTable [read-only]
If this design is a configured design or a configuration, this property returns the associated ConfigurationTopTable object. If this is not a configured design or configuration, this property returns null.

### contactSets : ContactSets [read-only]
Returns the contact sets associated with this design.

### derivedParameters : array [read-only]
Returns a read only list of all parameters that are derived into the design. This includes the user parameters and model parameters from all derives in this design.

### designIntent : DesignIntentTypes [read-write]
Gets and sets the use intent of this design. Changing the design intent from one type to another is not supported in all cases. For example, if an assembly contains any external or internal components it cannot be converted to a part.

### designPlasticRules : PlasticRules [read-only]
Gets the collection of plastic rules in the design.

### designSheetMetalRules : SheetMetalRules [read-only]
Gets the collection of sheet metal rules in the design.

### designType : DesignTypes [read-write]
Gets and sets the current design type (DirectDesignType or ParametricDesignType) Changing an existing design from ParametricDesignType to DirectDesignType will result in the timeline and all design history being removed and further operations will not be captured in the timeline.

### exportManager : ExportManager [read-only]
Returns the ExportManager for this design. You use the ExportManager to export the current design in various formats.

### flatPattern : FlatPattern [read-only]
Gets the flat pattern associated with this FlatPatternProduct.

### fusionUnitsManager : FusionUnitsManager [read-only]
Returns a specialized UnitsManager that can set the default length units and work with parameters.

### isAdaptiveGroundPlane : boolean [read-write]
Gets and sets if the position of the ground plane for this design is adaptive. If true, the ground plane will automatically move to be just below the model. The orientation of the ground plane is always normal to the "up" direction as defined by the view cube.

### isConfiguration : boolean [read-only]
Gets if this design is a configuration. If this returns true, the configurationRowId can be used to get the row used to define this configuration. Also, when this is true, the design is essentially read-only and edits are either blocked from taking place or cannot be saved.

### isConfiguredDesign : boolean [read-only]
Gets if this design is a configured design. A configured design contains a configuration table. Use the configurationTable property to get the associated table.

### isContactAnalysisEnabled : boolean [read-write]
Gets and sets whether contact analysis is enabled for all components. This is the equivalent of the "Disable Contact / Enable Contact" command. If this if True then any contact analysis defined (either all or contact sets) is enabled. if False, then no contact analysis is performed.

### isContactSetAnalysis : boolean [read-write]
Gets and sets whether contact analysis is done using contact sets or between all bodies, independent of any contact sets. If True and the isContactAnalysisEnabled property is True then contact analysis is performed using contact sets. If False and isContactAnalysisEnabled is True, then contact analysis is performed between all bodies. If isContactAnalysisEnabled is False then no contact analysis is performed.

### isModelingInAssemblyEnabled : boolean [read-write]
If this design is an assembly, this property gets and sets if the modeling functionality is enabled. If this design is a part or hybrid design, the value of this property should be ignored.

### isRootComponentActive : boolean [read-only]
Gets whether the root component is the active edit target in the user interface. This is the same as checking the state of the radio button next to the root component in the browser. To activate the root component use the ActivateRootComponent method.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### libraryPlasticRules : PlasticRules [read-only]
Gets the collection of plastic rules in the plastic rule library.

### librarySheetMetalRules : SheetMetalRules [read-only]
Gets the collection of sheet metal rules in the sheet metal rule library.

### materials : Materials [read-only]
Returns the materials contained in this document.

### namedViews : NamedViews [read-only]
Returns the NamedViews object associated with this product. The NamedViews collection provides access to the named views defined in this product and supports the creation of new named views.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### objectVisibility : ObjectVisibility [read-only]
Returns the ObjectVisibility object associated with this design which controls which objects are displayed in the graphics window. This is the equivalent of the "Object Visibility" settings in the Display Settings drop-down in the navigation toolbar at the bottom of the Fusion graphics window.

### parentDocument : Document [read-only]
Returns the parent Document object.

### productType : string [read-only]
Returns the product type name of this product. A list of all of the possible product types can be obtained by using the Application.supportedProductTypes property.

### renderManager : RenderManager [read-only]
Returns the RenderManager object associated with this design. Using the RenderManager you can access the same functionality that is available in the Render workspace.

### rootComponent : Component [read-only]
Returns the root Component.

### rootDataComponent : DataComponent [read-only]
Get the root DataComponent in this design. This is only available for top level designs.

### selectionSets : SelectionSets [read-only]
Returns the SelectionSets object associated with this product. If the product does not support selection sets, null is returned. The SelectionSets object is used to create and access existing selection sets.

### snapshots : Snapshots [read-only]
Returns the Snapshots object associated with this design which provides access to the existing snapshots and the creation of new snapshots.

### timeline : Timeline [read-only]
Returns the timeline associated with this design.

### unitsManager : UnitsManager [read-only]
Returns the UnitsManager object associated with this product.

### userParameters : UserParameters [read-only]
Returns the collection of User Parameters in a design

### workspaces : WorkspaceList [read-only]
Returns the workspaces associated with this product.
