#!/usr/bin/env node
/**
 * Convert SVG diagrams to PNG at 300 DPI using sharp (Node.js)
 */
const fs = require('fs');
const path = require('path');

// Check if sharp is available
let sharp;
try {
    sharp = require('sharp');
} catch (e) {
    console.error('Error: sharp module not found');
    console.error('Please install it with: npm install -g sharp-cli');
    console.error('Or use: npx sharp-cli input.svg -o output.png --density 300');
    process.exit(1);
}

async function svgToPng(svgPath, pngPath, dpi = 300) {
    try {
        // Read SVG file
        const svgBuffer = fs.readFileSync(svgPath);

        // Convert to PNG with specified DPI
        await sharp(svgBuffer, { density: dpi })
            .png()
            .toFile(pngPath);

        console.log(`✓ Created: ${path.basename(pngPath)}`);
        return true;
    } catch (error) {
        console.error(`✗ Error converting ${path.basename(svgPath)}: ${error.message}`);
        return false;
    }
}

async function convertAllSvgs() {
    const baseDir = '/Users/Gyber/GYBER_EXPERIMENT_DOCS/diagrams';

    // Find all SVG files recursively
    function findSvgFiles(dir) {
        let results = [];
        const items = fs.readdirSync(dir);

        for (const item of items) {
            const fullPath = path.join(dir, item);
            const stat = fs.statSync(fullPath);

            if (stat.isDirectory()) {
                results = results.concat(findSvgFiles(fullPath));
            } else if (item.endsWith('.svg')) {
                results.push(fullPath);
            }
        }

        return results;
    }

    const svgFiles = findSvgFiles(baseDir);

    if (svgFiles.length === 0) {
        console.log('No .svg files found');
        return;
    }

    console.log(`Found ${svgFiles.length} SVG diagram(s) to convert\n`);

    let successCount = 0;
    for (const svgFile of svgFiles) {
        console.log(`Processing: ${path.basename(svgFile)}`);

        const pngFile = svgFile.replace(/\.svg$/, '.png');

        if (await svgToPng(svgFile, pngFile, 300)) {
            successCount++;
        }

        console.log();
    }

    console.log(`Conversion complete: ${successCount}/${svgFiles.length} succeeded`);
}

convertAllSvgs().catch(err => {
    console.error('Error:', err);
    process.exit(1);
});
