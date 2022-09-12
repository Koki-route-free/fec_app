$(function(){
      document.getElementById("room_id_paste").addEventListener('paste', function(e){
        //クリップボードの文字列を引用
        var testtext = e.clipboardData.getData('Text').split('\n');
    
          //テキストボックスに出力
          $('[name="room_id"]').each(function(i, e){
            $(this).val(testtext[i]);
          });
    
      });
      document.getElementById("start_time_paste").addEventListener('paste', function(e){
        //クリップボードの文字列を引用
        var testtext = e.clipboardData.getData('Text').split('\n');
    
          //テキストボックスに出力
          $('[name="start_time"]').each(function(i, e){
            $(this).val(testtext[i]);
          });
    
      });
      document.getElementById("finish_time_paste").addEventListener('paste', function(e){
        //クリップボードの文字列を引用
        var testtext = e.clipboardData.getData('Text').split('\n');
    
          //テキストボックスに出力
          $('[name="finish_time"]').each(function(i, e){
            $(this).val(testtext[i]);
          });
    
      });
    
    });

// デフォルト値
var checkMon = document.getElementById("Mon").checked
if (checkMon){
  $('#Monday').addClass("is-active");
} 

// クリックした後
$(function() {
  $('[name="date"]:radio').change( function() {
    if($('[id=Mon]').prop('checked')){
      $('.area').removeClass("is-active");
      $('#Monday').addClass("is-active");
    } else if ($('[id=Tue]').prop('checked')) {
      $('.area').removeClass("is-active");
      $('#Tuesday').addClass("is-active");
    } else if ($('[id=Wed]').prop('checked')) {
      $('.area').removeClass("is-active");
      $('#Wednesday').addClass("is-active");
    } else if ($('[id=Thu]').prop('checked')) {
      $('.area').removeClass("is-active");
      $('#Thursday').addClass("is-active");
    } else if ($('[id=Fri]').prop('checked')) {
      $('.area').removeClass("is-active");
      $('#Friday').addClass("is-active");
    } else if ($('[id=Sat]').prop('checked')) {
      $('.area').removeClass("is-active");
      $('#Saturday').addClass("is-active");
    } 
  });
});