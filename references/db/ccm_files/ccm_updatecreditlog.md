# 信用更新日志-ccm_updatecreditlog

## 信用更新日志-主表 t_ccm_upcreditlog

- **表名称：** 信用更新日志-主表
- **表名：** t_ccm_upcreditlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | farchiveid | 信用档案ID | int8 | 64 |  | √ | 0 | 信用档案ID |
| 4 | fcreatetime | 操作日期 | timestamp | 0 |  |  | null | 操作日期 |
| 5 | farchivename | 档案名称 | varchar | 255 |  | √ | ' ' | 档案名称 |
| 6 | fop | 操作 | varchar | 30 |  | √ | ' ' | 操作 |
| 7 | fbillids | 单据 | varchar | 1000 |  | √ | ' ' | 单据 |
| 8 | funitid | 单位 | int8 | 64 |  | √ | 0 | 单位 |
| 9 | fentitykey | 实体对象 | varchar | 30 |  | √ | ' ' | 实体对象 |
| 10 | fnote | 说明 | varchar | 2000 |  | √ | ' ' | 说明 |
| 11 | famount | 本单增加额度 | numeric | 23 | 10 | √ | 0 | 本单增加额度 |
| 12 | foverduebillno | 逾期单据编号 | varchar | 100 |  | √ | ' ' | 逾期单据编号 |
| 13 | fcontrolmode | 控制强度 | varchar | 30 |  | √ | ' ' | 控制强度,枚举: cancel :取消交易 warning :预警提示 |
| 14 | fsuccess | 检查通过 | bpchar | 1 |  | √ | ' ' | 检查通过 |
| 15 | fbalance | 余额 | numeric | 23 | 10 | √ | 0 | 余额 |
| 16 | fscheme | 信控方案 | int8 | 64 |  | √ | 0 | 信用控制方案 ccm_schemes |
| 17 | fquotatype | 额度类型 | varchar | 30 |  | √ | ' ' | 额度类型,枚举: amount :信用额度 qty :信用数量 days :信用天数 overdueamt :逾期额度 |
| 18 | fdirection | 更新方向 | varchar | 30 |  | √ | ' ' | 更新方向,枚举: reduce :减少 increase :增加 |
| 19 | flogtype | 日志类型 | varchar | 30 |  | √ | ' ' | 日志类型,枚举: check :正常检查日志 other :其他日志 |
| 20 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_upcrelog_time |  | fcreatetime |
| 2 | pk_ccm_upcreditlog |  | fid |
