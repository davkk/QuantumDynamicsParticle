open type System.Math

seq { 1.0 .. 10.0 }
|> Seq.iter (fun i -> let omega = i * 0.5 * PI * PI in printfn "%f" omega)
