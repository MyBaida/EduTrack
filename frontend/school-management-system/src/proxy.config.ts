var  defaultTarget = "http://127.0.0.1:8000/api/users/login";

module.exports = [
    {
        context: ['/api/**'],
        target: defaultTarget,
        secure: false
    }
]