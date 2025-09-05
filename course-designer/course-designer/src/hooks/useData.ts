import { useState, useEffect } from 'react';
import type { Mark, Course, MarkWithCoordinates } from '../types';
import { coordinateToDecimal } from '../utils/coordinates';

export function useData() {
  const [marks, setMarks] = useState<MarkWithCoordinates[]>([]);
  const [courses, setCourses] = useState<Course[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadData = async () => {
      try {
        const baseUrl = import.meta.env.BASE_URL;
        const [marksResponse, coursesResponse] = await Promise.all([
          fetch(`${baseUrl}marks.json`),
          fetch(`${baseUrl}courses.json`)
        ]);

        if (!marksResponse.ok || !coursesResponse.ok) {
          throw new Error('Failed to fetch data');
        }

        const marksData: Mark[] = await marksResponse.json();
        const coursesData: Course[] = await coursesResponse.json();

        const marksWithPositions: MarkWithCoordinates[] = marksData.map(mark => ({
          ...mark,
          position: [
            coordinateToDecimal(mark.lat),
            coordinateToDecimal(mark.long)
          ] as [number, number]
        }));

        setMarks(marksWithPositions);
        setCourses(coursesData);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error');
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  return { marks, courses, loading, error };
}