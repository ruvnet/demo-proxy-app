const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/proxy/api/capitolai',
    createProxyMiddleware({
      target: 'http://localhost:8000/api/v1',
      changeOrigin: true,
      pathRewrite: {
        '^/proxy/api/capitolai': '', // This will remove the `/proxy/api/capitolai` part of the URL
      },
    })
  );
};