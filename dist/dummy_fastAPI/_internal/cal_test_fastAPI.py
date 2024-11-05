from resultflag_enum import ResultFlag

def run():
  result = {"resultflag": ResultFlag.PASS, "message": "hello world"}
  return result

def run_ssn(serial_number):
  return {"resultflag": ResultFlag.PASS, "message": r"Serial number set successfully to {}".format(serial_number)}

def run_ssr():
  return {'resultflag': ResultFlag.PASS, 'message': "Sensor RTC set successfully."}

def run_cad():
  res =  [
    {
      "itemlistdef_id": 2,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 2,
      "itemlistdef_itemname": "ext_ADC_max_abs_dev_lin_x",
      "itemlistdef_descriptor": "External ADC max abs deviation linearity (x)",
      "itemlistdef_description_text": "External ADC's maximum absolute deviation from fit-line check for linearity for the x direction",
      "itemlistdef_units": "ADC counts",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": 20.0,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 21.765716040681582,
      "passflag": -32
    },
    {
      "itemlistdef_id": 3,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 3,
      "itemlistdef_itemname": "ext_ADC_max_abs_dev_lin_y",
      "itemlistdef_descriptor": "External ADC max abs deviation linearity (y)",
      "itemlistdef_description_text": "External ADC's maximum absolute deviation from fit-line check for linearity for the y direction",
      "itemlistdef_units": "ADC counts",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": 20.0,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 23.72353190226204,
      "passflag": -32
    },
    {
      "itemlistdef_id": 4,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 4,
      "itemlistdef_itemname": "ext_ADC_slope_x",
      "itemlistdef_descriptor": "External ADC count per dac slope (x)",
      "itemlistdef_description_text": "Checking the external ADC's change in ADC count per DAC (slope) in the x direction",
      "itemlistdef_units": "ADC count per DAC",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": 0.4,
      "itemlistdef_fail_max": 0.8,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.6231977717635596,
      "passflag": 10
    },
    {
      "itemlistdef_id": 5,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 5,
      "itemlistdef_itemname": "ext_ADC_slope_y",
      "itemlistdef_descriptor": "External ADC count per dac slope (y)",
      "itemlistdef_description_text": "Checking the external ADC's change in ADC count per DAC (slope) in the y direction",
      "itemlistdef_units": "ADC count per DAC",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": 0.4,
      "itemlistdef_fail_max": 0.8,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.6189231539077589,
      "passflag": 10
    },
    {
      "itemlistdef_id": 6,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 6,
      "itemlistdef_itemname": "int_ADC_max_abs_dev_lin_x",
      "itemlistdef_descriptor": "Internal ADC max abs deviation linearity (x)",
      "itemlistdef_description_text": "Internal ADC's maximum absolute deviation from fit-line check for linearity for the x direction",
      "itemlistdef_units": "ADC counts",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": 20.0,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.0,
      "passflag": 10
    },
    {
      "itemlistdef_id": 7,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 7,
      "itemlistdef_itemname": "int_ADC_max_abs_dev_lin_y",
      "itemlistdef_descriptor": "Internal ADC max abs deviation linearity (y)",
      "itemlistdef_description_text": "Internal ADC's maximum absolute deviation from fit-line check for linearity for the y direction",
      "itemlistdef_units": "ADC counts",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": 20.0,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.0,
      "passflag": 10
    },
    {
      "itemlistdef_id": 8,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 8,
      "itemlistdef_itemname": "int_ADC_slope_x",
      "itemlistdef_descriptor": "Internal ADC count per dac slope (x)",
      "itemlistdef_description_text": "Checking the internal ADC's change in ADC count per DAC (slope) in the x direction",
      "itemlistdef_units": "ADC count per DAC",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": 0.4,
      "itemlistdef_fail_max": 0.8,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.0,
      "passflag": -31
    },
    {
      "itemlistdef_id": 9,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 9,
      "itemlistdef_itemname": "int_ADC_slope_y",
      "itemlistdef_descriptor": "Internal ADC count per dac slope (y)",
      "itemlistdef_description_text": "Checking the internal ADC's change in ADC count per DAC (slope) in the y direction",
      "itemlistdef_units": "ADC count per DAC",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": 0.4,
      "itemlistdef_fail_max": 0.8,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.0,
      "passflag": -31
    }
  ]
  return {'resultflag': ResultFlag.PASS, 'message': 'ADC DAC Calibration completed successfully.', "result": res}

