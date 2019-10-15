        package com.example.nasa;

        import android.Manifest;
        import android.annotation.SuppressLint;
        import android.content.Context;
        import android.content.Intent;
        import android.content.pm.PackageManager;
        import android.location.Location;
        import android.location.LocationListener;
        import android.location.LocationManager;
        import android.net.Uri;
        import android.os.Build;
        import android.os.Bundle;
        import android.provider.Settings;
        import android.view.View;
        import android.widget.Button;
        import android.widget.TextView;
        import android.widget.Toast;

        import androidx.annotation.NonNull;
        import androidx.annotation.Nullable;
        import androidx.appcompat.app.AppCompatActivity;
        import androidx.core.app.ActivityCompat;
        import androidx.core.content.FileProvider;

        import java.io.File;
        import java.io.FileOutputStream;

        public class Check_Safety extends AppCompatActivity {

            private Button b;
            private TextView data;
            private LocationManager locationManager;
            private LocationListener listener;


            @Override
            protected void onCreate(@Nullable Bundle savedInstanceState) {
                super.onCreate(savedInstanceState);

                setContentView(R.layout.activity_check__safety);

                data = (TextView) findViewById(R.id.textView);
                b = (Button) findViewById(R.id.button);
                double t1,t2;

                locationManager = (LocationManager) getSystemService(LOCATION_SERVICE);


                listener = new LocationListener() {
                    @Override
                    public void onLocationChanged(Location location) {
                        data.append("\n " + location.getLatitude() + "," + location.getLongitude());
                        try{
                            //saving the file into device
                            FileOutputStream out = openFileOutput("data.txt", Context.MODE_PRIVATE);
                            out.write((data.toString()).getBytes());
                            out.close();
                            Toast.makeText(Check_Safety.this,"Saved!",Toast.LENGTH_SHORT).show();

                            //exporting
                           /* Context context = getApplicationContext();
                            File filelocation = new File(getFilesDir(), "data.csv");
                            Uri path = FileProvider.getUriForFile(context, "com.example.nasa", filelocation);
                            Intent fileIntent = new Intent(Intent.ACTION_SEND);
                            fileIntent.setType("text/csv");
                            fileIntent.putExtra(Intent.EXTRA_SUBJECT, "Data");
                            fileIntent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
                            fileIntent.putExtra(Intent.EXTRA_STREAM, path);
                            startActivity(Intent.createChooser(fileIntent, "Send mail"));*/
                        }
                        catch(Exception e){
                            e.printStackTrace();
                            Toast.makeText(Check_Safety.this,"Error!",Toast.LENGTH_SHORT).show();
                        }
                    }

                    @Override
                    public void onStatusChanged(String s, int i, Bundle bundle) {

                    }

                    @Override
                    public void onProviderEnabled(String s) {

                    }

                    @Override
                    public void onProviderDisabled(String s) {

                        Intent i = new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS);
                        startActivity(i);
                    }
                };

                configure_button();
            }

            @Override
            public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
                switch (requestCode){
                    case 10:
                        configure_button();
                        break;
                    default:
                        break;
                }
            }

            void configure_button(){
                // first check for permissions
                if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
                    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                        requestPermissions(new String[]{Manifest.permission.ACCESS_COARSE_LOCATION,Manifest.permission.ACCESS_FINE_LOCATION,Manifest.permission.INTERNET}
                                ,10);
                    }
                    return;
                }
                // this code won't execute IF permissions are not allowed, because in the line above there is return statement.
                b.setOnClickListener(new View.OnClickListener() {
                    @SuppressLint("MissingPermission")
                    @Override
                    public void onClick(View view) {
                        //noinspection MissingPermission
                        locationManager.requestLocationUpdates("gps", 5000, 0, listener);
                    }
                });
            }

            /*public void export(View view)
            {
                try{
                    //saving the file into device
                    FileOutputStream out = openFileOutput("data.csv", Context.MODE_PRIVATE);
                    out.write((data.toString()).getBytes());
                    out.close();

                    //exporting
                    Context context = getApplicationContext();
                    File filelocation = new File(getFilesDir(), "data.csv");
                    Uri path = FileProvider.getUriForFile(context, "com.example.nasa", filelocation);
                    Intent fileIntent = new Intent(Intent.ACTION_SEND);
                    fileIntent.setType("text/csv");
                    fileIntent.putExtra(Intent.EXTRA_SUBJECT, "Data");
                    fileIntent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
                    fileIntent.putExtra(Intent.EXTRA_STREAM, path);
                    startActivity(Intent.createChooser(fileIntent, "Send mail"));
                }
                catch(Exception e){
                    e.printStackTrace();
                }
            }*/
        }