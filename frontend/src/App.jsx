import { useState } from "react";
import axios from "axios";

function App() {

  const [file, setFile] = useState(null);

  const [results, setResults] = useState(null);

  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {

    if (!file) return;

    const formData = new FormData();

    formData.append("file", file);

    try {

      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/pcap/upload",
        formData
      );

      setResults(response.data);

    } catch (error) {

      console.error(error);

      alert("Upload failed");

    } finally {

      setLoading(false);
    }
  };

  return (

    <div className="min-h-screen bg-slate-900 text-white p-8">

      <h1 className="text-4xl font-bold mb-8">
        AI Network Troubleshooter
      </h1>

      <div className="bg-slate-800 p-6 rounded-xl mb-8">

        <input
          type="file"
          onChange={(e) =>
            setFile(e.target.files[0])
          }
          className="mb-4"
        />

        <button
          onClick={handleUpload}
          className="bg-blue-600 px-6 py-2 rounded-lg"
        >
          {loading ? "Analyzing..." : "Upload PCAP"}
        </button>
      </div>

      {results && (

        <div className="space-y-6">

          <div className="bg-slate-800 p-6 rounded-xl">

            <h2 className="text-2xl font-semibold mb-4">
              Packet Analysis
            </h2>

            <pre className="overflow-auto text-sm">
              {JSON.stringify(
                results.analysis,
                null,
                2
              )}
            </pre>
          </div>

          <div className="bg-slate-800 p-6 rounded-xl">

            <h2 className="text-2xl font-semibold mb-4">
              AI Diagnostic Report
            </h2>

            <div className="whitespace-pre-wrap">
              {results.ai_diagnostic_report}
            </div>

          </div>

        </div>
      )}

    </div>
  );
}

export default App;