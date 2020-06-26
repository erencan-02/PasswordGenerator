# PasswordGenerator

PasswordGenerator is a small tool that generates cool passwords.

## Installation

Use the git clone command to install PasswordGenerator.

```bash
git clone https://github.com/erencan-02/PasswordGenerator.git
```

## Usage

```python
import PasswordGenerator

gen = PasswordGenerator.PasswordGenerator()
print(gen.generatePWD(LENGTH, STRENGTH))
```

## Note
You can extend the string variety by adding a string to the container list.

Password strenght depends on list indicies. 
container = [0, 1, 2, 3] \n
strength:   [1, 2, 3, 4]

## License
[MIT](https://choosealicense.com/licenses/mit/)

