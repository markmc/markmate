import type { Course } from '../types';

interface CourseSelectorProps {
  courses: Course[];
  selectedCourse: Course | null;
  onCourseChange: (course: Course) => void;
}

export function CourseSelector({ courses, selectedCourse, onCourseChange }: CourseSelectorProps) {
  const getTWA = (courseId: string): number => {
    const numericId = courseId.padStart(3, '0');
    return parseInt(numericId.slice(0, 2)) * 10;
  };

  return (
    <div className="mb-4">
      <label htmlFor="course-select" className="block text-sm font-medium mb-2">
        Select Course:
      </label>
      <select
        id="course-select"
        className="border border-gray-300 rounded px-3 py-2 min-w-48"
        value={selectedCourse?.id || ''}
        onChange={(e) => {
          const course = courses.find(c => c.id === e.target.value);
          if (course) onCourseChange(course);
        }}
      >
        <option value="">Select a course...</option>
        {courses.map((course) => (
          <option key={course.id} value={course.id}>
            Course {course.id} (TWA: {getTWA(course.id)}°)
          </option>
        ))}
      </select>
    </div>
  );
}