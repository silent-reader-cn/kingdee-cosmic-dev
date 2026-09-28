# 系统配置-ysq_sys_config

## 系统配置-主表 tk_ysq_sys_config

- **表名称：** 系统配置-主表
- **表名：** tk_ysq_sys_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fk_ysq_value | 配置值 | varchar | 2000 |  | √ | ' ' | 配置值 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fk_ysq_key | 配置项 | varchar | 100 |  | √ | ' ' | 配置项 |
| 9 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tk_ysq_sys_config |  | fid |
