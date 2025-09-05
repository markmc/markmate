import { useState } from 'react';
import { useData } from './hooks/useData';
import { CourseSelector } from './components/CourseSelector';
import { Map } from './components/Map';
import { CourseInfo } from './components/CourseInfo';
import type { Course } from './types';

function App() {
  const { marks, courses, loading, error } = useData();
  const [selectedCourse, setSelectedCourse] = useState<Course | null>(null);

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading course data...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center text-red-600">
          <h2 className="text-xl font-bold mb-2">Error Loading Data</h2>
          <p>{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            Course Designer - POC
          </h1>
          <p className="text-gray-600">
            Visualize sailing courses with marks, distances, and rounding indicators
          </p>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-1 space-y-6">
            <CourseSelector
              courses={courses}
              selectedCourse={selectedCourse}
              onCourseChange={setSelectedCourse}
            />
            
            <CourseInfo
              selectedCourse={selectedCourse}
              marks={marks}
            />
          </div>

          <div className="lg:col-span-2">
            <div className="bg-white p-4 rounded-lg shadow">
              <h2 className="text-xl font-semibold mb-4">Course Map</h2>
              <Map marks={marks} selectedCourse={selectedCourse} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
