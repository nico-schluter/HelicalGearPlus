# IAddIn
Namespace: adsk.core
Since: March 2022

The interface implemented by an add-in.

## Methods

### onActivate()
Lets the application do any initialization when it is safe to do so.

### onDeactivate(isAppClosing: boolean)
Lets the application do any termination when it is safe to do so. In general, if the add-in is closing, termination should be minimized.
