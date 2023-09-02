import click
import gpxpy
import subprocess
import sys

@click.command()
@click.argument('file', type=click.Path(exists=True))
def gpx_to_sim(file):
    click.echo(f'Reading: {file}')

    gpx_file = open(file, 'r')

    gpx = gpxpy.parse(gpx_file)

    subprocess.call(
        ["/usr/bin/open", "-a", "Simulator"]
    )

    # booted_device = None
    # while booted_device is None:
    #     for _, devices in Device.list_all().items():
    #         for device in devices:
    #             if device.state == 'Booted':
    #                 print(f'{device.name}, {device.udid}')
    #                 booted_device = device

    # print(f'{booted_device.name}: {booted_device.state}')
    # print(booted_device.is_available)

    # params = ["xcrun", "simctl", "location", f"{booted_device.udid}", "start", "--speed", "10"]
    params = ["xcrun", "simctl", "location", "booted", "start", "--speed", "6"]
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                lat = round(point.latitude, 4)
                lng = round(point.longitude, 4)
                # print('Point at ({0},{1}) -> {2}'.format(lat, lng, point.elevation))
                params.append(f"{lat},{lng}")
    print(params)
    subprocess.call(params)


if __name__ == '__main__':
    print(str(sys.argv))
    gpx_to_sim()
