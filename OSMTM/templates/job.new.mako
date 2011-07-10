<%inherit file="/base.mako"/>
<%def name="id()">job_new</%def>
<%def name="title()">New Job</%def>

<div class="content group wrap">
    <section class="new">
        <h1>New Job</h1>
        <form method="post" action="">
            <div class="field"> 
            <label for="id_title">Title</label> 
            <input type="text" class="text" id="id_title" name="title" value="" /> 
            </div> 
            <div class="field"> 
            <label for="id_description">Description</label> 
            <textarea class="text" id="id_description" name="description"></textarea> 
            </div> 
            <div class="field"> 
            <label for="id_relation">Area of interest</label> 
            <input type="text" class="text" id="id_relation" name="relation" value="" /> 
            <input type="hidden" id="geometry" name="geometry" value="" />
            <div id="relation_map">
                <div id="map"></div>
            </div>
            </div>
            <div class="field"> 
            <label for="id_workflow">Workflow</label> 
            <textarea class="text" id="id_workflow" name="workflow"></textarea> 
            </div> 
            <div class="field">
            <label for="id_zoom">Zoom level</label> 
            <select id="id_zoom" name="zoom">
                 <option>0</option>
                 <option>1</option>
                 <option>2</option>
                 <option>3</option>
                 <option>4</option>
                 <option>5</option>
                 <option>6</option>
                 <option>7</option>
                 <option>8</option>
                 <option>9</option>
                 <option>10</option>
                 <option>11</option>
                 <option selected="selected">12</option>
                 <option>13</option>
                 <option>14</option>
                 <option>15</option>
                 <option>16</option>
            </select>
            </div> 
            <div class="clear">
            <input type="submit" class="submit" value="Create the job" name="form.submitted" /> 
            </div>
        </form>
    </section>
</div>
<script type="text/javascript" src="http://openlayers.org/dev/OpenLayers.js"></script>
<script type="text/javascript" src="${request.static_url('OSMTM:static/Div.js')}"></script>
<script type="text/javascript" src="${request.static_url('OSMTM:static/Static.js')}"></script>
<script type="text/javascript" src="${request.static_url('OSMTM:static/job.new.js')}"></script>
