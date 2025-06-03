// src/views/ViewStep2.jsx
import SelectableCard from "../components/SelectableCard";

export default function ViewStep2({ genres, selectedGenre, onSelectGenre }) {
  return (
    <div className="step-container">
      <h2 className="step-subtitle">Step 1 of 3</h2>
      <h1 className="step-title">What do you feel like watching?</h1>
      <div className="step-grid">
        {genres.map((genre) => (
          <SelectableCard
            key={genre}
            label={genre}
            emoji="🎬"
            selected={selectedGenre === genre}
            onClick={() => onSelectGenre(genre)}
          />
        ))}
      </div>
    </div>
  );
}
