import express from "express";

const app = express();

app.get("/hello", (req, res) => res.send({ hi: "there", general: "kenobi" }));

app.get("*", (req, res) => {
  res.render("index");
});

app.listen(443);

export default app;