def run_spb():
  res = [
    {
    "itemlistdef_id": 11,
    "itemlistdef_itemlistrev_id": 1,
    "itemlistdef_itemnumber": 11,
    "itemlistdef_itemname": "uniformity_test_synthesizers",
    "itemlistdef_descriptor": "Synth power uniformity test",
    "itemlistdef_description_text": "Checks the uniformity of all four synthsizers by subtracting the highest peak minus the lowest peak",
    "itemlistdef_units": None,
    "itemlistdef_critical_spec": None,
    "itemlistdef_report_level": 2,
    "itemlistdef_warning_min": None,
    "itemlistdef_warning_max": None,
    "itemlistdef_fail_min": None,
    "itemlistdef_fail_max": 20.0,
    "itemlistdef_sanity_min": None,
    "itemlistdef_sanity_max": None,
    "itemlistdef_blobdata_exists": None,
    "value": 0.5684866753776117,
    "passflag": 10
    },
    {
    "itemlistdef_id": 12,
    "itemlistdef_itemlistrev_id": 1,
    "itemlistdef_itemnumber": 12,
    "itemlistdef_itemname": "synth1_power",
    "itemlistdef_descriptor": "Synth 1 power",
    "itemlistdef_description_text": "Synthesizer 1 peak power check",
    "itemlistdef_units": "dBm",
    "itemlistdef_critical_spec": None,
    "itemlistdef_report_level": 2,
    "itemlistdef_warning_min": None,
    "itemlistdef_warning_max": None,
    "itemlistdef_fail_min": None,
    "itemlistdef_fail_max": 20.0,
    "itemlistdef_sanity_min": None,
    "itemlistdef_sanity_max": None,
    "itemlistdef_blobdata_exists": None,
    "value": 7.075338410723682,
    "passflag": 10
    },
    {
    "itemlistdef_id": 13,
    "itemlistdef_itemlistrev_id": 1,
    "itemlistdef_itemnumber": 13,
    "itemlistdef_itemname": "synth2_power",
    "itemlistdef_descriptor": "Synth 2 power",
    "itemlistdef_description_text": "Synthesizer 2 peak power check",
    "itemlistdef_units": "dBm",
    "itemlistdef_critical_spec": None,
    "itemlistdef_report_level": 2,
    "itemlistdef_warning_min": None,
    "itemlistdef_warning_max": None,
    "itemlistdef_fail_min": None,
    "itemlistdef_fail_max": 20.0,
    "itemlistdef_sanity_min": None,
    "itemlistdef_sanity_max": None,
    "itemlistdef_blobdata_exists": None,
    "value": 6.968371428081276,
    "passflag": 10
    },
    {
    "itemlistdef_id": 14,
    "itemlistdef_itemlistrev_id": 1,
    "itemlistdef_itemnumber": 14,
    "itemlistdef_itemname": "synth3_power",
    "itemlistdef_descriptor": "Synth 3 power",
    "itemlistdef_description_text": "Synthesizer 3 peak power check",
    "itemlistdef_units": "dBm",
    "itemlistdef_critical_spec": None,
    "itemlistdef_report_level": 2,
    "itemlistdef_warning_min": None,
    "itemlistdef_warning_max": None,
    "itemlistdef_fail_min": None,
    "itemlistdef_fail_max": 20.0,
    "itemlistdef_sanity_min": None,
    "itemlistdef_sanity_max": None,
    "itemlistdef_blobdata_exists": None,
    "value": 6.8958138784216745,
    "passflag": 10
    },
    {
    "itemlistdef_id": 15,
    "itemlistdef_itemlistrev_id": 1,
    "itemlistdef_itemnumber": 15,
    "itemlistdef_itemname": "synth4_power",
    "itemlistdef_descriptor": "Synth 4 power",
    "itemlistdef_description_text": "Synthesizer 4 peak power check",
    "itemlistdef_units": "dBm",
    "itemlistdef_critical_spec": None,
    "itemlistdef_report_level": 2,
    "itemlistdef_warning_min": None,
    "itemlistdef_warning_max": None,
    "itemlistdef_fail_min": None,
    "itemlistdef_fail_max": 20.0,
    "itemlistdef_sanity_min": None,
    "itemlistdef_sanity_max": None,
    "itemlistdef_blobdata_exists": None,
    "value": 6.50685173534607,
    "passflag": 10
    }]
  # json_object = json.dumps(res, indent=4)

  return {"resultflag": ResultFlag.PASS, "message": f"Synthesizer power calibration completed successfully.", "result": res}
