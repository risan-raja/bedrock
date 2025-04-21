# Ideas for email Ingestion

## Email Classification:
The system will classify incoming emails into the following categories:
 - Policy and Document Inquiry: Requests related to policies, assignments, or required documents.
 - Assignment Change Request: Emails requesting a change to a crew member’s assignment.
 - Document Submission: Emails where crew members are submitting required documents (e.g., passports).
 - Unclear or Emergency Requests: Emails that do not fall under the above categories or require immediate human intervention.

## Email Processing or Decisions
 - Cued Email Responses for Review:
   - For classified emails (Policy and Document Inquiry, Document Submission), the system will generate an automated response.
   - AI will access data from policies (PDFs, Word docs) and assignments (SQL database) to tailor the response.

 - Workflow Integration:
   - Automatically create tickets for Assignment Change Requests, which will be routed to the appropriate manager for review.
   - Provide escalation to human agents for emails classified as Unclear or Emergency.
 - Data Storage and Extraction:
   - Store incoming emails along with their classification in a database.
   - Extract data from submitted documents (e.g., passport details) and store it in a structured format for easy access.
 - Monitoring and Tracking:
   - Users can track the status of each email through the system.
   - A dashboard will allow the Crew Planning team to review emails, monitor AI classification accuracy, and track the progress of each email.


Email Classification Components
 1. Structured Metadata Extraction. {From, to, subject, date etc}
 2. Message Extraction
 3. Attachment Processing Queueue
 4. Document Identification + Text Classification -> Email Classification
 5. Prepopulate features from historical data.

```mermaid
flowchart TD
    A[Email Ingestion] --> B[Structured Metadata Extraction]
    A --> C[Attachment Processing Queue]
    A --> H[Message Extraction]
    C --> D[Document Identification]
    D --> E[Text Classification]
    E --> F[Email Classification]
    F --> G{Decision}
    G -->|Policy and Document Inquiry| H[Automated Response]
    G -->|Assignment Change Request| I[Create Ticket]
    G -->|Document Submission| J[Store Document]
    G -->|Unclear or Emergency| K[Escalate to Human Agent]

```