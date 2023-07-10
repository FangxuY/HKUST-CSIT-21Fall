Name：`Yuan Fangxu`

Student ID: `20799126`

E-mail Address: `fyuanad@connect.ust.hk`

### 1

#### (a)

To determine whether a graph is structurally balanced, we simply need to determine whether each node matches the following three conditions:

- Friend of my friend is my friend
- Enemy of enemy is my friend
- Enemy of friend is my enemy

The above graph was judged to be structurally balanced.

#### (b)

|      | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   | 12   |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | X    | +    | -    | -    | -    | -    | +    | -    | +    | -    | -    | +    |
| 2    |      | X    | -    | -    | -    | -    | +    | -    | +    | -    | -    | +    |
| 3    |      |      | X    | +    | +    | +    | -    | +    | -    | +    | +    | -    |
| 4    |      |      |      | X    | +    | +    | -    | +    | -    | +    | +    | -    |
| 5    |      |      |      |      | X    | +    | -    | +    | -    | +    | +    | -    |
| 6    |      |      |      |      |      | X    | -    | +    | -    | +    | +    | -    |
| 7    |      |      |      |      |      |      | X    | -    | +    | -    | -    | +    |
| 8    |      |      |      |      |      |      |      | X    | -    | +    | +    | -    |
| 9    |      |      |      |      |      |      |      |      | X    | -    | -    | +    |
| 10   |      |      |      |      |      |      |      |      |      | X    | +    | -    |
| 11   |      |      |      |      |      |      |      |      |      |      | X    | -    |
| 12   |      |      |      |      |      |      |      |      |      |      |      | X    |

### 2

#### (a)

For example:

A -> X - 

X -> B -

Balance theory: A->B +

Status theory: A->B -

#### (b)

Graph1: A is lower than X, X is lower than B, so we predict  A is lower than B, sign = +.

Graph2: B is lower than X, A is higher than X, we predict sign = -.

Graph3: X is lower than A, higher than B. We predict A is higher than B, sign = -.

#### (c)

From A’s perspective:

Since B has negtive evaluation, B is low status. Thus, the evaluation A gives is more likely to be negtive than the generative baseline of A.

 

From B’s perpective:

Since A has negtive evaluation, A is low status. Thus, the evaluation B receives is more likely to be positive than the receptive baseline of B.

### 3

#### Step2

P(A) = 0.5 * 0.5 + 0.5 * 1/4 = 0.375

P(B) = 0.5 * 1/4 = 0.125

P(C) = 0.5 * 0.5 = 0.25

P(D) = 0.5 * 1/4 = 0.125

P(E) = 0.5 * 1/4 = 0.125

#### Step3

P(A) = 0.125 * 0.5 + 0.25 * 1/4 = 0.125

P(B) = 0.375 * 1/2 + 0.25 * 1/4 =  0.25

P(C) = 0.375 * 1/2 + 0.125 * 1/2 + 0.125 * 1/2 + 0.125 * 1/2 * 0.125 = 0.375

P(D) = 0.25 * 1/4 + 0.125 * 1/2 = 0.125

P(E) = P(D) = 0.125

#### Step4

P(A) = 0.25 * 1/2 + 0.375 * 1/4 = 0.21875

P(B) = 0.125 * 1/2 + 0.375 * 1/4 = 0.15625

P(C) = 0.125 * 1/2 + 0.25 * 1/2 + 0.125 * 1/2 * 2= 0.3125

P(D) = P(E) = 0.375 * 1/4 + 0.125 * 1/2 = 0.15625

### 4

#### (a)

| T    | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7     | 8     | 9     | 10    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----- | ----- | ----- | ----- |
| S(t) | 10   | 7.50 | 5.16 | 3.34 | 2.16 | 1.46 | 1.05 | 0.81  | 0.66  | 0.56  | 0.50  |
| I(t) | 5    | 6.25 | 7.03 | 7.09 | 6.50 | 5.58 | 4.59 | 3.68  | 2.91  | 2.28  | 1.77  |
| R(t) | 0    | 1.25 | 2.81 | 4.57 | 6.34 | 7.97 | 9.36 | 10.51 | 11.43 | 12.16 | 12.73 |

#### (b)

| T    | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| S(t) | 10   | 9.00 | 8.15 | 7.43 | 6.83 | 6.33 | 5.92 | 5.59 | 5.32 | 5.09 | 4.91 |
| I(t) | 5    | 4.75 | 4.42 | 4.03 | 3.62 | 3.21 | 2.82 | 2.45 | 2.11 | 1.81 | 1.54 |
| R(t) | 0    | 1.25 | 2.44 | 3.54 | 4.55 | 5.46 | 6.26 | 6.96 | 7.57 | 8.10 | 8.10 |

#### (c)

Virus strength = β/γ. In part (b), virus strength is less than that in (a). As a result, I(t) in *b* does not experience a up-and-down trend. It decreases directly from the beginning. Since the virus is not so strong in b, the trend in S(t) and R(t) is much slower. From a real-world perspective, when the virus is not as strong, not many people will be infected, so the susceptible population will remain large. Also, because fewer people are infected, the recovery population will not be as large.



### 5

#### (a)

Because there is only one node for large degree.

#### (b)

It is a bad idea. There are many points and their distribution is not smooth anyway, making it hard to follow a linear regression.

The good way is to plot Complementary CDF (CCDF) 𝑷 (𝑿 ≥ 𝒙). Then the estimated 𝛼 = 1 + 𝛼′

where 𝛼′ is the slope of 𝑃 (𝑋 > 𝑥).‘

#### (c)

Because a power law’s expectation is ![img](file:////Users/yuanfangxu/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image002.jpg). If α<=2, 𝐸[𝑥] = ∞. We set 2 < *α* < 3 so: E[x] = const, Var[x] = ∞.

