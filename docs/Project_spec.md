## Project goal 
I want to develop a full-stack application calleld MemoryOS2. This app will ingest data such as customer interviews, bugs, 

## The Data, datamodel and databases - 
Sample data is stored in markdown files within a series of directories om the the data folder in the project directory. The data folder also contains a file `README.md` that describes the structure of each file, details of the metadata and a high level description of how the app should work (Section Ingestion Recommendation)


# Databases - 
We will use SQLite as the source of truth and Chromadb to store embeddings. Instantiate persistent versions of each of teh databases, create the tables in SQLite as described in README.md and leave them empty until prompted to read data. 


# Backend - 
* Use FastAPI/Python for the backend. Make sure you enable permissions thorugh the CORSMiddleware package. Keep permissions open for all methods and appropriate for local demos for now. 
* Create routes for the following - suggesst any other routes you deem necessary
	- Reading in Sample Data
	- Clear the databases
	- Handle the user question. 


# Frontend - 
* Create a component-based frontend in React. Use Tailwind to style. 
* Create a dark background with a color scheme that has a pastel hues. 
* Create a sidebar with two buttons stacked vertically - 
	- Read Data - Upon clicking the backend should read in sample data as descibed in README.md section Ingestion recommendatation. Data should only be read in if the databases are empty. 
	- Clear Data - Upon clicking, all data in the databases should be deleted. 
* Create a status bar at the bottom. All status messages should be displayed here - egs include "Successfully read in data" or "Successfully recived LLM information" or errors such as "Failed to read in data" or any exceptions. Exceptions and erros should be displayed in red font. 
* The main body of the document shall have 
	- Title 'OpsPilot' at the top. Have larger font than the rest. Pick an appropriate color scheme. 
	- A Text box to enter the Demo questions for the user. Allow user to submit the questions either by pressing Enter or by clicking the submit button. 
	- Submit button to the side of the textbox. This has the same effect as pressing Enter in the question text box. 
	- Next, there will be two components side-to-side
		a) an uneditable text area to show LLM output
		b) a list of uneditable cards - these will show the chunks of the body, ranked in order of relevance that were used to generate the LLM output
	- Next, there should be an uneditable text area . When the user clicks on one of the cards about, the app should fetch the document the chunk belongs to and display in this area. Put the focus on the chunk within the file if you can. 

## Geenral app operation
* The user enters the question in the textbox
* Create embedding for the question
* Search Chroma locally for similar chunks
* Get top 5-10 chunks
* Send only those chunks + question to OpenAI
* OpenAI writes answer using retrieved context

## Miscellaneous 
* Usee OpenAI as the LLM . The key will be supplied in a `.env` as an environment variable 'OPENAI_KEY`
* Implement a simple character-based chunker with configurable CHUNK_SIZE and CHUNK_OVERLAP constants. Do not use an external chunking library yet.