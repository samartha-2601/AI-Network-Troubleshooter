import { useState } from "react";
import axios from "axios";

import {
  Tooltip,
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
} from "recharts";

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

  const getSeverity = () => {
    if (!results) return "LOW";

    const failed =
      results.analysis.tcp_analysis?.possible_failed_connections || 0;

    if (failed > 1000) return "HIGH";
    if (failed > 100) return "MEDIUM";

    return "LOW";
  };

  const protocolData = results
    ? Object.entries(results.analysis.protocols).map(
        ([name, value]) => ({
          name,
          value,
        })
      )
    : [];

  const talkerData = results
    ? results.analysis.top_talkers.map(([ip, count]) => ({
        ip,
        count,
      }))
    : [];



  return (
    <div className="min-h-screen bg-slate-900 text-white p-8">
      <h1 className="text-4xl font-bold mb-8">
        AI Network Troubleshooter
      </h1>

      {/* Upload Section */}
      <div className="bg-slate-800 p-6 rounded-xl mb-8">
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
          className="mb-4"
        />

        <button
          onClick={handleUpload}
          className="bg-blue-600 hover:bg-blue-700 px-6 py-2 rounded-lg ml-4"
        >
          {loading ? "Analyzing..." : "Upload PCAP"}
        </button>
      </div>

      {results && (
        <div className="space-y-8">

          {/* KPI Cards */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">

            <div className="bg-slate-800 p-5 rounded-xl">
              <h3 className="text-slate-400">Total Packets</h3>
              <p className="text-3xl font-bold mt-2">
                {results.analysis.packet_count}
              </p>
            </div>

            <div className="bg-slate-800 p-5 rounded-xl">
              <h3 className="text-slate-400">Protocols</h3>
              <p className="text-3xl font-bold mt-2">
                {Object.keys(results.analysis.protocols).length}
              </p>
            </div>

            <div className="bg-slate-800 p-5 rounded-xl">
              <h3 className="text-slate-400">Failed TCP</h3>
              <p className="text-3xl font-bold mt-2">
                {
                  results.analysis.tcp_analysis
                    ?.possible_failed_connections
                }
              </p>
            </div>

            <div className="bg-slate-800 p-5 rounded-xl">
              <h3 className="text-slate-400">Severity</h3>

              <p
                className={`text-3xl font-bold mt-2 ${
                  getSeverity() === "HIGH"
                    ? "text-red-500"
                    : getSeverity() === "MEDIUM"
                    ? "text-yellow-400"
                    : "text-green-400"
                }`}
              >
                {getSeverity()}
              </p>
            </div>
          </div>

          {/* Charts */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

            {/* Protocol Distribution */}

            <div className="bg-slate-800 p-6 rounded-xl">

              <h2 className="text-2xl font-semibold mb-4">
                Protocol Distribution
              </h2>

              <ResponsiveContainer
                width="100%"
                height={350}
              >
                <BarChart
                  layout="vertical"
                  data={protocolData}
                  margin={{
                    top: 10,
                    right: 30,
                    left: 20,
                    bottom: 10,
                  }}
                >
                  <CartesianGrid strokeDasharray="3 3" />

                  <XAxis type="number" />

                  <YAxis
                    type="category"
                    dataKey="name"
                  />

                  <Tooltip />

                  <Bar
                    dataKey="value"
                    fill="#3b82f6"
                  />
                </BarChart>
              </ResponsiveContainer>

            </div>

            {/* Top Talkers */}
            <div className="bg-slate-800 p-6 rounded-xl">
              <h2 className="text-2xl font-semibold mb-4">
                Top Talkers
              </h2>

              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={talkerData}>
                  <CartesianGrid strokeDasharray="3 3" />

                  <XAxis dataKey="ip" />

                  <YAxis />

                  <Tooltip />

                  <Bar
                    dataKey="count"
                    fill="#3b82f6"
                  />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* DNS Queries */}
          <div className="bg-slate-800 p-6 rounded-xl">
            <h2 className="text-2xl font-semibold mb-4">
              DNS Queries
            </h2>

            <div className="flex flex-wrap gap-3">
              {results.analysis.dns_queries.map(
                (query, index) => (
                  <span
                    key={index}
                    className="bg-blue-600 px-3 py-2 rounded-lg"
                  >
                    {query}
                  </span>
                )
              )}
            </div>
          </div>

          {/* Potential Issues */}
          <div className="bg-slate-800 p-6 rounded-xl">
            <h2 className="text-2xl font-semibold mb-4">
              Potential Issues
            </h2>

            {results.analysis.potential_issues.length >
            0 ? (
              results.analysis.potential_issues.map(
                (issue, index) => (
                  <div
                    key={index}
                    className="bg-red-600 p-3 rounded-lg mb-2"
                  >
                    {issue}
                  </div>
                )
              )
            ) : (
              <p>No issues detected.</p>
            )}
          </div>

          {/* AI Diagnostic Report */}
          <div className="bg-slate-800 p-6 rounded-xl">
            <h2 className="text-2xl font-semibold mb-4">
              AI Diagnostic Report
            </h2>

            <div className="whitespace-pre-wrap leading-8">
              {results.ai_diagnostic_report}
            </div>
          </div>

        </div>
      )}
    </div>
  );
}

export default App;