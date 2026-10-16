# Inter-rater agreement analysis — 20% duplicate-extraction calibration check

Comparing two independent extraction passes over the same 23-study calibration sample
(Covidence review 818465 / PROSPERO CRD420261485879):

- **"Philip" draft** — `extraction/20pct_sample_draft.md`
- **"Alaa" draft** — `Alaa extraction/20pct_sample_draft_alaa.md` (genuinely blind second pass,
  produced without reading the Philip draft)

Both drafts cover the same 23 studies (same Covidence numbers, same order) against the same
Sections A–I field spec (`extraction_template_spec.md` / `Infant_Microbiome_Codebook.docx`).
The two drafts format fields differently in places (alpha-diversity direction inline vs. its
own row; taxa names with/without italics; different label wording for the same field) — all
comparisons below judge substantive content, not literal string or label matching. A `⚑` prefix
in either draft marks "this field was flagged for some reason" (ambiguity, judgment call,
boundary case) — it is read past to the underlying content and is **not** treated as signaling
disagreement by itself.

**Fields compared** (34 fields across Sections A–I, per `extraction_template_spec.md` /
codebook):

- **A. Study identification (4):** First author/year; Country; Study design (review
  classification); Funding source
- **B. Population (4):** Total cohort N; Gestational age range/criteria; Infant age(s) at stool
  sampling; Delivery mode reported?
- **C. Exposure/comparator (4):** Feeding-group definitions (verbatim); Classification used;
  Ascertainment; N per feeding group
- **D. Profiling method (5):** Sequencing method; 16S hypervariable region; Sequencing
  platform; Bioinformatic pipeline; Reference database
- **E. Composition outcomes (8):** Alpha diversity (incl. direction); Beta diversity (incl.
  direction/separation); *Bifidobacterium*; *Bacteroides*; *Clostridia*; *Enterobacteriaceae*;
  *Lactobacillus*; Other differentially abundant taxa
- **F. Functional outcomes (1, combined):** Functional data reported? / type / direction
  (combined into one field — when both drafts say "No," Type/Direction are trivially N/A for
  both and scoring them separately would inflate the agreement count)
- **G. Covariates & age bands (3):** Age-stratified results?; Covariates adjusted for; Adequacy
  of covariate measurement
- **H. Race/ethnicity/ancestry (4):** (a) categories as reported; (b) construct used; (c)
  ascertainment; (d) analytic role
- **I. Notes (1):** substantive overlap of free-text observations

Classification scale used per field-comparison: **Full agreement** / **Partial agreement** /
**Disagreement** / **Not comparable** (see task instructions for definitions).

---

## 1. Per-field summary table

Counts are full agreement (FA) / partial agreement (PA) / disagreement (DA) / not comparable
(NC), out of 23 studies, with FA shown as a percentage. Compiled directly from the per-study
tables in Section 3.

### A. Study identification

| Field | FA | PA | DA | NC | FA % |
|---|---|---|---|---|---|
| A1 First author, year | 23 | 0 | 0 | 0 | 100% |
| A2 Country | 23 | 0 | 0 | 0 | 100% |
| A3 Study design (governs RoB tool) | 22 | 0 | 1 | 0 | 95.7% |
| A4 Funding source | 22 | 1 | 0 | 0 | 95.7% |

### B. Population

| Field | FA | PA | DA | NC | FA % |
|---|---|---|---|---|---|
| B1 Total cohort N | 22 | 1 | 0 | 0 | 95.7% |
| B2 Gestational age range/criteria | 21 | 1 | 0 | 1 | 91.3% |
| B3 Infant age(s) at stool sampling | 23 | 0 | 0 | 0 | 100% |
| B4 Delivery mode reported? | 22 | 1 | 0 | 0 | 95.7% |

### C. Exposure/comparator definition

| Field | FA | PA | DA | NC | FA % |
|---|---|---|---|---|---|
| C1 Feeding-group definitions (verbatim) | 23 | 0 | 0 | 0 | 100% |
| C2 Classification used | 19 | 4 | 0 | 0 | 82.6% |
| C3 Ascertainment | 23 | 0 | 0 | 0 | 100% |
| C4 N per feeding group | 22 | 1 | 0 | 0 | 95.7% |

### D. Profiling method

| Field | FA | PA | DA | NC | FA % |
|---|---|---|---|---|---|
| D1 Sequencing method | 23 | 0 | 0 | 0 | 100% |
| D2 16S hypervariable region | 22 | 0 | 0 | 1 | 95.7% |
| D3 Sequencing platform | 22 | 1 | 0 | 0 | 95.7% |
| D4 Bioinformatic pipeline | 22 | 0 | 1 | 0 | 95.7% |
| D5 Reference database | 22 | 0 | 1 | 0 | 95.7% |

### E. Composition outcomes

| Field | FA | PA | DA | NC | FA % |
|---|---|---|---|---|---|
| E1 Alpha diversity | 21 | 2 | 0 | 0 | 91.3% |
| E2 Beta diversity | 20 | 2 | 1 | 0 | 87.0% |
| E3 *Bifidobacterium* | 17 | 3 | 3 | 0 | 73.9% |
| E4 *Bacteroides* | 22 | 0 | 1 | 0 | 95.7% |
| E5 *Clostridia* | 21 | 2 | 0 | 0 | 91.3% |
| E6 *Enterobacteriaceae* | 22 | 0 | 1 | 0 | 95.7% |
| E7 *Lactobacillus* | 22 | 1 | 0 | 0 | 95.7% |
| E8 Other differentially abundant taxa | 18 | 5 | 0 | 0 | 78.3% |

### F. Functional outcomes

| Field | FA | PA | DA | NC | FA % |
|---|---|---|---|---|---|
| F1 Functional outcomes (reported/type/direction, combined) | 20 | 3 | 0 | 0 | 87.0% |

### G. Covariates & age bands

| Field | FA | PA | DA | NC | FA % |
|---|---|---|---|---|---|
| G1 Age-stratified results? | 23 | 0 | 0 | 0 | 100% |
| G2 Covariates adjusted for | 18 | 5 | 0 | 0 | 78.3% |
| G3 Adequacy of covariate measurement | 18 | 5 | 0 | 0 | 78.3% |

