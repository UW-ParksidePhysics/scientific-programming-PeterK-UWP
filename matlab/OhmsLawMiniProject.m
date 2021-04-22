
%Plug in 'a' for your currents of a 2 parallel resistor circuit
Given_Voltage = 6   % input
Resistor_one = 13
Resistor_two = 7


V = [Given_Voltage]
Resistances = [Resistor_one, Resistor_two]

currents_get = calculate_currents(Given_Voltage, Resistances)

total_current = currents_get(1,1) + currents_get(2,1)

spaceing = total_current/(Given_Voltage)
Varray = [0:1:Given_Voltage]
Iarray = [0:spaceing:current1]

Total_Resistance = 1/calculate_conductance(Given_Voltage, total_current)

for V = Varray
    for I = Iarray
       plot(Varray, Iarray, 'r-', Given_Voltage, total_current, 'md', 0, 0, 'gs')
    end
end
title('conductance')
xlabel('Given Potential')
ylabel('Total Curerent')
legend('conductance', 'max current', 'min-current')



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
