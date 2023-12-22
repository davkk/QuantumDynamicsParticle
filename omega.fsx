open type System.Math

let args = fsi.CommandLineArgs

seq { 1.0 .. float args[1] }
|> Seq.iter (fun i -> let omega = i * 0.5 * PI * PI in printfn "%f" omega)
