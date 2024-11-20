
  var TIME_CALC_URL = "/_calc_times";

  // Pass calctimes a <td> element containing the data for a control.
  // It extracts the distance and calls the server to get times to
  // fill in open and close times in a human-readable format.
  // (If we want to also keep the ISO-formatted times, we'll need to
  // stash them in hidden fields.) 
  function calc_times(control) {
    var km = control.find("input[name='km']").val();
    var begin_date = $("input[name='begin_date'").val();
    var begin_time = $("input[name='begin_time'").val();
    var distance = $("select[name='distance'").val();
    var open_time_field = control.find("input[name='open']");
    var close_time_field = control.find("input[name='close']");
    console.log("calc_times called")
    $.getJSON(TIME_CALC_URL, { dist_km: km, begin_date: begin_date, begin_time: begin_time, distance: distance }, 
      function(data) {
        console.log("Got a response: " + JSON.stringify(data));
        const response = data.result;
        if (response.error) {
          alert(response.error);
            return;
        }
        // Use UTC timezone
        open_time_field.val( moment(response.open).utc().format("ddd M/D H:mm"));
        close_time_field.val( moment(response.close).utc().format("ddd M/D H:mm"));
       } // end of handler function
     );// End of getJSON
    }

  $(document).ready(function(){
   // Do the following when the page is finished loading

      $('input[name="miles"]').change(
         function() {
             var miles = parseFloat($(this).val());
             var km = (1.609344 * miles).toFixed(1) ;
             console.log("Converted " + miles + " miles to " + km + " kilometers");
             var control_entry = $(this).parents(".control")
             var target = control_entry.find("input[name='km']");
             target.val( km );
             // Then calculate times for this entry
             calc_times(control_entry);
          });

      $('input[name="km"]').change(
         function() {
             var km = parseFloat($(this).val());
             var miles = (0.621371 * km).toFixed(1);
             console.log("Converted " + km + " km to " + miles + " miles");
             var control_entry = $(this).parents(".control")
             var target = control_entry.find("input[name='miles']");
             target.val( miles );
             // Then calculate times for this entry
             calc_times(control_entry);
          });

     });   // end of what we do on document ready
