from MDAnalysis import Universe

u = Universe("zno_ctab.pdb")
print(f"Total atoms: {len(u.atoms)}")
print(f"Residues: {len(u.residues)}")
print(f"Missing coordinates: {sum(~u.atoms.positions.any(axis=1))}")


# Verify residue composition
print("Residue breakdown:")
for res in u.residues:
    atoms = res.atoms.names
    print(f"Residue {res.resid}: {res.resname} ({len(atoms)} atoms)")