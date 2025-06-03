export default function ViewStep1({ username, onChange, onSubmit }) {
  return (
    <div className="step-container">
      <div className="step-content">
        <h1 className="step-title">What’s your Letterboxd username?</h1>
        <form onSubmit={onSubmit} className="step-form">
          <input
            type="text"
            placeholder="e.g. cinephile92"
            value={username}
            onChange={onChange}
            className="step-input"
          />
          <button type="submit" className="step-button">Next</button>
        </form>
      </div>
    </div>

  );
}
