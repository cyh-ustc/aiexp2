function r = predict(train, test)
%PREDICT 此处显示有关此函数的摘要
%   此处显示详细说明
    n = size(test, 1);
    bingo = 0;
    for i = 1:n
        m = train - test(i,:);
        m = abs(m);
        m = sum(m, 2);
        [~,z] = min(m);
        if fix((z-1)/8) == fix((i-1)/2)
            bingo = bingo + 1;
        end
    end
    r = bingo/n;
end

