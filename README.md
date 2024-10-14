# AllPrompt

AllPrompt is a web application that allows users to discover and copy high-quality prompts for AI projects. With a user-friendly interface and a vast collection of prompts, AllPrompt aims to enhance creativity and productivity for AI enthusiasts and professionals alike.

## Features

- **Extensive Prompt Collection**: Access a curated database of diverse prompts for various AI applications.
- **Easy Search**: Quickly find relevant prompts using our efficient search functionality.
- **User-Friendly Interface**: Navigate through prompts with a clean, intuitive design.
- **Copy with One Click**: Easily copy any prompt to your clipboard with a single button press.
- **Responsive Design**: Enjoy a seamless experience across desktop and mobile devices.
- **Pagination**: Browse through our extensive collection with convenient page navigation.
- **Expandable Cards**: View prompt details with expandable card functionality.

## Getting Started

### Prerequisites

- Node.js (v14 or later)
- npm (v6 or later)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/ligj1706/allprompts.git
   cd allprompts
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Prepare the prompt data:
   - Ensure you have a `prompts.csv` file in the project root with columns: `actor` and `prompt`.
   - Run the conversion script:
     ```
     python convert.py
     ```

4. Start the development server:
   ```
   npm run dev
   ```

5. Open your browser and visit `http://localhost:5173` to view the application.

### Building for Production

To create a production build:

```
npm run build
```

The built files will be in the `dist` directory.

## Usage

1. Use the search bar at the top of the page to find specific prompts.
2. Browse through prompts using the pagination controls at the bottom of the page.
3. Click the "Expand" button on a prompt card to view the full content.
4. Use the "Copy" button to copy a prompt to your clipboard.

## Contributing

We welcome contributions to AllPrompt! Here's how you can help:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

If you have prompts to contribute, please email them to mscreate358@gmail.com.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For any inquiries or copyright issues, please contact mscreate358@gmail.com.

---

Find your perfect prompt in one click with AllPrompt!