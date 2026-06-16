# 🖥️ Operating Systems — Interview Q&A

[← Back to index](README.md) · Related: [DBMS](dbms.md) · [Networks](computer-networks.md) · [OOP](oop.md)

---

## Core concepts (1-line each)

- **OS** = software that manages hardware and provides services to programs (process,
  memory, file, device, and I/O management).
- **Kernel** = the core of the OS that runs in privileged mode and controls everything.
- **System call** = the interface a user program uses to request a kernel service
  (e.g. `read`, `fork`, `open`).

---

## Top questions

**1. Process vs Thread?**
A *process* is an independent program in execution with its own memory space. A *thread*
is the smallest unit of execution **within** a process; threads of the same process
share code, data, and heap but have their own stack and registers. Threads are cheaper
to create and switch between.

**2. What is a context switch?**
Saving the state (registers, program counter) of the current process/thread and loading
the state of the next one. It's pure overhead — no useful work happens during it.

**3. Process states?**
New → Ready → Running → Waiting (blocked) → Terminated. A process moves to Ready when it
can run, Running when on the CPU, Waiting when it needs I/O.

**4. What is a deadlock? Four necessary conditions (Coffman conditions)?**
Two+ processes each waiting for a resource the other holds, forever. Needs **all four**:
*mutual exclusion, hold and wait, no preemption, circular wait*. Break any one to prevent it.

**5. Deadlock handling strategies?**
- **Prevention** — design so one Coffman condition can't hold.
- **Avoidance** — Banker's algorithm: only grant requests that keep the system in a safe state.
- **Detection & recovery** — let them happen, detect cycles, then kill/rollback.
- **Ostrich** — ignore it (used by most OSes for rare deadlocks).

**6. CPU scheduling algorithms?**
- **FCFS** — first come first served (simple, convoy effect).
- **SJF** — shortest job first (optimal avg wait, can starve long jobs).
- **Round Robin** — each gets a time quantum (fair, good for time-sharing).
- **Priority** — highest priority first (starvation → fix with aging).

**7. Preemptive vs Non-preemptive scheduling?**
Preemptive can take the CPU from a running process (Round Robin, SRTF). Non-preemptive
runs a process until it blocks or finishes (FCFS, SJF).

**8. What is a race condition? How to prevent it?**
When the result depends on the *timing* of threads accessing shared data. Prevent with
**synchronization**: mutexes, semaphores, or atomic operations protecting the *critical section*.

**9. Mutex vs Semaphore?**
A **mutex** is a lock owned by one thread (binary, ownership). A **semaphore** is a
counter allowing up to N concurrent accesses; no ownership. Binary semaphore ≈ mutex but
without the ownership rule.

**10. What is the critical section problem?**
A section of code accessing shared resources that must not be executed by more than one
thread at a time. A solution needs **mutual exclusion, progress, and bounded waiting**.

**11. Paging vs Segmentation?**
**Paging** splits memory into fixed-size pages (no external fragmentation, has internal).
**Segmentation** splits by logical units of variable size (code, stack, heap; has external
fragmentation). Many systems combine both.

**12. What is virtual memory?**
An abstraction that lets a process use more memory than physically available by keeping
parts on disk and loading pages on demand (**demand paging**).

**13. What is a page fault?**
A trap when a program accesses a page not currently in RAM. The OS loads it from disk,
possibly evicting another page (using a replacement policy).

**14. Page replacement algorithms?**
- **FIFO** — evict oldest (suffers Belady's anomaly).
- **LRU** — evict least recently used (good approximation of optimal).
- **Optimal** — evict the page used farthest in the future (theoretical benchmark).

**15. Thrashing?**
When a system spends more time swapping pages than executing — too many processes, too
little RAM. Fixed by reducing the degree of multiprogramming (working-set model).

**16. Internal vs External fragmentation?**
**Internal** — wasted space *inside* an allocated block (paging). **External** — free
memory split into small non-contiguous holes (segmentation); fixed by compaction.

**17. fork() — what does it do?**
Creates a child process that's a copy of the parent. Returns the child PID to the parent
and `0` to the child. Often paired with `exec()` to run a new program.

**18. Multiprogramming vs Multitasking vs Multiprocessing?**
*Multiprogramming* keeps several jobs in memory to maximize CPU use. *Multitasking* is
time-sharing among tasks for responsiveness. *Multiprocessing* uses multiple CPUs/cores.
