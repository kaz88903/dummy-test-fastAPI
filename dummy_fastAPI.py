from fastapi import FastAPI
import calibration.cal_test_fastAPI as ctf
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    cal_result = ctf.run()
    return {"message": cal_result}

@app.get("/set_serial_number/{serial_number}")
def get_user(serial_number: str):
    # Use user_id in your function
    result = ctf.run_ssn(serial_number)
    return result

@app.get("/set_sensor_rtc")
def execute_ssr_run():
    result = ctf.run_ssr()
    return result

@app.get("/calibration_cad")
def execute_cad_run():
    result = ctf.run_cad()
    return result

@app.get("/calibration_spb")
def execute_spb_run():
    result = ctf.run_spb()
    return result

@app.get("/calibration_crf")
def execute_crf_run():
    result = ctf.run_crf()
    return result

@app.get("/calibration_scc")
def execute_scc_run():
    result = ctf.run_scc()
    return result

@app.get("/calibration_ras")
def execute_ras_run():
    result = ctf.run_ras()
    return result

@app.get("/calibration_cmrxp")
def execute_cmrxp_run():
    result = ctf.run_cmrxp()
    return result

@app.get("/calibration_cr")
def execute_cr_run():
    result = ctf.run_cr()
    return result

@app.get("/calibration_cfs")
def execute_cfs_run():
    result = ctf.run_cfs()
    return result

@app.get("/calibration_cfl")
def execute_cfl_run():
    result = ctf.run_cfl()
    return result

@app.get("/calibration_cfps")
def execute_cfps_run():
    result = ctf.run_cfps()
    return result

@app.get("/calibration_cfpp")
def execute_cfpp_run():
    result = ctf.run_cfpp()
    return result

@app.get("/calibration_rrc")
def execute_rrc_run():
    result = ctf.run_rrc()
    return result

@app.get("/calibration_br")
def execute_br_run():
    result = ctf.run_br()
    return result

def run():
    uvicorn.run("calibration.dummy_fastAPI:app", host="127.0.0.1", port=8000)
    return

if __name__ == "__main__":
    run()