import { SelectionRange } from "plotly.js";
import React from "react"

interface ChosePlotCoordinatesFileButtonProps {
    onChange: (points: SelectionRange) => void;
}

export const ChosePlotCoordinatesFileButton: React.FC<ChosePlotCoordinatesFileButtonProps> = (props: ChosePlotCoordinatesFileButtonProps) => {
    const handleChange = (event: any) => {
        const reader = new FileReader();
        reader.onload = async (e: any) => { 
            const text = e.target.result;
            const coordinates = JSON.parse(text) as SelectionRange
            props.onChange(coordinates);
        };

        event?.target?.files?.length && reader.readAsText(event.target.files[0]);
    };

    return <input type="file" accept=".txt, .json" onChange={handleChange} />
}