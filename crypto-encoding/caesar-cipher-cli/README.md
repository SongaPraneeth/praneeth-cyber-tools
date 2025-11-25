**How to Install**

1. Clone the repository
`git clone https://github.com/SongaPraneeth/praneeth-cyber-tools/tree/cli/crypto-encoding/caesar-cipher-cli`

2. Go into the project folder
`cd caesar_cipher`

3. Install the tool globally
`pip install .`

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

Mode    : encrypt
Shift   : 13
Input   : Cyber Security
Result  : Plore Frphergl

**Decrypt**
`caesar -d "Plore Frphergl"`

**Output:**

Mode    : decrypt
Shift   : 13
Input   : Plore Frphergl
Result  : Cyber Security