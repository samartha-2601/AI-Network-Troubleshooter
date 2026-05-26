import { useEffect, useState } from "react";

import axios from "axios";

function History() {

  const [history, setHistory] = useState([]);

  const fetchHistory = async () => {

    try {

      const response = await axios.get(
        "http://127.0.0.1:8000/history/"
      );

      setHistory(response.data);

    } catch (error) {

      console.error(error);
    }
  };

  useEffect(() => {

    fetchHistory();

  }, []);

  const severityColor = (severity) => {

    if (severity === "HIGH")
      return "text-red-500";

    if (severity === "MEDIUM")
      return "text-yellow-400";

    return "text-green-400";
  };

  const downloadReport = (reportId) => {

    window.open(
      `http://127.0.0.1:8000/reports/${reportId}`,
      "_blank"
    );
  };

  return (

    <div>

      <h1 className="text-4xl font-bold mb-8">
        Analysis History
      </h1>

      <div className="bg-slate-800 p-6 rounded-xl">

        {history.length === 0 ? (

          <p>No analysis history found.</p>

        ) : (

          <div className="space-y-3">

            {history.map((item) => (

              <div
                key={item.id}
                className="
                  bg-slate-700
                  p-4
                  rounded-lg
                  flex
                  justify-between
                  items-center
                "
              >

                <div>

                  <div className="font-semibold">
                    {item.filename}
                  </div>

                  <div className="text-sm text-slate-400 mb-2">
                    {item.packet_count} packets
                  </div>

                  <button
                    onClick={() =>
                      downloadReport(item.id)
                    }
                    className="
                      bg-green-600
                      hover:bg-green-700
                      px-3
                      py-1
                      rounded-lg
                      text-sm
                    "
                  >
                    Download PDF
                  </button>

                </div>

                <div
                  className={`font-bold text-lg ${severityColor(
                    item.severity
                  )}`}
                >
                  {item.severity}
                </div>

              </div>

            ))}

          </div>

        )}

      </div>

    </div>

  );
}

export default History;