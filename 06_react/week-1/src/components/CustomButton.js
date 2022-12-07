function CustomButton(props) {
    const { color, onclick, children } = props;
    if (color) {
        return (
            <button
                style={{ backgroundColor: color, color: "white" }}
                onClick={props.onClick}
            >
                {props.children}
            </button>
        );
    }
    return <button onClick={props.onClick}>{props.children}</button>;
}

export default CustomButton;