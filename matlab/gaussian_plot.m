mu = 5
e = 2.718
x = [0:1:10]
y1 = (1 / ((0.5) * sqrt(2 * pi))) * e.^-((x-mu).^2) / (2 * (0.5).^2)
y2 = (1 / ((1.0) * sqrt(2 * pi))) * e.^-((x-mu).^2) / (2 * (1.0).^2)
y3 = (1 / ((1.5) * sqrt(2 * pi))) * e.^-((x-mu).^2) / (2 * (1.5).^2)

%1/((sigma)*sqrt(2*pi)) * e^-((x-5)^2/(2(sigma)^2)
y_values = []
sigma = 0.5:0.5:1.5
   


plot(x,y1,"-", x,y2,"--", x,y3,":")
xlabel('x')
ylabel('phi(x-5,sigma)')
