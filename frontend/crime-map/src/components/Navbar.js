import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';

const AppNavbar = () => {
    return (
        <Navbar bg="dark" variant="dark" expand="lg">
            <Navbar.Brand>Mapa Crimes</Navbar.Brand>
            <Navbar.Toggle aria-controls="app-navbar-collapse" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="ml-auto">
                    <LinkContainer to="/home">
                        <Nav.Link>Mapa</Nav.Link>
                    </LinkContainer>
                    <LinkContainer to="/estatisticas">
                        <Nav.Link>Estatísticas</Nav.Link>
                    </LinkContainer>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
};

export default AppNavbar;