### H. Race/ethnicity/ancestry

| Field | FA | PA | DA | NC | FA % |
|---|---|---|---|---|---|
| H1 (a) Categories as reported | 22 | 1 | 0 | 0 | 95.7% |
| H2 (b) Construct used | 22 | 1 | 0 | 0 | 95.7% |
| H3 (c) Ascertainment | 22 | 1 | 0 | 0 | 95.7% |
| H4 (d) Analytic role | 19 | 4 | 0 | 0 | 82.6% |

### I. Notes

| Field | FA | PA | DA | NC | FA % |
|---|---|---|---|---|---|
| I1 Notes (substantive overlap) | 8 | 15 | 0 | 0 | 34.8% |

### Grand total (34 fields × 23 studies = 782 field-comparisons)

| | FA | PA | DA | NC |
|---|---|---|---|---|
| Count | 711 | 60 | 9 | 2 |
| % of 782 | 90.9% | 7.7% | 1.2% | 0.3% |

---

## 2. Overall agreement rate

**771 of 782 total field-comparisons (98.6%) showed full or partial agreement** between the
Philip and Alaa extractions across all 23 studies and 34 fields (711 full agreement, 60 partial
agreement). Restricting to full agreement alone, the two independent passes matched exactly on
**711 of 782 field-comparisons (90.9%)**. Nine field-comparisons (1.2%) were scored as genuine
disagreements, and two (0.3%) as not comparable (both involving one extractor finding text the
other's pass states is not present — the "not reported in the visible text" vs. a specific
reported value pattern, see Section 5).

This is a high-agreement calibration result by the usual standard for duplicate extraction, and
the disagreement rate (1.3% of field-comparisons) is low in absolute terms. The more important
signal for the review team is not the headline rate but *where* the residual disagreement
concentrates (Section 5) and *what kind* of error each extractor is prone to (Section 4) — a
small number of fields (*Bifidobacterium*, Notes, covariate-handling fields) account for a
disproportionate share of the non-full-agreement cases, and several of the disagreements were
verifiable as one extractor being factually wrong against the source text rather than a genuine
difference in judgment.

---

## 3. Per-study comparison notes

Legend: **FA** full agreement · **PA** partial agreement · **DA** disagreement · **NC** not
comparable. Field codes follow Section headers above (A1–A4, B1–B4, C1–C4, D1–D5, E1–E8, F1,
G1–G3, H1–H4, I1).

### #143 — Myers/van Beijsterveldt 2026 (Netherlands/UK)

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | PA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | PA | FA | FA | FA | FA | FA | FA | FA | FA | PA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | PA |

Notes: B4 — Alaa gives Sophia Pluto's delivery-mode p-value (0.434) but not CBGS's (0.076),
which Philip includes; both agree delivery mode was reported with no significant difference.
D4 — both describe the same AdapterRemoval→Bowtie2→BWA-mem pipeline but characterize the final
taxonomic-profiling step differently (Philip: "custom negative-binomial signature-gene model";
Alaa: "CHAMP"). E8 — both name *S. epidermidis*/*S. thermophilus* as top taxa; Alaa gives a
10-EBF/27-EFF species split Philip does not restate. I1 — notes cover non-overlapping but
non-conflicting observations (Philip: cross-study mixed-feeding pattern, dose/duration
dissociation; Alaa: cohort-overlap check).

### #364 — Patangia 2025 (Ireland)

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | **DA** | FA | PA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| PA | FA | FA | FA | FA | FA | FA | FA | PA |

Notes: E6 (Enterobacteriaceae) is a genuine disagreement — see Section 4. E8 — Alaa's taxon
list is markedly more complete (includes *E. coli*, *B. longum* subsp. *longum*, *B. bifidum*,
*Enterococcus faecalis*, *S. salivarius*) than Philip's; core overlapping taxa (*B.
pseudocatenulatum*, *Collinsella aerofaciens*) agree in direction. F1 — both conclude "not
estimable as a single direction" but cite different specific pairwise p-values and GH-family
findings. I1 — non-overlapping notes (Philip: subspecies-level nuance under genus-level null;
Alaa: cohort-overlap and in-paper cross-references to #729/#582).

### #467 — Christensen 2024 (USA) — hybrid-design study

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | PA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | **DA** | FA | FA | FA | FA | PA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | PA | FA | FA | FA | PA |

Both reviewers converge independently on **non-randomized intervention / ROBINS-I** for the
breastfed-vs-formula contrast per the review's hybrid-design rule (A3 = FA). E3
(*Bifidobacterium*) is a genuine disagreement — see Section 4. A4 — Alaa additionally notes two
authors' unrelated conflicts (Synbiotic Health) that Philip's entry omits. H1 — Alaa explicitly
flags that ethnicity's own category labels are NOT REPORTED in extractable text (only race's
are), a distinction Philip's entry does not make.

### #582 — Heppner 2024 (Germany) — hybrid-design study

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | **NC** | FA | FA | FA | PA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | **NC** | FA | FA | FA | FA | FA | **DA** | FA | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA |

B2/D2 scored **not comparable**: Alaa reports a specific ≥37-week exclusion criterion and a
specific 16S region (V3–V4, named primers) that Philip's entry states are not findable in the
available text — a source-completeness gap, not a conflicting finding. E3 and C2 are discussed
in Section 4. I1 is **full agreement** here — both independently identify this study's
age-driven (not feeding-driven) compositional null, alongside a positive functional/metabolome
difference, as the sample's clearest single-study illustration of RQ1 method-dependence.

---

### #621 — Parkin 2024 (Australia)

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | PA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | PA |

Both independently infer *Bifidobacterium* = "higher in breastfed" from the same
variance-partition logic (E3 = FA, a nice convergent judgment call). E8 — Philip's entry
describes the same breastfed-group dominant taxa as "dominant... irrespective of solid-food
timing," while Alaa's entry for the identical taxa documents an explicit solids-timing
dependence within the breastfed group — see Section 4.

### #729 — Odiase 2023 (USA)

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | PA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | PA | PA |

Strongest full-agreement study so far (all 8 Section E fields full agreement, including both
independently reporting the *Bifidobacterium* "higher in breastfed" finding that stands out
against the no-difference cluster). B1 — Alaa notes 1 sample excluded for low read count
(115→114 analyzed) that Philip's draft omits; doesn't change reported group Ns. H4 — Alaa
records race's analytic role as *both* descriptive and adjusted-covariate; Philip records it as
adjusted-covariate only. I1 — Philip's notes flag the *Bifidobacterium* finding here as directly
**contradicting** the no-difference verdict in #143/#364/#467 (a cross-study discordance worth
featuring); Alaa's notes do not make this cross-study contradiction explicit, focusing instead
on race-as-covariate rigor.

### #814 — Yin 2023 (China) — hybrid-design study

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | PA | FA | FA | FA | FA | FA | FA | FA |

Both reviewers independently converge on **non-randomized intervention/ROBINS-I** and both
independently identify the same headline methodological flag (>40% mixed-feeding contamination
in the "formula" arms, explicitly self-acknowledged by the study's own authors) as the single
most consequential issue for RQ1 and risk of bias — unusually strong agreement throughout,
including Notes (I1 = FA). G1 — Philip's answer to "age-stratified?" hedges ("not a formal
age-stratified model — more a repeated cross-section"); Alaa answers a clean "Yes" with band
placement; same two timepoints underlying both.

### #833 — Barnett 2023 (Netherlands)

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | PA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | PA |

All 8 Section E fields full agreement, including an identical *Enterobacteriaceae* "not
estimable, discussed only re: antibiotics/C-section/homebirth" verdict and an independently
identical judgment call on F1 (both separately reason that the paper's HMO/LC-MS data
characterizes the *exposure*, not an infant-gut functional outcome, so Functional data reported
= No). C2 — Alaa catches that this single paper operationalizes "exclusive"/breastfeeding
exposure three different, inconsistent ways across its three analyses (continuous dose
variable; a ≥80%-of-feeds threshold mislabeled "exclusively breastfed"; a true exclusive
formula definition) — see Section 4.

---

### #992 — Rosas-Salazar 2022 (USA)

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | **DA** | **DA** | FA | FA | FA | FA | FA | FA | FA | PA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | PA | PA | FA | FA | FA | FA | PA |

D4/D5 are **verified against the source paper** (`extraction/992__10.1016_j.jaci.2022.02.023.md`)
— see Section 4, item 7. Both independently reach the identical nuanced "not estimable from
extractable text" verdict for all three of *Bifidobacterium*/Clostridia/Enterobacteriaceae (E3,
E5, E6), including the same reasoning (direction shown only in Figure 2) — a strong positive
convergence despite the D4/D5 slip.

