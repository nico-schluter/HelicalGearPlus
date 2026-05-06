# CustomFeatureDefinition
Namespace: adsk.fusion
Inherits: Base
Since: January 2021

The CustomFeatureDefinition object defines a specific type of custom feature. It contains the settings that apply to all custom features of that type and is used when creating new custom features of that type. It also supports the events used to handle changes to custom features of that type.

**Accessed from:** CustomFeature.definition, CustomFeatureDefinition.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(id: string, defaultName: string, iconFolder: string) -> CustomFeatureDefinition
A static function that creates a new CustomFeatureDefinition object. The creation of a CustomFeatureDefinition object is required to be able to create new custom features and for existing custom features to behave correctly. The CustomFeatureDefinition object defines all of the information that is common for all custom features of a particular type. For example, it defines the icon and the default name. The CustomFeatureDefinition object also supports the events that used to react to an existing feature being edited or re-computed.

The custom feature definition should be created when your add-in is initially loaded to notify Fusion that the add-in that supports that custom feature type is available.
- **id** (string): The unique ID for custom features of a particular type. Care must be taken to ensure that this is unique and you must be consistent in its use once you've chosen an ID. A good practice to help ensure unique naming is to use the name of your company in combination with the name of the feature, such as "CompanyName.FeatureName". For example, "WoodTools4U.Dovetail".
- **defaultName** (string): The default name of the feature. Fusion will use this name and append a number to each feature instance as it's created. For example, if this is "Dovetail" the first custom feature created will be named "Dovetail1" and the second will be "Dovetail2".

If you want to localize this name you can use the Application.Preferences.generalPreferences.userLanguage property to determine what language the user has chosen and use the corresponding name for that language.
- **iconFolder** (string): The folder that contains the image files that will be used for the icon for this feature in the timeline. This can be a full path or a relative path where it will be relative to the add-in file. The folder should contain the image files named 16x16.png and 32x32.png which should be images that are 16 and 32 pixels square.
- **Returns** (CustomFeatureDefinition): Returns the newly created CustomFeatureDefinition or null in the case of failure.

## Properties

### defaultName : string [read-write]
Gets and sets the default name of the feature. Fusion will use this name and append a number to each feature instance as it's created. For example, if this is "Dovetail" the first custom feature created will be named "Dovetail1" and the second will be "Dovetail2".

If you want to localize this name you can use the Application.Preferences.generalPreferences.userLanguage property to determine what language the user has chosen and use the corresponding name for that language.

### editCommandId : string [read-write]
Gets and sets which command will be invoked when the feature is edited. This is the id of the CommandDefinition object that you have created to do the edit of the feature.

### iconFolder : string [read-write]
Gets and sets the folder that contains the images that are used for the icon in the timeline for this custom feature. The folder should contain the image files named 16x16.png and 32x32.png which should be images that are 16 and 32 pixels square.

### id : string [read-only]
Gets the unique ID used for this type of custom feature.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Events

### customFeatureCompute
The customFeatureCompute event fires when Fusion is computing the timeline and reaches the custom feature. The event is fired if any of the dependencies of the custom feature have changed. You can modify the results of your custom feature based on the dependencies.
