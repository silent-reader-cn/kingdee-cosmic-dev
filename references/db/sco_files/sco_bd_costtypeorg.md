# 标准成本方案与组织对应表(后台)-sco_bd_costtypeorg

## 标准成本方案与组织对应表(后台)-主表 t_sco_costtypeorg

- **表名称：** 标准成本方案与组织对应表(后台)-主表
- **表名：** t_sco_costtypeorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 3 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 5 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 7 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: 0 :未确认 1 :已确认 |
| 8 | fconfirmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 9 | feffectdate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_costtypeorg_ccs_1 |  | fcostaccountid,fcalorgid,fstorageorgunitid |
| 2 | pk_sco_costtypeorg |  | fid |
