# 系统状态表-bd_systemstatus

## 系统状态表-主表 t_bd_systemstatus

- **表名称：** 系统状态表-主表
- **表名：** t_bd_systemstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fclosetime | 结账日期 | timestamp | 0 |  |  | null | 结账日期 |
| 3 | fisendinit | 是否已结束初始化 | bpchar | 1 |  | √ | '0' | 是否已结束初始化 |
| 4 | fiscloseing | 是否正在结账 | bpchar | 1 |  | √ | '0' | 是否正在结账 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcurperiod | 当前期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 7 | fbooktype | 账簿类型id | int8 | 64 |  | √ | 0 | 账簿类型id |
| 8 | fstartperiod | 启用期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 9 | forgtype | 组织职能 | bpchar | 2 |  | √ | '10' | 组织职能,枚举: 10 :核算组织 09 :资产组织 08 :资金组织 07 :结算组织 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_systemstatus_pkey |  | fid |
| 2 | idx_bd_systemstatus |  | forgid,fbooktype |
