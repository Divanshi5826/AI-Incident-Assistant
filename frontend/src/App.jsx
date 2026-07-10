import { useState } from 'react'

const API_URL =
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000/ask";

function SourceBadge({ source }) {
  return (
    <span className="inline-flex items-center rounded-full border border-accent-100 bg-accent-50 px-3 py-1 text-sm font-medium text-accent-700">
      {source}
    </span>
  )
}

function Spinner() {
  return (
    <div className="inline-flex items-center gap-3 text-sm font-medium text-accent-700">
      <span className="h-4 w-4 animate-spin rounded-full border-2 border-accent-200 border-t-accent-600" />
      Searching knowledge base...
    </div>
  )
}

export default function App() {
  const [query, setQuery] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  async function handleAnalyze(event) {
    event.preventDefault()

    const cleanQuery = query.trim()
    if (!cleanQuery) {
      setError('Please enter an incident description before analyzing it.')
      setResult(null)
      return
    }

    setLoading(true)
    setError('')
    setResult(null)

    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: cleanQuery }),
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data?.detail || 'Something went wrong while analyzing the incident.')
      }

      setResult(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unexpected error occurred.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="min-h-screen bg-slate-50 text-slate-900">
      <div className="mx-auto flex min-h-screen w-full max-w-5xl flex-col px-4 py-10 sm:px-6 lg:px-8">
        <section className="mb-8 rounded-3xl border border-slate-200 bg-white p-6 shadow-soft sm:p-8">
          <div className="max-w-3xl">
            <p className="mb-3 inline-flex rounded-full bg-accent-50 px-3 py-1 text-sm font-semibold text-accent-700">
              Incident Intelligence
            </p>
            <h1 className="text-3xl font-bold tracking-tight text-slate-900 sm:text-4xl">
              AI Incident Assistant
            </h1>
            <p className="mt-3 text-base leading-7 text-slate-600 sm:text-lg">
              Analyze software incidents using Retrieval-Augmented Generation (RAG).
            </p>
          </div>
        </section>

        <section className="grid gap-6 lg:grid-cols-[1.15fr_0.85fr]">
          <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-soft sm:p-8">
            <form onSubmit={handleAnalyze} className="space-y-4">
              <div>
                <label htmlFor="incident-query" className="mb-2 block text-sm font-semibold text-slate-700">
                  Incident description
                </label>
                <textarea
                  id="incident-query"
                  value={query}
                  maxLength={500}
                  onChange={(event) => setQuery(event.target.value)}
                  placeholder={'Example:\n"Login API returning 401 Unauthorized"'}
                  className="min-h-56 w-full rounded-2xl border border-slate-300 bg-slate-50 px-4 py-4 text-base text-slate-900 outline-none transition placeholder:text-slate-400 focus:border-accent-400 focus:bg-white focus:ring-4 focus:ring-accent-100"
                />
              </div>

              <button
                type="submit"
                disabled={loading}
                className="inline-flex items-center justify-center rounded-2xl bg-accent-600 px-6 py-3 text-base font-semibold text-white shadow-sm transition hover:bg-accent-700 disabled:cursor-not-allowed disabled:opacity-70"
              >
                {loading ? 'Analyzing...' : 'Analyze Incident'}
              </button>

              {loading ? <Spinner /> : null}

              {error ? (
                <div className="rounded-2xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
                  {error}
                </div>
              ) : null}
            </form>
          </div>

          <div className="space-y-6">
            <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-soft sm:p-8">
              <h2 className="text-lg font-semibold text-slate-900">Result</h2>
              <div className="mt-4 space-y-5">
                <div>
                  <p className="text-sm font-medium uppercase tracking-wide text-slate-500">Question</p>
                  <p className="mt-1 text-base text-slate-900">
                    {result?.question || 'Your question will appear here.'}
                  </p>
                </div>

                <div>
                  <p className="text-sm font-medium uppercase tracking-wide text-slate-500">Answer</p>
                  <p className="mt-1 whitespace-pre-wrap text-base leading-7 text-slate-700">
                    {result?.answer || 'The assistant response will appear here after analysis.'}
                  </p>
                </div>
              </div>
            </div>

            <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-soft sm:p-8">
              <h2 className="text-lg font-semibold text-slate-900">Sources</h2>
              <div className="mt-4 flex flex-wrap gap-2">
                {result?.sources?.length ? (
                  result.sources.map((source) => <SourceBadge key={source} source={source} />)
                ) : (
                  <p className="text-sm text-slate-500">Retrieved source files will appear here.</p>
                )}
              </div>
            </div>
          </div>
        </section>
      </div>
    </main>
  )
}
