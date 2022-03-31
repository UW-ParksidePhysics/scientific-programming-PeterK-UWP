% test comment
% test comment

a = 1:0.1:10;

yarray = a.^2

trapz(a, yarray)  % integral
% plot(a, yarray, '-')
% legend show

index = 1
for value = [yarray]
    if index > 1
        delta_y = value - yarray(index - 1)
        delta_x = a(index) - a(index-1)
        slope = delta_y / delta_x
        disp(slope)
    end
    index = index + 1
    % disp(value)
end

function
