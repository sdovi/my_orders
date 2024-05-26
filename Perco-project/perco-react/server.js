const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());

app.use(express.json());  // Middleware для парсинга JSON-тел запросов

app.post('/user/email', (req, res) => {
  const { title, description } = req.body;
  console.log(`Email: ${title}, Comment: ${description}`);
  res.send('Email received');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
