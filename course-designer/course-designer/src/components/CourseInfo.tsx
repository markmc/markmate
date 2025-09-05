import type { MarkWithCoordinates, Course } from '../types';
import { calculateDistance } from '../utils/coordinates';

interface CourseInfoProps {
  selectedCourse: Course | null;
  marks: MarkWithCoordinates[];
}

export function CourseInfo({ selectedCourse, marks }: CourseInfoProps) {
  if (!selectedCourse) return null;

  const getTWA = (courseId: string): number => {
    const numericId = courseId.padStart(3, '0');
    return parseInt(numericId.slice(0, 2)) * 10;
  };

  const calculateCourseDistance = (): number => {
    if (!selectedCourse || selectedCourse.marks.length < 2) return 0;

    let totalDistance = 0;
    
    for (let i = 0; i < selectedCourse.marks.length - 1; i++) {
      const currentMarkId = selectedCourse.marks[i].id;
      const nextMarkId = selectedCourse.marks[i + 1].id;
      
      const currentMark = marks.find(m => m.id === currentMarkId);
      const nextMark = marks.find(m => m.id === nextMarkId);
      
      if (currentMark && nextMark) {
        const distance = calculateDistance(
          currentMark.position[0],
          currentMark.position[1],
          nextMark.position[0],
          nextMark.position[1]
        );
        totalDistance += distance;
      }
    }
    
    return totalDistance;
  };

  const distance = calculateCourseDistance();
  const twa = getTWA(selectedCourse.id);

  return (
    <div className="bg-gray-100 p-4 rounded-lg mb-4">
      <h3 className="font-bold text-lg mb-2">Course {selectedCourse.id}</h3>
      <div className="space-y-1">
        <p><span className="font-medium">TWA:</span> {twa}°</p>
        <p><span className="font-medium">Distance:</span> {distance.toFixed(2)} nautical miles</p>
        <p>
          <span className="font-medium">Marks:</span>{' '}
          {selectedCourse.marks.map((courseMark, index) => (
            <span key={index}>
              {index > 0 && ' → '}
              <span 
                className={courseMark.rounding === 'S' ? 'text-green-600 underline font-semibold' : ''}
              >
                {courseMark.id}
              </span>
            </span>
          ))}
        </p>
      </div>
    </div>
  );
}