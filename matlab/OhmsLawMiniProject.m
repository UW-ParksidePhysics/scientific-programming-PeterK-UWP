
%first let us define Ohms law with a matrix
%we are looking for 

V = [6, 12, 17]

V1 = V(1,1)
V2 = V(1,2)
V3 = V(1,3)
R1 = [13,100, 73];

R2 = [7, 200, 45];

RT = [4.55, 66.67, 27.84]
% matA = [13, -13 ; 13, -20]
 %solx = [6 ; 0]
 %Ainverse = matA^(-1)
%current = [Ainverse] * [solx]


 
 
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

T1I1 = T1(1,1)
T1I2 = T1(2,1)
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
 
T2I1 = T2(1,1)
T2I2 = T2(2,1)
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

T3I1 = T3(1,1)
T3I2 = T3(2,1)
T3I3 = T3I1 - T3I2

%V = iR Ohm's Law
 % for test 1, i = [1.32, 0.86, 0.46] = [i1, i2, i3]
 % for test 2, i = [0.18, 0.06, 0.12] = [i1, i2, i3]
 % for test 3, i = [0.61, 0.38, 0.23] =[i1, i2, i3]
 
% In one place we have the results...

test1 = [T1I1, T1I2, T1I3]
test2 = [T2I1, T2I2, T2I3]
test3 = [T3I1, T3I2, T3I3]
%str = ["I1", "I2", "I3"]
currents = [test1 ;test2 ; test3]

totalcurrents = [test1(1,1), test2(1,1), test3(1,1)]
%and they are all correct! yay!
%now we will graph the potentials we used with the total currents to show
%our original resistances

%plot(V1, test1(1,1), 'o', V1, test1(1,2), 'o', V1, test1(1,3), 'o',V2, test2(1,1), 's', V2, test2(1,2), 's', V2, test2(1,3), 's', V3, test3(1,1), 'd', V3, test3(1,2), 'd', V3, test3(1,3), 'd')
%legend(' circle - test1 Resistances', 'square - test2 Resistances', 'diamond - test3 Resistances')
for currents = test1;
    
    for currents = test2;

        for currents = test3;
            
            plot(V1, test1,'ro', V2,test2, 'gs', V3, test3, 'md')
            
        end
    end
end
xlabel('Potential')
ylabel('Curerent')

