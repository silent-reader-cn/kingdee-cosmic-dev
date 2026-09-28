# 汇率换算配置操作日志-bd_exrate_config_oplog

## 汇率换算配置操作日志-主表 t_int_exrulelog

- **表名称：** 汇率换算配置操作日志-主表
- **表名：** t_int_exrulelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 3 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 4 | foptype | 操作类型 | bpchar | 1 |  | √ | '0' | 操作类型,枚举: 0 :修改 1 :删除 2 :新增 |
| 5 | fsourcecur | 原币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fisindirect | 使用间接汇率 | varchar | 32 |  | √ | ' ' | 使用间接汇率 |
| 7 | foldvalue | 原值 | bpchar | 1 |  | √ | '0' | 原值,枚举: 0 :关闭 1 :打开 |
| 8 | fuserid | 操作者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | ftargetcur | 目标币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | fnewvalue | 新值 | bpchar | 1 |  | √ | '0' | 新值,枚举: 0 :关闭 1 :打开 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_int_exrulelog |  | fid |
| 2 | idx_int_exrulelog_optime |  | foptime |
