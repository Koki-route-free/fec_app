var today = new Date();
var month = ('00' + (today.getMonth()+1)).slice(-2);
var date = ('00' + today.getDate()).slice(-2);
var ymd = today.getFullYear()+"-"+ month +"-"+ date;

var nextweek = new Date();
nextweek.setDate(nextweek.getDate()+7);
var month = ('00' + (nextweek.getMonth()+1)).slice(-2);
var date = ('00' + nextweek.getDate()).slice(-2);
var ymd_1 = nextweek.getFullYear()+"-"+ month +"-"+ date;

$('#calendar').html('<input type="date"  min="'+ ymd +'" max="' + ymd_1 + '" value="' + ymd +'" name="selectdate">');

var hour = ('00' + today.getHours()).slice(-2);
var min = ('00' + today.getMinutes()).slice(-2);
var time = hour+min;

if (time < 1040) {
  $('#lecture').html('<option value="1" selected>１限</option><option value="2">２限</option><option value="3">３限</option><option value="4">４限</option><option value="5">５限</option><option value="6">６限</option>');
} else if (1040 <= time && time < 1230){
  $('#lecture').html('<option value="1">１限</option><option value="2" selected>２限</option><option value="3">３限</option><option value="4">４限</option><option value="5">５限</option><option value="6">６限</option>');
} else if (1230 <= time && time < 1500){
  $('#lecture').html('<option value="1">１限</option><option value="2">２限</option><option value="3" selected>３限</option><option value="4">４限</option><option value="5">５限</option><option value="6">６限</option>');
} else if (1500 <= time && time < 1650){
  $('#lecture').html('<option value="1">１限</option><option value="2">２限</option><option value="3">３限</option><option value="4" selected>４限</option><option value="5">５限</option><option value="6">６限</option>');
} else if (1650 <= time && time < 1840){
  $('#lecture').html('<option value="1">１限</option><option value="2">２限</option><option value="3">３限</option><option value="4">４限</option><option value="5" selected>５限</option><option value="6">６限</option>');
} else {
  $('#lecture').html('<option value="1">１限</option><option value="2">２限</option><option value="3">３限</option><option value="4">４限</option><option value="5">５限</option><option value="6" selected>６限</option>');
}

//任意のタブにURLからリンクするための設定
function GethashID (hashIDName){
    if(hashIDName){
      //タブ設定
      $('#tab li').find('a').each(function() { //タブ内のaタグ全てを取得
        var idName = $(this).attr('href'); //タブ内のaタグのリンク名（例）#secondの値を取得 
        if(idName == hashIDName){ //リンク元の指定されたURLのハッシュタグ（例）http://example.com/#second←この#の値とタブ内のリンク名（例）#lunchが同じかをチェック
          var parentElm = $(this).parent(); //タブ内のaタグの親要素（li）を取得
          $('#tab li').removeClass("active"); //タブ内のliについているactiveクラスを取り除き
          $(parentElm).addClass("active"); //リンク元の指定されたURLのハッシュタグとタブ内のリンク名が同じであれば、liにactiveクラスを追加
          //表示させるエリア設定
          $(".area").removeClass("is-active"); //もともとついているis-activeクラスを取り除き
          $(hashIDName).addClass("is-active"); //表示させたいエリアのタブリンク名をクリックしたら、表示エリアにis-activeクラスを追加 
        }
      });
    }
  }
  
  //タブをクリックしたら
  $('#tab a').on('click', function() {
    var idName = $(this).attr('href'); //タブ内のリンク名を取得  
    GethashID (idName);//設定したタブの読み込みと
    return false;//aタグを無効にする
  });

  
  // 上記の動きをページが読み込まれたらすぐに動かす
  $(window).on('load', function () {
      $('#tab li:first-of-type').addClass("active"); //最初のliにactiveクラスを追加
      $('.area:first-of-type').addClass("is-active"); //最初の.areaにis-activeクラスを追加
    var hashName = location.hash; //リンク元の指定されたURLのハッシュタグを取得
    GethashID (hashName);//設定したタブの読み込み
  });

// ページ読み込まれたらクリック
window.onload = function () {
  document.getElementById( "default" ).click();
}






