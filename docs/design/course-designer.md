# Course Designer Tool - Project Plan v1.0

## Overview
An interactive course design tool for race officers to visually construct sailing courses by selecting marks from the existing marks database, with real-time map visualization and automatic course validation.

## Current State Analysis
- **Existing data**: 19 sailing marks in Dublin Bay with GPS coordinates, shapes, and colors
- **Course structure**: JSON format with course ID and mark sequence (some include rounding direction)
- **Course ID encoding**: First 2-3 digits represent wind angle (e.g., "021" = 20° wind angle)
- **Computation engine**: Existing functions for distance/bearing calculations and course length estimation

## Functional Requirements

### Core Features
1. **Interactive Course Builder**
   - Drag-and-drop interface to add marks to course sequence
   - Mark library showing all available marks with visual indicators
   - Course sequence editor with ability to reorder, add, remove marks
   - Rounding direction selector (Port/Starboard) for each mark

2. **Real-time Map Visualization**
   - Interactive map showing mark positions and current course path
   - Course legs drawn as lines between marks
   - Visual indicators for upwind legs and rounding directions
   - Zoom/pan capabilities for detailed course inspection

3. **Course Validation & Analytics**
   - Live course length calculation as marks are added
   - Wind angle analysis and leg classification (upwind/reaching/downwind)
   - Course balance validation (varied sailing angles)
   - Collision detection with land/hazards (future enhancement)

4. **Course Management**
   - Save new courses to courses.json
   - Load existing courses for editing
   - Course ID auto-generation based on wind conditions
   - Export course data for race instructions

### User Interface Components
1. **Mark Library Panel** - Grid of available marks with search/filter
2. **Course Builder Panel** - Current course sequence with edit controls
3. **Map Canvas** - Interactive map with marks and course visualization
4. **Properties Panel** - Course metadata (wind angle, length, notes)
5. **Action Bar** - Save, load, new, validate buttons

## Technical Architecture

### Frontend Framework
- **Web-based application** using modern JavaScript framework (React/Vue/Svelte)
- **Map library**: Leaflet.js or MapBox GL JS for interactive mapping
- **UI components**: Modern component library for consistent interface
- **State management**: Centralized store for course data and UI state

### Backend Integration
- **File I/O**: Read/write operations for marks.json and courses.json
- **Computation engine**: Leverage existing markmate.compute functions
- **API layer**: REST endpoints for course operations (CRUD)
- **Validation**: Server-side course validation and conflict checking

### Data Flow
1. Load marks from marks.json on application start
2. User constructs course through UI interactions
3. Real-time validation and calculation updates
4. Save validated course to courses.json
5. Generate course visualization and export options

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

### Web Application Options
1. **Standalone web app** - Separate application with its own server
2. **CLI integration** - Add web server capability to existing markmate tool
3. **Desktop application** - Electron wrapper for offline usage

### Map Visualization Libraries
- **Leaflet.js**: Open-source, lightweight, good marker/line support
- **MapBox GL JS**: Professional features, better performance, requires API key
- **OpenLayers**: Full-featured but complex

### Persistence Strategy
- **File-based**: Continue using JSON files (simple, matches existing pattern)
- **Database**: SQLite for better concurrent access and querying
- **Hybrid**: JSON for compatibility, optional database for advanced features

## Key Design Decisions Needed

1. **User Interface Framework**: React vs Vue vs Svelte vs vanilla JavaScript
2. **Map Provider**: Leaflet vs MapBox vs OpenLayers
3. **Deployment Model**: Standalone web app vs integrated CLI extension
4. **Styling Approach**: CSS framework vs custom styling
5. **Testing Strategy**: Unit tests, integration tests, user acceptance testing

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