def run_crf():
  res = [
    {
      "itemlistdef_id": 17,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 17,
      "itemlistdef_itemname": "ref_focus_pass",
      "itemlistdef_descriptor": "Reference focus",
      "itemlistdef_description_text": "Check to make sure reference focus (L2) is getting back desired Rx power",
      "itemlistdef_units": "dBm",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": -23.5,
      "itemlistdef_fail_max": -22.5,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": -21.869998931884766,
      "passflag": -32
    }
  ]
  return {"resultflag": ResultFlag.PASS, "message": f"Reference focus calibration completed successfully.", "result": res}
def run_scc():
  return {"resultflag": ResultFlag.PASS, "message": "Skew correction completed succesfully."}

def run_ras():
  return {"resultflag": ResultFlag.PASS, "message": f"RF ADC spectrum calibration completed successfully."}

def run_cmrxp():
  res = [
    {
      "itemlistdef_id": 24,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 24,
      "itemlistdef_itemname": "rx_noise_floor",
      "itemlistdef_descriptor": "RX Noise Floor ",
      "itemlistdef_description_text": "Ensure that the \"electronic noise\" is low",
      "itemlistdef_units": "dBm",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": -15.0,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": -15.505811289691925,
      "passflag": 10
    },
    {
      "itemlistdef_id": 25,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 25,
      "itemlistdef_itemname": "rx_saturation",
      "itemlistdef_descriptor": "RX Saturation ",
      "itemlistdef_description_text": "Examine the saturation threshold, so that the Rx power from most points is viable",
      "itemlistdef_units": "dBm",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": 20.0,
      "itemlistdef_fail_max": None,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 19.116156463623046,
      "passflag": -31
    }
  ]
  return {"resultflag": ResultFlag.PASS, "message": "Min max RX power calibration completed successfully.", "result": res}

def run_cr():
  res =  [
    {
      "itemlistdef_id": 19,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 19,
      "itemlistdef_itemname": "stdev_phase_0",
      "itemlistdef_descriptor": "Stdev of phase 0",
      "itemlistdef_description_text": "Check the circular standard deviation for phase 0",
      "itemlistdef_units": "radians",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": 0.9,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.0063362406151683945,
      "passflag": 10
    },
    {
      "itemlistdef_id": 20,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 20,
      "itemlistdef_itemname": "stdev_phase_1",
      "itemlistdef_descriptor": "Stdev of phase 1",
      "itemlistdef_description_text": "Check the circular standard deviation for phase 1",
      "itemlistdef_units": "radians",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": 0.9,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.0064712583719826805,
      "passflag": 10
    },
    {
      "itemlistdef_id": 21,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 21,
      "itemlistdef_itemname": "stdev_phase_2",
      "itemlistdef_descriptor": "Stdev of phase 2",
      "itemlistdef_description_text": "Check the circular standard deviation for phase 2",
      "itemlistdef_units": "radians",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": 0.9,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.006852915200748292,
      "passflag": 10
    },
    {
      "itemlistdef_id": 22,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 22,
      "itemlistdef_itemname": "stdev_phase_3",
      "itemlistdef_descriptor": "Stdev of phase 3",
      "itemlistdef_description_text": "Check the circular standard deviation for phase 2",
      "itemlistdef_units": "radians",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": 0.9,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": -0.0,
      "passflag": 10
    }
  ]
  return {"resultflag": ResultFlag.PASS, "messsage": "Reference Calibration completed succesfully", "result": res}

def run_cfs():
  return {"resultflag": ResultFlag.PASS, "message": "Calibration focus search completed successfully"}

