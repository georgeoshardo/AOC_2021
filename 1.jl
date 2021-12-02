using DelimitedFiles
file = readdlm("1.txt")
diffs = diff(file[:,1])
println(sum(diffs .> 0))

function rolling_diff(file, window)
    a = []
    for x ∈ 1:(length(file)-window)
        push!(a,sum(file[x+1:x+window]) - sum(file[x:x+window-1]))
    end
    return a
end
println(sum(rolling_diff(file,3) .> 0))

## Or:

a = file
sum([1 for (x,y) in zip(a[2:end], a[1:end-1]) if x>y])
sum([1 for (x,y) in zip([sum([x,y,z]) for (x,y,z) in zip(a[1:end-2],a[2:end-1],a[3:end])][2:end], [sum([x,y,z]) for (x,y,z) in zip(a[1:end-2],a[2:end-1],a[3:end])][1:end-1]) if x>y])

## Or
using RollingFunctions

sum(diff(rolling(sum,vec(a),3)) .> 0)