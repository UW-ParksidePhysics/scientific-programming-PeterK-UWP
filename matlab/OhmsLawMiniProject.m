
%Plug in 'inputs' for your currents and conductances of a 2 parallel resistor circuit
%        ___i1__>>_______i2__>>___
%       |            |            |
%       |  +      i3 | +          | +
%      VOLT       \/ R1           R2
%       |  -         | -          | -
%       |____________|____________|

Given_Voltage = 6;   % input
Resistor_one = 13;
Resistor_two = 7;


V = [Given_Voltage]
Resistances = [Resistor_one, Resistor_two]

currents_get = calculate_currents(Given_Voltage, Resistances)

total_current = currents_get(1,1) + currents_get(2,1)

spaceing = total_current/(Given_Voltage)
spaceing1 = currents_get(1,1)/(Given_Voltage)
spaceing2 = currents_get(2,1)/(Given_Voltage)
Varray = [0:1:Given_Voltage];
Iarray = [
    0:spaceing:total_current ;
    0:spaceing1:currents_get(1,1) ;
    0:spaceing2:currents_get(2,1)
];

Total_Resistance = 1/calculate_conductance(Given_Voltage, total_current)
Total_Power = calculate_power(Given_Voltage, total_current)

hold on
plot_conductance(Varray, Iarray(1,:), Given_Voltage, total_current, 'r-', 'total conductance')
plot_conductance(Varray, Iarray(2,:), Given_Voltage, currents_get(1,1), 'b-', 'conducatance R1')
plot_conductance(Varray, Iarray(3,:), Given_Voltage, currents_get(2,1), 'g-', 'conductance R2')
hold off

function plot_conductance(Varray, Iarray, Given_Voltage, total_current, color, label)
         
    plot(Varray, Iarray, color, 'DisplayName', label)            
   
    plot(Given_Voltage, total_current, 'md', 'DisplayName', 'maximum current')
    plot(0, 0, 'gs', 'DisplayName', 'minimum current')
    title('conductance')
    xlabel('Given Potential (V)')
    ylabel('Total Curerent (A)')
    legend show
end

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

function power = calculate_power(voltage, current)
%P = I*V
    power = current * voltage;
end
