import './App.css';
import {useState} from 'react';
import { CapitolAiWrapper, CreateStory, EditorStory } from '@capitol.ai/react';

const App = () => {
  const [storyId, setStoryId] = useState(null);
  return (
    <CapitolAiWrapper>
      {!storyId
        ? <CreateStory callbackOnSubmit={setStoryId} /> 
        : <EditorStory storyId={storyId} />
      }
    </CapitolAiWrapper>
  );  
};

export default App;
