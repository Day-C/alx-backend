// Node redis client

import ( createCleint } from 'redis';

const client = createClient();

async function nodeRedis() {
  try {
    await client.connect()
    console.log('Redis cleint connected to the server');
  } catch (error) {
    console.log('Redis client not connected to the server:', error);
  }
};

nodeRedis()
