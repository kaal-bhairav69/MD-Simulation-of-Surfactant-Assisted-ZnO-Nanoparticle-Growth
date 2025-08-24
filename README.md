# MD Simulation of ZnO Nanoparticle Growth with CTAB

This repository contains input files, data, and results for a **Molecular Dynamics (MD) simulation of ZnO nanoparticle growth** stabilized with **CTAB (cetyltrimethylammonium bromide)** using **LAMMPS**.

---

## 📌 Files in this Repository

- **input.txt** – Main LAMMPS input script (contains minimization, equilibration, and production settings).  
- **output.data** – System data file (atom types, bonds, angles, charges, etc.).  
- **log.lammps** – Log file from the LAMMPS run.  
- **dump.zno_ctab.lammpstrj** – Trajectory dump file (can be visualized in VMD/OVITO).  
- **zno_ctab.pdb** – Initial CTAB + ZnO system structure.  
- **zno_ctab_combined.pdb** – Combined structure before fixing.  
- **zno_ctab_combined_fixed.pdb** – Corrected structure used for the simulation.  
- **untitled0.py** – Small Python script for basic trajectory/energy analysis.  

---

## ▶️ Running the Simulation

1. Install [LAMMPS](https://www.lammps.org/).  
2. Run the simulation using:  
   ```bash
   lmp_serial -in input.txt

---

## Outputs:

System trajectory: dump.zno_ctab.lammpstrj

Simulation log: log.lammps

Restart/system file: output.data

---

🔬 Visualization
Use VMD or OVITO to visualize the trajectory:
 --vmd output.data dump.zno_ctab.lammpstrj--
The .pdb files can be opened in VMD/PyMOL to inspect the molecular system before simulation.

---

📊 Analysis
Example Python analysis script: untitled0.py

Modify to compute RDF, cluster sizes, or energy evolution from the trajectory.

For more detailed analysis, see LAMMPS output (log.lammps) and use tools like MDAnalysis or OVITO Python API.

✨ Author
👤 Nimit Garg , Gunjeet Kumawat, Pradeep Bishnoi
