"""This module defines project-level constants."""

UNITS = {
    "$ ^o $$ C $": ["T"],
    "$ psu $": ["S"],
    "$ tot $": ["pH"],
    "$ ppm $": ["pCO2"],
    "$ m $": ["r_bub"],
    "$ nd $": ["LimLight", "LimT", "LimN", "Om_Ar"],
    "$ μM$ $ d^- $$ ^1 $": [
        "CaCO3_form",
        "CaCO3_diss",
        "DOM_decay_ox",
        "DOM_decay_denitr",
        "POM_decay_ox",
    ],
    "$ d^- $ $^1 $": ["GrowthPhy", "GrazPhy", "GrazPOM"],
    "$ ng $ $ L^- $$ ^1 $": [
        "Ci_free",
        "Ci_phy",
        "Ci_het",
        "Ci_POM",
        "Ci_DOM",
        "Ci_biota",
        "Ci_tot_diss",
        "Ci_tot_part",
    ],
    "$ ng $ $ dm^- $$ ^2 $ $ d^- $$ ^1 $": [
        "fick:Ci_free",
        "fick:Ci_phy",
        "fick:Ci_het",
        "fick:Ci_POM",
        "fick:Ci_DOM",
        "sink:Ci_phy",
        "sink:Ci_het",
        "sink:Ci_POM",
    ],
    "$ ng $ $ L^- $$ ^1 $ $ d^- $$ ^1 $": [
        "Ci_tot_biodegrad",
        "Ci_tot_photolysis",
        "Ci_tot_hydrolysis",
    ],
    "$\\mu$$g$ $ kg^- $$ ^1 $": ["Ci_in_biota"],
}
