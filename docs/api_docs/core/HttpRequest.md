# HttpRequest
Namespace: adsk.core
Inherits: Base
Since: January 2024

Supports the ability to make HTTP requests.

**Accessed from:** HttpRequest.create, HttpResponse.request

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(url: string, method: HttpMethods) -> HttpRequest
Creates a new HttpRequest object.
- **url** (string): The URL to make the request to.
- **method** (HttpMethods): The method to use for the request. The default is GetMethod.

This is an optional argument whose default value is HttpMethods.GetMethod.
- **Returns** (HttpRequest): Returns the new HttpRequest object.

### execute() -> boolean
Execute this request asynchronously. The response will be sent to the completed event.
- **Returns** (boolean): Returns true if the request was successfully started.

### executeSync() -> HttpResponse
Execute this request synchronously. This will block the thread until the request completes.
- **Returns** (HttpResponse): Returns the response from making this request, or null if an error prevents the request from starting.

### getHeader(name: string) -> string
Gets the value of the specified header and returns the value.
- **name** (string): The case insensitive name of the header.
- **Returns** (string): Returns the value of the header, or empty if the header was not found. You can use the hasHeader method to determine if the header exists before getting it. This is especially useful in the case where the header exists but has an empty string value.

### hasHeader(name: string) -> boolean
Gets if the request has a header with the given name. This is useful to distinguish between the case where a header is not set and the case where a header is set to an empty string.
- **name** (string): The case insensitive name of the header.
- **Returns** (boolean): Returns true if a header with this name was set in the response.

### headers(names: string[], values: string[]) -> boolean
Get the request headers.
- **names** (string[]): An array of all the header key names.
- **values** (string[]): An array of all the header values.
- **Returns** (boolean): Returns true on success or false on error.

### removeHeader(name: string) -> boolean
Removes a header from the request.
- **name** (string): The case insensitive name of the header.
- **Returns** (boolean): Returns true if the header was found and removed.

### setHeader(name: string, value: string) -> boolean
Sets a header for the request.
- **name** (string): The name of the header value.
- **value** (string): The header's value.
- **Returns** (boolean): Returns true if setting the header succeeds.

## Properties

### data : string [read-write]
Gets and sets the body data to send with this request.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### method : HttpMethods [read-write]
Gets and sets the method to use for the request.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### url : string [read-write]
Gets and sets the URL to make the request to.

## Events

### completed
The completed event fires when the request has completed. This event will fire on successful or failure.

## Samples
- **Gets all properties using GraphQL**: Fetches bulk component properties of the root component and from occurrences via single GraphQL query.
- **Get part number using GraphQL**: Fetches part number of root component and from occurrences via GQL query.
- **Set part number using GraphQL**: Sets part number of root component and from occurrences via GQL query.
