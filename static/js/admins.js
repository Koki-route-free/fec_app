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