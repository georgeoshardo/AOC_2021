using DelimitedFiles
a = readdlm("2.txt")

let
    x = sum(a[:,2] .* (a .== "forward")[:,1])
    z = sum(a[:,2] .* (a .== "down")[:,1]) - sum(a[:,2] .* (a .== "up")[:,1]) 
    p1 = x*z
end

mutable struct Ship
    z::Int
    x::Int
    aim::Int
end

let
    myship = Ship(0,0,0)
    for (dir, n) ∈ eachrow(a)
        if dir == "down"
            myship.aim += n
        elseif dir == "up"
            myship.aim -= n
        elseif dir == "forward"
            myship.x += n
            myship.z += myship.aim*n
        end
    end
    println(myship.x*myship.z) 
end
