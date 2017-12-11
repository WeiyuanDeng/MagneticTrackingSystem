function B= bfield(P)

%computes B field of dipole in cartesian coordiantes. Dipole is pointing in
%+z direction and is located at the origin (0,0,0).

%Input: P = x,y,z coordinates in an nx3 matrix (path of sensor)
%Output: B = Bx,By,Bz in an nx3 matrix

x=P(:,1);
y=P(:,2);
z=P(:,3);

A=(x.^2+y.^2+z.^2).^2.5;
B= [(3*x.*z)./A,(3*y.*z)./A,-(x.^2+y.^2)./A+2*z.^2./A];

%Example:
%X=zeros(100,3); %make a trajectory
%X(:,3)=logspace(0,2,100); %100 pts from 10^0 to 10^2
%B=bfield(X); %calculate the B-field along the path
%plot(log10(X(:,3)),log10(B(:,3)),'b-'); %plot the Bz component vs. z coordinate
%% Now offset path so it doesn't pass through center of dipole
%X(:,2)=X(:,1)+2;
%Bnew=bfield(X); %calculate the B-field along the path
%hold on;
%plot(log10(X(:,3)),log10(Bnew(:,3)),'g-');
%hold off
