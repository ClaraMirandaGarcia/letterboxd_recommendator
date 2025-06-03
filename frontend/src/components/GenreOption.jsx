// src/components/GenreOption.jsx
export default function GenreOption({ label, selected, onClick }) {
  return (
    <div
      onClick={onClick}
      className={`genre-card ${selected ? "genre-card-selected" : ""}`}
    >
      <div className="genre-emoji">🎬</div>
      <div className="genre-label">{label}</div>
    </div>
  );
}
