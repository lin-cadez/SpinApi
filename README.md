# Github documentation for Spin library

## Introduction

Spin is a Python library that provides an easy way to access the latest information about accidents happening in Slovenia. The library uses the Spin3 RSS feed to fetch the data and parse it into an easily readable format.

## Installation

Download spinalert.py from Github and move it to directory of your script.

## Usage

To use Spin, you first need to import the library:

```
from spinalert import *
```

### Creating a Spin instance

To start using Spin, you need to create a Spin object. The Spin constructor takes one optional arguments:

- `url`: The URL of the Spin3 API endpoint. This defaults to `https://spin3.sos112.si/api/javno/ODRSS/true`.

You can adjust it here: https://spin3.sos112.si/javno/od

```
spin_instance = Spin(url="https://spin3.sos112.si/api/javno/ODRSS/true")
```

### Fetching the latest event

To fetch the latest event, you can use the `last` property of the Spin object:
```
latest_event = spin_instance.last
```

The `last` property returns a `SpinDict` object, which is a subclass of the Python `dict` class. It contains the following properties:

- `title`: The title of the event.
- `summary`: A summary of the event.
- `location`: The location of the event.
- `published`: The date and time the event was published.

### Fetching all events

To fetch all events, you can use the `events` method of the Spin object:

```
all_events = spin_instance.events()
```

The `events` method returns a list of `SpinDict` objects, each containing the properties described above.

## Example usage

Here is an example of how to use the Spin library to fetch and print the latest event:

```
from spinalert import *

spin_instance = Spin()

print("Title:", spin_instance.last.title)
print("Summary:", spin_instance.last.summary)
print("Location:", spin_instance.last.location)
print("Published:", spin_instance.last.published)
```



