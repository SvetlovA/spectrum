import React from "react"

interface ChosePlotCoordinatesFileButtonProps {
    onChange?: (fileText: string) => void;
}

export const ChosePlotCoordinatesFileButton: React.FC<ChosePlotCoordinatesFileButtonProps> = (props: ChosePlotCoordinatesFileButtonProps) => {
    const handleChange = (event: any) => {
        const reader = new FileReader();
        reader.onload = async (e: any) => { 
            const text = e.target.result;
            console.log(text);
            props.onChange && props.onChange(text);
        };
        reader.readAsText(event.target.files[0]);
    };

    return <input type="file" accept=".txt" onChange={handleChange} />
}