# ValidateInputsEventHandler
Namespace: adsk.core
Inherits: EventHandler
Since: August 2014

An event handler base class that a client derives from to handle events triggered by a ValidateInputsEvent. A client implemented instance of this class can be added to a ValidateInputsEvent to receive these event notifications.

## Methods

### notify(eventArgs: ValidateInputsEventArgs)
This notify member is called when an event is triggered from any event that this handler has been added to.
- **eventArgs** (ValidateInputsEventArgs): The arguments object with details about this event and the firing ValidateInputsEvent.
