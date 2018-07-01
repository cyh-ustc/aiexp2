load('faces.mat')
traindata = zeros(320, 10304);
testdata = zeros(80, 10304);
for i = 0:39
    ri = randperm(10, 10);
    for j = 1:8
        traindata(i*8+j,:) = rawdata(i*10+ri(j),:);
    end
    for j = 1:2
        testdata(i*2+j,:) = rawdata(i*10+ri(j+8),:);
    end
end
clear rawdata;
clear ans;
clear i;
clear j;
clear ri;
m = mean(traindata);
testdata = testdata - m;
traindata = traindata - m;
clear m;
sigma = traindata' * traindata;
sigma = sigma / 320;
% [u, s, ~] = svd(sigma);
[u, s, ~] = eig(sigma);
s = ones(1, length(s)) * s;
