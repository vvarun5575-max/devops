def parse_fasta(fasta_text):
    sequences = []
    current_id = ""
    current_seq = ""

    for line in fasta_text.split("\n"):
        line = line.strip()
        if not line:
            continue

        if line.startswith(">"):
            if current_id:
                sequences.append({
                    "id": current_id,
                    "sequence": current_seq,
                    "length": len(current_seq)
                })
            current_id = line[1:]
            current_seq = ""
        else:
            current_seq += line

    if current_id:
        sequences.append({
            "id": current_id,
            "sequence": current_seq,
            "length": len(current_seq)
        })

    return sequences