Description
############

.. image:: https://travis-ci.com/exosite/lib_exoedge_modbus_python.svg?token=tgjcyH1MG5sXqcVsD1kG&branch=master
    :target: https://travis-ci.com/exosite/lib_exoedge_modbus_python

This project is a Modbus source for Exosite's ``ExoSense`` which uses ``ExoEdge``.

Install
#########

From Source
""""""""""""

.. code-block::

    pip install -r requirements.txt
    python setup.py install

From PyPi
""""""""""""

The wheel for this hasn't been published yet.

.. code-block::

    pip install exoedge_modbus

ExoEdge Configuration
######################

In order to start using this Modbus source, start the ``edged`` daemon with your desired parameters. For more information on ``edged``, visit `ExoEdge <https://pypi.org/project/exoedge/>`_ on PyPi.

Example
""""""""

.. code-block::

    $ cat modbus-test1.ini
    [device]
    murano_host = mqtt://f5330e5s8cho0000.m2.exosite.io/
    murano_id = modbus-test1
    $ edged -i modbus-test1.ini go


ExoSense Configuration
########################

Below is an example ``config_io`` settings that illustrates how Modbus RTU data can be sent to ExoSense via ExoEdge.

.. code-block:: json

    {
      "channels": {
        "001": {
          "display_name": "Input Register 1",
          "description": "Input Register 1.",
          "channel_name": "001",
          "properties": {
            "data_unit": "NUMBER",
            "data_type": "TEMPERATURE",
            "min": null,
            "max": null,
            "precision": null,
            "device_diagnostic": false
          },
          "protocol_config": {
            "timeout": null,
            "report_on_change": false,
            "report_rate": 2000,
            "application": "Modbus_RTU",
            "app_specific_config": {
              "byte_endianness": "big",
              "register_range": "INPUT_REGISTER",
              "register_offset": "0002",
              "register_count": 1,
              "register_endianness": "big",
              "bitmask": "0xffffffff",
              "slave_id": 1,
              "evaluation_mode": "unsigned"
            },
            "sample_rate": 2000,
            "input_raw": {},
            "offset": 0,
            "interface": "/dev/ttyM0",
            "down_sample": "ACT"
          }
        }
      }
    }

Below is the ``config_applications`` configuration needed for the ``config_io`` above:

.. code-block:: json

    {
      "applications": {
        "Modbus_RTU": {
          "application_display_name": "Modbus RTU",
          "interfaces": [
              {
                "interface": "/dev/ttyM0",
                "baud_rate": 19200,
                "stop_bits": 1,
                "data_bits": 7,
                "parity": "none"
              }
          ]
        }
      }
    }

Below is a ``config_io`` example for ``Modbus_TCP``:

.. code-block:: json

    {
      "channels": {
        "1": {
          "display_name": "Input Register 1",
          "description": "One-second intervals of input register 1.",
          "properties": {
            "max": null,
            "precision": null,
            "data_type": "BINARY",
            "min": null
          },
          "protocol_config": {
            "application": "Modbus_TCP",
            "report_on_change": false,
            "report_rate": 1000,
            "sample_rate": 1000,
            "down_sample": "ACT",
            "app_specific_config": {
              "ip_address": "192.168.11.139",
              "port": 5020,
              "register_range": "INPUT_REGISTER",
              "register_offset": 0,
              "register_count": 1,
              "byte_endianness": "big",
              "register_endianness": "big",
              "evaluation_mode": "string-ascii",
              "bitmask": "0x0000"
            }
          }
        }
      }
    }
