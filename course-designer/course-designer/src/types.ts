export interface Coordinate {
  deg: number;
  min: number;
}

export interface LatLong {
  lat: Coordinate;
  long: Coordinate;
}

export interface Mark {
  id: string;
  name: string;
  shape: string;
  color: string;
  lat: Coordinate;
  long: Coordinate;
}

export interface CourseMark {
  id: string;
  rounding?: 'P' | 'S';
}

export interface Course {
  id: string;
  marks: CourseMark[];
}

export interface MarkWithCoordinates extends Mark {
  position: [number, number];
}