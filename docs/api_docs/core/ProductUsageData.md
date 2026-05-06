# ProductUsageData
Namespace: adsk.core
Inherits: Base
Since: August 2014

Provides access to the product usage data settings.

**Accessed from:** Preferences.productUsageData

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isGoogleAnalyticsTrackingEnabled : boolean [read-write]
Gets and sets if Google Analytics tracking is enabled.

### isLearningPanelContextEnabled : boolean [read-write]
Gets and sets if data can be collected to enable the Learning Panel to show information based on the current context.

### isTrackingToImproveCommunicationEnabled : boolean [read-write]
Gets and sets if data can be collected to improve communications. This is the preferences setting titled "Customize our messaging".

### isTrackingToImproveSoftwareEnabled : boolean [read-write]
Gets and sets if data can be collected to help improve the products and services that Autodesk provides. This is the preference setting titled "Help develop our products and services".

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
