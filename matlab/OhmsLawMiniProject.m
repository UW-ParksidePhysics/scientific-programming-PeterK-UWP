
%Plug in 'a' for your currents of a 2 parallel resistor circuit
Given_Voltage = 6   % input
Resistor_one = 13
Resistor_two = 7


V = [Given_Voltage]
Varray = [0:1:Given_Voltage] 
R1 = [Resistor_one]
R2 = [Resistor_two]


for V = V(1,1)
    for R1 = R1(1,1)
        for R2 = R2(1,1)
%             matv = [R1, -R1 ; R1, -(R2 + R1)]
%             soli = [V ; 0]
%             vinverse = matv^(-1)
%             currents = [vinverse] * [soli]
              currents = calculate_currents(V, ([R1 R2]))
        end
    end    
end
current3 = currents(1,1)
current2 = currents(2,1)
current1 = currents(1,1) + currents(2,1)

your_input = [current1, current2, current3]
total_current = your_input(1,1)

spaceing = current1/(Given_Voltage)
Iarray = [0:spaceing:current1]

for V = Varray
    for I = Iarray
       plot(Varray, Iarray, 'r-', Given_Voltage, total_current, 'md', 0, 0, 'gs')
    end
end

xlabel('Given Potential')
ylabel('Total Curerent')
legend('inverse of Resistance', 'max current', 'min-current')


Total_Resistance = 1/calculate_conductance(Given_Voltage, total_current)

function currents = calculate_currents(voltage, resistances)
% Calculate currents in two-parallel-resistor, single-source circuit
% v = i1 * R1 --> (R1 0  (i1  = (v
% v = i2 * R2      0  R2) i2)    v)
    matrix = diag(resistances);
    vector = voltage * ones([2, 1]);
    currents = matrix\vector;
end

function conductance = calculate_conductance(voltage, current)
% G = I / V  
% Conductance in a passive resistor equals the ratio of current through
% the resistor to the voltage drop across it
    conductance = current/voltage;
end

