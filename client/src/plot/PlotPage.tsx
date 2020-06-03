import React from 'react';
import Plot from 'react-plotly.js';

interface PlotPageProps {

}

export const PlotPage: React.FC<PlotPageProps> = (props: PlotPageProps) => {
    return (
        <Plot
            data = {[
                {
                  x: [1, 2, 3],
                  y: [2, 6, 3],
                  type: 'scatter',
                  mode: 'lines+markers',
                  marker: {color: 'red'},
                }
            ]}
            layout={ {width: 320, height: 240, title: 'A Fancy Plot'} }
        />
    );
};