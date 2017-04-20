Ext.onReady(function() {
    Ext.get('waitProgressBar').on('click', function(){
        Ext.MessageBox.show({
            msg: 'Asking Khadgar, please wait...',
            progressText: 'Summoning Khadgar...',
            width:300,
            wait:true,
            waitConfig: {interval:200},
            animEl: 'waitProgressBar'
        });
    });
})
