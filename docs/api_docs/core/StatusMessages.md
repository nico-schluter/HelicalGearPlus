# StatusMessages
Namespace: adsk.core
Inherits: Base
Since: July 2021

A collection of status messages associated with a Status object. The primary purpose of the messages is to describe the reason for a warning or failure and display the messages in the alert dialog.

**Accessed from:** Status.statusMessages, StatusMessage.childStatusMessages

## Methods

### addError(messageId: string, message: string) -> StatusMessage
Adds a new error status message to the list of warning and error messages.
- **messageId** (string): The ID of a predefined message or if an empty string is provided, the default error message will be used. The displayed message is localized based on the current default language in Fusion. Below is a list of some valid message ID's and the corresponding English message.

"API_COMPUTE_ERROR" - "Cannot compute this feature."
"API_COMPUTE_WARNING" - "This feature computed with warnings."
"CFLANGE_INVALID_GEOM" - "Invalid input sketch curve."
"DRAFT_MISSING_FACE_REFERENCES" - "Missing face references"
"DRAFT_MISSING_REFERENCE_PLANE" - "Missing reference plane"
"FEATURE_ENTITY_TYPE_INVALID" - "Entity type is invalid"
"FEATURE_FAILED_TO_CREATE" - "Failed to create feature"
"FEATURE_MISSING_INPUTS" - "Missing inputs"
"FEATURE_REFERENCE_LOST" - "Reference is lost"
"Feature_Compute_Error" - "Compute Failed"
"Feature_Input_Compute_Error" - "Reference Failures"
"InvalidWPntInput" - "Invalid input"
"NO_TARGET_BODY" - "No target body!"
"ORIGIN_SELECTION_MISSING" - "Origin geometry is missing."
"DRPOINT_COMPUTE_FAILED" - "Failed to evaluate the point due to the invalid input"


This is an optional argument whose default value is "".
- **message** (string): This is not currently supported for custom feature compute errors and will be ignored.

This is an optional argument whose default value is "".
- **Returns** (StatusMessage): Returns true if the error message was successfully added.

### addWarning(messageId: string, message: string) -> StatusMessage
Adds a new warning status message to the list of warning and error messages.
- **messageId** (string): The ID of a predefined message or if an empty string is provided, the default error message will be used. The displayed message is localized based on the current default language in Fusion. Below is a list of some valid message ID's and the corresponding English message.

"API_COMPUTE_ERROR" - "Cannot compute this feature."
"API_COMPUTE_WARNING" - "This feature computed with warnings."
"CFLANGE_INVALID_GEOM" - "Invalid input sketch curve."
"DRAFT_MISSING_FACE_REFERENCES" - "Missing face references"
"DRAFT_MISSING_REFERENCE_PLANE" - "Missing reference plane"
"FEATURE_ENTITY_TYPE_INVALID" - "Entity type is invalid"
"FEATURE_FAILED_TO_CREATE" - "Failed to create feature"
"FEATURE_MISSING_INPUTS" - "Missing inputs"
"FEATURE_REFERENCE_LOST" - "Reference is lost"
"Feature_Compute_Error" - "Compute Failed"
"Feature_Input_Compute_Error" - "Reference Failures"
"InvalidWPntInput" - "Invalid input"
"NO_TARGET_BODY" - "No target body!"
"ORIGIN_SELECTION_MISSING" - "Origin geometry is missing."
"DRPOINT_COMPUTE_FAILED" - "Failed to evaluate the point due to the invalid input"


This is an optional argument whose default value is "".
- **message** (string): This is not currently supported for custom feature compute errors and will be ignored.

This is an optional argument whose default value is "".
- **Returns** (StatusMessage): Returns true if the warning message was successfully added.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> StatusMessage
Returns the specified status message using an index into the collection.
- **index** (uinteger): The index of the status message within the collection to return. The first item in the collection has an index of 0.
- **Returns** (StatusMessage): Returns the specified StatusMessage or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of status messages in this collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
