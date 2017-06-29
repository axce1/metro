
// http://plugins.krajee.com/file-input/demo#basic-usage
$(document).ready(function() {
  console.log( "ready!" );
      $("#input-img").fileinput({
        initialPreview: [
                      'http://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/FullMoon2010.jpg/631px-FullMoon2010.jpg',
                      'http://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Earth_Eastern_Hemisphere.jpg/600px-Earth_Eastern_Hemisphere.jpg'
                  ],
        initialPreviewAsData: true,
        initialPreviewConfig: [
                      {caption: "Moon.jpg", size: 930321, width: "120px", key: 1},
                      {caption: "Earth.jpg", size: 1218822, width: "120px", key: 2}
                  ],
        //deleteUrl: "/site/image-upload",
        overwriteInitial: false,
        maxFileSize: 1000,
        showUpload: false,
        allowedFileExtensions: ["jpg", "jpeg", "png"],
        initialCaption: "The Moon and the Earth"
  });
});
