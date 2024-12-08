import { Button } from "./components/ui/button";

function App() {
  return (
    <div className="flex justify-center items-center h-screen flex-col">
      <h1 className="text-3xl font-bold underline text-green-500">
        Hello world!
      </h1>
      <Button variant={"destructive"}>Submit</Button>
    </div>
  );
}

export default App;
