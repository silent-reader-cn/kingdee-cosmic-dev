# 其他存货核算接口配置-cal_othercost_settings

## 其他存货核算接口配置-主表 t_cal_othercalcsettings

- **表名称：** 其他存货核算接口配置-主表
- **表名：** t_cal_othercalcsettings

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 3 | fissys | 系统预制 | bpchar | 1 |  | √ | '0' | 系统预制 |
| 4 | finterface | 核算接口 | varchar | 300 |  | √ | ' ' | 核算接口 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_othercalcsettings |  | fid |
| 2 | idx_cal_othercalcsettings |  | fbiztype |
