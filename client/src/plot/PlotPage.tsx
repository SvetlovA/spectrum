import React from 'react';
import Plot from 'react-plotly.js';
import { ChosePlotCoordinatesFileButton } from './ChosePlotCoordinatesFileButton';

interface PlotPageProps {

}

export const PlotPage: React.FC<PlotPageProps> = (props: PlotPageProps) => {

    return (
        <div>
            <Plot
                data={[
                    {
                        x: [1, 2, 3],
                        y: [2, 6, 3],
                        type: 'scatter',
                        mode: 'lines+markers',
                        marker: { color: 'red' },
                    }
                ]}
                layout={{ title: 'A Fancy Plot', autosize: true }}
                useResizeHandler={true}
                style={{ width: "100%", height: "100%" }}
            />
            <ChosePlotCoordinatesFileButton />
        </div>
    );
};