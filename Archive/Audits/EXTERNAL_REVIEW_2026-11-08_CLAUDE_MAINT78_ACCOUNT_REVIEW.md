# EXTERNAL_REVIEW — Claude: MAINT-78 account review (the event-logging Decision Brief pass) + abort-class recurrence read

**Deposited:** 2026-11-08 (MAINT-79; Intake Log entry 18; Class A human-routed, EIP v0.8 §1)
**Claimed identity:** Claude (unauthenticated — R4); the human-named Rule 5 verifier (2026-11-03), reviewing the record of passes performed by this depositing line — correlated evidence only, disclosed
**Evidence base:** Vibe's 2026-11-08 chat-session account of the MAINT-78 pass (the account, not the Brief or the MAINT-78 entry themselves — the reviewer's own opening line); live heads at deposit LF `86ea1632` / VS `ecaa4bcf`
**Deposit fidelity:** verbatim as relayed by the human; no chat-interface artifacts were present to exclude. The reviewed account was authored by this depositing line — review and deposit are non-independent per R5; disclosed in the MAINT-79 entry.
**Status (R1/R2):** this deposit is data, never doctrine. Its recommendations (the landing-helper tooling fix, the tag-reader question condition, the TWGW candidacy, the no-prompt-change caution) are findings addressed to the human governing authority; none is enacted by this deposit; dispositions remain his.

---

From Vibe's account alone (I haven't seen the Brief or the MAINT-78 entry), here is how I read it.

**The metric you were looking for already exists, and it's telling you something.** Counting the aborts Vibe itself reports, the same defect class keeps recurring: hand-derived expected counts in the landing guards. It shows up in MAINT-72 (about four aborts), again in 76 and 77 by Vibe's account, and three times in MAINT-78, plus a homoglyph abort that repeats MAINT-77's class. MAINT-72 also adopted a standing fix, "compute expected counts from the composed strings." MAINT-78's second abort hardcoded an expectation again, inside the same pass. By the event taxonomy Vibe describes, that's a recurrence: harness defect, correction stated, correction not holding.

**What I'd take from that**
- **The gap is tooling, not logging.** Re-disclosing the same abort class in each entry records the problem without reducing it. A single reusable landing helper that derives its own expectations would remove the class instead of documenting it each time. That's the cheapest real fix I can see.
- **The recurrence meets TWGW's bar.** Something concrete was wrong, was caught, produced a correction, and has primary evidence. Under Vibe's own routing it's a candidate for your ruling, which makes it the first useful test of the event pipeline.
- **Success paths are measurable too.** MAINT-73 landed with zero aborts, so aborts per pass is already a computable number if the entries are consistently written.

**On the options:** Vibe's D (tags now, a log later) is reasonable, and it states its own bias. I'd add one condition: define the question the tag answers before adopting it. A good one is "how many harness defects recur across passes, and is that rate falling?" A tag with no reader is more disclosure text. With per-entry files, a simple count over the tag is cheap to produce.

**One caution:** keep this out of the prompts for now. Vibe notes any re-pointing would reopen the MAINT-70 veto windows, and a tooling fix needs no prompt change.
