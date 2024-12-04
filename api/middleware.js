const rateLimit = require('express-rate-limit');
const { createHash } = require('crypto');

// 创建访问令牌
function generateToken(req) {
  const data = `${req.ip}-${new Date().toDateString()}`;
  return createHash('sha256').update(data).digest('hex');
}

// 设置访问频率限制
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15分钟
  max: 100, // 限制每个IP 15分钟内最多100次请求
  message: 'Too many requests from this IP, please try again later.',
  standardHeaders: true,
  legacyHeaders: false,
});

// 验证请求来源
function validateOrigin(req, res, next) {
  const referer = req.get('Referer');
  if (!referer || !referer.includes('allprompt.club')) {
    return res.status(403).json({ error: 'Access denied' });
  }
  next();
}

// 混淆数据
function obfuscateData(data) {
  return data.map(item => ({
    ...item,
    id: Buffer.from(item.id.toString()).toString('base64'),
    prompt: item.prompt.length > 200 
      ? item.prompt.substring(0, 200) + '...' 
      : item.prompt
  }));
}

module.exports = {
  limiter,
  validateOrigin,
  obfuscateData,
  generateToken
};
