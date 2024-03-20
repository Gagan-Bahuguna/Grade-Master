```
html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Font with JavaScript</title>
</head>
<body>
    <h1 id="myHeading">Hello, World!</h1>
    <button onclick="changeFont()">Change Font</button>

    <script>
        function changeFont() {
            var heading = document.getElementById("myHeading");
            heading.style.fontFamily = "Arial, sans-serif";
        }
    </script>
</body>
</html>
```