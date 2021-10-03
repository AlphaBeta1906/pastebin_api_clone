class Car extends React.Component {
  render() {
    return <h2>Hi, I am a Car!</h2>;
  }
}


function Hello() {
    const [inputs,set_inputs] = React.useState({});

    const handle_change = (event) =>{
      const name = event.target.name
      const value = event.target.value
      set_inputs(values => ({...values, [name]: value}))
    }

    const handle_submit = (event) =>{
      alert(inputs.code_name)
      
    }
    return (
    <div className="container" onSubmit={handle_submit} >
      <h1>Hello World!</h1>
      <form>
        <label className="pr-4">Code name</label>
        <input value={inputs.code_name} type="text" name="code_name" onChange= {(e) => {handle_change}} />
        <br/>
        <br/>
        <label className="pr-4">Languange</label>
        <select value={inputs.languange} name="languange">
          <option value="Python">Python</option>
          <option value="Javascript">Javascript</option>
          <option value="Java">Java</option>
        </select>
        <br/>
        <br/>
        <br/>
        <label className="pr-4">Code</label>
        <br/>
        <textarea value={inputs.code} name="" id="" cols="30" rows="10" name="code" onChange= {(e) => {handle_change}}></textarea>
        <br/>
        <br/>
        <input type="submit" />
      </form>
    </div> );
}

ReactDOM.render(<Hello />, document.getElementById('mydiv'))
