const express = require('express');
const { Pool } = require('pg');
const redis = require('redis');
const cors =require('cors')

const app = express();
app.use(express.json());
app.use(cors());

// PostgreSQL connection
const pool = new Pool({ connectionString: process.env.DATABASE_URL });

// Redis connection
const cache = redis.createClient({ url: process.env.REDIS_URL });
cache.connect();

// Create table on startup
pool.query(`CREATE TABLE IF NOT EXISTS messages
  (id SERIAL PRIMARY KEY, text TEXT, created_at TIMESTAMPTZ DEFAULT NOW())`);

app.get('/', (req, res) => res.json({ status: 'ok', service: 'api' }));

// POST a message — saved to Postgres
app.post('/messages', async (req, res) => {
    const { text } = req.body;
    const result = await pool.query(
        'INSERT INTO messages (text) VALUES ($1) RETURNING *', [text]
    );
    await cache.del('messages');
    res.json(result.rows[0]);
});

// GET all messages — cached in Redis
app.get('/messages', async (req, res) => {
    const cached = await cache.get('messages');
    if (cached) return res.json({ source: 'cache', data: JSON.parse(cached) });
    const result = await pool.query('SELECT * FROM messages ORDER BY created_at DESC');
    await cache.set('messages', JSON.stringify(result.rows), { EX: 30 });
    res.json({ source: 'database', data: result.rows });
});

app.listen(3000, () => console.log('API running on port 3000'));