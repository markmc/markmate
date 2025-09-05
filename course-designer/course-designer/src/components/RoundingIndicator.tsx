import { useEffect } from 'react';
import { useMap } from 'react-leaflet';
import { DivIcon, LatLng } from 'leaflet';
import L from 'leaflet';
import type { MarkWithCoordinates } from '../types';

interface RoundingIndicatorProps {
  mark: MarkWithCoordinates;
  rounding: 'P' | 'S' | undefined;
  nextMark?: MarkWithCoordinates;
}

function createRoundingIcon(rounding: 'P' | 'S'): DivIcon {
  const arrow = rounding === 'P' ? '⭮' : '⭯';
  const color = rounding === 'P' ? '#00FF00' : '#FF0000';
  
  return new DivIcon({
    html: `<div style="color: ${color}; font-size: 16px; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.7);">${arrow}</div>`,
    iconSize: [20, 20],
    iconAnchor: [10, 10],
    className: 'rounding-indicator'
  });
}

export function RoundingIndicator({ mark, rounding, nextMark }: RoundingIndicatorProps) {
  const map = useMap();

  useEffect(() => {
    if (!rounding) return;

    const icon = createRoundingIcon(rounding);
    const position = new LatLng(mark.position[0], mark.position[1]);
    
    let offsetPosition = position;
    if (nextMark) {
      const bearing = calculateBearing(mark.position, nextMark.position);
      const offsetDistance = 0.001; // Small offset in degrees
      const offsetBearing = bearing + (rounding === 'P' ? -45 : 45);
      offsetPosition = offsetCoordinate(position, offsetDistance, offsetBearing);
    }

    const marker = L.marker(offsetPosition, { icon }).addTo(map);

    return () => {
      map.removeLayer(marker);
    };
  }, [map, mark, rounding, nextMark]);

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

function offsetCoordinate(position: LatLng, distance: number, bearing: number): LatLng {
  const bearingRad = bearing * Math.PI / 180;
  const lat = position.lat + distance * Math.cos(bearingRad);
  const lng = position.lng + distance * Math.sin(bearingRad);
  return new LatLng(lat, lng);
}