const processRequest = async (path: string, method: string, data: any) => {
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');

    let response = await fetch(path, {
        headers,
        method: method,
        body: JSON.stringify(data),
        credentials: 'include'
    });

    return await response.json();
};

export default processRequest;