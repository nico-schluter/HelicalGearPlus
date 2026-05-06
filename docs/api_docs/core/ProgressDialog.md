# ProgressDialog
Namespace: adsk.core
Inherits: Base
Since: January 2016

Provides access to the progress dialog.

**Accessed from:** UserInterface.createProgressDialog

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### hide() -> boolean
Hides the progress dialog. This should be used when the process has completed.
- **Returns** (boolean): Returns true if successful.

### reset() -> boolean
Method that resets the progress bar. The progress bar "rewinds" and shows no progress. This is the same as setting the progress value to the minimum value.
- **Returns** (boolean): Returns true if successful

### show(title: string, message: string, minimumValue: integer, maximumValue: integer, delay: integer) -> boolean
Displays the progress dialog that includes a progress bar that can be used to display a continually updated message indicating the progress of a process that will take more than a few seconds. The progress is determined by comparing the current progress value with the minimum and maximum values.
- **title** (string): Sets the title for the progress dialog
- **message** (string): The message to display along with the progress bar. The following symbols can be used to display values. "%p" is replaced by the percentage completed. "%v" is replaced by the current value. %m is replaced by the total number of steps. For example, the message "Processing section %v of %m." will result in the message "Processing section 1 of 10." to be displayed if the maximum value is 10 and the current value is 1.
- **minimumValue** (integer): The minimum value of the progress bar. This is used along with the maximum value and the progress value to compute the current percentage complete. This is also the initial progress value when the progress bar is first displayed.
- **maximumValue** (integer): The maximum value of the progress bar. This is used along with the minimum value and the progress value to compute the current percentage complete.
- **delay** (integer): Specifies the time interval in seconds to delay displaying the Progress Dialog. This provides a way to hide the progress dialog before it actually gets displayed, which is useful for cases where the progress of the operation being tracked completes quickly and there is no need to indicate progress to the user.

This is an optional argument whose default value is 0.
- **Returns** (boolean): Returns true if successful.

## Properties

### cancelButtonText : string [read-write]
Sets the text label on the Cancel button. The default text label is "Cancel".

### isBackgroundTranslucent : boolean [read-write]
Gets and sets if the dialog background is translucent. This is false by default

### isCancelButtonShown : boolean [read-write]
Gets and sets if the cancel button is included in the dialog. This is false by default.

### isShowing : boolean [read-only]
Gets if the Progress Dialog is currently being displayed

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maximumValue : integer [read-write]
The maximum value of the progress bar. This is used along with the minimum value and the progress value to compute the current percentage complete.

### message : string [read-write]
Gets and sets the message to display along with the progress bar. The following symbols can be used to display values. "%p" is replaced by the percentage completed. "%v" is replaced by the current value. %m is replaced by the total number of steps. For example, the message "Processing section %v of %m." will result in the message "Processing section 1 of 10." to be displayed if the maximum value is 10 and the current value is 1. Specify an empty string ("") for no message to appear along with the progress panel.

### minimumValue : integer [read-write]
The minimum value of the progress bar. This is used along with the maximum value and the progress value to compute the current percentage complete. This is also the initial progress value when the progress bar is first displayed.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### progressValue : integer [read-write]
Gets and sets the current progress bar value. Progress is determined based on this value relative to the minimum and maximum values. This will update the values displayed in the message string.

### title : string [read-write]
Gets and sets the title of the progress dialog

### wasCancelled : boolean [read-only]
Indicates if the cancel button was selected the last time the Progress Dialog was shown.

## Samples
- **Generate Toolpaths API Sample**: Demonstrates generating the toolpaths in the active document.
- **Progress Dialog API Sample**: Demonstrates how to use progress dialog
