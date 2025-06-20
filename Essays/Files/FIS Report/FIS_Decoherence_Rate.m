% Create a Mamdani FIS
A = mamfis('Name', 'FIS Decoherence Rate');



% Add input (Temperture in mK. 1 Kelvin = 1000 mK
A = addInput(A, [5 150], 'Name', 'Temperture (milliKelvin)'); 
% Add Membership Functions for Input
A =addMF(A,'Temperture (milliKelvin)','gaussmf',[4 5],'Name','Very Cold');
A =addMF(A,'Temperture (milliKelvin)','gaussmf',[12 50],'Name','Cold');
A =addMF(A,'Temperture (milliKelvin)','gaussmf',[14 100],'Name','Warm');
A =addMF(A,'Temperture (milliKelvin)','gaussmf',[18 150],'Name','Hot');



% Add input (Magnetic Field Strength in mT. 1 tesla = 1000 miliTesla
A = addInput(A, [0 10], 'Name', 'Magnetic Field Strength (milliTesla)'); 
% Add Membership Functions for Input
A =addMF(A,'Magnetic Field Strength (milliTesla)','gaussmf',[1 0],'Name','Low');
A =addMF(A,'Magnetic Field Strength (milliTesla)','gaussmf',[1.5 4],'Name','Medium');
A =addMF(A,'Magnetic Field Strength (milliTesla)','gaussmf',[1.5 10],'Name','High');



% Add input for Noise Level (with trapezoidal MFs)
A = addInput(A, [0 1], 'Name', 'Noise Level (Unitless)'); 
% Add Membership Functions for Input
A = addMF(A, 'Noise Level (Unitless)', 'trapmf', [0 0 0.2 0.4], 'Name', 'Low');
A = addMF(A, 'Noise Level (Unitless)', 'trapmf', [0.3 0.5 0.5 0.7], 'Name', 'Medium');
A = addMF(A, 'Noise Level (Unitless)', 'trapmf', [0.6 0.8 1 1], 'Name', 'High');



% Add output for Decoherence Rate (with trapezoidal MFs)
A = addOutput(A, [0 0.001], 'Name', 'Decoherence Rate (per nanosecond)'); 
% Add Membership Functions for Input
A = addMF(A, 'Decoherence Rate (per nanosecond)', 'gaussmf', [0.0001 0], 'Name', 'Low');
A = addMF(A, 'Decoherence Rate (per nanosecond)', 'gaussmf', [0.0001 0.0005], 'Name', 'Medium');
A = addMF(A, 'Decoherence Rate (per nanosecond)', 'gaussmf', [0.0002 0.001], 'Name', 'High');



% The declaration for each rule
Rule1 = [1 1 1 1 1 1];
Rule2 = [1 1 2 1 1 1];
Rule3 = [1 1 3 2 1 1];
Rule4 = [1 2 1 1 1 1];
Rule5 = [1 2 2 2 1 1];
Rule6 = [1 2 3 2 1 1];
Rule7 = [1 3 1 2 1 1];
Rule8 = [1 3 2 2 1 1];
Rule9 = [1 3 3 2 1 1];
Rule10 = [2 1 1 1 1 1];
Rule11 = [2 1 2 2 1 1];
Rule12 = [2 1 3 2 1 1];
Rule13 = [2 2 1 2 1 1];
Rule14 = [2 2 2 2 1 1];
Rule15 = [2 2 3 2 1 1];
Rule16 = [2 3 1 2 1 1];
Rule17 = [2 3 2 2 1 1];
Rule18 = [2 3 3 3 1 1];
Rule19 = [3 1 1 2 1 1];
Rule20 = [3 1 2 2 1 1];
Rule21 = [3 1 3 2 1 1];
Rule22 = [3 2 1 2 1 1];
Rule23 = [3 2 2 2 1 1];
Rule24 = [3 2 3 3 1 1];
Rule25 = [3 3 1 2 1 1];
Rule26 = [3 3 2 3 1 1];
Rule27 = [3 3 3 3 1 1];
Rule28 = [4 1 1 2 1 1];
Rule29 = [4 1 2 2 1 1];
Rule30 = [4 1 3 3 1 1];
Rule31 = [4 2 1 2 1 1];
Rule32 = [4 2 2 3 1 1];
Rule33 = [4 2 3 3 1 1];
Rule34 = [4 3 1 3 1 1];
Rule35 = [4 3 2 3 1 1];
Rule36 = [4 3 3 3 1 1];



% A matrix to hold the rule arrays
ruleList = [Rule1;Rule2;Rule3;Rule4;Rule5;Rule6;Rule7;Rule8;Rule9;Rule10;Rule11;Rule12;Rule13;Rule14;Rule15;Rule16;Rule17;Rule18;Rule19;Rule20;Rule21;Rule22;Rule23;Rule24;Rule25;Rule26;Rule27;Rule28;Rule29;Rule30;Rule31;Rule32;Rule33;Rule34;Rule35;Rule36];
% Add the rules to the fis
A = addRule(A, ruleList);



% Visualizing rules in the rules list 
ruleview(A)



% Plot Membership Functions
subplot(4,1,1),plotmf(A, 'input', 1)

subplot(4,1,2),plotmf(A, 'input', 2)

subplot(4,1,3),plotmf(A, 'input', 3)

subplot(4,1,4),plotmf(A, 'output', 1)



% ------------------------  TESTING THEORETICAL DATA -----------------------

Theoretical_Data = [
    25.00, 0.50, 0.50;
    50.00, 0.70, 0.10;
    18.00, 4.00, 0.90;
    135.27, 9.48, 0.23;
    63.91, 2.15, 0.63;
    89.34, 7.73, 0.04;
    14.66, 0.18, 0.87;
    141.89, 3.02, 0.31;
    46.22, 5.57, 0.96;
    101.78, 1.13, 0.44
];   

% Theoretical Data fuzzified 
for n = 1:size(Theoretical_Data, 1) % array through theoretical data

    x = Theoretical_Data(n, :);
    fprintf('\n===== Test Case %d =====\n', n); 
  
    for i = 1:length(A.Inputs) % array through Input Variavles
    
        mfStructs = A.Inputs(i).MembershipFunctions;
        InputName = A.Inputs(i).Name;
        fprintf('Evaluating membership functions for input variable: %s (x = %g)\n', InputName, x(i));
    
        for y = 1:length(mfStructs) % array through the Input variable membership functions 
    
            name = mfStructs(y).Name;
            mfType = mfStructs(y).Type;
            params = mfStructs(y).Parameters;
            mu = feval(mfType, x(i), params);  % fuzzy value
            fprintf('μ_%s(%g) = %.4f\n', name, x(i), mu);
    
        end
    end
end

% Theoretical Data Output Results
Theory_Crisp_Outputs = evalfis(A, Theoretical_Data);
fprintf('\n');

for n = 1:length(Theory_Crisp_Outputs)
    input_values = Theoretical_Data(n, :);
    fprintf('Crisp Input %d: [%.2f, %.2f, %.2f] --> Crisp Output = %.6f\n', n, input_values(1), input_values(2), input_values(3), Theory_Crisp_Outputs(n));
end
















