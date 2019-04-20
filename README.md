# ghant
Solution for quick generation and calculation of the ghantt chart (see table 2) from the planning matrix (see table 1)

**_Table 1. The planning matrix._**

|     | **O1** | **O2** | ... | **On** |
| --- | ------ | ------ | --- | ------ |
| D1  | `t11`  | `t12`  | ... | `t1n`  |
| D2  | `t21`  | `t22`  | ... | `t2n`  |
|     | `...`  | `...`  |     | `...`  |
| Dm  | `tm1`  | `tm2`  | ... | `tmn`  |

**_Table 2. The Ghantt diagram numeric structure. Example_ **

|        |t=1|*2*|*3*|*4*|*5*|*6*|*7*|*8*|*9*|*10*|*11*|*12*|*13*|*14*|
| ------ | - | - | - | - | - | - | - | - | - | -- | -- | -- | -- | -- |
| **O1** |`1`|`1`|`2`|`2`|`2`|`3`|`3`|`3`|`4`|    |    |    |    |    |
| **O2** |   |`1`|`1`|`1`|`2`|`2`|   |   |`3`|`4` |`4` |    |    |    |
| **O3** |   |   |   |   |`1`|   |`2`|   |   |`3` |`3` |`4` |`4` |`4` |
