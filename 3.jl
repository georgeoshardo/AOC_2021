using DelimitedFiles
a = readdlm("3.txt",String)
function get_common_bit(a,m_l)
    most_common_bit = [sum([1 for x in a if x[i] == '0']) for i in 1:length(a[1])] .<=length(a)/2
    if m_l == "most"
        return join([string(x*1) for x in most_common_bit])
    elseif m_l == "least"
        return join([string(x*1) for x in .~most_common_bit])
    end
end

most_common_bit = get_common_bit(a,"most")
least_common_bit = get_common_bit(a,"least")
p1 = parse(Int, most_common_bit, base=2) * parse(Int, least_common_bit, base=2)
println(p1)
function get_rating()
    o_gen = copy(a) 
    c_gen = copy(a)
    i = 1
    while length(o_gen) != 1
        o_gen = o_gen[[if (x[i] == get_common_bit(o_gen,"most")[i]) true else false end for x in o_gen]]
        i += 1
    end
    i = 1
    while length(c_gen) != 1
        c_gen = c_gen[[if (x[i] == get_common_bit(c_gen,"least")[i]) true else false end for x in c_gen]]
        i += 1
    end
    return o_gen[1], c_gen[1]
end

println(prod(parse.(Int,get_rating(),base=2)))