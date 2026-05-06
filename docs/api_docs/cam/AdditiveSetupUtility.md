# AdditiveSetupUtility
Namespace: adsk.cam
Inherits: ModifyUtility
Since: September 2023

AdditiveSetupUtility provides functionality for modifications of additive setups.

## Methods

### assignPartsToBodyPreset(parts: Base[], presetName: string) -> Operation
Assigns an array of parts to the body preset operation corresponding to the chosen PrintSettingItem in the PrintSetting. If a part has been previously assigned to a different preset (i.e. the default preset), it will be removed from its previous owner to ensure a body can only be mapped to one preset. If the previous owner preset ends up being empty, it will be removed from the setup.
- **parts** (Base[]): Parts to be assigned to a preset. The array may contain BRepBody, MeshBody or Occurrence objects. If occurrences are passed in, the preset will contain their resolved bodies or meshes. If the array is empty, the preset will be removed from the setup, but the PrintSettingItem will stay in the PrintSetting.
- **presetName** (string): The name of the PrintSettingItem defined in the PrintSetting, which serves as the basis for the to be created operation.
- **Returns** (Operation): The preset corresponding to the preset name. Returns null if the preset has been removed from the setup due to passing an empty or invalid array.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### removeExcessParts() -> integer
Remove components from setups, that are outside of the buildroom.
- **Returns** (integer): Returns count of removed parts on success and -1 on failure.

### splitSupport(targets: Base[], splitType: SplitSupportTypes) -> boolean
Splits support structure of given target bodies into separate mesh body.
- **targets** (Base[]): Targets contain any input bodies whose support is to be inserted into a new mesh body. Input target must belong to the setup and must be part of the associated manufacturing model. Raises an error if any input target is not part of the setup or is not part of the associated manufacturing model.
- **splitType** (SplitSupportTypes): The splitType defines the behavior for support that contains solid and open mesh geometry.
- **Returns** (boolean): True on success, false on errors

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
