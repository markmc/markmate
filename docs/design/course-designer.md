# Course Designer Tool - Project Plan v2.0

## Overview
A courses.json editor that allows race officers to define race infrastructure and create multiple sailing courses with real-time map visualization. The tool operates on a single courses.json file while using marks from the existing marks.json database.

## Current State Analysis
- **Existing data**: 19 sailing marks in Dublin Bay with GPS coordinates, shapes, and colors (immutable)
- **Course structure**: JSON format with course ID, True Wind Angle (TWA), and mark sequence
- **Race infrastructure**: Start point, finish point, and first upwind mark distance shared across all courses
- **Computation engine**: Existing functions for distance/bearing calculations and course length estimation

## Functional Requirements

### Core Features
1. **Race Infrastructure Setup**
   - Define start point coordinates (single GPS point)
   - Define finish point coordinates (single GPS point)
   - Set first upwind mark distance (default 0.5 nautical miles)
   - Infrastructure applies to all courses in the file

2. **Multi-Course Editor**
   - Create and edit multiple courses within single courses.json
   - Set True Wind Angle (TWA) for each course
   - Build mark sequences using drag-and-drop interface
   - Course sequence editor with reorder, add, remove capabilities
   - Rounding direction selector (Port/Starboard) for each mark

3. **Complete Race Visualization**
   - Interactive map showing: Start → First Upwind Mark → Course Marks → Finish
   - Course legs drawn as lines between all waypoints
   - Visual indicators for upwind legs and rounding directions
   - Mark library showing all available marks (read-only)
   - Zoom/pan capabilities for detailed course inspection

4. **Course Analytics & Validation**
   - Live course length calculation including all segments
   - Wind angle analysis using course TWA
   - Leg classification (upwind/reaching/downwind)
   - Course balance validation

5. **File Management**
   - Load existing courses.json for editing
   - Save complete race setup (infrastructure + all courses)
   - Data validation and integrity checking

### User Interface Components
1. **Infrastructure Panel** - Set start/finish coordinates and first upwind distance
2. **Course List Panel** - Manage multiple courses with add/delete/select
3. **Course Editor Panel** - Edit selected course (TWA, mark sequence, rounding)
4. **Mark Library Panel** - Grid of available marks from marks.json (read-only)
5. **Map Canvas** - Complete race visualization with all waypoints
6. **Properties Panel** - Course analytics (TWA, length, leg breakdown)
7. **Action Bar** - Save, load, validate, export buttons

## Technical Architecture

### Static Web Application Stack
- **Frontend**: React + TypeScript for type safety and developer experience
- **Styling**: Tailwind CSS for modern utility-first styling
- **Build System**: Vite for fast development and optimized production builds
- **IDE**: VS Code with standard React/TypeScript extensions
- **Map Library**: Leaflet.js for interactive mapping
- **Map Providers**: 
  - OpenStreetMap for coastline/street view
  - ESRI World Imagery for satellite view
  - Layer switcher for toggling between views

### Deployment Model
- **Static hosting**: GitHub Pages, Netlify, S3, or any static file server
- **Zero backend**: Pure client-side application
- **File bundling**: Ships with marks.json and template courses.json files
- **URL-based templates**: `?courses=tuesday-night.json` loads specific race format
- **Cross-platform**: Runs on any device with modern web browser

### Data Management
- **File I/O**: Browser-based file upload/download
- **Persistence**: Auto-save to localStorage with session management
- **Validation**: Strict JSON schema validation for uploaded files
- **Change Tracking**: Course-level modification indicators

### Data Structure
```json
{
  "start": {"lat": {"deg": 53, "min": 25.0}, "long": {"deg": -6, "min": 4.0}},
  "finish": {"lat": {"deg": 53, "min": 24.0}, "long": {"deg": -6, "min": 3.0}},
  "first_upwind_distance": 0.5,
  "courses": [
    {
      "id": "001",
      "twa": 45,
      "marks": [
        {"id": "W", "rounding": "P"},
        {"id": "I"}
      ]
    }
  ]
}
```

### Data Flow
1. Load marks.json (read-only reference data)
2. Load or create courses.json with infrastructure + courses
3. User edits race infrastructure and course definitions
4. Real-time visualization shows complete race: Start → First Upwind → Marks → Finish
5. Live calculations include all race segments
6. Save complete race setup to courses.json

## Implementation Phases

### Phase 1: Core Infrastructure
- Set up web application framework
- Create basic map visualization with static marks
- Implement mark library and course builder UI
- Basic course path rendering on map

### Phase 2: Interactive Features
- Drag-and-drop course construction
- Real-time course calculations
- Rounding direction controls
- Course validation feedback

### Phase 3: Advanced Features
- Course loading/editing capabilities
- Enhanced map controls and styling
- Wind analysis and course optimization suggestions
- Export functionality

### Phase 4: Polish & Integration
- User experience refinements
- Integration with existing markmate CLI
- Documentation and user guides
- Testing and bug fixes

## Technology Stack Considerations

### User Workflow
1. **Template Loading**: User clicks link with specific courses.json template
2. **Race Setup**: Configure infrastructure (start/finish points, upwind distance)
3. **Course Design**: Create multiple courses with TWA and mark sequences
4. **Visualization**: Real-time map showing complete race paths
5. **Collaboration**: Download courses.json, email to technical person
6. **Version Control**: Technical person loads file, reviews, commits to git

### Session Management
- **Change Indicators**: Visual markers for modified courses vs. original
- **Auto-save**: Browser localStorage prevents work loss
- **Fresh Start**: "New Race" clears session, loads template
- **Reset Options**: Revert individual courses or entire race setup
- **File Operations**: Load existing courses.json, download current state

### Map Visualization Requirements
- **Marine focus**: Minimal land detail, emphasis on coastline and water areas
- **Essential features**: Coastline, islands, navigation hazards
- **Course elements**: Mark positions, course paths, wind direction indicators
- **User controls**: Zoom, pan, layer switching (street/satellite)
- **Clean interface**: Nautical-appropriate styling with minimal distractions

## Technology Rationale

### Developer-Friendly Choices
- **React + TypeScript**: Industry standard, any JavaScript developer can contribute
- **Tailwind CSS**: Modern, popular utility-first approach
- **Vite**: Fast, modern build tool with excellent developer experience
- **VS Code**: Standard IDE with built-in TypeScript and React support
- **Leaflet**: Most popular open-source mapping library

### Static Deployment Benefits
- **No backend complexity**: Zero server infrastructure required
- **Universal hosting**: Works on any static file hosting service
- **Offline capable**: Functions after initial load
- **Version control friendly**: All code and data files in git
- **Cost effective**: Free hosting options available

## Success Criteria
- Race officers can construct courses 5x faster than manual editing
- Visual validation reduces course design errors by 90%
- All existing courses can be loaded and edited correctly
- New courses integrate seamlessly with existing markmate tools
- Tool is intuitive enough for non-technical race officers

## Risks & Mitigation
- **Complexity creep**: Start with MVP, iterate based on user feedback
- **Performance**: Optimize map rendering and calculations for smooth interaction
- **Browser compatibility**: Target modern browsers, provide graceful degradation
- **Data integrity**: Implement robust validation and backup mechanisms

## Next Steps
1. Review and refine requirements with stakeholders
2. Select technology stack and create proof-of-concept
3. Design detailed UI mockups and user flows
4. Set up development environment and project structure
5. Begin Phase 1 implementation

---
*This document will evolve as requirements are refined and implementation progresses.*