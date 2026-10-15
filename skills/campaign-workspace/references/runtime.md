# Open the workspace

The public skill includes `assets/campaign-workspace.html`, a standalone Folloze app with seven bundled webinar skills. Open it in a browser or use an AI tool that supports interactive HTML. The app supports text uploads, account CSVs, local browser progress, skill attachment, and campaign-record export.

Start empty. Company documents and account lists come from the participant's own approved workspace. Missing tools or documents stay visible; use manual exports and uploads when a connector is unavailable.

Use skill prepares a request containing the selected bundled skill's instructions and Markdown references. Copy it into the AI chat with the relevant approved context. Return named output files, review them, and upload them to the matching stage. Additional skill ZIP attachments retain instructions in browser mode; their supporting resources need a capable host or connector.

Folder access, campaign-file persistence, and automatic chat handoff require a separately installed compatible Campaign Workspace connector. If that connector is already available, use its exposed tools and configured source scope. Read [the result contract](result-contract.md) when recording connector results. Do not invent a connection or call tools that are absent.

Installing this skill does not install a connector, company documents, or third-party services. Keep credentials and participant data in the participant's private workspace. Test native rendering and handoff in the exact AI client before demonstrating them.
