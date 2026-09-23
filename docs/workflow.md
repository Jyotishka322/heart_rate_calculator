# Workflow Diagram

```text
START
  |
  v
Display project title
  |
  v
Enter name
  |
  v
Is name valid?
  |---- NO ----> Show error ----> Enter name again
  |
 YES
  |
  v
Enter number of beats
  |
  v
Enter time in seconds
  |
  v
Are inputs valid?
  |---- NO ----> Show error ----> Enter values again
  |
 YES
  |
  v
Calculate BPM
(beats / time) * 60
  |
  v
Classify BPM
  |
  v
Display result
  |
  v
Save result to JSON
  |
  v
END
```
