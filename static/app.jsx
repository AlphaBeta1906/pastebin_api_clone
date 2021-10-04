function App() {
    const [inputs,set_inputs] = React.useState({});
    const [data,set_data] = React.useState("")
    const [isLoad,set_load] = React.useState(false)
    const [disabled,set_disabled] = React.useState(false)

    const handle_change = (event) =>{
      const name = event.target.name
      const value = event.target.value
      set_inputs(values => ({...values, [name]: value}))
    }
    const size = {
      heigth:"100%"
    };
    const handle_submit = (event) =>{
      set_disabled(true)
      event.preventDefault()
      if(inputs.languange == null){
        inputs.languange = "Python"
      }
      fetch(`https://pastebincloneapi.pythonanywhere.com/add_code?code_title=${encodeURIComponent(inputs.code_name)}&code=${encodeURIComponent(inputs.code)}&languange=${encodeURIComponent(inputs.languange)}&test=${encodeURIComponent(true)}`, {
        method: "POST",   
      }).then(response => response.json()
        .then(data=>{ 
          console.log(data);
          set_load(true)
          set_disabled(false)
          set_data(data)
          console.log(isLoad)
        })
        ).catch(function(error){
        console.log(error)
      })
      set_inputs("")
      $("#load").removeAttr("hidden")
      $("select").val("Python")
      
    }
    return (
    <div style={size} className="card shadow rounded container text-white bg-gray-600 h-full" >
      <h1>add code endpoint test</h1>
      <form onSubmit={handle_submit} className="py-2" >
        <label className="px-2 font-semibold">Code name</label>
        <input 
          className="rounded-lg px-2 text-gray-700 " 
          value={inputs.code_name || ""} 
          placeholder="input code title" 
          type="text" 
          required 
          name="code_name" 
          onChange= {handle_change} />
        <br/>
        <br/>
        <label className="px-2 font-semibold">Languange</label>
        <select value={inputs.languange} onChange={handle_change} name="languange">
          <option value="Python">Python</option>
          <option value="Javascript">Javascript</option>
          <option value="Java">Java</option>
        </select>
        <br/>
        <br/>
        <br/>
        <label className="pr-4 font-semibold">Code</label>
        <br/>
        <textarea 
          className="px-2" 
          required 
          placeholder="input code" 
          value={inputs.code || ""} 
          cols="30" 
          rows="10" name="code" 
          onChange= {handle_change}></textarea>
        <br/>
        <br/>
        <input 
        className="btn btn-outline-primary hvr-back-pulse" 
        type="submit" 
        disabled={disabled} 
        value="test post method" />
        <div className="pt-3">
            <div id="load" hidden>
              {
                isLoad?
                <pre><code className="hljs languange-json">{JSON.stringify(data, null, 2)}</code></pre>
                :
                <div class="spinner-border" role="status">
                  <span class="visually-hidden">Loading...</span>
                </div>
              }
            </div>
        </div>
      </form>
    </div> 
    );
}

ReactDOM.render(<App />, document.getElementById('root'))
