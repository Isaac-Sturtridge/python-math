from pylab import plot, show, title, xlabel, ylabel, legend, axis


london_temp_tue = [12, 11, 11 ,13, 14, 16, 16, 14]
time = ['01:00 AM', '04:00 AM', '07:00 AM', '10:00 AM', '13:00 PM', '16:00 PM', '19:00 PM,', '22:00 PM']

plot(time, london_temp_tue, marker='o')
title('Average daily temperature in London')
xlabel('Time')
ylabel('Temperature in C')
legend(['Tuesday May 24th'])
axis(ymin=0)

show()

