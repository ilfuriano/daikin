import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate_ir
from esphome.const import CONF_USE_FAHRENHEIT


AUTO_LOAD = ["climate_ir"]

daikin_brc52a61_ns = cg.esphome_ns.namespace("daikin_brc52a61")
DaikinClimate = daikin_brc52a61_ns.class_("DaikinClimate", climate_ir.ClimateIR)

CONFIG_SCHEMA = climate_ir.climate_ir_with_receiver_schema(DaikinClimate)
    
async def to_code(config):
    var = await climate_ir.new_climate_ir(config)
    cg.add(var.set_fahrenheit(config[CONF_USE_FAHRENHEIT]))
