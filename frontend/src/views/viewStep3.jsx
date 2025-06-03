// src/views/ViewStep3.jsx
import SelectableCard from "../components/SelectableCard";

export default function ViewStep3({
  era,
  density,
  setEra,
  setDensity,
  handleSubmit,
  handleBack,
  eras,
  densities,
  genre
}) {
  return (
    <div className="step-container">
      <h2 className="step-subtitle">Step 2 & 3 of 3 — {genre}</h2>
      <h1 className="step-title">What era are you in the mood for?</h1>

      <div className="step-grid">
        {eras.map((option) => (
          <SelectableCard
            key={option}
            label={option}
            emoji="📽️"
            selected={era === option}
            onClick={() => setEra(option)}
          />
        ))}
      </div>

      {era && (
        <>
          <h1 className="step-title">And how heavy do you want it?</h1>
          <div className="step-grid">
            {densities.map((option) => (
              <SelectableCard
                key={option}
                label={option}
                emoji="🍿"
                selected={density === option}
                onClick={() => setDensity(option)}
              />
            ))}
          </div>
        </>
      )}

      <div className="flex justify-between w-full max-w-3xl mt-8">
        <button onClick={handleBack} className="text-sm text-gray-400 hover:underline">
          ← Back
        </button>
        {era && density && (
          <button
            onClick={handleSubmit}
            className="bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700 transition"
          >
            Show me the movie 🎬
          </button>
        )}
      </div>
    </div>
  );
}
