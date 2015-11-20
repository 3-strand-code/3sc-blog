var gulp = require('gulp');
var cp = require('child_process');
var runSequence = require('run-sequence');

gulp.task('default', function (cb) {
    runSequence(
        'serve',
        'existence',
        'kill-serve',
        cb
    );
});

gulp.task('serve', function (cb) {
    cp.exec('cd ./output && python -m SimpleHTTPServer 8080', function (err, stdout, stderr) {
        stdout && console.log(stdout);
        stderr && console.log(stderr);
    });
    cb();
});

gulp.task('existence', function (cb) {
    cp.exec('existence ./output', function (err, stdout, stderr) {
        stdout && console.log(stdout);
        stderr && console.log(stderr);
        cb();
    });
});

gulp.task('kill-serve', function (cb) {
    cp.exec('kill $(ps aux | grep -v grep |grep -i "python -m SimpleHTTPServer 8080" | awk \'{print $2;}\')',
        function (err, stdout, stderr) {
            stdout && console.log(stdout);
            stderr && console.log(stderr);
            cb();
        });
});
