import React from 'react';
import './HomePage.css';
import logo from './logo.svg';

interface HomePageProps {

}

export const HomePage: React.FC<HomePageProps> = (props: HomePageProps) => {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Specturm
                </p>
            </header>
        </div>
    );
};