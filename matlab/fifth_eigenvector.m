% Test comment
%2 -1 0 0 0
%-1 2 -1 00
%0 -1 2 -1 0 
%0 0 -1 2 -1
%0 0 0 -1 2

five_ones = ones(1,5)
five_twos = 2 * five_ones

H1 = diag(five_twos)

four_ones = ones(1,4)
four_negative_ones = -1 * four_ones
diagonal_negative_ones = diag(four_negative_ones)

H2 = [[zeros(1,4) ; diagonal_negative_ones] zeros(5,1)]
H3 = H2'
H4 = H1 + H2 + H3
H5 = H4 * (1/(2*(1/(5+1))^2))

e = eig(H5)
[V,D] = eig(H5)
fith_eigenvector = V(:,5)
fith_eigenvalue = D(5,5)


%x1 = (1/(5+1))
%x2 = (5/(5+1))
%x = linspace(x1,x2,n)
%n = 5
x = [0.1667, 0.3333, 0.5000, 0.6667, 0.8333]
%fith_eigenvector = V(:,5)
x3 = [0:.1:1]
y = sqrt(2) * sin(x3 * pi)

plot(x, fith_eigenvector, '--',x3,y, ':')
xlabel('x')
ylabel('eigenvectoers')