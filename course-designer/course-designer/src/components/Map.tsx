import { useEffect } from 'react';
import { MapContainer, TileLayer, Marker, Polyline, useMap } from 'react-leaflet';
import { Icon, LatLngBounds } from 'leaflet';
import type { MarkWithCoordinates, Course, CourseMark } from '../types';
import { RoundingIndicator } from './RoundingIndicator';
import 'leaflet/dist/leaflet.css';



function getMarkColor(color: string): string {
  const colorMap: { [key: string]: string } = {
    'Black': '#000000',
    'Orange': '#FFA500',
    'Yellow': '#FFFF00',
    'Red': '#FF0000',
    'Green': '#008000',
    'Blue': '#0000FF',
    'White': '#FFFFFF'
  };
  return colorMap[color] || '#808080';
}

function createMarkIcon(mark: MarkWithCoordinates, isInCourse: boolean = false): Icon {
  const color = getMarkColor(mark.color);
  const size = isInCourse ? 12 : 8;
  
  const svgIcon = `
    <svg width="${size * 2}" height="${size * 2}" xmlns="http://www.w3.org/2000/svg">
      <circle cx="${size}" cy="${size}" r="${size - 1}" 
              fill="${color}" 
              stroke="#000" 
              stroke-width="1"/>
      <text x="${size}" y="${size + 3}" 
            text-anchor="middle" 
            font-size="8" 
            font-weight="bold" 
            fill="${color === '#FFFFFF' || color === '#FFFF00' ? '#000' : '#FFF'}">${mark.id}</text>
    </svg>
  `;
  
  return new Icon({
    iconUrl: `data:image/svg+xml;base64,${btoa(svgIcon)}`,
    iconSize: [size * 2, size * 2],
    iconAnchor: [size, size],
    popupAnchor: [0, -size]
  });
}

interface AutoFitBoundsProps {
  courseMarks: MarkWithCoordinates[];
}

function AutoFitBounds({ courseMarks }: AutoFitBoundsProps) {
  const map = useMap();

  useEffect(() => {
    if (courseMarks.length > 0) {
      const bounds = new LatLngBounds(courseMarks.map(mark => mark.position));
      map.fitBounds(bounds, { padding: [20, 20] });
    }
  }, [map, courseMarks]);

  return null;
}

interface MapProps {
  marks: MarkWithCoordinates[];
  selectedCourse: Course | null;
}

export function Map({ marks, selectedCourse }: MapProps) {
  const courseMarks: MarkWithCoordinates[] = [];
  const coursePath: [number, number][] = [];

  if (selectedCourse) {
    selectedCourse.marks.forEach((courseMark: CourseMark) => {
      const mark = marks.find(m => m.id === courseMark.id);
      if (mark) {
        courseMarks.push(mark);
        coursePath.push(mark.position);
      }
    });
  }

  const defaultCenter: [number, number] = marks.length > 0 
    ? [marks[0].position[0], marks[0].position[1]]
    : [53.42, -6.07];

  return (
    <MapContainer
      center={defaultCenter}
      zoom={13}
      style={{ height: '500px', width: '100%' }}
      className="rounded-lg"
    >
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      
      {marks.map((mark) => {
        const isInCourse = courseMarks.some(cm => cm.id === mark.id);
        return (
          <Marker
            key={mark.id}
            position={mark.position}
            icon={createMarkIcon(mark, isInCourse)}
          />
        );
      })}

      {coursePath.length > 1 && (
        <Polyline
          positions={coursePath}
          color="#FF0000"
          weight={3}
          opacity={0.8}
        />
      )}

      {selectedCourse && selectedCourse.marks.map((courseMark, index) => {
        const mark = marks.find(m => m.id === courseMark.id);
        const nextCourseMark = selectedCourse.marks[index + 1];
        const nextMark = nextCourseMark ? marks.find(m => m.id === nextCourseMark.id) : undefined;
        
        if (mark && courseMark.rounding) {
          return (
            <RoundingIndicator
              key={`rounding-${mark.id}-${index}`}
              mark={mark}
              rounding={courseMark.rounding}
              nextMark={nextMark}
            />
          );
        }
        return null;
      })}

      {courseMarks.length > 0 && (
        <AutoFitBounds courseMarks={courseMarks} />
      )}
    </MapContainer>
  );
}