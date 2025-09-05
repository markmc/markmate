import { useEffect } from 'react';
import { useMap } from 'react-leaflet';
import L from 'leaflet';
import type { MarkWithCoordinates } from '../types';

interface CoursePathWithArrowsProps {
  coursePath: [number, number][];
  courseMarks: MarkWithCoordinates[];
}

export function CoursePathWithArrows({ coursePath, courseMarks }: CoursePathWithArrowsProps) {
  const map = useMap();

  useEffect(() => {
    if (coursePath.length < 2) return;

    const layers: L.Layer[] = [];

    // Create lines with arrows and sequence numbers
    for (let i = 0; i < coursePath.length - 1; i++) {
      const start = coursePath[i];
      const end = coursePath[i + 1];
      
      // Create the line
      const polyline = L.polyline([start, end], {
        color: '#FF0000',
        weight: 3,
        opacity: 0.8
      });
      
      // Position arrow and number closer to source mark (1/3 along the line)
      const arrowLat = start[0] + (end[0] - start[0]) * 0.33;
      const arrowLng = start[1] + (end[1] - start[1]) * 0.33;
      
      // Calculate bearing for arrow rotation (from start to end)
      const bearing = calculateBearing(start, end);
      
      // Create arrow marker
      const arrowIcon = L.divIcon({
        html: `<div style="transform: rotate(${bearing - 90}deg); color: #FF0000; font-size: 16px; font-weight: bold;">➤</div>`,
        iconSize: [20, 20],
        iconAnchor: [10, 10],
        className: 'course-arrow'
      });
      
      const arrowMarker = L.marker([arrowLat, arrowLng], { icon: arrowIcon });
      
      // Create sequence number marker (closer to arrow position)
      const offsetDistance = 0.0005; // Much smaller offset
      const offsetBearing = bearing + 90; // Perpendicular to line direction
      const offsetPos = offsetCoordinate([arrowLat, arrowLng], offsetDistance, offsetBearing);
      
      const numberIcon = L.divIcon({
        html: `<div style="background: white; border: 2px solid #FF0000; border-radius: 50%; width: 20px; height: 20px; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: bold; color: #FF0000;">${i + 1}</div>`,
        iconSize: [20, 20],
        iconAnchor: [10, 10],
        className: 'course-sequence'
      });
      
      const numberMarker = L.marker(offsetPos, { icon: numberIcon });
      
      // Add to map and track for cleanup
      polyline.addTo(map);
      arrowMarker.addTo(map);
      numberMarker.addTo(map);
      
      layers.push(polyline, arrowMarker, numberMarker);
    }

    // Cleanup function
    return () => {
      layers.forEach(layer => map.removeLayer(layer));
    };
  }, [map, coursePath, courseMarks]);

  return null;
}

function calculateBearing(from: [number, number], to: [number, number]): number {
  const [lat1, lon1] = from;
  const [lat2, lon2] = to;
  
  const dLon = (lon2 - lon1) * Math.PI / 180;
  const lat1Rad = lat1 * Math.PI / 180;
  const lat2Rad = lat2 * Math.PI / 180;
  
  const y = Math.sin(dLon) * Math.cos(lat2Rad);
  const x = Math.cos(lat1Rad) * Math.sin(lat2Rad) - Math.sin(lat1Rad) * Math.cos(lat2Rad) * Math.cos(dLon);
  
  let bearing = Math.atan2(y, x) * 180 / Math.PI;
  return (bearing + 360) % 360;
}

function offsetCoordinate(position: [number, number], distance: number, bearing: number): [number, number] {
  const bearingRad = bearing * Math.PI / 180;
  const lat = position[0] + distance * Math.cos(bearingRad);
  const lng = position[1] + distance * Math.sin(bearingRad);
  return [lat, lng];
}