<h1 align="center">

**FIRE SCRIPT CLI**
</h1>
<h2 align="center">

[![GitHub license](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Github Followers](https://img.shields.io/github/followers/shubham-chhimpa?label=Follow&style=social)
![GitHub stars](https://img.shields.io/github/stars/shubham-chhimpa/fire-script-cli?style=social)
![GitHub forks](https://img.shields.io/github/forks/shubham-chhimpa/fire-script-cli?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/shubham-chhimpa/fire-script-cli?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/shubham_chhimpa?label=Follow&style=social)
</h2>

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Usage](#usage)
- [Contribution](#contribution)
- [Contact](#contact)
- [License](#license)

# Description
CLI to update all documents with a new field in a collection of Firebase
[Firestore](https://firebase.google.com/docs/firestore/quickstart) Database

You need the service key json file which you can get bt following these [steps](https://firebase.google.com/docs/firestore/quickstart#initialize)

# Requirements

1. You should have python 3
2. Install the requirements
```
pip install -r requirements.txt
```

# Usage
```
usage: fire-script-cli.py [-h] [-k KEY] [-c COLLECTION] [-f FIELD] [-v VALUE]

CLI to update all documents with new field in a collection of Firebase
Firestore Database

optional arguments:
  -h, --help            show this help message and exit
  -k KEY, --key KEY     Google Cloud Service Key File(JSON) path
  -c COLLECTION, --collection COLLECTION
                        Collection Name
  -f FIELD, --field FIELD
                        Field Name
  -v VALUE, --value VALUE
                        Field Value

```

# Contribution
If you want to contribute to this library, you're always welcome! See [Contributing Guidelines.](https://github.com/shubham-chhimpa/fire-script-cli/blob/master/CONTRIBUTING.md)

# Contact
If you need any help, you can connect with me.

Visit : [shubham-chhimpa.github.io](http://shubham-chhimpa.github.io)
# License
```
Copyright (c) 2020 Shubham Chhimpa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```