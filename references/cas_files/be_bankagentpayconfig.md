# 打包代发规则-be_bankagentpayconfig

## 打包代发规则-主表 t_be_bankagentpayconfig

- **表名称：** 打包代发规则-主表
- **表名：** t_be_bankagentpayconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbankinterfaceid | 银企接口 | varchar | 200 |  |  | null | 银企接口,枚举: 1 :接口A 2 :接口B |
| 3 | fmaxpay | 每笔最大金额 | numeric | 19 | 6 | √ | 0.000000 | 每笔最大金额 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fcount | 最大笔数 | int8 | 64 |  | √ | 0 | 最大笔数 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_be_bankagentpayconfig_pkey |  | fid |
| 2 | idx_be_fbankinterfaceid |  | fbankinterfaceid |
