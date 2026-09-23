# Storage Design / ER Diagram

The project does not use a relational database. It uses a JSON file because the application is small and educational.

## JSON Record

```text
history.json
|
+-- name
+-- beats
+-- time_seconds
+-- heart_rate_bpm
`-- category
```

## Example

```json
{
    "name": "xyz",
    "beats": 60,
    "time_seconds": 60,
    "heart_rate_bpm": 60,
    "category": "60-100 BPM"
}
```

A traditional ER diagram is not applicable because there are no relational database tables.
