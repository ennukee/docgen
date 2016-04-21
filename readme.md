# DOCGEN (Documentation Generator)

Work in progress mini-project that will generate a large HTML/Markdown file containing documentation of all methods / classes in a project directory (for any supported language)

### TO-DO

( red denotes to be down, green denotes it has been completed )

```diff
- Output data to HTML/Markdown
- Provide option between the two before exporting
+ Support multiple languages
- Sort by file, then by class, then by methods (hierarchy)
- Expand to in-class comments (just under header) since many programmers place 'subtitles' there
```

### Requirements

 * Python 3
 * (that's it, for now!)

### To use

 1. Download it to wherever you like (it's easiest if you put it outside your project directory though).
 2. Call it using `docgen.py <language>`
 3. Input the absolute path or relative path (i.e. `../../stuff` vs `C:\stuff` (or `/var/stuff` for Unix))
 4. Let it be free!
