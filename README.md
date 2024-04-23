## Draw.io Diagrams Integration

### Introduction
This Odoo addon integrates Draw.io, a popular diagramming tool, into Odoo, allowing users to create and manage diagrams directly within the platform. This integration enhances the functionality of Odoo modules like Project Tasks and Helpdesk Tickets by providing a visual diagramming feature. The base module's abstraction allows developers to implement different ways of presenting and interacting with the diagramming tool and data.

### Features
- **Base Draw.io Diagram Module**: Establishes the core functionalities and setups for embedding Draw.io into Odoo.
- **Diagram Management**: Users can create, save, and load diagram versions directly associated with specific records in the Project Task and Helpdesk Ticket modules.
- **Automatic Diagram Versioning**: Diagrams are automatically versioned with a timestamp and associated with specific tasks or tickets for easy reference and management.
- **Diagram Visualization**: Users can view and interact with diagrams embedded in the task or ticket forms.

### Module Structure
This addon consists of several modules, each serving distinct purposes:
1. **base_draw_io**: The core module that embeds the Draw.io tool into Odoo and provides base functionalities.
2. **diagram_helpdesk_ticket**: Extends the Helpdesk Ticket module to include diagramming capabilities.
3. **diagram_project_task**: Integrates diagramming features into the Project Task module.

### Installation
1. Compatible with Odoo Community, Enterprise (helpdesk), and Odoo.sh
2. Copy the module directory into your Odoo addons directory.
3. Update the module list in the Odoo backend.
4. Install the base module and one of the diagram_* modules using the Odoo Apps interface.

### Usage
- **Project Task and Helpdesk Ticket Forms**: After installation, a new tab labeled "Diagrams" will appear in the form views of Project Tasks and Helpdesk Tickets.
- **Creating and Saving Diagrams**: Users can create diagrams directly in the form view. Once a diagram is saved, it is stored as a version linked to the specific record.
- **Loading Diagram Versions**: Users can load existing diagrams associated with the task or ticket from the diagram version history.

### Dependencies
- **Odoo Core Modules**: `project` for Project Tasks, `helpdesk` for Helpdesk Tickets.
- **base_draw_io**: Must be installed first as it provides the necessary infrastructure for other diagramming modules.

### License
- GPL-3

For more information and support, visit our [website](https://www.harrison.consulting).

### Contact
For support or inquiries, please create issues.

### Contributions
Contributions are welcome. Please send pull requests on GitHub.

This integration leverages the robust capabilities of Draw.io to enhance project management and support ticketing in Odoo by adding a visual dimension to task and issue tracking.