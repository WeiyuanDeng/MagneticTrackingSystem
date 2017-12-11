function d=meandiff(X)

%calculates the root mean squared difference between the field at a given
%location and the field at the current location (used for minimizing function)
%Note that the position is given in the yz-plane and that the diple is oriented in the z-direction 


%put detector at a given location
det_X = [0,1,10];
B_actual=bfield(det_X);

%calculate field at guess location
B_guess=bfield([0, X]);

%calculate the RMS difference
d=sqrt(sum((B_actual-B_guess).^2));

%example of function use
%fminunc(@meandiff,[-5,12])
%%the function returns [1, 10] as the actual location of the 