%2 0 0 0 n 0 0 0 0 0
%0 2 0 0 0 0 0 0 0 0
%0 0 2 0 0 0 0 0 0 0
%0 0 0 2 0 0 0 0 0 0
%0 0 0 0 2 0 0 0 0 0
%0 0 0 0 0 2 0 0 0 0
%0 0 0 0 0 0 2 0 0 0
%0 0 0 0 0 0 0 2 0 0
%0 0 0 0 0 0 0 0 2 0
%0 0 0 0 0 0 0 0 0 2

ten_ones = ones(1,10)
ten_twos = 2 * ten_ones

H1 = diag(ten_twos)

nine_ones = ones(1,9)
nine_negative_ones = -1 * nine_ones
diagonal_negative_ones = diag(nine_negative_ones)

H2 = [[zeros(1,9) ; diagonal_negative_ones] zeros(10,1)]
H3 = H2'

H4 = H1 + H2 + H3

e = eig(H4)
[V,D] = eig(H4)
teth_eigenvector = V(:,10)
teth_eigenvalue = D(10,10)

%after n insertion
%n = 10
%H4(:,5) = n
%H4(:,10) = n

%x1 = (1/(10+1))
%x2 = (10/(10+1))
%x = linspace(x1,x2,n)
%n = 10
x = [0.091, 0.182, 0.273, 0.364, 0.455, 0.545, 0.636, 0.727, 0.818, 0.909]
%fith_eigenvector = V(:,5)
x3 = [0:.1:1]
y = sqrt(2) * sin(x3 * pi)

plot(x, teth_eigenvector, '--',x3,y, ':')
xlabel('x')
ylabel('eigenvectoers')