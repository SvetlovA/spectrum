import { SelectionRange } from 'plotly.js';
import React, { useState } from 'react';
import { Button } from 'react-bootstrap';
import Plot from 'react-plotly.js';
import { ChosePlotCoordinatesFileButton } from './ChosePlotCoordinatesFileButton';

interface PlotPageProps {

}

export const PlotPage: React.FC<PlotPageProps> = (props: PlotPageProps) => {
    const [selectionRange, setSelectionRange] = useState({} as SelectionRange);
    return (
        <>
            <Plot
                data={[
                    {
                        x: selectionRange.x,
                        y: selectionRange.y,
                        type: 'scatter',
                        mode: 'lines+markers',
                        marker: { color: 'red' },
                    }
                ]}
                layout={{ title: 'Haar transform', autosize: true }}
                useResizeHandler={ true }
                style={{ width: '100%', height: '100%' }}
            />
            <ChosePlotCoordinatesFileButton onChange={coordinates => setSelectionRange(coordinates)} />
            <Button variant='primary'>Filter</Button>
        </>
    );
};