# WebRequestEventArgs
Namespace: adsk.core
Inherits: EventArgs
Since: May 2016

The WebRequestEventArgs provides information associated with a web request event. These are events fired as a result of a Fusion protocol handler being invoked from a web page. Note that some properties are not available on every event.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### file : string [read-only]
Returns the value specified as the "file" parameter in the URL.

### firingEvent : Event [read-only]
The event that the firing is in response to.

### id : string [read-only]
Returns the value specified as the "id" parameter in the URL. This will be decoded. It can be an empty string if the "id" parameter was not specified in the URL.

### isCanceled : boolean [read-write]
Used during the insertingFromURL and openingFromURL events to get or set if the insert or open should be allowed to continue. This defaults to false, which will allow the operation to continue as normal. This property should be ignored for all events besides the insertingFromURL and openingFromURL events.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### occurrenceOrDocument : Base [read-only]
Used during the insertedFromURL or openedFromURL events and returns the Document (openedFromURL) or Occurrence (insertedFromURL) that was just created.

### privateInfo : string [read-only]
Returns the value specified as the "privateInfo" parameter in the URL. This will be decoded and can be an empty string if the "privateInfo" parameter was not specified in the URL.

### properties : string [read-only]
Returns the value specified as the "properties" parameter in the URL. This will be decoded and should be in JSON format if it was properly provided by the web page. It can be an empty string if the "properties" parameter was not specified in the URL.
