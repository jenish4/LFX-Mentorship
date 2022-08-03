# LFX-Mentorship

### Jenish Shah (jenishshah08@gmail.com)

---

## Prerequisite Task: Coding Challenge


* https://mentorship.lfx.linuxfoundation.org/project/4d633e10-48bd-4834-891c-0e076eb79a18

* https://gist.github.com/pawks/98863e5eca71c8b80b18e060cb4d9558

* https://github.com/pawks/lfx-mentorship/issues


1. Write a python program which takes a valid RISC-V ISA string(described in Chapter 28 of the [RISC-V specification(unpriv)](https://github.com/riscv/riscv-isa-manual/releases/download/Ratified-IMAFDQC/riscv-spec-20191213.pdf)) and generates coverpoints for each of the relevant bits in the `extension` field of `misa` register 
described in section 3.1.1 of the [RISC-V privileged ISA](https://github.com/riscv/riscv-isa-manual/releases/download/Priv-v1.12/riscv-privileged-20211203.pdf). Briefly describe the events (i.e list out the possible exceptions and why) in the test which will occur while testing one such coverpoint. Refer to the `csr_comb` node described [here](https://riscv-isac.readthedocs.io/en/0.13.1/cgf.html) to understand the format for the coverpoints. 
Example: for RV32IM, two relevant coverpoints are to check whether the bit at index 12 of misa is 0 and 1(```misa && 0x1000 == 0x1000```). 
Note - You can restrict yourself to list of ratified extensions for the sake of this task. The program need not check for the validity of the ISA string. 

![](https://drive.google.com/uc?export=view&id=1W-meo8feSQ1jqAXyo1arzbC6_0BWp4tC)


2. Write an assembly test which covers one of the coverpoints generated above. Bonus points if the test contains a trap handler.

What is a coverpoint?
A coverpoint specifies a boolean expression over the fields of an architectural element(instruction/state) that is required to be satisfied at least once during execution. The fields which can be used in the expression varies based on the type of the coverpoint. For example, a rs2 coverpoint specifies that atleast one instruction of the given opcode should have the rs2 field set to the register(x2) specified in the coverpoint. More information about the different types of coverpoints and the available variables can be found [here](https://riscv-isac.readthedocs.io/en/0.13.1/cgf.html).
