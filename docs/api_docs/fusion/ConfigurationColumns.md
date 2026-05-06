# ConfigurationColumns
Namespace: adsk.fusion
Inherits: Base
Since: January 2024

Returns a collection of the columns in the table. The Name column is not included in this list.

**Accessed from:** ConfigurationCustomThemeTable.columns, ConfigurationTopTable.columns

## Methods

### addClearanceTypeColumns(holeFeature: HoleFeature, holeClearanceColumns: ConfigurationClearanceHoleColumns) -> ConfigurationFeatureAspectColumn
Creates the columns in the configuration table to control the clearance information associated with a clearance hole. Because configuring a clearance hole requires several pieces of related information, this method collects it all at once and creates all the corresponding feature aspect columns.

The fit is also a setting that controls the hole clearance, but it's independent of the other settings and can be created independently using the addFeatureAspectColumn method.
- **holeFeature** (HoleFeature): The hole feature that defines a clearance hole whose clearance will be controlled by the configuration table.
- **holeClearanceColumns** (ConfigurationClearanceHoleColumns): Enum value that indicates which columns should be created to control the clearance hole definition. You can fully define the clearance hole by specifying the standard, fastener type, and size. Or you can leave the standard controlled by the hole and only configure the fastener type, and size. Or you can leave the standard and fastener type controlled by the hole and only configure the size. As a result, this can create and return 3, 2, or 1 columns.

The fit is also a setting that controls the hole clearance, but it's independent of the other settings and can be created independently using the addFeatureAspectColumn method.
- **Returns** (ConfigurationFeatureAspectColumn): Returns an array of the columns created. They are in order of standard, fastener type, and size.

### addFeatureAspectColumn(feature: Base, aspectType: ConfigurationFeatureAspectTypes) -> ConfigurationFeatureAspectColumn
Creates a new column to control an aspect of a feature that supports being configured.
- **feature** (Base): The feature to be configured. The term "feature" is used broadly and includes ThreadFeature, HoleFeature that is tapped, Joint, and AsBuiltJoint objects. The existing column is returned if a feature aspect column already exists for the feature and aspect type.
- **aspectType** (ConfigurationFeatureAspectTypes): The aspect type to create a column for. The type specified must be a valid type for the specified feature; otherwise, this will fail with an error.
- **Returns** (ConfigurationFeatureAspectColumn): Retruns the created ConfigurationFeatureAspectColumn or null in the case of failure.

### addInsertColumn(occurrence: Occurrence) -> ConfigurationInsertColumn
Add a new column to control which configuration is used for an inserted configuration. If an insert column already exists for the occurrence, the existing column is returned.

This is only valid for ConfigurationTopTable and ConfigurationCustomThemeTable objects and will fail for all other table types.
- **occurrence** (Occurrence): The occurrence that references a configuration.
- **Returns** (ConfigurationInsertColumn): Returns the new column or null in the case of failure.

### addInsertStandardDesignColumn(occurrence: Occurrence) -> ConfigurationInsertStandardDesignColumn
Add a new column to control which standard design is used for an inserted design. If an insert column already exists for the occurrence, the existing column is returned.

This is only valid for ConfigurationTopTable and ConfigurationCustomThemeTable objects and will fail for all other table types.
- **occurrence** (Occurrence): The occurrence that references a standard design.
- **Returns** (ConfigurationInsertStandardDesignColumn): Returns the new column or null in the case of failure.

### addParameterColumn(parameter: Parameter) -> ConfigurationParameterColumn
Adds a new parameter column to the configuration table. If a parameter column already exists for the parameter, the existing column is returned.

This is only valid for TopConfigurationTable and ThemeConfigurationTable objects. It will fail for all other table types.
- **parameter** (Parameter): The parameter to add to the table.
- **Returns** (ConfigurationParameterColumn): Returns the new column or null in the case of failure.

### addPropertyColumn(property: Property) -> ConfigurationPropertyColumn
Add a new column to control the property inside the component. The component is the owner of the property. This is only valid for TopConfigurationTable. It will fail for all other table types.
- **property** (Property): The property to add to the table.
- **Returns** (ConfigurationPropertyColumn): Returns the new column or null in the case of failure.

### addSuppressColumn(feature: Base) -> ConfigurationSuppressColumn
Adds a new column to control the suppression of a feature. The term "feature" is used broadly and includes anything displayed in the timeline. If a suppression column already exists for the feature, the existing column is returned.

This is only valid for TopConfigurationTable and ThemeConfigurationTable objects. It will fail for all other table types.
- **feature** (Base): The feature to add to the table. Any object that is displayed in the timeline can be used as input. For example, some valid objects are any modeling features, sketches, construction geometry, and joints.
- **Returns** (ConfigurationSuppressColumn): Returns the new column or null in the case of failure.

### addThreadTypeColumns(threadFeature: Feature, threadColumns: ConfigurationThreadColumns) -> ConfigurationFeatureAspectColumn
Creates the columns in the configuration table to control the type of thread associated with a thread feature or a tapped hole. Because configuring a thread requires several pieces of information, this method collects it all at once and creates all the corresponding feature aspect columns.
- **threadFeature** (Feature): The thread or tapped hole feature whose thread will be controlled by the configuration table.
- **threadColumns** (ConfigurationThreadColumns): Enum value that indicates which columns should be created to control the thread type. You can fully define the thread type by specifying the type, size, designation, and class. Or you can leave the thread type controlled by the feature and only configure the size, designation, and class. Or you can leave the thread type and size controlled by the feature and only configure the designation and class. Or you can leave the thread type, size, and designation controlled by the feature and only configure the class. As a result, this can create and return 4, 3, 2, or 1 columns.
- **Returns** (ConfigurationFeatureAspectColumn): Returns an array of the columns created. They are in order of type, size, designation, and class.

### addVisibilityColumn(entity: Base) -> ConfigurationVisibilityColumn
Adds a new column to control the visibility of an entity. If a visibility column already exists for the entity, the existing column is returned.

This is only valid for ConfigurationTopTable and ConfigurationCustomThemeTable objects and will fail for all other table types.
- **entity** (Base): Returns the entity whose visibility will be controlled by this column.
- **Returns** (ConfigurationVisibilityColumn): Returns the new column or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ConfigurationColumn
A method that returns the specified column object using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ConfigurationColumn): Returns the specified item or null if an invalid index was specified.

### itemById(id: string) -> ConfigurationColumn
A method that returns the specified column object using the ID of the column.
- **id** (string): The ID of the column within the collection to return.
- **Returns** (ConfigurationColumn): Returns the specified item or null if no column matches the provided ID.

## Properties

### count : uinteger [read-only]
Returns the number of columns in the table. The name column is not included.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
