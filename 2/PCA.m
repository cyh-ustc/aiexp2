function [ u_reduce, i ] = PCA( u, s,threshold)
%PCA 此处显示有关此函数的摘要
%   此处显示详细说明
    n = length(s);
    se = sum(s) * threshold;
    ze = 0;
    for i = 1:n
        ze = ze + s(i);
        if ze > se
            break
        end
    end
    u_reduce = u(:,1:i);
end

