import React, { useState } from "react";
import { Container, Form, Button, Table, Card } from "react-bootstrap";

const CategorizeTrigger = () => {
  const [inputSequences, setInputSequences] = useState("");
  const [results, setResults] = useState([]);
  const [error, setError] = useState(""); // To show error messages

  // Function to calculate GC content
  const calculateGCContent = (sequence) => {
    const gCount = (sequence.match(/G/g) || []).length;
    const cCount = (sequence.match(/C/g) || []).length;
    const totalLength = sequence.length;
    const gcContent = ((gCount + cCount) / totalLength) * 100;
    return gcContent.toFixed(2); // Rounds to 2 decimal places
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    // Split input into an array of sequences
    const sequences = inputSequences
      .split(",")
      .map(seq => seq.trim()) // Trim whitespace
      .filter(seq => seq.length > 0); // Remove empty entries

    if (sequences.length === 0) {
      setError("Please enter at least one valid DNA sequence.");
      return;
    }

    if (sequences.length > 5) {
      setError("You can enter a maximum of 5 sequences.");
      return;
    }

    // Check each sequence for valid characters (CTAG)
    for (let i = 0; i < sequences.length; i++) {
      const sequence = sequences[i];
      if (!/^[CTAG]+$/.test(sequence)) {
        setError(`Sequence ${i + 1} contains invalid characters. Only 'C', 'T', 'A', and 'G' are allowed.`);
        return;
      }

      // Check if the sequence follows the correct format
      const regex = /^([CTAG]{10,15})([CTAG]{4})(GACTC)(T)([CTAG]{10,15})$/;
      if (!regex.test(sequence)) {
        setError(`Sequence ${i + 1} is not in the correct format. Please follow the format: 
        [10-15 trigger bases][4 random bases][GACTC (for cutting)][T][repeat trigger bases]`);
        return;
      }
    }

    // Clear any previous errors
    setError("");

    // Generate dummy stats (replace with real calculations later!!! GC content is good tho)
    const generatedResults = sequences.map((seq, index) => ({
      id: index + 1,
      sequence: seq,
      specificity: Math.floor(Math.random() * 30) + 70 + "%", // Random 70-99% specificity
      Tm: (Math.random() * 10 + 60).toFixed(2) + "°C", // Random 60-70°C
      gcContent: calculateGCContent(seq) + "%", // Calculate GC content
    }));

    // Sort by highest specificity
    const sortedResults = generatedResults.sort((a, b) =>
      parseInt(b.specificity) - parseInt(a.specificity)
    );

    setResults(sortedResults);
  };

  return (
    <Container className="mt-5 d-flex flex-column align-items-center">
      <h2 className="mb-4">Test Templates Sequences</h2>

      <p>Enter your DNA template sequences below. Ensure your sequences follow the format: <br/>
        <strong>[</strong>10-15 trigger bases<strong>]</strong>
        <strong>[</strong>4 random bases<strong>]</strong>
        <strong>[</strong>GACTC (for cutting)<strong>]</strong>
        <strong>[</strong>T<strong>]</strong>
        <strong>[</strong>repeat trigger bases<strong>]</strong>
      </p>

      <br></br>
      <p>For testing: GTCGACTAATGCCAGACTCTGTCGACTAAT,GCTTAGAGCTCGCTGACTCTGCTTAGAGCT,ACAGCCGTGCCCAAGACTCTACAGCCGTGC</p>

      {/* Error Message */}
      {error && <div className="alert alert-danger">{error}</div>}

      {/* Input Form */}
      <Form onSubmit={handleSubmit} className="w-50 p-4 border rounded shadow-sm bg-light">
        <Form.Group className="mb-3">
          <Form.Label>Enter Up to 5 Sequences (comma-separated):</Form.Label>
          <Form.Control
            type="text"
            value={inputSequences}
            onChange={(e) => setInputSequences(e.target.value)}
            required
            placeholder="Example: ATGCGA, TCGATC, AGGCTA"
          />
        </Form.Group>
        <Button variant="primary" type="submit" className="w-100">
          Categorize
        </Button>
      </Form>

      {/* Results Table */}
      {results.length > 0 && (
        <Card className="mt-4 w-75 shadow-sm">
          <Card.Body>
            <Card.Title>Ranked Template Analysis Results</Card.Title>
            <Table striped bordered hover>
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>Sequence</th>
                  <th>Specificity</th>
                  <th>Tm (°C)</th>
                  <th>GC Content</th>
                </tr>
              </thead>
              <tbody>
                {results.map((result, index) => (
                  <tr key={result.id}>
                    <td>{index + 1}</td>
                    <td>{result.sequence}</td>
                    <td>{result.specificity}</td>
                    <td>{result.Tm}</td>
                    <td>{result.gcContent}</td>
                  </tr>
                ))}
              </tbody>
            </Table>
          </Card.Body>
        </Card>
      )}
    </Container>
  );
};

export default CategorizeTrigger;

