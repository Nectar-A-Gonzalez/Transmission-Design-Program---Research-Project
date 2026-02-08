# Néctar
- Q: Is it better to have classes defined in seperate files or all in one file?
    - This could depend if it makes files easier to edit seperatly or harder
    - Also could depend on how PEP 8 defines it, if it does at all
(Relating to having Shaft.py or just putting basically everything in Transmission.py. Only things that would make sense not to include would be
Inputs class and CatalogData class, since those will then be adapted with AI and other integrations, which I think is easier to implement if they stay seperate)

A: From what I've found, it might be better to keep it in one file.
Source: 
"Edit: To give a firm answer, I would: Use a single file in the beginning, expand to multiple files if complexity demands. When expanding to multiple files, consider using files prepended by _ (to indicate that they are internal and should not be used by the external user). If complexity is big from the start, start with multiple files."

