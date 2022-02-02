![](https://raw.githubusercontent.com/rafneta/RNlibro/master/imagenes/banner.png)

```{contents}
:depth: 4
```

# NumPy

- [Página principal de NumPy](https://numpy.org/)
- [Documentación](https://numpy.org/doc/stable/)


![Image](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41586-020-2649-2/MediaObjects/41586_2020_2649_Fig2_HTML.png?as=webp)



import numpy as np

dir(np)

help(np.linalg)

help(np.shape)

a = np.arange(15)
a

np.shape(a)

type(a)

dir(a)

help(np.ndarray.shape)

a.shape

help(np.ndarray.reshape)

help(a.reshape)

help(np.reshape)

a.reshape((5,3))

a.reshape((5,3),order='F')

## Arreglos

![Image](https://www.pythoninformer.com/img/numpy/2d-array.png) ![Image](https://www.pythoninformer.com/img/numpy/3d-array-stack.png) 



a = np.linspace(1,10,3)
a

a.shape

b = np.linspace(1,15,15)
print(b)
print(b.shape)
b = b.reshape((3,5))
print(b)
b.shape

c = np.linspace(1,30,30)
print(c)
print(c.shape)
c = c.reshape((2,3,5))
print(c)
c.shape

d = np.ones((2,3,5))
print(d.shape)
d

![Image](https://media.geeksforgeeks.org/wp-content/uploads/Numpy1.jpg)

c

c[1,1,2]

e = np.linspace(1,8,8)
e.reshape((2,2,2))

e = np.array([[[1., 2.],[3., 4.]],[[5., 6.],[7., 8.]]])
e

e[0,:,:]*e[1,:,:]

e[0,:,:]@e[1,:,:]

e[0,:,:].dot(e[1,:,:])

help(np.linalg.multi_dot)

np.linalg.multi_dot([e[0,:,:],e[1,:,:]])

print(a)
print(c[0,:,:])
r = a.dot(c[0,:,:])
print(r)
print(r.shape)
r.ndim

ap = a.reshape((1,3))
print(ap)
ap.shape
rp = ap.dot(c[0,:,:])
print(rp)
print(rp.shape)
rp.ndim

at = a.T
print(at)
at.shape

apt = ap.T
print(apt)
apt.shape

print(at)
r = np.ones((3,3)).dot(at)
print(r)
print(r.shape)
r.ndim

print(apt)
r = np.ones((3,3)).dot(apt)
print(r)
print(r.shape)
r.ndim