def run_cfl():
  return {"resultflag": ResultFlag.PASS, "message": "Focus Lens Calibration completed successfully."}

def run_cfps():
  return {"resultflag": ResultFlag.PASS, "message": "Flat Plane Scan calibration completed successfully."}

def run_cfpp():
  res = [
    {
      "itemlistdef_id": 27,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 27,
      "itemlistdef_itemname": "optical_system_calibration_optimization_success",
      "itemlistdef_descriptor": "Optical System Optitmization Success",
      "itemlistdef_description_text": "Optical system optimization success flag",
      "itemlistdef_units": "integer",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": 0.5,
      "itemlistdef_fail_max": None,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.0,
      "passflag": -31
    },
    {
      "itemlistdef_id": 28,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 28,
      "itemlistdef_itemname": "optical_system_calibration_error",
      "itemlistdef_descriptor": "Optical System Optimization Final Cost Function",
      "itemlistdef_description_text": "Optical system optimization standard deviation of plane fitting residuals",
      "itemlistdef_units": "mm",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": 0.075,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.035897846403777925,
      "passflag": 10
    },
    {
      "itemlistdef_id": 29,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 29,
      "itemlistdef_itemname": "optical_system_calibration_error_scan1",
      "itemlistdef_descriptor": "Optical System Optimization Cost Function Scan 1",
      "itemlistdef_description_text": "Optical system optimization standard deviation of plane fitting residuals for scan 1",
      "itemlistdef_units": "mm",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": 0.075,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.07660469570737356,
      "passflag": -32
    },
    {
      "itemlistdef_id": 30,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 30,
      "itemlistdef_itemname": "optical_system_calibration_error_scan2",
      "itemlistdef_descriptor": "Optical System Optimization Cost Function Scan 2",
      "itemlistdef_description_text": "Optical system optimization standard deviation of plane fitting residuals for scan 2",
      "itemlistdef_units": "mm",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": 0.075,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.07515429870090622,
      "passflag": -32
    },
    {
      "itemlistdef_id": 31,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 31,
      "itemlistdef_itemname": "optical_system_calibration_error_scan3",
      "itemlistdef_descriptor": "Optical System Optimization Cost Function Scan 3",
      "itemlistdef_description_text": "Optical system optimization standard deviation of plane fitting residuals for scan 3",
      "itemlistdef_units": "mm",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": 0.075,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.07010356565726213,
      "passflag": 10
    },
    {
      "itemlistdef_id": 32,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 32,
      "itemlistdef_itemname": "optical_system_calibration_error_scan4",
      "itemlistdef_descriptor": "Optical System Optimization Cost Function Scan 4",
      "itemlistdef_description_text": "Optical system optimization standard deviation of plane fitting residuals for scan 4",
      "itemlistdef_units": "mm",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": 0.075,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.06728848195112665,
      "passflag": 10
    },
    {
      "itemlistdef_id": 33,
      "itemlistdef_itemlistrev_id": 1,
      "itemlistdef_itemnumber": 33,
      "itemlistdef_itemname": "optical_system_calibration_error_scan5",
      "itemlistdef_descriptor": "Optical System Optimization Cost Function Scan 5",
      "itemlistdef_description_text": "Optical system optimization standard deviation of plane fitting residuals for scan 5",
      "itemlistdef_units": "mm",
      "itemlistdef_critical_spec": None,
      "itemlistdef_report_level": 2,
      "itemlistdef_warning_min": None,
      "itemlistdef_warning_max": None,
      "itemlistdef_fail_min": None,
      "itemlistdef_fail_max": 0.075,
      "itemlistdef_sanity_min": None,
      "itemlistdef_sanity_max": None,
      "itemlistdef_blobdata_exists": None,
      "value": 0.06982742202111072,
      "passflag": 10
    }
  ]
  return {"resultflag": ResultFlag.PASS, "message": "Flat Plane Optimization completed successfully.", "result": res}

def run_rrc():
  return {"resultflag": ResultFlag.PASS, "message": "Calibration data uploaded successfully."}

def run_br():
  return {"resultflag": ResultFlag.PASS, "message": "Calibration records built successfully."}
