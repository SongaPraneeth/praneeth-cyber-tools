**How to Install**

`pipx` is the best way to install **Python CLI tools** globally without affecting your system packages.
It creates a safe isolated environment and still lets you run the tool anywhere.

1. **Install pipx**

If you don’t already have pipx, install it:

```markdown

sudo apt install pipx
pipx ensurepath

```

Close and reopen your terminal (or run source ~/.bashrc) so PATH updates.

2. **Clone the repository**
`git clone https://github.com/SongaPraneeth/praneeth-cyber-tools`

3. **Go into the project folder**
`cd praneeth-cyber-tools/crypto-encoding/caesar-cipher-cli`

4. **Install the tool globally**
`pip install .` or `pipx install .`

That’s it! Now you can use the `caesar` command anywhere on your system.

 **How to Use:**

1. Encrypt text

`caesar -e "hello world"`

2. Decrypt text

`caesar -d "uryyb jbeyq"`

3. Use a custom shift

Default shift = 13
To use a custom shift (example: 5):

Encrypt:
`caesar -e -s 5 "attack at dawn"`

Decrypt:
`caesar -d -s 5 "fyyfhp fy ifbs"`

4. **Examples**

**Encrypt**
`caesar -e "Cyber Security"`

**Output:**

```
Mode    : encrypt
Shift   : 13
Input   : Cyber Security
Result  : Plore Frphergl
```

**Decrypt**
`caesar -d "Plore Frphergl"`

**Output:**

```
Mode    : decrypt
Shift   : 13
Input   : Plore Frphergl
Result  : Cyber Security
```

[image alt](https://github.com/SongaPraneeth/praneeth-cyber-tools/blob/afee132bcaa8da512e0b2873d6fc474bdf72eccc/Projects%20photos/caesar%20cipher.png)





