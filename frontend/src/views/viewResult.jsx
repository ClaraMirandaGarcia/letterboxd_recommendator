// src/views/ViewResult.jsx
export default function ViewResult({ username, recommendation, onRestart }) {
  return (
    <div className="min-h-screen bg-black text-white flex flex-col items-center p-8">
      <h1 className="text-3xl font-bold mb-4">
        Here’s a recommendation for you, {username}!
      </h1>
      <p className="mb-6 text-center text-gray-400 max-w-xl">
        {recommendation.reason}
      </p>

      <div className="bg-gray-800 rounded-lg overflow-hidden shadow-lg mb-8 max-w-xs">
        <img
          src={recommendation.poster}
          alt={recommendation.title}
          className="w-full"
        />
        <div className="p-4 text-center">
          <h2 className="text-xl font-semibold">{recommendation.title}</h2>
          <a
            href={recommendation.link}
            target="_blank"
            rel="noopener noreferrer"
            className="text-blue-400 hover:underline mt-2 inline-block"
          >
            View on Letterboxd →
          </a>
        </div>
      </div>

      <button
        onClick={onRestart}
        className="text-sm text-gray-400 hover:underline"
      >
        ← Start over
      </button>
    </div>
  );
}
