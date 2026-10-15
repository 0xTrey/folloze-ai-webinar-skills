# Store and use the brain

Storage and AI access are separate choices. A company may approve a Drive folder without approving its contents for a particular AI tool. Confirm private-document use before reading or uploading it.

Select a read or save operation from the supplied tool map, following [tool-map-use.md](tool-map-use.md). Recheck that operation in the current workspace. Keep unavailable reads, write permissions, and charged operations distinct; use the manual path below when the selected operation is not usable.

## Choose a storage path

| Choice | If a connection is available and authorized | Manual fallback |
|---|---|---|
| Google Drive | Read only the named files or folder. Save the new brain only when a write tool exists and the participant has requested that destination. Read back saved contents. | Ask the participant to export approved Docs as text, Markdown, PDF, or Word and upload them here. Return Markdown files; have them create a `Company Brain` folder and upload the files. |
| OneDrive | Read only the named files or folder through an available authorized connection. Save and read back only with an authorized write tool. | Ask the participant to download approved Word, PowerPoint, PDF, or text files and upload them here. Return Markdown files for upload to a `Company Brain` folder in OneDrive. |
| Local folder | Read the chosen folder if the workspace permits it. Create a separate `company-brain` output folder; preserve source files. Read the output back. | Ask for uploaded copies or relevant approved excerpts. Return named Markdown blocks if file access or creation is unavailable; have the participant save each as a `.md` file. |

A pasted cloud link does not prove the assistant can read it. A synced Drive or OneDrive folder can use the local-folder path when authorized. Do not install a connector, broaden access, alter sharing, or move original documents to make a path work.

If a file is unreadable, request a readable export with page or section labels. If the participant cannot share it, record the missing decision and request an approved summary. Keep useful work moving from accessible sources.

## Load it in an approved AI workspace

If the workspace supports project files, attach `README.md`, the relevant core files, `source-manifest.md`, and `proof-and-claims.md`. Otherwise paste their contents into the task with filenames. A storage link alone may not provide retrieval access.

Use this prompt:

> Use the attached company brain for this task. Cite the source file and section behind key decisions. Use claims approved for this purpose. Keep inferred guidance labeled. If context is missing or conflicting, show the gap instead of inventing a fact. Task: {your marketing task}.

Check retrieval with:

> Name our audience, one voice rule, one product limit, and one held claim. Cite the brain file and source for each. If an item is missing, say so.

Inspect the answer against the files. Wrong or missing citations mean retrieval is not verified. Provide smaller relevant files or paste the needed sections, then retry the affected check.

Do not claim automatic discovery, persistent memory, or a live integration without checking it. This skill installs instructions; the resulting company brain is a separate set of context files.

## Maintain one current version

Agree on a review owner and cadence, such as monthly, then confirm the choice. Recheck affected sections after a product release, positioning change, audience change, new proof, or revised brand rule.

Keep source dates and owner decisions. Reapprove changed claims, retire superseded guidance, rerun affected tasks, and replace the workspace's old version deliberately. Do not change cloud permissions or delete older files without authorization.
