// Connector.ts
import React from 'react';
import { Root, createRoot } from 'react-dom/client';

export class ReactConnector {
    private root: Root;

    constructor(targetEl: HTMLElement, Component: React.ComponentType, props: any = {}) {
        this.root = createRoot(targetEl);
        this.render(Component, props);
    }

    render(Component: React.ComponentType, props: any = {}) {
        this.root.render(<Component {...props} />);
    }

    unmount() {
        this.root.unmount();
    }
}
