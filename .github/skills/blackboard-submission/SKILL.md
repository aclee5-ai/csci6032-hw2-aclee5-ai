---
name: blackboard-submission
description: Safely prepare and, only with fresh student confirmation, submit this homework archive and repository URL to the Blackboard assignment page.
---

# Blackboard submission

Use this skill only for the `csci6032-hw2-aclee5-ai` homework repository. The workflow is deliberately fail-closed: do not continue past a failed check, do not infer consent from an earlier approval, and do not handle authentication information.

## Safety rules

- Confirm the repository identity before doing any submission work. The expected repository directory name is `csci6032-hw2-aclee5-ai`, and the expected remote URL is `https://github.com/aclee5-ai/csci6032-hw2-aclee5-ai.git`.
- Do not read, request, type, store, print, upload, or expose passwords, MFA codes, session cookies, access tokens, private keys, browser profiles, or other credentials. The student must authenticate personally in the browser.
- Do not open or control Blackboard until the student gives explicit permission in response to that specific request.
- Navigate only to the homework assignment's Blackboard submission page. Do not browse other courses, assignments, accounts, messages, or personal pages.
- Do not commit screenshots, receipts, browser data, downloaded pages, or personal information to the repository. Keep any temporary browser artifacts outside the repository and remove them when finished.
- Never use a general earlier approval as approval for the final submission. The final irreversible action requires a new, explicit confirmation after the exact staged payload is shown.
- If any check is ambiguous, stop and report the blocking condition rather than guessing.

## Inputs and expected artifacts

Set these values from the repository and the assignment instructions without embedding credentials:

- `EXPECTED_REPOSITORY_URL=https://github.com/aclee5-ai/csci6032-hw2-aclee5-ai.git`
- `ARCHIVE_NAME=csci6032-hw2-aclee5-ai.tar.gz`
- `NOTEBOOK_NAME=CSCI6032_hw2.ipynb`
- `ARCHIVE_PATH` must be outside the repository, or in an ignored temporary location that will not be committed.
- `SUBMISSION_TEXT` must contain only the repository URL and any assignment-required non-sensitive identifying text. Never include a password, token, cookie, student ID, or other personal information unless the student explicitly supplies non-sensitive assignment text for this purpose.

If the assignment requires a different notebook name or additional artifact, stop and ask the student to confirm the requirement before changing these values.

## Required workflow

### 1. Confirm the repository

Verify all of the following before preparing anything:

1. The current working directory resolves to the expected homework repository.
2. `git rev-parse --show-toplevel` succeeds.
3. The repository's canonical origin URL, normalized for an optional trailing slash and `.git`, matches `aclee5-ai/csci6032-hw2-aclee5-ai`.
4. The expected notebook exists at the repository root.

If the directory, repository identity, or notebook does not match, stop.

### 2. Run the preflight

Run a read-only preflight and show its results to the student. It must check:

- current branch name and `HEAD`;
- `git status --short` and whether the tracked worktree and index are clean;
- the five most recent commits;
- fetch and push remote URLs, with the expected origin URL;
- required files, including `CSCI6032_hw2.ipynb`, `README.md`, `src/text_stats.py`, and `tests/test_text_stats.py`;
- whether `HEAD` is a commit and whether the required notebook is tracked at `HEAD`;
- whether the current branch has an upstream and whether it is ahead of the upstream;
- tracked filenames and text for apparent credentials, private keys, personal browser data, or other private material.

Use a conservative secret scan that reports only filenames and the type of match, never matching content. Include checks for common token/password/private-key patterns and suspicious files such as `.env`, credential stores, browser profiles, key files, and cache directories. Treat any unresolved match as a blocker and ask the student to resolve it; do not redact-and-submit around it.

Stop if the tree is not clean, a required artifact is absent, `HEAD` is not the reviewed commit, the remote is unexpected, the branch is not pushed, or unresolved secrets/private data are apparent.

### 3. Confirm the reviewed branch is pushed

After the student identifies the branch and commit to review, verify that the exact local `HEAD` is reachable from the configured upstream or remote branch. If it is not pushed, explain that pushing changes repository state and ask for separate explicit permission before running `git push`. Never push with force or rewrite history. Re-run the clean-tree and exact-`HEAD` checks after any push.

### 4. Prepare the archive from committed `HEAD`

Create `csci6032-hw2-aclee5-ai.tar.gz` from the committed `HEAD`, not from the working directory:

```sh
git archive --format=tar --prefix=csci6032-hw2-aclee5-ai/ HEAD | gzip -n > "$ARCHIVE_PATH/csci6032-hw2-aclee5-ai.tar.gz"
```

Before using it, verify that the archive:

- contains only files tracked by `HEAD`;
- contains no `.git/` directory, credentials, private keys, caches, browser data, generated artifacts, or unrelated files;
- contains the required notebook and assignment source/test files;
- is readable and non-empty; and
- has the expected archive filename.

If any tracked file itself appears to contain unresolved secret or private data, stop rather than submitting it. Do not silently alter the committed content or create a second, unreviewed archive.

### 5. Show the exact proposed submission

List the archive contents without extracting them into the repository. Then show, exactly and in separate labeled blocks:

1. the notebook path that will be submitted inside the archive;
2. the archive path and byte size;
3. the repository URL;
4. the complete proposed submission text.

The displayed submission text must not contain credentials or newly discovered personal information. Stop if the archive contents or text differ from what the student reviewed.

### 6. Dry run

Support a `dry-run` mode. In dry-run mode, perform every possible local check above, including repository identity, clean status, commit and push verification, secret/private-data scan, archive creation in a temporary location, archive-content inspection, required-file checks, and exact payload display. Do not open Blackboard, open or control a browser tab, upload files, type into a page, or submit anything. State clearly that no Blackboard action occurred.

### 7. Request permission to open Blackboard

Only after the local preflight and archive checks pass, ask the student whether to open or control the Blackboard tab. Do not open Blackboard or use browser automation before receiving an affirmative response to this specific request. A dry-run result, permission to prepare the archive, or permission to push is not permission to open Blackboard.

### 8. Student authentication and constrained navigation

When permission is granted:

1. Open only the Blackboard homework submission page supplied by the student or assignment instructions.
2. If Blackboard asks for authentication, stop and hand control to the student. The student must authenticate personally.
3. Do not request, read, store, type, copy, or expose credentials or MFA codes.
4. After authentication, verify that the page is for this course and homework. If it is not unambiguously the correct page, stop.
5. Stage only the prepared archive and the repository URL in the required fields. Do not upload screenshots, receipts, browser data, or unrelated files.

Do not click the final Submit/Turn In/Confirm action during staging.

### 9. Final confirmation gate

Immediately before the irreversible submission action, stop and show the student exactly what Blackboard will receive:

- the assignment/course page identity;
- the archive filename, size, and complete archive listing;
- the repository URL;
- the exact text in every submission field;
- any Blackboard-visible metadata that will be sent.

Ask for a new, explicit confirmation such as: `Submit exactly this payload now?` A prior general approval is insufficient. If the student does not explicitly confirm, leave the page unsubmitted and stop.

### 10. Submit and verify

Only after that fresh confirmation, perform the final submission action. Verify the resulting confirmation page or receipt, including the assignment identity and any confirmation number or timestamp that Blackboard visibly provides. Report success only when the confirmation is actually present. If submission fails or the receipt is ambiguous, report the exact state without retrying blindly.

Do not save or commit Blackboard screenshots, receipts, browser profiles, cookies, downloaded pages, or personal information. Remove temporary local artifacts after verification, retaining only the intended archive if the student requests it and it is outside the public repository.