### #1063 — Estorninos 2022 (Philippines) — hybrid-design study

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | PA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | PA |

Both independently identify HFI-vs-CG (unsupplemented formula) as the cleanest PECO-isolable
contrast, with Alaa explicitly cross-referencing her own earlier #582 nuance. E5 (Clostridia) —
Philip's field cites an RDA/cesarean-confound finding, Alaa's field cites the targeted qPCR
pathogen panel; once both documents are read in full the underlying data agree (qPCR shows no
HFI-vs-CG difference), but the two "Clostridia" field entries alone would look like different
answers — a field-placement rather than substantive disagreement.

### #1236 — Sugino 2021 (USA)

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | **DA** | FA | FA | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | PA |

C2 is a strong **independent convergence** worth flagging positively: both reviewers, unprompted,
separately caught that this study's "≤20% human milk" comparator group pools true
exclusive-formula infants with infants still receiving up to 20% breastmilk — Alaa additionally
frames it as the mirror image of #814's contamination problem. E2 (beta diversity) is a
**verified disagreement** — see Section 4, item 8.

### #1245 — Jones 2020 (USA)

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | PA | FA |

All 8 Section E fields full agreement **and** both independently flag the identical cross-study
three-way contradiction on *Enterobacteriaceae* direction against #833/#1063 by study number —
see Section 5. I1 (Notes) is the strongest Notes convergence of the batch (near-complete overlap
of substantive points). H4 — both agree this study's Hispanic-only cohort doesn't fit any
standard analytic-role category, but Philip invents a new label ("eligibility/inclusion
criterion") while Alaa maps it to the nearest existing codebook option ("not used") with a
flag — a difference in how to handle an edge case against a controlled vocabulary, not a
substantive disagreement about the study itself.

---

### #1301 — Castanet 2020 (France/Greece/Austria) — hybrid-design study

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | PA | FA | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | PA | PA | FA | FA | FA | FA | PA |

E3 — **verified against source** (`extraction/1301__10.3390_nu12051481.md`, line 274): the paper
explicitly states "the species contributing to the increase in bifidobacteria was mainly *B.
breve* in the BF group and *B. longum* in the formula groups" — a real species-level finding
Alaa captures and Philip's entry omits entirely. G2/G3 — Alaa flags an unaddressed gap Philip's
entry doesn't raise: despite the 6-site, 3-country design, no site/country breakdown or
adjustment appears anywhere, a notable omission for a genuinely multi-country trial. I1 — Philip
flags something important that Alaa's #1301 entry omits entirely: a direct study-lineage tie to
**#1815** (Simeoni 2016) testing a near-identical synbiotic formula, likely overlapping
authorship/sponsor — see Section 4.

### #1305 — Li 2020 (China)

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | PA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | PA | FA | FA | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| PA | FA | FA | FA | FA | FA | FA | FA | FA |

Both independently identify the SAME two major unaddressed confounds (CF group ~5 months older;
FF group's striking Han/Manchu ethnicity imbalance) as this study's headline methodological
issues — a strong positive convergence, scored FA on I1. C2 — Alaa flags that the CF category
is a diet-stage category, not cleanly comparable to the other three milk-type categories, a
nuance Philip's "clean match" characterization doesn't carry. E2 — **verified against source**
(`extraction/1305__10.3389_fmicb.2020.00714.md`, line 141 vs. Figure 1 caption): the body text
reports the overall community-structure test as R²=0.1058, but the Figure 1C caption separately
reports R²=0.1461 for what appears to be the same overall test — a genuine paper-internal
inconsistency Philip's entry flags and Alaa's entry does not (Alaa's own cited R² values —
0.1058, 0.1081, 0.0521 — are each individually accurate, just incomplete).

### #1334 — Berger 2020 (Italy/Belgium) — hybrid-design study

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | PA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | PA | PA | FA | FA | FA | FA | FA |

Both independently and correctly catch the same genus-vs-species *Bifidobacterium* scale
dependence (E3 = FA, strong convergence) and converge almost point-for-point in Notes (funding
cluster of 3 Nestlé trials, intervention-effect fade by 12 months, FCT as a sophisticated
measure outside the standard taxon-direction scale). G2/G3 — same recurring pattern as #1301:
Alaa flags the unaddressed Italy-vs-Belgium site/country gap, and additionally notes that the
authors' own randomization-based reassurance about missing covariates applies only to the
randomized control-vs-test contrast, not to the non-randomized BF-vs-formula contrast this
review actually extracts — a sharp methodological point absent from Philip's entry.

### #1499 — Akagawa 2019 (Japan)

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | **DA** | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | PA | PA | FA | PA | FA | PA | FA |

All 8 Section E fields full agreement despite the study-design disagreement at A3 — see Section
4 for the A3 disagreement (a genuine Study-design/RoB-tool-relevant classification difference).
G2/G3 — Alaa catches a confound Philip's entry never mentions: all cesarean-delivered infants'
mothers received intrapartum cefmetazole, a universal exposure within the CD arm that is never
disentangled from delivery mode itself. H2/H4 — same recurring pattern as study #1245: Alaa maps
an edge case to the nearest existing codebook option with a flag (combined-or-conflated; not
used) where Philip effectively creates a new label (ethnicity/nationality; eligibility/inclusion
criterion).

---

### #1536 — Korpela 2018 (Finland) — hybrid-design study (structurally distinct: feeding type was never a trial design axis)

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | PA | FA | FA | FA | FA | FA |

Exceptionally strong agreement throughout, including both independently landing on the identical
key insight (stated almost identically in both I1 sections): this study's entire analytic frame
treats feeding type as an effect-modifier of a probiotic intervention, not a standalone exposure,
so most Section E/F "not reported" answers reflect a reporting-framing issue rather than a null
finding — both drafts flag this explicitly rather than silently recording nulls.

### #1547 — Savage 2018 (USA) — VDAART cohort (cross-reference: #1734 in batch 6)

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | PA | **DA** | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | PA |

A3 — both ultimately record the same final classification ("Prospective cohort"), but Alaa
explicitly flags it as an unresolved line-drawing question for the review team (should the
hybrid-design rule extend to VDAART-nested feeding analyses, as it does for #1536?) while
Philip settles it without raising the question — scored FA since the final field value matches.
E3/E4 — see Section 4 for two source-verified findings: Alaa correctly characterizes the
*Bifidobacterium*×race/ethnicity interaction as a non-significant trend (matching the paper's
own P=.10 against its own .05 cutoff), while Philip's Notes state it as settled fact; and for
*Bacteroides*, Philip's cited adjusted-model numbers (β=−0.07, P=.86) do not appear anywhere in
the source table, while Alaa's (P=.98 demographic-adjusted, P=.93 demographic+dietary-adjusted)
match it exactly. I1 — **Alaa's Notes explicitly flag the VDAART cohort overlap with #1734**;
Philip's #1547 Notes do not (see Section 6 for the full VDAART cross-check once #1734 is
processed).

### #1594 — Claassen-Weitz 2018 (South Africa)

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | PA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | PA | FA | **DA** | FA | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | PA | FA | FA | FA | PA | PA | PA |

E3 is a **source-verified disagreement about this study's own headline finding** — see Section
4, item 11 (this is the single most consequential verification finding in the whole comparison,
since both drafts separately call it "the most important" result in the study). E1 — Alaa
explicitly flags that the alpha-diversity finding deserves the same confounding caution the paper
itself applied to *Bifidobacterium*, a meta-level caution Philip's entry (which calls this
"Ninth concordant... one of the most consistently replicated" findings) does not raise. G2 —
Alaa catches that antibiotic exposure is never addressed anywhere in this paper, an unaddressed
gap Philip's entry doesn't mention at all.

### #1643 — Wopereis 2018 (Australia/Singapore/England/Ireland) — hybrid-design study

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | PA |

All 8 Section E fields and F1 full agreement, including both independently flagging the identical
methodological nuance that the *Bifidobacterium*/*Clostridium* statistics are pHF-OS-vs-control
(intra-formula) rather than directly-quoted BF-vs-control numbers, with the BF direction inferred
— one of the cleanest full-agreement studies in the sample.

---

### #1734 — Sordillo 2017 (USA) — VDAART cohort, sister paper to #1547

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | PA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | PA | FA | FA | FA | PA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA |

A3 — both independently classify this study as **cross-sectional** (matching), but Alaa explicitly
flags that this is inconsistent with her own "prospective cohort" answer for sibling paper #1547
(same underlying cohort/design reality) and recommends the review team apply one consistent
label to both — a self-auditing observation Philip's parallel pair of entries doesn't make (Philip
also gave #1547 "prospective cohort" and #1734 "cross-sectional" without flagging the tension).
**E5 (Clostridia) is the single strongest full-agreement result in the entire comparison** — see
Section 6 for the full VDAART cross-check. E3/E7 — Philip explicitly contrasts this paper's
*Bifidobacterium* adjustment-direction with #1547's opposite pattern; Alaa's E3 states the same
finding without making that specific cross-paper contrast. For *Lactobacillus* (E7), Philip flags
genuine textual ambiguity about whether the univariate finding survived adjustment; Alaa states
confidently that it did not.

### #1815 — Simeoni 2016 (France/Poland) — hybrid-design study, direct predecessor to #1301

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | PA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | PA |

D3 — both agree on the platform (Roche 454) but Philip's own cross-study running tally of
454-pyrosequencing studies miscounts (lists 4, omitting #1734, which Philip's *own* #1734 entry
elsewhere correctly identifies as 454-platform); Alaa's count of 5 is arithmetically correct. I1 —
**confirms the #1301 lineage-flag omission is symmetric**: Alaa's #1815 Notes, like her #1301
Notes, never state that this study's synbiotic test formula is the same intervention later
re-tested as #1301's FLPP arm — see Section 4, item 9, which this entry corroborates from the
other direction.

### #1860 — Bäckhed 2015 (Sweden) — final study, corpus "anchor" reference

| A1 | A2 | A3 | A4 | B1 | B2 | B3 | B4 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | FA | PA |

| D1 | D2 | D3 | D4 | D5 | E1 | E2 | E3 | E4 | E5 | E6 | E7 | E8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FA | FA | FA | FA | FA | PA | PA | FA | FA | FA | FA | FA | FA |

| F1 | G1 | G2 | G3 | H1 | H2 | H3 | H4 | I1 |
|---|---|---|---|---|---|---|---|---|
| PA | FA | FA | FA | FA | FA | FA | FA | PA |

E1 — Philip answers "Yes" to whether this study reports feeding-type alpha diversity (treating
a non-significant newborn-stage PERMANOVA plus the "gut microbiota age" proxy as satisfying the
field); Alaa answers that no classical scalar index comparison by feeding group is reported at
all, treating "gut microbiota age" as a structurally different outcome the field doesn't cleanly
capture — both agree on the underlying direction, but differ on whether this study "has" an
alpha-diversity answer in the classical sense. F1 — Alaa explicitly flags that the specific
functional-module findings (PTS transporters, bile-acid genes, etc.) sit against a
**non-significant omnibus PERMANOVA** (1.30% variance, P=.33) and should be read cautiously;
Philip reports the same specific modules without this caveat. I1 — both independently flag this
paper as a "corpus anchor" cited by several other studies in the sample, but name different,
non-overlapping subsets of citing studies (Philip: #814/#1334/#1499/#1594; Alaa: #364/#833/#1734)
— plausibly both partial, non-exhaustive samples of a larger true citation set rather than a
genuine contradiction.

---

*(All 23 studies processed. Sections 1, 2, 5, and 6 below are compiled from the cumulative
scoring across all batches.)*

---

## 4. Notable disagreements

*(Only the genuinely interesting ones — different substantive conclusions, different
design/RoB-tool implications, different funding/COI reads. Brief quotes plus a one-sentence
explanation of why it's a real disagreement, not just different phrasing.)*

### Batch 1 (#143, #364, #467, #582)

**1. #364 (Patangia 2025) — *Enterobacteriaceae* direction.**
Philip: "Not estimable as a BF-vs-formula direction — *E. coli*... showed a decreasing trend
over time in every group alike, not a between-group direction difference."
Alaa: "⚑ Higher in breastfed — inferred from the species-level finding that *E. coli*... 'was
always associated with the Exc Breast Fed group' in Songbird differential analysis."
*Why genuine:* the two drafts reach opposite conclusions about whether this paper's own data
support a breastfed-vs-formula direction for this taxon — Philip read the *E. coli* finding as a
time effect common to all groups, Alaa read the same taxon's Songbird ranking as a genuine
between-group (higher-in-breastfed) signal.

**2. #467 (Christensen 2024) — *Bifidobacterium*, genus level.**
Philip: "No difference at genus level — explicitly tested and stated: 'No differences in
abundance of the *Bifidobacterium* genus... were detected between study groups.'"
Alaa: "Discrepant by method within the same paper. Wilcoxon... **no difference**... DESeq2 on
ASV-level data: formula groups had **higher** *Bifidobacterium*-classified ASVs vs. HM at Day
60... Flagging the Wilcoxon-vs-DESeq2 genus-level contradiction explicitly rather than picking
one."
*Why genuine:* Philip reports a clean, settled null; Alaa surfaces a within-paper
method-dependent contradiction (a second statistical approach in the same paper shows a
positive effect) that changes the overall characterization from "no difference" to
"discrepant/method-dependent" — directly relevant to this review's own RQ1.

**3. #582 (Heppner 2024) — *Bifidobacterium*, overall verdict.**
Philip: "⚑ Not estimable as a single BF-vs-formula direction... Direction depends entirely on
*which* formula arm and *which* timepoint."
Alaa: "No difference (BF vs. formula, direct comparison)... 'complete loss of significance
between any of the interventional groups at 3 months.'"
*Why genuine:* both drafts cite the same underlying arm/timepoint-dependent data but resolve it
into different categorical verdicts on the review's four-way scale — "not estimable" vs. "no
difference" — which is itself a small case study in how two careful readers can differ on
collapsing ambiguous multi-arm data into a fixed scale.

**4. #582 (Heppner 2024) — Classification used / which contrast this study actually extracts.**
Philip's flagged nuance: an ad hoc, post-hoc mixed-feeding subgroup identified only in the
3-month metabolomics analysis.
Alaa's flagged nuance: "Recorded as: core extractable contrast = BF vs. formula A; formula
B/C/D are supplementary intra-formula comparisons, not the review's primary extracted contrast."
*Why genuine:* this is a materially different read of what comparison the study contributes to
the review — Alaa proposes narrowing the PECO-eligible contrast to BF-vs-placebo-only, which
neither Philip's draft nor (noted for consistency) Alaa's own Section E entries actually apply
(both describe outcomes as BF vs. "the formula groups" collectively). Worth the review team
resolving explicitly rather than leaving implicit.

### Batch 2 (#621, #729, #814, #833)

Batch 2 is the most concordant batch so far — no outright contradictions on a direction-of-effect
field, only completeness/depth differences. Two are worth surfacing because they show a real
difference in how thoroughly a nuance was captured, not just phrasing:

**5. #621 (Parkin 2024) — whether breastfed-group *Bifidobacterium* taxa track solid-food
timing.**
Philip (Other taxa, Section E): "*B. infantis*, *B. longum*, *B. breve* dominant in breastfed
group **irrespective of solid-food timing**."
Alaa (Other taxa, Section E): "in predominantly breastfed infants, *B. infantis* and *B. breve*
more abundant with solids introduced **after 6 months**, *B. bifidum* more abundant with solids
**before 5 months**, *B. infantis* abundance... significantly **lower** with solids before 5
months."
*Why genuine:* for the same taxa in the same group, Philip's phrasing implies stability
regardless of solids timing, while Alaa documents a specific, statistically supported
timing-dependence for those same taxa — relevant to this review's RQ6 dose/timing framing, and
a difference a verifier should resolve by re-checking the source table rather than averaging
away.

**6. #833 (Barnett 2023) — how many different ways "exclusive breastfeeding" is operationalized
within this one paper.**
Philip (Classification used): "'Other' — a continuous proportion-of-breastfeeding variable...
a new instance of this review's 'other' category." (Treats the paper as having one primary
exposure definition, with the GOS/HMO subgroups noted only descriptively elsewhere.)
Alaa (Classification used): "Heterogeneous within the same paper... Three different operational
meanings of 'exclusive'/breastfeeding exposure within one paper" — flagging that the HMO
sub-cohort's own label "exclusively breastfed" is actually a ≥80%-of-feeds threshold, which by
this review's own terminology is **predominant**, not exclusive.
*Why genuine:* Alaa catches a mislabeling in the source paper itself (a sub-cohort the authors
call "exclusively breastfed" doesn't meet this review's definition of exclusive) that Philip's
entry does not flag at all — a completeness gap with direct RQ1/RQ4 relevance, not just a
different phrasing of the same read.

### Batch 3 (#992, #1063, #1236, #1245) — two disagreements independently verified against source

**7. #992 (Rosas-Salazar 2022) — bioinformatic pipeline and reference database (Section D).**
Philip (D4): "DADA2 (ASV-based inference), with contaminant-sequence removal per Davis et al.
method." Philip (D5): "SILVA."
Alaa (D4): "⚑ Described only as 'an amplicon sequence variant–based pipeline' with the specific
software deferred to prior methods papers (refs. 19–21) not named in the visible main text."
Alaa (D5): "NOT REPORTED in the visible main text (deferred to online/prior methods)."
**Verified against the source** (`extraction/992__10.1016_j.jaci.2022.02.023.md`, line 71): the
body text reads only "grouped sequences using an amplicon sequence variant–based pipeline[19-
21]" — DADA2 and SILVA are never named in the prose; "DADA2" and "SILVA" appear *only* as
citation-list entries for references 19 and 20 (the methods papers for those tools, cited but
not confirmed as this study's own choices). **Alaa's "not reported" is the accurate reading;
Philip's specific tool names appear to be inferred from the reference list rather than stated in
text** — a genuine extraction error, not a difference in judgment, and a concrete illustration
of why the "verify against a live source" discipline matters even inside a calibration exercise.

**8. #1236 (Sugino 2021) — did beta diversity (Bray-Curtis) remain significant after covariate
adjustment?**
Philip: "remained significant for Sorensen but not Bray-Curtis once other covariates were added
in the multivariate model — ⚑ another instance of beta-diversity-metric-dependent significance
(echoing #467's precedent)."
Alaa: "human milk exposure the dominant explanatory variable across models (R²≈0.10–0.19),
**robust to adjustment** for BMI, delivery mode, sex, shipping time, age, and cohort."
**Verified against the source** (`extraction/1236__10.1177_0890334420957571.md`, Table 5): in
the fully adjusted Model 3, the human-milk term is Sorensen R²=0.14, p=.002 (significant) but
Bray-Curtis-genus R²=0.10, p=.2 and Bray-Curtis-phylum R²=0.08, p=.42 (both non-significant) —
**Philip's characterization is correct; Alaa's "robust to adjustment" over-generalizes from the
paper's own self-congratulatory Discussion-section framing ("this result is robust to
multivariate analysis") without checking Table 5's actual per-metric p-values.** A second
concrete, source-verified error, and itself a nice within-paper illustration of this review's
own RQ1 beta-diversity-metric-dependence concern.

### Batch 4 (#1301, #1305, #1334, #1499)

**9. #1301 (Castanet 2020) — undisclosed study non-independence (Notes, not a scored field but
a material omission).**
Philip: "**Direct study lineage**: the FLPP formula tested here (BMOS + lactoferrin + *B.
lactis*) is a near-identical follow-up of the exact same synbiotic formula tested in the pilot
study **#1815** (Simeoni 2016, cited here as ref. 14...). The review team should be aware these
two studies likely share overlapping authorship, sponsor, and intervention — not fully
independent evidence points for any vote-counting or synthesis."
Alaa's #1301 Notes make no mention of #1815 at all.
*Why genuine:* this is exactly the kind of cross-study non-independence flag a systematic
review's synthesis needs to catch before vote-counting studies as if they were independent
replications — Alaa's blind pass missed a connection Philip's did not (worth checking, when
processing #1815 itself in a later batch, whether Alaa catches it from the other direction).

**10. #1499 (Akagawa 2019) — Study design classification (Section A, RoB-tool-relevant).**
Philip: "Prospective cohort with a retrospective 2×2 (delivery mode × feeding type) grouping,
sampled longitudinally at two timepoints per infant."
Alaa: "⚑ Prospective sample collection with retrospective group classification... **Recorded as
cross-sectional** for the feeding-type comparison specifically (feeding groups did not exist as
an analytic category until the 1-month endpoint)."
*Why genuine:* this is a different final answer on the one field the review's own spec says
"governs RoB tool" — Philip's label is "Prospective cohort," Alaa's is "Cross-sectional." Both
likely still route to ROBINS-I as observational, but the specific design label affects which
ROBINS-I domain language applies (e.g., "selection of participants into the study" reads
differently for a cohort vs. a cross-sectional comparison) and is exactly the kind of
disagreement a human verifier should resolve explicitly rather than let an automation script
pick one silently.

### Batch 5 (#1536, #1547, #1594, #1643) — including the most consequential verified finding in the whole comparison

**11. #1547 (Savage 2018) — overstated significance of the race×breastfeeding interaction for
*Bifidobacterium*.**
Philip (E3 and Notes): "this effect was itself ethnicity-dependent (see Section H): present in
Hispanic and White infants but essentially absent in African American infants... **The single
most important race/ethnicity-by-feeding-type interaction finding in this entire 23-study
batch**."
Alaa (E8): "Race×breastfeeding interaction trends (**not fully significant**) for
*Bifidobacterium* (P=.10) and *Lactobacillus* (P=.09)."
**Verified against the source** (`extraction/1547__10.1016_j.jpeds.2018.07.066.md`, line 57):
"There was a trend toward race/ethnicity × breastfeeding status interactions with regard to
*Bifidobacterium* spp counts (**P=.10**)... " — against the paper's own stated significance
cutoff of P≤.05. **Alaa's "trend, not fully significant" is the accurate reading; Philip's
framing presents a non-significant interaction as settled fact**, which matters because Philip's
own Notes elevate this to the single most important finding of the entire batch.

**12. #1547 (Savage 2018) — fabricated-looking adjusted statistics for *Bacteroides*.**
Philip: "the difference was not significant after full adjustment (**adjusted β=−0.07, P=.86**)."
Alaa: "not significant after adjustment for demographic variables (**P=.98**) or
demographic+dietary variables (**P=.93**)."
**Verified against the source**, Table IV, "Breastfeeding vs formula feeding" section: unadjusted
b=0.60 (0.03, 1.18), P=.04; demographic-adjusted (−0.85, 0.87), P=.98; demographic+dietary-adjusted
(−0.83, 0.91), P=.93. **Alaa's numbers match this row exactly.** "−0.07" and "P=.86" are not
fabricated, but they are not this row's values either: they are the demographic+dietary-adjusted
*Bacteroides* figures from Table IV's separate **"Solid food introduction"** section (−0.07
[−0.83, 0.69], P=.86) — real numbers from the same table, apparently transcribed against the wrong
exposure comparison.

**13. #1594 (Claassen-Weitz 2018) — which *Bifidobacterium* finding is HIV-confounded (the
study's own headline result).**
Philip: "At the **meconium/discharge level**, feeding type showed a *validated*... association...
— **higher in breastfed, genuinely feeding-attributable**. But at **4–12 weeks**, the naive
finding... was... determined... to be **driven by maternal HIV status, not feeding type**."
Alaa: "Initial unadjusted analysis found... higher proportions of beneficial *Bifidobacterium*
(P=.010 **at 4–12 weeks**, P=.045 at 20–28 weeks)... the authors' own refitted-GLM validation
explicitly concluded: 'maternal HIV status was the primary driver of this observation'...
Recorded as **not estimable as a true feeding effect**[, applied to both timepoints]."
**Verified against the source** (`extraction/1594__10.1038_s41598-018-22244-6.md`): the paper's
own abstract states plainly, "**HIV-exposed infants had lower proportions of *Bifidobacterium*
(p=0.010) at 4–12 weeks**" — tying p=.010 to the HIV/4–12-week finding, not to a separate,
validated, feeding-attributable meconium-level result. The body text's confounding narrative
("upon validation... maternal HIV status was the primary driver") does not describe a second,
distinct, feeding-attributable meconium finding anywhere in the visible text. **Philip's
bifurcation into a "validated meconium feeding effect" plus a separately-confounded "4-week
finding" does not appear to be supported by the source; Alaa's uniform "HIV-confounded, not
estimable" treatment is the better-supported reading.** This is the most consequential
verification finding in this entire comparison, since both drafts independently call this result
the single most important finding of the study (and of the batch, in Alaa's case) — getting the
timepoint/attribution wrong here would misinform the review's own worked example of RQ7
confounding.

---

## 5. Patterns across fields

**1. Notes is the clear outlier field, and this is expected, not alarming.** At 34.8% full
agreement, Notes is by far the lowest-scoring field — but this reflects the field's open-ended
nature (each reviewer chooses what to highlight from a large space of valid observations) rather
than a genuine quality problem. Where both reviewers happened to converge on the same specific
observation (the VDAART *Clostridium* contradiction, the #814/#1236 mirror-image exposure-
contamination problem, several "corpus anchor" citations), the convergence was strong and often
nearly word-for-word — suggesting the two extractors are applying similar judgment, just sampling
different valid points from a larger pool on any given study. This field should not be scored or
weighted the same way as a fixed-answer field in any formal kappa-style calculation.

**2. *Bifidobacterium* (E3) is the single most fragile composition field (73.9% full agreement,
with 3 of 23 studies scored as outright disagreement and 3 more as partial) — several times the
non-agreement rate of every other named taxon (all ≥91%).** This is not because the genus is
inherently more ambiguous in the source papers than, say, *Bacteroides* or *Enterobacteriaceae*
— it is because *Bifidobacterium* is this review's most-discussed taxon, so papers report it
with the most nuance (species/subspecies splits, arm-by-arm and timepoint-by-timepoint
breakdowns, discussion-vs-results tension), giving two careful readers the most surface area to
resolve differently into one four-way-scale verdict. The three outright disagreements (#467,
#582, #1594) each trace to a different root cause: #467 and #582 are genuine judgment calls about
how to collapse ambiguous multi-arm/multi-timepoint data into the review's fixed scale (in both
cases Alaa surfaces a within-paper methodological discrepancy, or a different resolution of
arm-dependent data, that Philip's entry does not carry — see Section 4, items 2 and 3); #1594's
is source-verifiable as a genuine extraction error on Philip's side, misattributing which
timepoint's finding was HIV-confounded (Section 4, item 13, the single most consequential
verification finding in this whole exercise). The three partial-agreement cases (#1301, #1547,
#1734) are milder — one side adding a species-level nuance or cross-paper observation the other
lacks, without contradicting the core direction. **Recommendation: *Bifidobacterium* should be a
priority field for a third-reviewer adjudication pass across the full 111-study corpus, not just
this calibration sample**, given both its unusually high non-agreement rate and its centrality to
this review's RQ1.

**3. The covariate-handling fields (G2/G3) and the C2 "Classification used" field show a
consistent, specific pattern: Alaa's entries more often surface an additional, substantive
methodological gap or nuance that Philip's parallel entry does not carry**, rather than
contradicting it. Recurring examples: unaddressed multi-country/geography gaps in two Nestlé
hybrid-design trials (#1301, #1334); an unaddressed intrapartum-antibiotic confound in #1499; an
unaddressed antibiotics gap in #1594; a CF-category comparability flag in #1305; and a
≥80%-mislabeled-as-"exclusive" sub-cohort in #833. This is not evidence Alaa's pass is "better"
in some global sense — both passes made their own unique catches (Philip caught the #1301/#1815
formula-lineage non-independence in both directions, something Alaa's pass never surfaces, and
Philip's running cross-study tallies, while occasionally miscounted, provide a scaffolding Alaa's
draft doesn't attempt). But it does mean the two passes are not simply noisy versions of the same
judgment — they have different sensitivities, and a verifier should not assume either one's
completeness subsumes the other's.

**4. A real but not absolute asymmetry: of five source-verified factual errors found in this
exercise, four were in Philip's draft and one was in Alaa's — this is a correction to an earlier
draft of this finding, which had claimed the asymmetry was total.** Spot-checking five concrete,
checkable claims against the underlying paper text (not relying on either draft's own
characterization) found, on Philip's side: #992's bioinformatic-pipeline and reference-database
values ("DADA2," "SILVA") were inferred from a reference-list citation rather than stated in the
body text Alaa correctly flagged as unnamed; #1547's race×feeding interaction was reported by
Philip as settled fact when the paper's own text calls it a non-significant trend (P=.10); #1547's
*Bacteroides* adjusted statistics (β=−0.07, P=.86) do not appear anywhere in the source's
breastfeeding-vs-formula row of Table IV — those exact figures belong to a *different* row of the
same table (the solid-food-introduction comparison), apparently copied into the wrong exposure;
and #1594's central confounding narrative was more complex in Philip's retelling (a hypothesized
"validated meconium-level feeding effect") than the paper's own abstract supports. Running the
other direction, on Alaa's side: #1236's claim that a beta-diversity result was "robust to
adjustment" did not hold up against the paper's own Table 5, which Philip correctly read as
metric-dependent — here it is Alaa's characterization that over-generalized from the paper's
Discussion-section framing ("this result is robust to multivariate analysis") without checking
Table 5's actual per-metric p-values. This is not a claim that either draft is more reliable
overall — the large majority of both drafts' several hundred other factual claims were not
independently checked, and most of the ones that were held up on both sides — but it is a
specific, actionable finding for a third-reviewer verification pass: **both drafts contain at
least one confidently-stated numeric/qualitative claim that does not survive a source check, so
neither draft's more specific or more confident-sounding reading should be preferred by default
without going back to the primary source** — the deciding factor in every one of these five cases
was the source table or text itself, not which extractor's prose read as more authoritative.

**5. The hybrid-design classification itself (A3) is near-perfect agreement (22/23 full
agreement) — both reviewers applied the review's 15-Oct standing rule consistently across all
nine studies it touches**, including the structurally distinct #1536 case (feeding type never a
trial design axis at all). The sole A3 disagreement (#1499) is a genuine, substantive one — see
Section 4, item 10 — precisely because #1499 is not a named hybrid-design study at all, so
neither reviewer had a standing rule to fall back on and each made an independent judgment call.

---

## 6. VDAART cross-check (#1547 / #1734 *Clostridium* contradiction)

**The cross-check passes: both drafts independently and correctly catch the same cross-study
contradiction, and both correctly agree with each other about what each paper found.**

#1547 (Savage 2018) and #1734 (Sordillo 2017) are sister ancillary-microbiome studies drawn from
the same VDAART trial, the same NIH grant (identical grant numbers), the same three U.S. sites,
overlapping authorship, and near-identical sample sizes (323 vs. 333). Within each paper's own
entry, both drafts report the same substantive finding for that paper:

- **#1547**: both drafts report *Clostridium* significantly **higher in breastfed** infants, and
  both quote the paper's own Introduction noting this contradicts the literature direction it
  cites ("breastfeeding has been shown to... decreased *Clostridium* spp... opposite findings are
  reported with formula feeding").
- **#1734**: both drafts report *Clostridiales*/*Clostridium*-related taxa **lower in breastfed**
  (the conventional-expectation direction), validated via the paper's own multivariate (MaAsLin)
  modeling, and both quote the paper's own Conclusion ("formula feeding was linked to higher
  levels of Clostridia in the infant gut").

Both drafts then independently flag the resulting **contradiction between the two papers** as one
of the single most important findings in the entire 23-study sample:

- Philip (#1734, Notes): "⚑⚑ **The single most informative internal contradiction in this entire
  23-study sample**: this paper found Clostridiales/*Clostridium*-related taxa **lower in
  breastfed** infants..., while its own sister paper #1547 found *Clostridium* **higher in
  breastfed** infants... from the same parent trial."
- Alaa (#1734, Notes): "**The single most consequential cross-study finding in this entire
  calibration sample:**... Two papers built on what may be the same underlying dataset report
  **opposite directions for the same taxon** in relation to the same exposure..."
- Alaa also makes the identical point a second time, independently, in her own closing
  cross-study-observations section (#1, titled "The single most important finding: a direct
  within-cohort contradiction on *Clostridium* direction") — written before reaching #1860,
  confirming this was not a one-off note but a conclusion Alaa's pass reached and restated.
- Philip's own closing cross-study-observations section (#4) makes the same point a second time
  as well, additionally cross-referencing #1860 (Bäckhed 2015) as a third, independent data point
  siding with #1734's direction — a synthesis move Alaa's draft does not make (Alaa's #1860 entry
  and cross-study observations never link #1860 back into the VDAART discussion).

**Score:** this is recorded as **E5 = FA (full agreement)** for #1734 in Section 3 — not because
the two *studies* agree with each other (they don't; that is the whole point of the finding), but
because the two *extractors* agree with each other about what each study independently found and
about the significance of the resulting contradiction. The methodology correctly distinguishes
"the extractors disagree about what a paper says" (which this is not) from "the paper itself
disagrees with another paper, and both extractors correctly caught it" (which this is) — exactly
the distinction the task asked this analysis to get right.

One genuine, minor difference worth noting: Alaa's #1547 entry (but not Philip's) explicitly flags
the VDAART cohort-overlap as a *protocol.md* "duplicate reports of the same cohort" concern the
review team should resolve, and raises an unresolved question about whether #1547/#1734 should
be classified as hybrid-design studies at all (since protocol.md's named list doesn't include
them) — a substantive methodological question Philip's parallel entries do not raise, though
Philip's entries do independently flag the sample-overlap/non-independence point in different
words ("These two studies must not be treated as independent evidence in any vote-counting or
meta-synthesis").
