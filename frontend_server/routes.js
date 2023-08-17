const express = require('express');

const router = express.Router();

router.get('/api/data', (req, res) => {
  const data = { name: 'John', age: 30 };
  res.json(data);
});

module.exports = router;
