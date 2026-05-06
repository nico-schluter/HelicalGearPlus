# GeneralPreferences
Namespace: adsk.core
Inherits: Base
Since: August 2014

Provides access to the general preferences.

**Accessed from:** Preferences.generalPreferences

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### activeUserInterfaceTheme : UserInterfaceThemes [read-only]
Gets the active user interface theme. This property is only different from userInterfaceTheme in the case the theme is DeviceUserInterfaceTheme. In that case the theme used will be returned.

### areAutodesk360NotificationsShown : boolean [read-write]
Gets and sets if Autodesk 360 notifications are shown.

### areInCommandErrorsAndWarningsShown : boolean [read-write]
Gets and sets if in command errors and warnings are shown.

### areTipsAndTricksShown : boolean [read-write]
Gets and sets if in command tips and tricks are shown.

### areTooltipsShown : boolean [read-write]
Gets and sets if tooltips are shown.

### automateVersioningTimeInterval : integer [read-write]
Gets and sets the interval, in minutes, for automatic versioning.

### defaultModelingOrientation : DefaultModelingOrientations [read-write]
Gets and sets the default for which direction is considered "up".

### defaultOrbit : DefaultOrbits [read-write]
Get and sets the type of orbit.

### graphicsDriver : GraphicsDrivers [read-write]
Gets and sets the graphics driver used to display the graphics.

### isAutomaticSaveOnCloseEnabled : boolean [read-write]
Gets and sets if the file is automatically saved on close.

### isAutomaticVersioningEnabled : boolean [read-write]
Gets and sets if a version of the file is automatically saved using a background thread.

### isCameraPivotEnabled : boolean [read-write]
Gets and sets if zoom and orbit commands use camera pivot point for transition.

### isCommandPromptShown : boolean [read-write]
Gets and sets if the command prompt is shown.

### isDefaultMeasureShown : boolean [read-write]
Gets and sets if the default measure is shown.

### isGestureBasedViewNavigationUsed : boolean [read-write]
Gets and sets if gesture based view navigation is used.

### isHangDetectionEnabled : boolean [read-write]
Gets and sets whether hang detection is enabled. This is a Windows only setting. If True, Fusion will detect when a task processes for longer than a specific time. A dialog is displayed if a hang is detected, allowing the user to continue processing or stop Fusion and send an error report.

### isSkipCreationWhenLiveUpdate : boolean [read-write]
Gets and sets if the creation of launch items should be skipped for live update.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isZoomDirectionReversed : boolean [read-write]
Gets and sets if the direction of the zoom is reversed.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### offlineCachePeriod : double [read-write]
Gets and sets the length of time, in days, that the offline cache of a document will remain.

### panZoomOrbitShortcuts : PanZoomOrbitShortcuts [read-write]
Gets and sets how pan, zoom, and orbit should behave.

### userInterfaceTheme : UserInterfaceThemes [read-write]
Gets and sets which color theme is used by the user interface.

### userLanguage : UserLanguages [read-write]
Gets and sets the current language. Setting the language does not take effect until the next time Fusion is started.
