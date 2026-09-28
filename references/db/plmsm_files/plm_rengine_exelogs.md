# 调用日志(规则引擎)-plm_rengine_exelogs

## 调用日志(规则引擎)-主表 t_plm_egn_exelog

- **表名称：** 调用日志(规则引擎)-主表
- **表名：** t_plm_egn_exelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftraceid | TraceId | varchar | 50 |  | √ | ' ' | TraceId |
| 4 | fbizapp | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 5 | ferrormsg | 异常信息 | varchar | 500 |  | √ | ' ' | 异常信息 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbatchresult | 批量结果 | varchar | 500 |  | √ | ' ' | 批量结果 |
| 8 | finitstatus | 初始化状态 | varchar | 50 |  | √ | 'C' | 初始化状态,枚举: 0 :进行中 1 :已验证 2 :已完成 |
| 9 | fexecosttime | 耗时 | int4 | 32 |  | √ | 0 | 耗时 |
| 10 | finitbatch | 初始化批次 | int8 | 64 |  | √ | 0 | 初始化批次 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fresponsecode | 调用编码 | varchar | 50 |  | √ | ' ' | 调用编码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fscenename | 场景名称 | varchar | 100 |  | √ | ' ' | 场景名称 |
| 15 | finitdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :手工录入 1 :初始化 |
| 16 | fresponsedesc | 调用状态 | varchar | 1500 |  | √ | ' ' | 调用状态,枚举: success :成功执行 KDBizException :业务异常 SystemException :系统异常 |
| 17 | fisbatch | 调用类型 | varchar | 2 |  | √ | ' ' | 调用类型,枚举: 1 :批量 0 :单次 |
| 18 | fpolicyresults | 匹配策略 | varchar | 50 |  | √ | ' ' | 匹配策略 |
| 19 | fexestarttime | 调用时间 | timestamp | 0 |  |  | null | 调用时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_egn_exelog |  | ftraceid |
| 2 | pk_plm_egn_exelog |  | fid |
