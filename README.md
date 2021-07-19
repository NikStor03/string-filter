# string-filter
This code will help you to filter all censors in your strings

# Install

`git clone https://github.com/NikStor03/string-filter`

Just transfer main.py to your project

# Usage

Fast start
```py
from string_filter import Censore

censore = Censore()

censore.censore("fuck you")
# **** you
```

Add your own words
```py
from string_filter import Censore

censore = Censore()

censore.censore("Hi test man", ['test', 'hi'])
# ** **** man
```

Add your own words
```py
from string_filter import Censore

censore = Censore()

censore.censore("Hi test man", custom_words=['test', 'hi'], masking_symbol="$")
# $$ $$$$ man
```

Deep filter
```py
from string_filter import Censore

censore = Censore()

censore.censore("Hi fuckshit")
# Hi ********

censore.censore("Hi fuckshitpeople")
# Hi ********people

```
