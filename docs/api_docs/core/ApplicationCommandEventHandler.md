# ApplicationCommandEventHandler
Namespace: adsk.core
Inherits: EventHandler
Since: November 2015

An application command event handler base class that a client derives from to handle events triggered by an ApplicationCommandEvent. A client implemented instance of this class can be added to an ApplicationCommandEvent to receive these event notifications.

## Methods

### notify(eventArgs: ApplicationCommandEventArgs)
This notify member is called when an event is triggered from any event that this handler has been added to.
- **eventArgs** (ApplicationCommandEventArgs): The arguments object with details about this event and the firing ApplicationCommandEvent.
