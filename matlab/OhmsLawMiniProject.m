%first let us define Ohms law with a matrix
%we are looking for 

V = [6, 12, 17];
R1 = [13,100, 73];
R2 = [7, 200, 45];

%V = iR Ohm's Law
 % for test 1, i = [1.32, 0.86, 0.46] = [i1, i2, i3]
 % for test 2, i = [0.18, 0.06, 0.12] = [i1, i2, i3]
 % for test 3, i = [0.61, 0.38, 0.23] =[i1, i2, i3]
for V = [6];
    for R1 = [13];
        for R2 = [7];    
            matv = [R1, -R1 ; R1, -(R2 + R1)]
            soli = [V ; 0]
            vinverse = matv^(-1)
            T1 = [vinverse] * [soli]
        end
    end
end

T1I1 = T1(1:1)
T1I2 = T1(2:1)
T1I3 = T1I1 - T1I2

 for V = [12];
    for R1 = [100];
        for R2 = [200];    
            matv = [R1, -R1 ; R1, -(R2 + R1)]
            soli = [V ; 0]
            vinverse = matv^(-1)
            T2 = [vinverse] * [soli]
        end
    end
 end
 
T2I1 = T2(1:1)
T2I2 = T2(2:1)
T2I3 = T2I1 - T2I2

for V = [17];
    for R1 = [73];
        for R2 = [45];    
            matv = [R1, -R1 ; R1, -(R2 + R1)]
            soli = [V ; 0]
            vinverse = matv^(-1)
            T3 = [vinverse] * [soli]
        end
    end
end

T3I1 = T3(1:1)
T3I2 = T3(2:1)
T3I3 = T3I1 - T3I2

% In one place we have the results...
test1 = [T1I1, T1I2, T1I3]
test2 = [T2I1, T2I2, T2I3]
test3 = [T3I1, T3I2, T3I3]

currents = [test1, test2, test3]

% matA = [13, -13 ; 13, -20]
 %solx = [6 ; 0]
 %Ainverse = matA^(-1)
%current = [Ainverse] * [solx]

