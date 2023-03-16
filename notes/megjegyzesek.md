# Megjegyzések a beadandókhoz

## numpy trükkök / vektorizálás

```python
# 100 gridpont

# Eredeti ~ 6-7 sec
for i in range(1,nz-1): 
    T[i] = (Tn[i] + sigma * (Tn[i+1] - 2.0 * Tn[i] + Tn[i-1]))

# Vektorizált ~ 1-2 sec
tn = Tn[1:-1]
T[1:-1] = tn + sigma * (Tn[2:] - 2.0 * tn + Tn[:-2])
```


```python
for i in range(N):
    x=pos[i]
    out+=f_1*(x-out)*sampl_time
    res.append(out)
    out_2+=f_2 * (x-out_2) * sampl_time
    res_2.append(out_2)

```

```python
# eredeti kód
t = np.linspace(a,b,step)
h = t[1] - t[0]
Y = [y0]
N = len(t)
n = 0
y = y0

for n in range(0,N-1) :
    y = y + h*f(y,t[n])
    Y.append(y)
    n = n+1  

Y = np.array(Y)

# előre lefoglalt vektor / mátrix megoldás
t = np.linspace(a,b,step)
h = t[1] - t[0]
N = len(t)
Y = np.zeros((N,))
Y[0] = y0
n = 0
y = y0

for n in range(0,N-1) :
    y = Y[n]
    Y[ii + 1] = y + h * f(y, t[n]) 
    n = n + 1  
```


## Könyvtárhasználat

- ha a `plt.plot` függvénynek megadunk egy `label` paramétert (pl.
  `label='Illesztett pontok'`) meg kell hívni a `plt.legend` függvényt
  hogy ténylegesen megjelenjen az ábrán a jelmagyarázat


## Stilisztikai, praktikák

```python
# extra zárójel nem szükséges
nt = (int)(T1max/dt)

# átláthatóbb
nt = int(T1max / dt)
```

```python
label = (r'fit param.: $\beta_0$ = ' + '{:.1f}'.format(b0) 
         + r' - $\beta_1$ = ' + '{:.2f}'.format(b1) + 
         r' - $r_{xy}^{2}$ = ' + '{:.2f}'.format(rho_value**2))

label = (
    r"fit param.: $\beta_0$ = {b0:.1f} - $\beta_1$ = {b1:.1f}"
     " - $r_{xy}$ = {rho_val:.2f}".format(
        b0 = b0,b1 = b1, rho_val = rho_value**2
    )
)
```

```python
# explicit
for n in range(0, N-1):

# rövidebb
for n in range(N - 1):
```
