from fenics import *

# Define o domínio
mesh = RectangleMesh(Point(0, 0), Point(1, 1), 10, 10)

# Define o espaço de função
V = FunctionSpace(mesh, 'P', 1)

# Define as condições de contorno
def boundary(x, on_boundary):
    return on_boundary

bc = DirichletBC(V, Constant(0), boundary)

# Define a equação de Laplace
u = TrialFunction(V)
v = TestFunction(V)
f = Constant(-6)
a = dot(grad(u), grad(v)) * dx
L = f * v * dx

# Resolve a equação de Laplace
u = Function(V)
solve(a == L, u, bc)

# Plota a solução
plot(u)
